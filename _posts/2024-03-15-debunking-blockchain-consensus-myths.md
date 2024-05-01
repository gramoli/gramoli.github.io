---
layout: post
author: Vincent
tags: consensus DBFT
---

Blockchain technologies rely on a large body of complex research topics like the Byzantine consensus problem. Although such a problem was defined four decades ago, its subtle ramifications are largely misunderstood by many blockchain developers, let alone application programmers who build upon these blockchains. These misconceptions are dramatic as they prevent these applications from working efficiently and they make them vulnerable to attacks. In a recent chapter [1], we debunk the 10 major myths about blockchain consensus by evaluating three distributed ledgers, Hyperledger Fabric, Redbelly Blockchain and R3 Corda, as well as three important consensus algorithms, BFT-SMaRt, Democratic BFT and HotStuff. Below we discuss the five first myths.

A consensus protocol is a key element of the blockchain system as it helps a distributed set of machines agree on a unique block at each given index of a chain. In contrast with the problem of consensus that has been known by the distributed computing community for the past four decades [2], a significant part of these proposals is often unclear. Most of these new consensus protocols are described in white papers, wikis and online documentations, rather than in more traditional academic publications and it is unclear whether they satisfy the application requirements.

The first myth is that the various Po* mechanisms, that encompass Proof-of-Work and Proof-of-Stake solve consensus. They typically limit the nodes that can create valid blocks but unfortunately they do not guarantee agreement about a unique block to append to the next available index of the chain. 

The second and third myths is that consensus is the bottleneck of blockchain systems in LAN and WAN. It is true that consensus is needed by blockchain and that its consensus often involves at least a quadratic communication complexity that rapidly consumes the bandwidth as the system enlarges [3], however, consensus is not always the bottleneck. Simple evaluations of the performance of Hyperledger Fabric and Corda running BFT-SMarRt indicates that they  are significantly slower than BFT-SMarRt.

![Leader-based vs. leaderless design](/img/msg-pattern.png){: width="500" }

Other myths involve the folklore believes that blockchains are secure because they make use of hashes and signatures or integrate a Byzantine fault tolerant consensus algorithm. A first problem is that blockchain clients typically believe the information they receive from a single source, making them vulnerable to a single Byzantine failure. A second problem is that replacing the orderer module of Hyperledger Fabric by a Byzantine fault tolerant module was insufficient as the whole blockchain architecture needed to be redesigned to become Byzantine fault tolerant.

[1] D. Hyland, J. Sousa, G. Voron, A. Bessani and V. Gramoli. [Ten Myths About Blockchain Consensus](https://gramoli.github.io/pubs/Ten-myths-preprint.pdf). Blockchains Advances in Information Security, Springer, Volume 35, doi:10.1007/978-3-031-32146-7_1, 2024.

[2] M.C. Pease, R.E. Shostak, L. Lamport. [Reaching agreement in the presence of faults](https://dl.acm.org/doi/10.1145/322186.322188). J. ACM 27(2), 228–234 (1980).

[3] P. Civit, M. A. Dzulfikar, S. Gilbert, V. Gramoli, R. Guerraoui, J. Komatovic, M. Vidigueira. [Byzantine Consensus is Theta(n^2): The Dolev-Reischuk Bound is Tight even in Partial Synchrony!](https://gramoli.github.io/pubs/DISC22-quadratic-consensus.pdf) 36th International Symposium on Distributed Computing (DISC), 2022
