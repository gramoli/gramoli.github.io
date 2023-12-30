---
layout: post
author: Vincent
tags: security consensus
---

As new flaw in the Solana consensus protocol will be presented in four days [1], it might be the right time to discuss the importance of formal methods.
Classic blockchains had a hard time being adopted in production. When the largest bank of Australia asked me to do some consulting work, 
I had to inform them that the way they were using Ethereum was flawed as we managed to hack a copy of their setup [2]. 
After we reported the vulnerability to both Geth and Parity security teams, they both acknowledged the problem but it took some time for 
Parity to implement our counter measure. It is thus not surprising that the traditional finance industry has been slow at integrating blockchain 
to their production system. We discuss the importance of the problem and how we tackled it with formal verification.

The crux of the problem is that the consensus problem at the heart of blockchain is a complex problem. Some of my colleagues have worked for four 
decades on this problem. I have only worked for two decades on this problem, but I still started way before Bitcoin came out. 
The first time I looked at how the traditional finance industry was using blockchain was when I talked to R3, that at the time were using Ethereum. 
After some experiments, my student and myself came to the conclusion that one node of their network could easily steal the assets of all other partners 
of the consortium. This work was the first blockchain work ever published in the largest scientific conference of the dependable community [3].

To summarize the problem, note that classic blockchains do not solve consensus to agree on a unique block before this block gets appended to the chain. 
Sometimes this is intentional: Ethereum and Bitcoin fork in order to try to reach consensus later on. Sometimes it is not intentional: Tendermint, 
HoneyBadgerBFT, Quorum, Ripple had some flaws [4], just like Solana [1].  The problem is the same: when the consensus is not reached, then we have some uncertainty: is the network stuck or is it telling me that my transaction is committed while it will be reverted?
Because the key ingredient to steal assets is precisely to convince someone that the transaction paying her is committed and then rolling it back later on.

Knowing all the flaws that were reported about consensus protocols used in blockchain, we took the decision of formally verifying the consensus protocol, 
DBFT, we use in our blockchains. First, the flaws we saw is the tip of the iceberg and they are probably many more problems we are not aware of.
Second, hand written proofs are insufficient due to the complexity of the consensus protocol and the fact that human are prone to errors. 
After a couple of years of collaboration with expert in formal methods from Australia, Austria, France, Germany and US, we finally managed to formally verify 
a blockchain consensus protocol [5] using threshold automata as illustrated in the figure below. Thanks to parameterised model checking, 
we were able to show (provided that the model checker and the environment is 
correct) that our protocol solves the consensus protocol in any possible executions of any system sizes.

![Dictatorship](/img/formal-verif.png){: width="500" }

This drastically reduces the risks of human errors and we invite researchers and blockchain designers to use our methodology or to build upon the formally 
verified blockchain consensus. This is needed to reduce the risks of assets being stolen, especially as the traditional finance industry wants to adopt 
blockchain in production.

[1] Q. Kniep, F. Schaich, J. Sliwinski, R. Wattenhofer. [Halting the Solana Blockchain with Epsilon Stake](https://tik-db.ee.ethz.ch/file/9d40dad802dd12d9ba1f1b7c1759920c/). 25th International Conference on Distributed Computing and Networking. 2024.

[2] P. Ekparinya, V. Gramoli, G. Jourjon. [The attack of the clones against proof-of-authority](https://gramoli.github.io/pubs/Clone-PoA-NDSS.pdf).  27th Annual Network and Distributed System Security Symposium (NDSS), 2020. Community Ethereum Development Conference, 2019

[3] C. Natoli, V. Gramoli. [The balance attack or why forkable blockchains are ill-suited for consortium](https://gramoli.github.io/pubs/Balance_Attack_DSN17.pdf).  47th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN), 2017.

[4] P. Tholoniat and V. Gramoli. [Formal Verification of Blockchain Byzantine Fault Tolerance](https://arxiv.org/pdf/1909.07453.pdf). In Springer Optimization and Its Applications - Handbook on Blockchain. p.389-412.

[5] N. Bertrand, V. Gramoli, M. Lazić, I. Konnov, P. Tholoniat, J. Widder. [Holistic Verification of Blockchain Consensus](https://gramoli.github.io/pubs/DISC22-holistic-verification.pdf). 36th International Symposium on Distributed Computing (DISC), 2022.
 
