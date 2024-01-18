---
layout: post
author: Vincent
tags: consensus, centralisation
---

Most blockchains have an inherently centralised design, which restricts their scalability. It is the consequence of research on the consensus problem from the 80s and the influential leader-based consensus protocols from the 2000s. We had to wait until until 2021 for the problem to be redefined in a decentralised way for blockchains to scale to large networks.

Since its inception, blockchain has been inherently leader-based. Despite the large body of work on decentralisation and distribution, an interesting centralisation aspects underlies the implementation of many blockchain systems. Whether it is about choosing a block or favouring messages, these blockchains always promote one lucky node that imposes its block to the rest of the network [1].

This inherent centralisation dates back from the 80’s where the consensus problem (and in particular its validity property) was defined as the problem of deciding the proposal of *one* of the existing nodes. At the time it made sense, because to simplify the problem researchers were focusing on binary values and did not want consensus to be reached on value 1 if all nodes were proposing value 0.

The problem was exacerbated in 1999 when Castro and Liskov introduces PBFT for 4 nodes to agree in a Local Area Network (LAN). In order to decide only one of the proposed values, they used the concept of a leader: a single node that imposes its value to the rest of the network. This centralisation was key to make consensus practical in a LAN. The problem is that the paper was so influential that most consensus algorithms are now variants of PBFT, all relying on a leader. This centralisation is why these consensus protocols do not scale to Wide Area Networks.

![Leader-based vs. leaderless design](/img/leaderless.png){: width="500" }

In 2021, we defined the Set Byzantine Consensus [3], allowing nodes to agree on multiple blocks at the next available index. This allowed us to leverage the resources of all the nodes instead of relying on a leader bottleneck: view it as introducing network collaboration where there was only network competition.
The result led to scalability in a WAN environment as performance would grow with the size of the network. 
This is illustrated by the graph of the blockchain scalability MOOC [4] above, comparing the times to propagate information with and without a leader [4].

[1] Satoshi Nakamoto. Bitcoin: A Peer-to-Peer Electronic Cash System. [https://bitcoin.org/bitcoin.pdf](https://bitcoin.org/bitcoin.pdf)

[2] Miguel Castro and Barbara Liskov. [Practical Byzantine Fault Tolerance](https://pmg.csail.mit.edu/papers/osdi99.pdf). OSDI 1999.

[3] Tyler Crain, Chris Natoli and Vincent Gramoli. [Red Belly: A Secure Fair and Scalable Open Blockchain](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf). S&P 2021. 

[4] Blockchain Scalability and its Foundations in Distributed Systems. [https://www.coursera.org/learn/blockchain-scalability](https://www.coursera.org/learn/blockchain-scalability)
