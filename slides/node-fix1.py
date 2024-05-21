from argparse import ArgumentParser
from blockchain import *
from concurrent.futures import ThreadPoolExecutor
import cryptography.hazmat.primitives.asymmetric.ed25519 as ed25519
import logging
from math import ceil
from network import *
from pathlib import Path
import signal
import socketserver
import time

def transaction_bytes(transaction: dict):
	return json.dumps({k: transaction.get(k) for k in ['sender', 'message', 'nonce']}, sort_keys=True).encode()

def make_transaction(message: str, private_key: ed25519.Ed25519PrivateKey, nonce: int):
	transaction = {'sender': private_key.public_key().public_bytes_raw().hex(), 'message': message, 'nonce': nonce}
	signature = private_key.sign(transaction_bytes(transaction)).hex()
	transaction['signature'] = signature
	return transaction

def validate_transaction(transaction: dict, nonces: dict, pool: list=None) -> bool:
	# should contain sender, message, nonce, signature
	if len(transaction) != 4:
		return False
	keys = [('sender', str), ('message', str), ('signature', str), ('nonce', int)]
	for (key, type_) in keys:
		if key not in transaction or not isinstance(transaction[key], type_):
			print(f'[TX] Received an invalid transaction, wrong {key} - {transaction}')
			return False
	try:
		public_key = ed25519.Ed25519PublicKey.from_public_bytes(bytes.fromhex(transaction['sender']))
	except:
		print(f'[TX] Received an invalid transaction, wrong sender - {transaction}')
		return False
	current_nonce = nonces.get(transaction['sender'], None)
	if current_nonce != None and current_nonce >= transaction['nonce'] or transaction['nonce'] < 0:
		# nonce mismatch
		print(f'[TX] Received an invalid transaction, wrong nonce - {transaction}')
		return False
	same_nonce = pool and [x for x in pool if x['sender'] == transaction['sender'] and x['nonce'] <= transaction['nonce']]
	if same_nonce:
		print(f'[TX] Received an invalid transaction, wrong nonce - {transaction}')
		return False
	try:
		public_key.verify(bytes.fromhex(transaction['signature']), transaction_bytes(transaction))
	except:
		print(f'[TX] Received an invalid transaction, wrong signature mssage - {transaction}')
		return False
	# message should be no more than 70 alnum characters
	if len(transaction['message']) > 70 or not transaction['message'].isalnum():
		print(f'[TX] Received an invalid transaction, wrong message - {transaction}')
		return False
	return True

def validate_block(block: dict, nonces: dict, my_block: dict) -> bool:
	if len(block) != 4:
		return False
	keys = [('transactions', list), ('current_hash', str), ('previous_hash', str), ('index', int)]
	for (key, type_) in keys:
		if key not in block or not isinstance(block[key], type_):
			return False
	if not all([validate_transaction(tx, nonces) for tx in block['transactions']]):
		return False
	try:
		if calculate_hash(block).digest() != bytes.fromhex(block['current_hash']):
			return False
	except:
		return False
	for key in ['previous_hash', 'index']:
		if block[key] != my_block[key]:
			return False
	return True

class RemoteNode():
	def __init__(self, host, port) -> None:
		self.host = host
		self.port = port
		self.disabled = False
		self.client = None

	def connect(self) -> bool:
		if self.client:
			self.client.close()
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(5)
		try:
			sock.connect((self.host, self.port))
		except:
			sock.close()
			return False
		logging.info(f'{id(self)} connected to {self.host}:{self.port}')
		self.client = Client(sock)
		return True

	def retry_send_receive(self, request: dict, timeout=None):
		if self.disabled:
			logging.info(f'{id(self)} RemoteNode::retry_send_receive disabled')
			return None
		data = None
		for _ in range(2):
			try:
				self.client.send(json.dumps(request))
				data = self.client.recv()
			except:
				self.connect()
			else:
				break
		if not data:
			self.disabled = True
			return None
		try:
			message = json.loads(data)
		except:
			logging.debug(f'{id(self)} RemoteNode::retry_send_receive cannot parse {data}')
			return None
		return message

	def values(self, index):
		logging.info(f'{id(self)} RemoteNode::values')
		message = self.retry_send_receive({'type': 'values', 'payload': index})
		logging.info(f'{id(self)} RemoteNode::values got {message}')
		if not isinstance(message, list) or any(['current_hash' not in b for b in message]):
			return None
		return {b['current_hash']: b for b in message}

	def transaction(self, transaction):
		logging.info(f'{id(self)} RemoteNode::transaction')
		message = self.retry_send_receive({'type': 'transaction', 'payload': transaction})
		logging.info(f'{id(self)} RemoteNode::transaction got {message}')
		if not isinstance(message, dict):
			return None
		return message

