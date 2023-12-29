---
layout: post
author: Vincent
tags: social_choice governance
---

Non-dictatorship is a property that appeared in the work of Arrow back in 1950 [1]. We explain why it turns out to be fundamental property for today's blockchain governance. We then explain how one can devise a governance protocol that ensures this property.

Non-dictatorship is vital to the existence of a blockchain governance. In particular, not ensuring this property would simply defeat the purpose of the blockchain. A blockchain is implemented in a distributed fashion to tolerate isolated failures. The service is provided despite the failure of one of its node. With a dictator, a single individual or entity going rogue, would lead the system to go rogue. Hence dictatorship would lose the benefit of distribution.

In order to ensure non-dictatorship in blockchain governance, let's try to define this notion in the blockchain context. The blockchain governance is the set of rules in place to decide upon important changes that impact the blockchain protocol (e.g., its upgrades, its governance reconfiguration).  Such a change must happen only if multiple entities decide so, to prevent a single entity going rogue from compromising the entire blockchain protocol. Note that for this change to happen, the entities have to reach consensus. 

However, it is well known that consensus cannot be reached in the general setting, where the time it takes to deliver a message is unknown [2] if the number of misbheaving (or Byzantine) participants among n participants unless <i>f < n/3</i>. To prevent dicatorship in blockchain it is thus crucial to make sure that even a dictator, even when part of a coalition of <i>f < n/3</i> cannot dictate the governance. We can thus define non-dictatorship as the ability to prevent a single adversary, controlling up to <i>f < n/3</i> Byzantine voters, from imposing their individual preference as the election outcome.

We have devised a governance protocol to allow the governance to take important decisions while ensuring non-dictatorship at all times. Theorem 2 of [3] shows how we ensure this property and we implemented this governance as a Solidity smart contract.

[1]  K. J. Arrow, “A difficulty in the concept of social welfare,” Journal of Political Economy, vol. 58, no. 4, pp. 328–346, 1950.

[2] M. C. Pease, R. E. Shostak, and L. Lamport, “Reaching agreement in the presence of faults,” J. ACM, vol. 27, no. 2, pp. 228–234, 1980.

[3] Blockchain Proportional Governance Reconfiguration: Mitigating a Governance Oligarchy. D. Tennakoon, V. Gramoli. The 23rd IEEE/ACM International Symposium on Cluster, Cloud and Internet Computing (CCGrid), 2023.
