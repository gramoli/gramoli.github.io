---
layout: post
author: Vincent
tags: finality security synchrony finance centralisation governance
---

Redbelly offers fixed transaction fees. This might look counter-intuitive as its native coin, RBNT, can be subject to high volatility like any other cryptocurrency. And to our knowledge, no other blockchains offer fixed price, even though this is known to be a highly desirable feature. Afterall any company needs to budgetize its financial year ahead, simply to make sure it will not go bankrupt before the end of the year. Prior to this, varying fees have prevented companies from using blockchain technologies, as they were not able to anticipate the usage cost for their partners, their customers or themselves.

### Predictable Transaction Fees

The secret recipe of Redbelly is to fix its native transaction fee to 1 cent of a US dollar.
And Redbelly does not need to build a stable US dollar coin where every stablecoin is backed by a FED-issued US dollar to achieve this. 
Instead, Redbelly simply relies on a distributed set of exchange rate sources and adjusts the gas price in real time.
The result is that 21,000 gas, which is roughly the amount of gas needed by a native transfer is about US$0.01 at all times.

This is a radical shift in the way we use blockchain. A user needs enough inherent value in their wallet to issue a transaction as the amount of RBNT needed may increase if the value of RBNT decreases.
But businesses do no longer have surprises: they can budgetize their expenses ahead of time. 
They can predict their PNL based on the volume of purchases because the fee associated with every purchase becomes predictable.
This simplifies economic relationships: one can predict profits and losses based on volume targets.

### The Single Point of Failure Problem

It is fair to ask why not simply using an oracle that would give the exchange rate to adjust gas price in real time.
The problem goes back to the initial motivation for blockchain.
Remember in 2020 when a system using ChainLink misreported the XAG/USD exchange rate [1]:  
Traders exploited this human error to extract US$36K. The issue is that trusting a single source defeats the purpose of using a blockchain: your distributed ledger remains at risk if you need to trust a single source of truth or oracle.

### A Distributed Computing Problem

At Redbelly we use a distributed set of $n$ sources or nodes so that we can tolerate the failure of a portion of them.
The key idea relies on the combination of two observations: 
- one needs to solve the consensus problem to design a correct blockchain [2,3,4];
- to solve the consensus problem in an open network like the Internet you need *n>3t+1* nodes where up to *t* are faulty [5].
The conjunction of these two observations implies that a blockchain needs *n>3t+1* nodes to work correctly.
Of course there are blockchain solutions that tolerate disagreements (called forks) in order to tolerate even a majority of failures [6], but they cannot guarantee that a transaction you see is there to stay.

![Oracles](/img/oracles.png){: width="500" }

As none of these sources/nodes may report the exact same value because exchange rates are moving all the time, we need to refine the problem of identifying the right exchange rate. The problem becomes to select an exchange rate value $v$ that is bounded 
by two values $v_1$ and $v_2$ reported by correct sources/nodes, more formally, $v_1 \leq v \leq v_2$.  

### Replication to Tolerate Failures and Misinformations

Building upon this observation, Redbelly uses *n* nodes to gather one value each. As we can at best wait for $n-t$ of these nodes to give their value, we only gather the values received from the $n-t$ most responsive nodes. The problem is that these are not necessarily values coming from correct nodes. It could be the case that it took longer than expected to collect the value from a correct node, simply because we cannot predict the time it will take to receive a particular message in an open network like the Internet.

Anyway, as there are at most $t$ faulty nodes, among the collected $n-t$ values we are guaranteed to have $n-2t$ values that come from correct nodes and at most $t$ values from faulty nodes. Since $n>3t$, we thus know that there are a majority of correct values and at most a minority of lies. The median $v$ is thus guaranteed to either: 
- have at most $t$ larger values, implying that there is at least one remaining correct value, say $v_1$, that is lower than $v$.
- have at most $t$ lower values, implying that there is at least one remaining correct value, say $v_2$, that is larger than $v$.

Selecting the median guarantees that $v_1 \leq v \leq v_2$ and is thus the solution to our problem.

### Conclusion

Redbelly ensures the correctness of the exchange rate selection that guarantees that a transaction fee of 21,000 gas corresponds to ~1 cent of a US dollar. Through the selection of the median from $3t+1$ distributed sources, Redbelly tolerates the misinformation or unresponsiveness of $t$ sources, preserving its resilience optimality property. These fixed fees allow businesses and users to anticipate the cost of using the blockchain.

### References

[1] ChainLink Improving and Decentralizing ChainLink feature release and network upgrade process. 
https://blog.chain.link/improving-and-decentralizing-chainlinks-feature-release-and-network-upgrade-process/
Accessed: 1st July 2025.

[2] Antonio Fernández Anta, Kishori Konwar, Chryssis Georgiou, and Nicolas Nicolaou. 2018. Formalizing and Implementing Distributed Ledger Objects. SIGACT News 49, 2 (June 2018), 58–76. https://doi.org/10.1145/3232679.3232691

[3] Michel Raynal. Fault-Tolerant Message-Passing Distributed Systems - An Algorithmic Approach. Springer 2018, ISBN 978-3-319-94140-0, pp. 1-459

[4] R. Guerraoui, P. Kuznetsov, M. Monti, M. Pavlovic and D.-A. Seredinschi. The Consensus Number of a Cryptocurrency. PODC 2019.

[5] Leslie Lamport, Robert Shostak, and Marshall Pease. 1982. The Byzantine Generals Problem. ACM Trans. Program. Lang. Syst. 4, 3 (July 1982), 382–401. https://doi.org/10.1145/357172.357176

[6]  A. Ranchal-Pedrosa, V. Gramoli. [ZLB: A Blockchain to Tolerate Colluding Majorities](https://gramoli.github.io/pubs/DSN24-ZLB.pdf). 54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN), 2024.