class TransactionPool():
	def __init__(self) -> None:
		self.pool = []
		self.lock = threading.Lock()
		self.nonces = {}

	def add_transaction(self, transaction):
		logging.debug(f'{id(self)} add_transaction')
		with self.lock:
			if validate_transaction(transaction, self.nonces, self.pool):
				logging.debug(f'{id(self)} add_transaction added from {transaction["sender"]}')
				self.pool.append(transaction)
				return True
			return False

	def copy(self):
		logging.debug(f'{id(self)} copy')
		with self.lock:
			return self.pool.copy(), self.nonces.copy()

	def remove_transactions(self, block):
		logging.debug(f'{id(self)} remove_transactions')
		with self.lock:
			for transaction in block['transactions']:
				maybe_tx = [x for x in self.pool if x['sender'] == transaction['sender'] and x['nonce'] <= transaction['nonce']]
				if maybe_tx:
					self.pool.remove(maybe_tx[0])
				# update nonce
				current_nonce = self.nonces.get(transaction['sender'], None)
				assert(current_nonce == None and transaction['nonce'] >= 0 or transaction['nonce'] > current_nonce)
				self.nonces[transaction['sender']] = transaction['nonce']

class Consensus():
	def __init__(self, f) -> None:
		self.index = None
		self.values = None
		self.f = f
		self.lock = threading.Lock()
		self.cond = threading.Condition(self.lock)

	def broadcast(self, block, ps: list[RemoteNode], nonces: dict):
		logging.debug(f'{id(self)} broadcast')
		assert(len(ps) >= 2 * self.f)
		with self.lock:
			self.index = block['index']
			self.values = {block['current_hash']: block}
			self.cond.notify_all()
		responses_count = [0] * len(ps)
		for _ in range(self.f + 1):
			for idx, p in enumerate(ps):
				v_p = p.values(self.index)
				if not v_p:
					continue
				for value in v_p.values():
					if not validate_block(value, nonces, block):
						continue
				with self.lock:
					self.values.update(v_p)
				responses_count[idx] += 1
		can_decide = responses_count.count(self.f + 1) >= len(ps) - self.f
		block = None
		if can_decide:
			with self.lock:
				try:
					block = self.values[min(map(lambda x: x['current_hash'], filter(lambda x: x['transactions'], self.values.values())))]
				except:
					pass
		return block

	def get_values(self, index):
		logging.debug(f'{id(self)} get_values')
		with self.lock:
			self.cond.wait_for(lambda: self.index and self.index >= index)
			logging.debug(f'{id(self)} get_values self.index {self.index}, index {index}')
			return self.values if self.index == index else None

class MyThreadingMixIn:
	def __init__(self) -> None:
		self.threads: list[tuple[socket.socket, threading.Thread]] = []

	def process_request_thread(self, request, client_address):
		try:
			self.finish_request(request, client_address)
		except Exception:
			self.handle_error(request, client_address)
		finally:
			self.shutdown_request(request)

	def process_request(self, request, client_address):
		t = threading.Thread(target = self.process_request_thread,
							 args = (request, client_address))
		self.threads = [t for t in self.threads if t[1].is_alive()]
		self.threads.append((request, t))
		t.start()

	def server_close(self):
		super().server_close()
		for t in self.threads:
			t[0].close()
			t[1].join()
		self.threads.clear()

class MyTCPServer(MyThreadingMixIn, socketserver.TCPServer):
	def __init__(self, server_address, RequestHandlerClass, f, blockchain: Blockchain, bind_and_activate: bool = True) -> None:
		self.blockchain = blockchain
		self.pool = TransactionPool()
		self.consensus = Consensus(f)
		self.consensus_executor = ThreadPoolExecutor(max_workers=1)
		self.remotes: list[RemoteNode] = []
		self.shutdown_requested = False
		self.shutdown_lock = threading.Lock()
		MyThreadingMixIn.__init__(self)
		socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate)

	def request_execute_round(self, index=None):
		logging.debug(f'{id(self)} request_execute_round')
		self.consensus_executor.submit(self.execute_round, index)
		logging.debug(f'{id(self)} request_execute_round submitted')

	def execute_round(self, index):
		if index != None and index != self.blockchain.last_block()['index'] + 1:
			logging.debug(f'{id(self)} execute_round round too old or too new')
			return
		logging.debug(f'{id(self)} execute_round pool.copy()')
		transactions, nonces = self.pool.copy()
		if len(transactions) == 0 and index is None:
			logging.debug(f'{id(self)} execute_round pool empty')
			return
		with self.shutdown_lock:
			if self.shutdown_requested:
				logging.debug(f'{id(self)} shutting down')
				return
		logging.debug(f'{id(self)} execute_round blockchain.propose_block(transactions)')
		block = self.blockchain.propose_block(transactions)
		logging.debug(f'{id(self)} execute_round consensus.broadcast(block, self.remotes)')
		print(f'[PROPOSAL] Created a block proposal: {block}')
		block = self.consensus.broadcast(block, self.remotes, nonces)
		if block:
			logging.debug(f'{id(self)} execute_round blockchain.append_block(block) {block}')
			self.blockchain.append_block(block)
			print(f'[CONSENSUS] Appended to the blockchain: {block['current_hash']}')
			logging.debug(f'{id(self)} execute_round pool.remove_transactions(block)')
			self.pool.remove_transactions(block)
		else:
			logging.error(f'{id(self)} could not reach consensus')

	def shutdown(self) -> None:
		self.consensus_executor.shutdown(cancel_futures=True)
		with self.shutdown_lock:
			logging.debug(f'{id(self)} set shutdown requested')
			self.shutdown_requested = True
		with self.consensus.lock:
			logging.debug(f'{id(self)} notify consensus')
			self.consensus.cond.notify_all()
		return super().shutdown()

