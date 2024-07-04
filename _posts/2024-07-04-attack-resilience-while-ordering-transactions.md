---
layout: post
author: Vincent
tags: MEV consensus frontrunning cryptography
---

Front running attacks that are illegal on Wall St. happen all the time on Main St. due to the 
lack of regulation around the blockchain technology. The difficulty, as mentioned in [a previous 
blog post](https://gramoli.github.io/2024/01/07/fair-resource-sharing-using-crypto.html), is that
preventing the reordering of transactions is costly and consists of building transaction 
dependency graphs that may create cylic dependencies. We have thus published two scientific articles 
to address these two problems [1,2].

The first of these two research achievements, proposing an optimal protocol, was published at the 
[54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN)](https://dsn2024uq.github.io/).
It was described in [a previous blog post](https://gramoli.github.io/2024/05/05/optimal-prevention-of-reordering-attacks.html).
The second of these two achievemnts, published at the [9th European Symposium on Research in Computer Security 
(ESORICS)](https://esorics2024.org/), limits the power of the adverary to attack fair separability, a 
property that reduces the cyclic dependencies while preventing reorderings.

![ESORICS 2024](/img/ESORICS24.png){: width="500" }

In particular, we observed that the Best Paper at OSDI'20 [3] that proposed a property called
ordering linerizability would only apply ordering constraints to committed transactions. 
This means that even transactions that were assigned a correct order by the correct participants 
may never be committed. 

Previous alternatives implement a different property called *fair separability* and, furthermore, 
it also achieves resilience to downgrade attacks. However, to do so, processes must rebroadcast 
each transaction they observe. As a result, these solutions output every transaction observed 
by any correct process, even if it was sent by a Byzantine process to a single correct process.
This gives an unfair advantage to malicious participants that only needs to use a constant amount of
network resources to order their transactions where correct processes needs a linear amount of 
network resources.

We show in [2] that this drawback can be avoided while implementing fair separability.
Our solution is an implementation of fair separability that preserves the property we call 
*chain quality*: submitting a transaction has the same asymptotic cost for all processes
and the output requires input from a quorum of processes. In addition, we show that fair 
separability can be achieved without having to output
every transaction observed by a correct process, which is of independent
theoretical interest.

Compared to existing fair separability solutions, our protocol has the same
cost per transaction for both correct and Byzantine processes and decides its
output using a quorum of processes. As a result, it provides resilience to 
chain-quality attacks. 


[1] [AOAB: Optimal and Fair Ordering of Financial Transactions](https://gramoli.github.io/pubs/DSN24_AOAB_preprint.pdf). 
V. Gramoli, Z. Lu, Q. Tang, P. Zarbafian. 
54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN), 2024.

[2] [Resilience to Chain-Quality Attacks in Fair Separability](https://gramoli.github.io/pubs/ESORICS24-FairSeparability.pdf).
V. Gramoli, Z. Lu, Q. Tang, P. Zarbafian. 
9th European Symposium on Research in Computer Security (ESORICS), 2024.

[3] [Byzantine ordered consensus without byzantine oligarchy](https://www.usenix.org/system/files/osdi20-zhang_yunhao_0.pdf). 
Y. Zhang, S. Setty, Q. Chen, L. Zhou, L. Alvisi. 
In 13th USENIX Symposium on Operating Systems Design and Implementation (OSDI), pages 633–649, 2020.
