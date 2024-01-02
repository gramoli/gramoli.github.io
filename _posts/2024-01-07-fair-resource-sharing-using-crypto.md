---
layout: post
author: Vincent
tags: MEV, consensus, frontrunning, cryptography
---

With the digital revolution, services are becoming decentralised. This trend is driven by users wanting to retain the custody of 
their personal identifiable information or data, the growing use of Web3 over the Internet, and the desire for nations to become 
self-sovereign in a globalised world. In this decentralised setting, a tech-savvy participant regularly front-runs a common 
victim to get an unfair access to resources before her victim. This unfair access impacts financial resources every day but could 
soon generalize to resources that are vital to a nation's economy (e.g., energy). Here we discuss the problem and list 
recent cryptographic solutions to ensure a fair access to resources.

![The front-running attack](/img/frontrunning.png){: width="500" }

As an example, consider the figure above where Alice, who needs to invest her pension, requests a stock order. A malicious user, 
say Malory, who learns about Alice's order, can unfairly buy the same stocks ahead of Alice and resell them, 
at a higher price, to Alice. The crux of the problem is the lack of fair ordering between requests issued by decentralised participants. 
Networks do not even guarantee the triangle inequality [3] as Malory might access a remote resource faster than Alice by routing her request through Bob. 

Decades of research results on the consensus problem are helpless, precisely because they ensure that “some” request order is consistent 
across the network, but do not dictate “which” order. This is why, cryptographic techniques are necessary to guarantee that the order in which 
requests are executed is provably the order in which they were received by the network. Pompe [1] introduced recently a new ordering property, yet 
it only deals with committed commands and disregards the ordering compared to aborted commands.

We have thus provided an alternative solution called Lyra [2] which uses the network delays measured between processes so that processes can predict 
the times when their commands are received by other processes. It reduces the latency of Pompe but just like Pompe can let front running attacks happen. 
A more recent approach calls Aion [3] prevents front running attacks (and sandwich attacks) completely by using trusted execution environments. 
Ensuring this ordering of transactions promises to give users a fair access to shared resources, this has become a vital problem.

[1] Y. Zhang, S. Setty, Q. Chen, L. Zhou, and L. Alvisi. [Byzantine ordered consensus without byzantine oligarchy](https://www.usenix.org/system/files/osdi20-zhang_yunhao_0.pdf). In OSDI, pages 633–649, 2020.

[2] P. Zarbafian and V. Gramoli. [Lyra: Fast and scalable resilience to reordering attacks in blockchains](https://gramoli.github.io/pubs/IPDPS23-Lyra.pdf). In Proceedings of the IEEE International Parallel & Distributed Processing Symposium (IPDPS), 2023.

[3] P. Zarbafian and V. Gramoli. [Aion: Secure transaction ordering using tees](https://gramoli.github.io/pubs/ESORICS23-Aion.pdf). In ESORICS, 2023.
