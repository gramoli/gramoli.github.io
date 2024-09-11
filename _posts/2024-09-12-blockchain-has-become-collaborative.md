---
layout: post
author: Vincent
tags: centralisation consensus
---

With the new release of the Redbelly Network, blockchain has entered a new era: collaboration. Since its inception, the blockchain protocol has always been built on competition: as only one of the validator nodes could win the lottery by imposing its block to the rest of the system. This competition led to adversarial effects over time. As the number of validators entering the competition kept growing as a result of the built-in incentives, so did the amount of wasted resources. As a result, performance would never increase with more validators.

Back in 2021, the original Redbelly paper was published in the flagship security conference, IEEE S&P [1], to present a collaborative alternative that would allow blockchain to scale. The idea, also called the superblock optimisation, is very simple and was already discussed in an earlier [blog post](https://github.com/gramoli/gramoli.github.io/blob/main/_posts/2024-01-19-why-blockchains-were-actually-centralised.md). In short, what if instead of having a competition between validators resulting in a single block among thousands of proposed blocks, we could leverage a collaboration among these validators that would then combine all the acceptable blocks into a superblock?

Back then, we already knew that this collaboration was key to achieving scalability. After all it makes sense, if you append a superblock that results from the combination of as many blocks as you have validators, then the number transactions you can commit per unit of time will grow linearly with the number of validators. In particular, the research prototype of the Redbelly Network at the time scaled to one thousand machines spread all over the world, the largest blockchain experiments ever made at the time. Moreover, the performance this blockchain delivered on only 300 nodes was around 660,000 transactions per second.

![Scalability](/img/scalability.png){: width="500" }

Now turning a research prototype into a production system is not an easy task, and one problem we faced was the following: How can all validators that contribute be rewarded? Traditional blockchains reward the only contributing validator with the fees of the transactions within its block. With the superblock optimisation, you would then need to reward hundreds if not thousands of validators for their contributions each time there is a new superblock. It would be unfair for Redbelly not to reward all these validators simply because they are too many. After all they are the ones offering resources to make Redbelly scale where other blockchains would simply become congested.

Today, we have finally solved this problem. Since Redbelly offers complex smart contracts implemented in Solidity, we simply encapsulated the logic of the rewarding of all validators to a dedicated smart contract. This means that the transaction fees within a superblock are simply transferred to a single smart contract address, just like it would be done in the classic competitive approach. Later, it is the task of the smart contract to fairly split the reward among the collaborating validators. This way, we get the best of both worlds: the Redbelly Network scales well by benefiting from this collaboration and the transaction fees are rewarded fast without delaying the creation of new blocks.

[1] [Red Belly: A secure, fair and scalable open blockchain](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf). T Crain, C Natoli, V Gramoli. IEEE Symposium on Security and Privacy (S&P), 466-483, 2021. 
