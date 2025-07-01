---
layout: post
author: Vincent
tags: governance security
---

Redbelly offers fixed transaction fee. This might look counter-intuitive as its native coin, RBNT, is subject to volatility like any other chain.
This is also surprising as well, given that to our knowledge no other blockchain can offer fixed price, and this is known to be a highly desirable feature so say the least.
Afteall any company needs to budgetize its financial year ahead, simply to make sure it will not go bankrupt before the end of the year.
This has prevented a lot of companies from using blockchain technologies, as they were not able to anticipate the cost the usage of blockchain will incur to their business, to their partners, or unabel to project 
the cost for their customers.

The secret recipe of Redbelly is to fix its native transaction fee to 1 cent of a US dollar.
And Redbelly does not need to build a stable US dollar coin backed where every stablecoin is backed by a FED-issued US dollar to achieve this. 
Instead, Redbelly simply relies on a distributed set of exchange rate sources and adjusts the gas price in real time.
The result is that 21,000 gas, which is roughly the amount of gas needed by a native transfer is about US$0.01 at all times.

This is radical shift in the way we use blockchain. One need enough inherent value in their wallet to issue a transaction as the amount of RBNT needed may increase.
But the business does no longer have surprises. It can budgetize its expenses ahead of time. 
It can predict its PNL by computing it based on the volume of purchases because the fee associated with every purchase becomes predictable.
This simplifies economic relationships: one can predict revenues based on volume targets.

It is fair to ask why not simply using an oracle that would give the exchange rate to adjust gas price in real time.
The problem is not that simple and goes back to the initial motivation for blockchain.
Remember in 2020 when ChainLink misreported the XAG/USD exchange rate? Traders exploited this human error to profit US$36K [1].
The issue is that trusting a single source defeats the purpose of using a blockchain: your distributed ledger remains at risk if you need to trust 
a single source of truth or Oracle.

![Dictatorship](/img/formal-verif.png){: width="500" }

At Redbelly we use a distributed set of sources so that we can tolerate the failure of a portion of them.
The key idea relies on the observation that the consensus cannot be solved in a general open network like the Internet when a third of the participants are faulty.
Since consensus is required to implement a blockchain [2], we know that we need less than a third of the consensus participant to be faulty for the blockchain to work.
Of course there are variants that accept transient forks (disagreements) in order to tolerate even a majority of failures [3], but it comes to offering certainties there is no solution.



Redbelly uses *n* exchange rate sources out of which less than *n/3* can be faulty. Using well-known Byzantine fault tolerant techniques, 
it extract the median of the values it receives from these striclty more than *2n/3* sources.
As at most *t<n/3* sources can report wrong estimates, we know that the median estimate among all estimates is either a correct estimate or something very close to a correct estimate because 
the median is neither one of the *t* smallest estimates nor one of the *t* largest estimates.



[1] ChainLink Improving and Decentralizing ChainLink feature release and network upgrade process. 
https://blog.chain.link/improving-and-decentralizing-chainlinks-feature-release-and-network-upgrade-process/
Accessed: 1st July 2025.

[2] Consensus number of cryptocurrency.

[3] ZLB
