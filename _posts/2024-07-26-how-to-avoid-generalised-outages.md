---
layout: post
author: Vincent
tags: centralisation governance
---

The dependence of critical industry sectors on any specific technology is dangerous. It 
translates into assuming that health services, distribution of goods, transportation 
can serve us as long as a single product, like Microsoft Windows, does not experience 
a bug. This is giving way too much trust to any central vendor, let alone a single 
product.

The outage from last Friday that affected computers using Microsoft Windows is an 
illustration of this problem. Microsoft uses an American security company, CrowdStrike, 
to apply security patches at its operating system level. Once a programmer introduced a 
null pointer in a patch of the Crowdstrike Falcon product, 8.5 millions computers running
Windows version 7.11 or above crashed, sometimes showing the infamous BSOD (blue screen 
of death) each time the machine would reboot. 

This outage led airlines to ground more than 5,000 flights worldwide, the Australian NSW 
state to lose AU$200M in revenue, hundreds of thousands of businesses to stop trading, 
including general practitioners, pharmacies, and hospitals who had to postpone 
appointments. Outside the health and transportation sectors, the economy at large was 
impacted as businesses had to revert back to paper and pen receipts
while they were unable to process transactions on a computer.

Decentralisation has been key to remove this dependence for decades now: Replication is 
a well established strategy for companies to recover from disasters [1], cloud computing offers the ability for an institution to spawn machines running operating systems from different vendors, and blockchains [2] distribute the computation of payments over an heterogeneous set of machines by removing the trust in central financial institutions. 

The idea behind decentralisation is simple: a decentralised service runs on multiple 
machines so that even if one of the machines experiences a bug, an outage or gets 
compromised, it is not a problem because the decentralised service keeps running on the 
other unaffected machines. The intricacy lies, however, in the underlying distributed 
protocols that guarantee this smooth operation at all times, an area of research called 
distributed computing or distributed systems.

With the advent of Web3, services are naturally becoming decentralised. Besides payments, 
distributed ledgers can now execute arbitrarily complex programs, offering various types 
of services. In a recent research publication [3], we even used a decentralised 
transportation system to evaluate how blockchains could run a mobility service. While 
most modern blockchains suffer from congestion [3], a more recent blockchain, called 
Redbelly Blockchain could run this and other real world applications efficiently in a 
highly decentralised fashion [4], with machines running on different continents. This 
line of work, on tackling dependability through decentralisation, is getting traction 
in the scientific community. Recently a ‘Best Paper’ was awarded by the main scientific 
conference of the Dependable community for our publication on the ‘Zero Loss 
Blockchain’ [5] that expands on this scalable blockchain system.

As this blockchain software is moving into production, now is probably the time to deploy 
more critical infrastructures on this mature decentralised technology.

[A copy of this post is available on Medium.](https://medium.com/@redbellyblockchain/b2e8f0df9245?source=friends_link&sk=645b087ef135d51a4867d9382ea18120)

[1] Vincent Gramoli, Guillaume Jourjon, Olivier Mehani. Disaster-Tolerant Storage with 
SDN. Proceedings of the International Conference on Networked Systems (NetSys) 2015 - p293-307.

[2] Satoshi Nakamoto. 
[Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf). 2008.

[3] V. Gramoli, R. Guerraoui, A. Lebedev, C. Natoli, G. Voron. 
[Diablo: A Benchmark Suite for Blockchains](https://gramoli.github.io/pubs/Eurosys23-Diablo.pdf). 
18th ACM European Conference on Computer Systems (EuroSys), 2023. 

[4]  D. Tennakoon, Y. Hua, V. Gramoli. 
[Smart Redbelly Blockchain: Reducing Congestion for Web3](https://gramoli.github.io/pubs/IPDPS23-SmartRedbelly.pdf). 
37th IEEE International Parallel & Distributed Processing Symposium (IPDPS), 2023.

[5] A. Ranchal-Pedrosa, V. Gramoli. 
[ZLB: A Blockchain to Tolerate Colluding Majorities](https://gramoli.github.io/pubs/DSN24-ZLB.pdf). 
54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN), 2024.
