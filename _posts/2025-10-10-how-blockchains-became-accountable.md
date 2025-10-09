---
layout: post
author: Vincent
tags: accountability 
---

Blockchain systems have been hiding hackers for too long. It is now time to protect users to make this technology widely available.
Since 2019, we have known how to provably detect double spenders, but the solution could not scale to very large networks.
Finally, a new scalable accountable consensus solution is about to be published in the flagship cybersecurity conference, Oakland'26.
Let me explain how this will help democratise blockchain technology.


### Polygraph

Our original Polygraph solution, as its name suggests, is an enriched version of the DBFT consensus protocol [5] that detects liars. Each time hackers manage to create a fork by fooling different parts of the network about two conflicting blocks, an undeniable proof-of-fraud against some of these hackers is generated. 
This led to a new line research on distributed system forensic [7].
The key idea of Polygraph was to piggyback an amount of signed data independent from the number of previous messages in the consensus instance. 
Already a good progress towards scalability as the experiments showed, yet not optimal: 
https://
eprint.iacr.org/2019/587.pdf	

### ZLB 

This proof-of-fraud generation became key to accountability. Once the proof-of-fraud is generated, and since it is undeniable, every correct participants can agree to punish the hackers. In ZLB, we designed and implemented this punishment mechanism: each participant first has to stake some assets. 
Each time a hacker gets detected with Polygraph, then ZLB would kick this hacker out of the system and use their stake to reimburse the potential victims. Thanks to this punishment strategy, ZLB became the first blockchain to be resilient to a colluding majority. Although the performance of ZLB were getting close to Redbelly’s, we needed to reduce the number of messages to make it scale.

### ABC

But what if a blockchain was using a different consensus protocol than DBFT, then it would be difficult to make it accountable. 
This is why we introduced ABC, a more efficient generic transformation of any consensus protocol into an accountable consensus version with a simple additive quadratic communication factor. It is probably the simplest way to make blockchain participants truly accountable by detecting their double spending attempts.  A generalization over ABC was proposed in Crime and Punishment [6] in order to work on various decision tasks even when the decision of all processes was not expected to be identical.  But the quadratic factor and the amount of signatures needed would be an overkill at large scale, so we needed a more efficient solution.

### ABC++

Finally, we managed to lower this additive communication complexity factor to a sub quadratic factor. Our tricks use a VRF-based probabilistic quorum system with BLS verification optimisations. The ratifier uses a VRF to produce a one-round quorum selection incurring O(\lambda n) messages where \lambda is a statistical security parameter and where the message size depends on \kappa, a computational parameter.
The propagator then requires O(√nλ) per-process message-complexity and 2 rounds between a safety violation and detection where each message has size O(λlog n+ κ) when using generic succinct non-interactive arguments (SNARGs), or size O(λκ) when employing pairing-based proofs.
Composing sequentially the ratifier with the propagator offers the same confirmer as in ABC, hence offering accountability on top of any Byzantine Agreement, Reliable Broadcast, or Consistent Broadcast primitives. Because of its subquadratic complexity, it offers a scalable accountability, hence promising to secure blockchains.

### RWA

Now think about application to blockchains for Real World Assets (RWA). You would not want a hacker who stole your property to get away without being identified. This is exactly what this accountable result solves for: protecting users while using RedbellyNetwork.

[1] A. Haeberlen, P. Kuznetsov, P. Druschel. [PeerReview: practical accountability for distributed systems](https://dl.acm.org/doi/abs/10.1145/1323293.1294279), ACM SIGOPS operating systems review 41(6) 2007.
[2] S. Micali, K. Ohta, and L. Reyzin. [Accountable-subgroup multisignatures: Extended abstract](https://dl.acm.org/doi/10.1145/501983.502017). In CCS’01,
pages 245–254. ACM, 2001.
[3] P. Civit, S. Gilbert, V. Gramoli.[Polygraph: Accountable byzantine agreement](https://eprint.iacr.org/2019/587.pdf) IEEE 41st International Conference on Distributed Computing Systems (ICDCS), 2021.
[4] [ZLB: A Blockchain to Tolerate Colluding Majorities](https://gramoli.github.io/pubs/DSN24-ZLB.pdf). A. Ranchal-Pedrosa, V. Gramoli. 54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN), 2024,
[5] T. Crain, V. Gramoli, M. Larrea, M. Raynal. [DBFT: Efficient Leaderless Byzantine Consensus and its Application to Blockchains](https://ieeexplore.ieee.org/document/8548057). IEEE 17th International Symposium on Network Computing and Applications (NCA) 2018.
[6] P. Civit, S. Gilbert, V. Gramoli, R. Guerraoui, J. Komatovic, Z. Milosevic, A. Seredinschi. [Crime and Punishment in Distributed Byzantine Decision Tasks](https://gramoli.github.io/pubs/ABC-IPDPS2022.pdf). 42nd IEEE International Conference on Distributed Computing Systems (ICDCS), 2022.
[7] P. Sheng, G. Wang, K. Nayak, S. Kannan, and P. Viswanath.
[BFT protocol forensics](https://dl.acm.org/doi/10.1145/3460120.3484566). CCS ’21: 2021 ACM SIGSAC
Conference on Computer and Communications Security, 2021.
[Online]. Available: https://doi.org/10.1145/3460120.348456