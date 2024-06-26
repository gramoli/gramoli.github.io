---
layout: post
author: Vincent
tags: cross-chain interoperability synchrony
---

For blockchain to become securely interoperable, one must first solve the cross-chain payment problem.
Not only should one user of a blockchain be able to pay the user of another blockchain successfully, but it should do so 
without assuming that messages always take less than some period to arrive. Otherwise the solution can be easily hacked.
It turns out that the general problem is unsolvable but, fortunately, there exists a solution to a variant of this problem.

A payment between two customers of the same bank that do not trust each other is simple as long as both customers trust the bank.
Now if two banks trust each other then a payment between two customers of these two banks is feasible as well, 
simply by routing the money through these banks. This is how banks operate transfers today. But what if the banks were smart 
contracts running on different blockchains without trusting each other?

The problem becomes more challenging when customers trust their bank but banks do not trust each other. 
Some solutions involve having customers of multiple banks playing the role of escrow accounts between these banks.
Typical attempts to solve this problem [1,2] are either synchronous or do not offer any guarantee that 
the transfer can happen: without synchrony the protocol may never transfer anything. 

This means that to guarantee cross-chain transfer success, existing solutions needed to assume 
that no messages could take longer than expected to reach their destination. Once this unrealistic assumption is made, 
it is sufficient for both ends of the network to count the time and consider that after some timer expires, 
then the transfer has to abort. This is the classic notion of time-lock that is vulnerable to network attacks, 
natural disasters, BGP misconfigurations, etc [3]. 

We have recently shown [4] that this does not come necessarily as a surprise because 
there exists no algorithm that can solve the cross-chain payment problem without assuming synchrony, 
even if we only require eventual (instead of time-bounded) termination or if participants fail by crashing (even without failing by 
adopting an arbitrary behaviour).

One may thus think that the problem is unsolvable for blockchains. As blockchains typically operate in an open network 
where all message transmissions cannot be capped by a known delay, it appears impossible to design a cross-chain protocol
that offers some transfer success. 

Interestingly, we also show that there is a way to relax the problem definition to guarantee success of cross-chain transfers. 
The idea stems from relaxing the liveness guarantee to be solvable with partial synchrony.
In particular, this solution ensures that honest participants of this protocol cannot be cheated.
But perhaps more interestingly, our problem definition also guarantees that it is not possible for all 
participants to always abort, hence guaranteeing transfer success.

So not only are cross-chain transfers possible without risky techniques like time-locks, but they can be 
guaranteed to succeed in some executions. It is now time to explore this solution to avoid the hacks
that happen when people try to interconnect multiple blockchains.

[1] S. Thomas, E. Schwartz. 
[A Protocol for Interledger Payments](https://interledger.org/interledger.pdf). Whitepaper, 2015. 

[2] M. Herlihy, B. Liskov, L. Shrira.
[Cross-Chain Deals and Adversarial Commerce](https://arxiv.org/abs/1905.09743v5). 
Proceedings of the VLDB Endowment 13(2), pp. 100–113,
doi:10.14778/3364324.3364326, 2019.

[3] A. Ranchal-Pedrosa, V. Gramoli.
[Platypus: Offchain Protocol Without Synchrony](https://ieeexplore.ieee.org/document/8935037). 
IEEE International Symposium on Network Computing and Applications, pp. 1-8, 2019.

[4] R. van Glabbeek, V. Gramoli, P. Tholoniat. 
[Cross-Chain Payment Protocols with Success Guarantees](https://gramoli.github.io/pubs/DC23-CrossChain-Preprint.pdf). 
Distributed Computing, 2023, doi: 10.1007/s00446-023-00446-0.
