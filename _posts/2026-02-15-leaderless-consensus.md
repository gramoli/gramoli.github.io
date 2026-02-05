---
layout: post
author: Vincent
tags: leader consensus
---

Recently, I have been asked what a leaderless protocol is. This notion has been so instrumental to ensure scalability that it is important 
to explain it here.

### Leader-based consensus protocols

Since 1999, with the influence of the Practical Byzantine Fault Tolerant (PBFT) consensus protocol [1], most consensus protocols designed to cope with 
unexpected message delays and Byzantine failures had a leader. They were often variants of the PBFT consensus protocol, this is why so many blockchains built upon leader-based consensus protocols, like Tendermint, Concord, Quorum, Aptos, Diem... to name a few.

### Leader-based design for four LAN nodes

For at least the past 16 years, researchers knew that leaders were creating bottlenecks [2], this was even mentioned in this previous [blog post](https://github.com/gramoli/gramoli.github.io/blob/main/_posts/2024-01-19-why-blockchains-were-actually-centralised.md). However, the leader abstraction was well known to 
break the symetry needed for all correct nodes to converge to a common decision, especially in a network where messages could take longer than 
expected to arrive. With PBFT, this abstraction even proved practical to achieve good performance in a local area network of four machines or nodes. 
The problem arose when trying with more nodes and in a wide area network.

### Bottleneck effect

In a leader-based context, the leader would typically send some data item (be it a block or a general value) to everyone in order for them 
to agree on it. In a wide area network where 
the broadcast primitive does not exist at the IP layer, the leader has to send repeatedly the same information to different recipient. 
Therefore when the number of nodes grow, so does the amount of data the leader has to send. The network interface of the leader then 
becomes the bottleneck. Although they are alternatives that try to minimize this bottleneck effect where the leader does not send all the
data to everyone, it just delay the bottleneck observation to more nodes. As one can see on this graph taken from [7], leader-based protocols
send to all other nodes that then either exchange among themselves or send back to the leader.

![Leader-based](/img/leader-based.png){: width="500" }

### Bittorrent

With the advent of peer-to-peer systems in the 2000s, new communication patterns were proved instrumental to share a file fast by 
bypassing the bottleneck effect of a single sender. The idea was share a file in a large network by splitting it in a series of chunks, such 
that all nodes would contribute to sending distinct chunks to the recipient. By having multiple nodes sending smaller chunks, the recipient would
obtain the file faster than if all its chunks were sent by the same sender. 

### Pattern 

Redbelly [3] made an interesting observation that blocks could be combined into superblocks rather than deciding upon a single block proposed by a
leader, a winner of a proof-of-work, etc. The idea was to leverage the blocks proposed by multiple nodes rather than discarding them in order
to scale by accepting more proposed transactions as the number of nodes would grow. 

![Leaderless](/img/leaderless.png){: width="500" }

### Leader-freedom

The idea of leader-less consensus protocol became the idea of a consensus protocol that would be able to converge despite a single
node acting arbitrarily. In DBFT [4], this notion means that you can take any individual node and make him do whatever you want 
(even outside the protocol), there exist some execution that will converge to an agreement regardless of its behaviour. 
A formal but slightly stricter definition [5] that received the Best Paper Award of ICDCS'21 [6] was later, required that any execution would 
converge regardless of the behaviour of one node. Although theoretically interesting, we are not award of implementations that would be 
as efficient as DBFT, Dispel or Redbelly in practice.

### Conclusions

[1] Miguel Castro and Barbara Liskov. Practical Byzantine Fault Tolerance. OSDI 1999.

[2] A leader-free Byzantine consensus algorithm.  Fatemeh Borran and André Schiper. In Distributed Computing and Networking,
pages 67–78, Berlin, Heidelberg, 2010. Springer Berlin Heidelberg.

[3] [Red Belly: A secure, fair and scalable open blockchain](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf). T Crain, C Natoli, V Gramoli. IEEE Symposium on Security and Privacy (S&P), 466-483, 2021.

[4] [DBFT: Efficient Leaderless Byzantine Consensus and its Application to Blockchains](https://redbelly.network/research/2018-NCA-DBFT.pdf)  T. Crain, V. Gramoli, M. Larrea and M. Raynal. In 
2018 IEEE 17th International Symposium on Network Computing and Applications (NCA), 2018.

[5] Leaderless Consensus. K. Antoniadis, A. Desjardins, V. Gramoli, R. Guerraoui, I. Zablotchi. IEEE 41st International Conference on Distributed Computing Systems (ICDCS), 392-402, 2021, *Best Paper Award*.

[6] [Leaderless Consensus](https://gramoli.github.io/pubs/JPDC23-Leaderless-Preprint.pdf). K. Antoniadis, J. Benhaim, A. Desjardins, P. Elias, V. Gramoli, R. Guerraoui, G. Voron, I. Zablotchi. Journal of Parallel and Distributed Computing, 2023, doi: 10.1016/j.jpdc.2023.01.009.

[7] [Planetary Scale Byzantine Consensus]([https://dl.acm.org/doi/10.1609/aaai.v39i25.34818](https://gramoli.github.io/pubs/2023-applied.pdf).  G. Voron, V. Gramoli. ACM Workshop on Advanced tools, programming languages, and PLatforms for Implementing and Evaluating algorithms for Distributed systems (ApPLIED), 2023.
