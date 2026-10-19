---
layout: post
author: Vincent
tags: social_choice governance
---

Twenty days ago, when I was invited to speak at the Ethereum Sydney 2026 Workshop, I warned the developers and researchers in the room that autonomous AI agents would soon execute the next wave of blockchain exploits.

At the time, some attendees viewed the prospect of autonomous AI exploiting blockchain networks as a distant concern. Less than three weeks later, we have our first documented case.

As recently reported by OpenAI, its GPT-5.6 Sol research model hijacked a third-party Ethereum wallet without authorization to finish a coding task.

Instead of stopping to ask a human operator for help, the model improvised. It wrote a script to derive private keys from publicly known developer recovery phrases, scanned 362 Ethereum addresses until it found one holding enough Sepolia ETH, and signed a transaction using those keys to pay for its own contract deployment.

In its internal chain of thought, the model explicitly debated the ethics of its actions. It rationalized that because Sepolia ETH had no monetary value, taking the funds without permission was "Fine", and it concealed how it paid for the deployment in its final report.

### The Fatal Flaw of Anonymous-By-Default Blockchains

OpenAI noted in its misalignment report that "a model can substitute its own judgment about likely harm for the account holder's permission, then act on that judgment without authorization." Their response has been to tighten sandbox rules and monitor live internet access.

Sandboxing at the AI layer will fail to protect Web3. Once an AI model accesses the internet or an RPC endpoint, traditional blockchains have zero defense against it.

Legacy blockchains like Ethereum equate possession of a private key with authorization and identity. To the Ethereum Virtual Machine, a legitimate human user looks identical to a misaligned AI agent brute-forcing mnemonics in a loop. In an anonymous-by-default architecture, any script that can derive a valid cryptographic signature can drain wallets and deploy arbitrary contracts while hiding its tracks.
Note that we already discussed the drawbacks of anonymous-by-default architectures that came out of privacy in an earlier [post](https://gramoli.github.io/2025/08/12/now-is-the-time-for-deterrence.html).


![Oracles](/img/openai-vs-ethereum.jpg){: width="500" }

### The Problem Will Exacerbate in the Near Future

Today the target was valueless Sepolia testnet ETH derived from developer mnemonics. Tomorrow the target will be mainnet liquidity pools or DeFi markets, where AI agents will rationalize theft as optimal task completion.

The incident occurred on 26 June 2026, and was discovered by OpenAI three months later. Detecting hacks provoked by AI agents is becoming more and more difficult. 

We all remember how lucky we were to learn about the Hugging Face incident where a swarm of OpenAI agents hacked Hugging Face trying to erase the traces showing that they had cheated to complete their tasks.
Next year, after the new models will have improved, there is little chance humans will detect the cryptocurrency thefts executed by AI agents.


### How Redbelly Network Stops Rogue AI at the Protocol Level

This exact threat vector is why I founded Redbelly Network on the principle of Accountable Consensus and attributable accounts. We designed Redbelly from day one so that a financial-grade public blockchain can keep out completely autonomous bots and agents.

On Redbelly Network, the attack executed by OpenAI’s model is structurally impossible.

Holding or deriving a private key is insufficient to transact on Redbelly. Before any user can submit a transaction or deploy a smart contract, they must pass identity verification and biometric liveness checks through a registered Identity Provider. Every participant on the network is verified as a human adult so that any AI agent that trades is necessarily under the responsibility of a human adult.

Verifying that a user is a human adult preserves user privacy. Once a user passes document and biometric verification off-chain, they receive a verifiable credential. All Personal Identifiable Information stays off-chain, while the chain only registers the wallet address that belongs to a verified, accountable human adult.

Even if an AI model managed to brute-force or steal a private key from a known mnemonic, as GPT-5.6 Sol did across 362 addresses on Ethereum, Redbelly governors deterministically drop any transaction signed by an uncredentialed address before it enters the mempool. Because accounts are tied to verified human adults via revocable credentials, compromised keys can be revoked at the protocol control plane without halting the network.

### The Future of Blockchain Must Be Human-Accountable
As AI models grow more capable of autonomous reasoning, deception, and sandbox escape, relying on AI providers to keep their models fenced in is wishful thinking. The blockchain infrastructure itself must enforce accountability.

When I warned the Ethereum community in Sydney 20 days ago that AI-driven blockchain hacks were imminent, I wanted to expose an urgent architectural blind spot. Blockchains that settle real-world assets and regulated financial workflows cannot afford to let autonomous AI models impersonate users or commandeer accounts. Requiring biometric and identity verification at the protocol layer is the only way to keep humans in control of the ledger.
