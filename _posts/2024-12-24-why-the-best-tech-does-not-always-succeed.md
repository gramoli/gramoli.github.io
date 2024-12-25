---
layout: post
author: Vincent
tags: verification consensus RWA
---

The best technology does not necessarily lead to success! Indeed, some great technologies did not succeed.  Sometimes this was due to a narrow ecosystem compatibility, sometimes it was due to user inconvenience and sometimes it was due to lower security. But sometimes great tech can help turn a company into a unicorn, a privately-owned company valued at over US$1 billion. I can now say that unicorns exist as I saw Redbelly Network I founded becoming one, but to found a unicorn, one has first to avoid these pitfalls.  

To understand the first of these pitfalls, let us consider one of the most cited failed tech scenarios from Betamax developed by Sony. In 1976, Betamax was offering superior quality to the Video Home System (VHS). Yet, it did not have the broad support from video rental stores which in part led to the success of VHS.

At Redbelly, we could have invented the perfect language virtual machine with smaller word sizes than 256 bits. However, we would have probably lost the battle of the ecosystem now that most decentralised applications have already been compiled into the Ethereum Virtual Machine (EVM) bytecode. A blockchain is less appealing if it offers less applications, this is why we decided to implement the Scalable EVM or SEVM, that supports the exact same bytecode as the EVM [1] rather than coming up with a radically different technology and risking of losing the existing support of an active development community.

To understand the second pitfall, consider the glasses that Google launched in 2013. The product failed to attract mass-market adoption and was discontinued in 2015. Part of the problem was that its built-in camera produced privacy violation fears among users, whereas other AR technology for gaming or professional environments like Microsoft HoloLens have been more successful. Retrospectively, we can attribute the failure of Google glasses to the user inconvenience produced by the technology, it overweight the user convenience of their voice-controlled ubiquitous computer, writing notifications in real time on a wearable display.

Similarly, one of the biggest impediments of blockchain technology has been the fear in the absence of user protection. As everyone is pseudonymous or anonymous, there is no accountability and hackers easily steal assets from random users without having to ever pay back. These risks have hampered mass adoption. At Redbelly, we bypass this problem by making blockchains comply with regulations: every user must have a real world identity. This ensures, for example, that no users are trading with AI bots, Redbelly could even inform the payer whether there is a real person associated to the recipient address before actioning a payment. By mitigating this risk, Redbelly democratizes the use of blockchain technology.

To understand the last pitfall, consider HD-DVD from Toshiba in 2006 that was better for cost and production than Sony's Blu-ray and HD-DVD players were about 3 times cheaper than Blu-ray players. Blu-ray had however a superior storage capacity and a more advanced protection against piracy. 
In 2007, consumers were inundated with marketing about both technologies. But progressively, retailers started offering exclusively Blu-ray disks, this was the case of Target, Blockbuster, Netflix and Wal-Mart. Blu-ray became the defacto standard, hence leading to the failure of HD-DVD when Toshiba and Microsoft stopped manufacturing HD-DVD players.

![Unprecedented performance of the Redbelly technology](/img/throughput.png){: width="500" }

At Redbelly, we could have tried to come up with a lower quality product to reach production readiness quicker. In 2017, the Initial Coin Offering (ICO) craziness was helping companies raise large sums of money based on a white paper promises, sometimes without any clue whether the promise was achievable. The same year, we were instead presenting the largest blockchain experiments, as shown in the picture above, showcasing our technology at MIT, Fracebook, Visa Research, etc. Instead of launching an ICO, we dedicated the next 7 years to improving our blockchain technology before releasing it in production.
Among other things, we focused on high security and spent three years formally verifying our consensus protocol to drastically mitigate the risks of human errors, which were too common in competing products [2] as we explained in [a previous post](https://gramoli.github.io/2023/12/30/formal-verif-to-the-rescue.html). This led to a more mature product, which we believe is key to real world assets (RWAs), that depart drastically from CryptoKitties or NFT memes.

Retrospectively, the decisions of adopting the larger ecosystem of decentralised applications, focusing on user protection and improving the security of our technology before moving it in production have paid off. This required us to first go on the long path of research before launching our product, where most of the blockchain companies moved to production first to raise funds that would allow them to improve their product by hiring researchers later on. This has paid off as we have obtained [a patent](https://gramoli.github.io/2024/11/11/smart-redbelly-a-retrospective.html), and the quality of our product has been recognized. Within seconds of its token generation event, our company became valued at more than US$2 billion. The effort is not over and more work is needed to reach the network effect but Redbelly is now a unicorn.

[1] [Deconstructing the Smart Redbelly Blockchain](https://gramoli.github.io/pubs/2024-SRBB-TC.pdf) D. Tennakoon, V. Gramoli. IEEE Transactions on Computers, DOI:10.1109/TC.2024.3475573, 2024.

[2] [Holistic Verification of Blockchain Consensus](https://gramoli.github.io/pubs/DISC22-holistic-verification.pdf) N. Bertrand, V. Gramoli, M. Lazić, I. Konnov, P. Tholoniat, J. Widder. 36th International Symposium on Distributed Computing (DISC), 2022.





