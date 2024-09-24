---
layout: post
author: Vincent
tags: synchrony DBFT centralisation
---

Blockchain promises to prevent global crashes like the CrowdStrike outage that affected 8.5 millions of computers around the world.
Intuitively, this is due to the decentralisation of the blockchain software and the diversity of nodes participating in the blockchain network.
Interestingly, the first thorough investigation of the blockchain tolerance to failures [1] has just revealed surprising results depending 
on the considered blockchain protocol: While Redbelly could tolerate failures, Avalanche and Solana could not.

STABL, which stands for Sensitivity Testing and Analaysis for BLockchain, is an open source tool recently developed in collaboration with 
the University of Sydney, Redbelly Network and the Swiss Federal Institute of Technology of Lausanne to evaluate the 
blockchain tolerance to four classes of failures: transient node failures, permanent failures, transient network partitions and Byzantine failures.
STABL has been validated empirically with five blockchains---Algorand, Aptos, Avalanche, Redbelly and Solana. 

The results of this study indicates that Avalanche and Solana cannot recover from more than a third of their nodes failing temporarily or 
when a partition delays the communciation between a third of the network and the rest of the network. Although the model in which some blockchain 
protocols are supposed to work is unclear, such a lack of recovery if surprising: First, we know that under a strong synchrony assumption where 
all messages are delivered in a maximum amount of time, one should be able to implement a blockchain protocol that solves consensus despite even a third of 
nodes experiencing a crash failure. Second, even in the same synchronous setting, 
a blockchain protocol equipped with signatures can also tolerate more than a third of arbitrary failures [2].
Third, we know that under partial synchrony (i.e., even if the bound 
on the message delays is unknown) like it is the case in the Internet, then we can solve consensus as long as node communication is re-enabled after 
failures for long enough [3]. This is why it is surprising to find blockchains that cannot tolerate benign transient failures.

Another result indicates that some design decisions in blockchain software prevent them from being resilient to permanent failures. 
In particular, the leader-based design that one can find in Aptos hampers the recovery of the 
protocol after permanent node failures. This is similar to the previous observations that HotStuff-like consensus protocols, like DiemBFT, 
suffer from faulty leaders. Algorand acts differently, as it selects a sample of nodes among which crash nodes tend to increase the latency, 
hence impacting the resilience of Algorand.  
By contrast, Redbelly builds upon the DBFT leaderless consensus protocol, hence its protocol can progress despite the failure 
of a single node and is thus resilient to a small portion of permanent failures.

![Blockchain Sensitivity to Failures](/img/radar.png){: width="500" }

Overall and as depicted in the above figure, the results show that some blockchains, like Avalanche and Solana, cannot recover from transient node 
failures or transient link failures. Some other blockchains show different levels of resilience to permanent benign failures, with fast stabilitsation 
for Redbelly and slower stabilisation in Algorand and Aptos. Finally, Byzantine fault tolerance, evaluated with redundant transaction requests does 
not seem to impact the blockchains protocols as much as other types of failures.

[1] STABL: Blockchain Fault Tolerance. Vincent Gramoli and Rachid Guerraoui and Andrei Lebedev and Gauthier Voron. 
Technical report 2409.13142, arXiv, 2024.

[2] The Byzantine Generals Problem. Leslie Lamport, Robert Shostak, and Marshall Pease.
ACM TOPLAS, 1982.

[3] Consensus in the Presence of Partial Synchrony. Cynthia Dwork, Nancy Lynch, Larry Stockmeyer.
J. ACM, 1988.

