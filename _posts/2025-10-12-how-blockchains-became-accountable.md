---
layout: post
author: Vincent
tags: security RWA 
---

Blockchain systems have been hiding hackers for too long. It is now time to protect users to make this technology widely available.
Since [2019](https://eprint.iacr.org/2019/587.pdf), we have known how to provably detect double spenders, but the solution could not scale to very large networks.
Finally, a new scalable accountable consensus solution [[8]](https://gramoli.github.io/pubs/2026-Scalable-Accountability.pdf) is about to be published in the flagship cybersecurity conference, Oakland'26. Let me explain how this will help democratise blockchain technology.

### Polygraph, detecting liars

Our original Polygraph solution [[2]](https://eprint.iacr.org/2019/587.pdf), as its name suggests, is an enriched version of the DBFT consensus protocol [[3]](https://ieeexplore.ieee.org/document/8548057) that detects liars. Each time hackers manage to create a fork by fooling different parts of the network about two conflicting blocks, an undeniable proof-of-fraud against some of these hackers is generated. 
This departs from accountability in cryptography [[4]](https://dl.acm.org/doi/10.1145/501983.502017) and led to a new line of research on distributed system forensic [[5]](https://dl.acm.org/doi/10.1145/3460120.3484566).
The key idea of Polygraph was to piggyback an amount of signed data independent from the number of previous messages of the same consensus instance. 
Already a good progress towards scalability as the experiments showed, yet not optimal.	

![Polygraph](/img/Polygraph.png){: width="500" }

### ZLB to cope with colluding majorities 

This proof-of-fraud generation became key to accountability. Once the proof-of-fraud is generated, and since it is undeniable, every correct participants can agree to punish the hackers. In ZLB [[6]](https://gramoli.github.io/pubs/DSN24-ZLB.pdf), we designed and implemented this punishment mechanism: each participant first has to stake some assets. 
Each time a hacker gets detected with Polygraph, then ZLB would kick this hacker out of the system and use their stake to reimburse the potential victims. Thanks to this punishment strategy, ZLB became the first blockchain to be resilient to a colluding majority. Although the performance of ZLB was getting close to Redbelly’s, we needed to reduce the number of messages to make it scale.

### ABC, accountable consensus made simple 

But what if a blockchain was using a different consensus protocol from DBFT, then it would be difficult to make it accountable. 
This is why we introduced ABC [[7]](https://gramoli.github.io/pubs/JPDC2023-ABC-preprint.pdf), a more efficient generic transformation of any consensus protocol into an accountable consensus version with a simple additive quadratic communication factor. It is probably the simplest way to make blockchain participants truly accountable by detecting their double spending attempts.  A generalization over ABC was proposed in Crime and Punishment [[8]](https://gramoli.github.io/pubs/ABC-IPDPS2022.pdf) in order to work on various decision tasks even when the decision of all processes was not expected to be identical.  But the quadratic factor and the amount of signatures needed would be an overkill at large scale, so we needed a more efficient solution.

### ABC++, scaling accountability to large network

Finally, we managed to lower this additive communication complexity factor to a sub quadratic factor [[1]](../pubs/2026-Scalable-Accountability.pdf). Our tricks use a VRF-based probabilistic quorum system with BLS verification optimisations. The ratifier uses a VRF to produce a one-round quorum selection incurring *O(λn)* messages where *λ* is a statistical security parameter and where the message size depends on *κ*, a computational parameter.
The propagator then requires *O(√(nλ))* per-process message-complexity and 2 rounds between a safety violation and detection where each message has size *O(λlog n+κ)* when using generic succinct non-interactive arguments (SNARGs), or size *O(λκ)* when employing pairing-based proofs.
Composing sequentially the ratifier with the propagator offers the same confirmer as in ABC, hence offering accountability on top of any Byzantine Agreement, Reliable Broadcast, or Consistent Broadcast primitives. Because of its subquadratic complexity, it offers a scalable accountability, hence promising to secure blockchains.

### RWA as an application for accountable blockchains

Now think about applications of blockchains to Real World Assets (RWA). You would not want a hacker who stole your property to get away without being identified. This is exactly what this accountable result solves for: protecting users.

### References

[1] P. Civit, D. Collins, V. Gramoli, R. Guerraoui, J. Komatovic, M. Vidigueira, P. Zarbafian. [Scalable Accountable Byzantine Agreement and Beyond]([../pubs/2026-Scalable-Accountability.pdf](https://gramoli.github.io/pubs/2026-Scalable-Accountability.pdf)). 47th IEEE Symposium on Security and Privacy (Oakland), 2026.
[2] P. Civit, S. Gilbert, V. Gramoli. [Polygraph: Accountable byzantine agreement](https://eprint.iacr.org/2019/587.pdf) IEEE 41st International Conference on Distributed Computing Systems (ICDCS), 2021.
[3] T. Crain, V. Gramoli, M. Larrea, M. Raynal. [DBFT: Efficient Leaderless Byzantine Consensus and its Application to Blockchains](https://ieeexplore.ieee.org/document/8548057). IEEE 17th International Symposium on Network Computing and Applications (NCA) 2018.
[4] S. Micali, K. Ohta, and L. Reyzin. [Accountable-subgroup multisignatures: Extended abstract](https://dl.acm.org/doi/10.1145/501983.502017). In CCS’01,
pages 245–254. ACM, 2001.
[5] P. Sheng, G. Wang, K. Nayak, S. Kannan, and P. Viswanath.
[BFT protocol forensics](https://dl.acm.org/doi/10.1145/3460120.3484566). CCS ’21: 2021 ACM SIGSAC
Conference on Computer and Communications Security, 2021.
[6] [ZLB: A Blockchain to Tolerate Colluding Majorities](https://gramoli.github.io/pubs/DSN24-ZLB.pdf). A. Ranchal-Pedrosa, V. Gramoli. 54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN), 2024,
[7] P. Civit, S. Gilbert, V. Gramoli, R. Guerraoui, J. Komatovic. [As easy as ABC: Optimal (A)ccountable (B)yzantine (C)onsensus is easy!](https://gramoli.github.io/pubs/JPDC2023-ABC-preprint.pdf) Journal of Parallel and Distributed Computing (JPDC), 2023.
[8] P. Civit, S. Gilbert, V. Gramoli, R. Guerraoui, J. Komatovic, Z. Milosevic, A. Seredinschi. [Crime and Punishment in Distributed Byzantine Decision Tasks](https://gramoli.github.io/pubs/ICDCS2022.pdf). 42nd IEEE International Conference on Distributed Computing Systems (ICDCS), 2022.