class MyTCPHandler(socketserver.BaseRequestHandler):
	server: MyTCPServer

	def setup(self):
		self.client = Client(self.request)
		self.blockchain: Blockchain = self.server.blockchain
		self.pool: TransactionPool = self.server.pool
		self.consensus: Consensus = self.server.consensus
		self.remotes: list[RemoteNode] = self.server.remotes

	def handle(self):
		while True:
			logging.debug(f'{id(self)} handle')
			try:
				data = self.client.recv()
			except:
				logging.debug(f'{id(self)} leaving handle')
				break
			try:
				message = json.loads(data)
			except:
				logging.debug(f'{id(self)} cannot parse {data}')
				continue
			if len(message) != 2:
				continue
			if 'type' not in message or not isinstance(message['type'], str) or not 'payload' in message:
				continue
			if message['type'] == 'transaction':
				logging.debug(f'{id(self)} handle transaction')
				print(f'[NET] Received a transaction from node {self.client_address[0]}: {message['payload']}')
				added = False
				if isinstance(message['payload'], dict):
					transaction = message['payload']
					added = self.pool.add_transaction(transaction)
				logging.debug(f'{id(self)} handle transaction {added}')
				self.client.send(json.dumps({'response': added}))
				if added:
					print(f'[MEM] Stored transaction in the transaction pool: {transaction['signature']}')
					self.server.request_execute_round()
			elif message['type'] == 'values':
				logging.debug(f'{id(self)} handle values')
				print(f'[BLOCK] Received a block request from node {self.client_address[0]}: {message['payload']}')
				values = {}
				if isinstance(message['payload'], int):
					index = message['payload']
					self.server.request_execute_round(index)
					values = self.consensus.get_values(index)
					if not values:
						block = self.blockchain.get_block(index)
						if not block:
							logging.error(f'{id(self)} check impl')
							assert(False)
						values = {block['current_hash']: block}
					assert(next(iter(values.values()))['index'] == index)
					logging.debug(f'{id(self)} handle values {values}')
				self.client.send(json.dumps(list(values.values())))
			else:
				logging.info(f'{id(self)} unknown message type')

class ServerRunner():
	def __init__(self, host, port, f=0) -> None:
		self.blockchain = Blockchain()
		self.server = MyTCPServer((host, port), MyTCPHandler, f, self.blockchain)
		self.thread = threading.Thread(target=self.server.serve_forever)

	def start(self):
		self.thread.start()

	def shutdown(self):
		self.server.shutdown()

	def join(self):
		self.thread.join()

	def server_close(self):
		self.server.server_close()

	def append(self, remote_node: RemoteNode):
		self.server.remotes.append(remote_node)

class Client():
	def __init__(self, sock) -> None:
		self.sock = sock

	def send(self, data: str):
		send_prefixed(self.sock, data.encode())

	def recv(self):
		return recv_prefixed(self.sock).decode()

	def close(self):
		self.sock.close()

if __name__ == '__main__':
	# logging.basicConfig(level=logging.DEBUG)
	parser = ArgumentParser()
	parser.add_argument('port', type=int)
	parser.add_argument('nodesfile', type=Path)
	args = parser.parse_args()
	port: int = args.port
	nodesfile: Path = args.nodesfile

	nodes: list[tuple[str, int]] = []
	with open(nodesfile) as f:
		for line in f.readlines():
			tokens = line.split(':')
			nodes.append((tokens[0], int(tokens[1])))

	runner = ServerRunner('0.0.0.0', port, f=ceil((len(nodes)+1)/2)-1)
	runner.start()

	for node in nodes:
		remote = RemoteNode(node[0], node[1])
		while not remote.connect():
			time.sleep(5)
		runner.append(remote)

	signal.signal(signal.SIGINT, lambda signum, frame: runner.shutdown())
	runner.join()
	runner.server_close()
