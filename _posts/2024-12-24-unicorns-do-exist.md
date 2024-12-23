---
layout: post
author: Vincent
tags: verification consensus RWA
---

The best technology does not lead to success! But sometimes it can help turn a company into a unicorn. Indeed, some great technologies did not succeed.  Sometimes this is due to a narrow ecosystem compatibility, sometimes it is due to user inconvenience and sometimes it is due to lack of partnerships. But unicorns do exist as I have witnessed one, but to see one, one has first to avoid these pitfalls.  

As a first example of great technology failures, let us consider one of the most cited scenarios from Betamax developed by Sony. In 1976, Betamax was offering superior quality to the Video Home System (VHS). Yet, it did not have the broad support from video rental stores which in part led to the success of VHS.

At Redbelly, we could have invented the perfect language virtual machine with stronger type safety. However, we would have lost the battle of the ecosystem now that most applications have been compiled into the Ethereum Virtual Machine (EVM) bytecode. A blockchain is less appealing if it offers less applications, this is why we decided to implement the Scalable EVM or SEVM, that supports the exact same bytecode as the EVM [1].  

As a second example, consider the glasses that Google launched in 2013. The product failed to attract mass-market adoption and was discontinued in 2015. Part of the problem was that its built-in camera produced privacy violation fears among users, whereas other AR technology for gaming or professional environments like Microsoft HoloLens have been more successful. Retrospectively, we can attribute the failure of Google glasses to the user inconvenience produced by the technology, it overweight the user convenience of their voice-controlled ubiquitous computer, writing notifications in real time on a wearable display.

Similarly, one of the biggest impediments of blockchain technology has been the lack of user protection. As everyone is pseudonymous or anonymous, there is no accountability and hackers easily steal assets from random users without the fear of having to pay back. These risks have hampered mass adoption. At Redbelly, we bypass this problem by making blockchain comply with regulations: every users has to use a real world identity. This allows to ensure that we are not trading with AI bot, Redbelly could even inform the payer whether there is a real person associated to the recipient address before actioning a payment. By mitigating this risk, Redbelly democratizes the use of blockchain technology.

As a final example, consider HD-DVD in 2006 that was better for cost and production than Blu-ray, however, Blu-ray had a superior storage capacity and support from major studios. Blu-ray became the standard leading to the failure of HD-DVD.
At Redbelly, we could have tried to come up with a lower quality product to reach production readiness quicker. However, even though the unprecedented performance results of our prototype implementation were already presented in 2017 to MIT, Facebook, Visa Research, etc. we focused on improving its quality for 7 years before releasing it in production.

Among other things, we focused on high security and spent three years formally verifying our consensus protocol to drastically mitigate the risks of human errors, that were too common in competing products [2] as we explained in [a previous post](https://gramoli.github.io/2023/12/30/formal-verif-to-the-rescue.html). This led to a much more mature product, which we believe is key to adoption especially in the context of real world assets (RWAs), that depart drastically from Crypto Kitties or NFT memes.

Retrospectively, the decisions of adopting the larger ecosystem of decentralised applications, focusing on user protection and improving the security of our technology before moving it in production have paid off. This required us to first go on the long path of research and exploration before launching our product, where most of the blockchain companies moved to production fast to raise funds that would allow them to improve their product by hiring researchers later on. This has paid off as we have obtained a product whose quality has been recognized almost instantaneously. Within seconds of its public listing our company became a double unicorn valued at more than US$ 2 billion.
The effort is not over and more work is needed to reach the network effect but Redbelly successfully reconciliated blockchain and regulation.  

[1] [Deconstructing the Smart Redbelly Blockchain](https://gramoli.github.io/pubs/2024-SRBB-TC.pdf) D. Tennakoon, V. Gramoli. IEEE Transactions on Computers, DOI:10.1109/TC.2024.3475573, 2024.

[2] [Holistic Verification of Blockchain Consensus](https://gramoli.github.io/pubs/DISC22-holistic-verification.pdf) N. Bertrand, V. Gramoli, M. Lazić, I. Konnov, P. Tholoniat, J. Widder. 36th International Symposium on Distributed Computing (DISC), 2022.





