---
layout: post
author: Vincent
tags: verification cryptography
---

As the Smart Redbelly Blockchain has just been accepted for publcation in the flagship journal of Computer Science, IEEE TC [1], 
now is the right time to look back at what makes Redbelly Blockchain unique.
The original idea of Redbelly Blockchain was to make blockchain secure and efficient.
We achieve efficiency by introducing collaboration: Instead of letting participants compete to insert the next block, our collaborative approach leveraged their resources to scale.
Although seemingly simple, this idea took lawyers 6 years to recognise its novelty and we are happy that the US Patent and Trademark Office has finally approved our corresponding patent. 

![The collabortive blockchain patent has just been approved in the US](/img/patent.png){: width="500" }

This collaborative feature is how the first version of Redbelly turned blockchain into a scalable software [2]. But there was another novelty that had impact: optimising validations. 
Back in 2017, we noted in our early experiments that the CPU consumption involved by validating, in particular, the cryptographic signature of transactions was significant. 
In an effort to optimise this verification process we identified the redundant validations of transactions of most blockchains, including Ethereum. 
Transactions are validated while being propagated individually throughout the network and while being propagated within blocks throughout the network. 
This redundant validation was unnecessary, and the formal treatment of Redbelly led to identify the necessary and sufficient conditions under which the transaction validations were needed. 

The paper features other systems optimisations around Inputs/Outputs that helped us bypass out-of-memory errors or how decoupling could help boosting performance even further.
It also presents some of the trials that we conducted by decoupling the SEVM or the Scalable version of the Etherum Virtual Machine execution from the consensus protocol execution on distinct machines.

But one of the most striking results is probably the performance comparison of Algorand, Avalanche, Diem, Ethereum, Quorum, Solana, Smart Redbelly (SRBB) and the naive implementation of an EVM coupled with the model checked blockchain consensus protocol, DBFT, on realistic applications.
These extensive experiments building upon the Diablo benchmark suite [3] demonstrated empirically that not only Redbelly is the only one of these tested blockchains that can commit all transactions of an Exchange and a Mobility decentralised applications, but it does so the fastest. 
These results build upon a long series of research work, on the DBFT consensus protocol, the collaborative blockchain [2], formal verification, and integration of the language virtual machine to support smart contract execution [4].

To conclude, after almost a decade of work on trying to make blockchains more secure and efficient, we have finally demonstrated that collaboration was the way to proceed.
Not only did this inherently solve the scalability problem that plagued blockchains but it has just been recognised as a novel patented idea and allowed to support the 
demand of realistic decentralised applications. Now that scalability has been solved at layer-1, the future of blockchains is bright.

[1] D. Tennakoon, V. Gramoli. [Deconstructing the Smart Redbelly Blockchain](https://gramoli.github.io/pubs/2024-SRBB-TC.pdf). 
IEEE Transactions on Computers, DOI:10.1109/TC.2024.3475573, 2024.

[2] T Crain, C Natoli, V Gramoli. [Red Belly: A secure, fair and scalable open blockchain](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf). IEEE Symposium on Security and Privacy (S&P), 466-483, 2021.

[3] V. Gramoli, R. Guerraoui, A. Lebedev, C. Natoli, G. Voron. [Diablo: A Benchmark Suite for Blockchains](https://gramoli.github.io/pubs/Eurosys23-Diablo.pdf). 18th ACM European Conference on Computer Systems (EuroSys), 2023.

[4] D. Tennakoon, Y. Hua, V. Gramoli. [Smart Redbelly Blockchain: Reducing Congestion for Web3](https://gramoli.github.io/pubs/IPDPS23-SmartRedbelly.pdf). 37th IEEE International Parallel & Distributed Processing Symposium (IPDPS), 2023.
