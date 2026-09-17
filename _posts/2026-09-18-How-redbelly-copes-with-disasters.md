---
layout: post
author: Vincent
tags: DBFT centralisation security
---

While AWS has just lost data, it is interesting to compare cloud computing to modern blockchains with deterministic guarantees.
Redbelly Network mainnet is a deterministic blockchain network that has been running without interruption since December 2024. 
During these last 21 months, not only Redbelly did not lose any data, but it did not suffer from any service disruption. 
It is interesting to understand what this means and how this is achieved.

### The Amazon Data Loss

Two days ago, Amazon Web Services (AWS) said it could not restore some customer data from its Gulf facilities. 
Iranian drone strikes had hit AWS sites in the UAE and Bahrain this spring. Data hosted only in Bahrain's ME-SOUTH-1 region, 
or only in UAE zone mec1-az2, could not be brought back. Amazon said the Bahrain damage crossed several availability zones (AZs) and 
exceeded what regional and multi-AZ services are designed to withstand.

A cloud region is a cluster of buildings in one country. Multi-AZ replication keeps a service running when a rack or a hall 
fails. A strike that takes the region takes those copies with it. Customers who stored state only in those Gulf locations 
lost that state. The three-nines SLA for ordinary cloud outages never covered a destroyed region, an unfortunate consequence 
of an insufficient disaster recovery plan.

### Blockchain's decentralisation is not always sufficient

By contrast, Redbelly Network has been designed to recover from the most drastric disasters by diversifying the jurisdictions,
the machines providers, the institutions on which it runs. This is what led Redbelly Network to survive cloud provider 
global network outages or bugs as previously discussed [here](https://gramoli.github.io/2024/07/26/how-to-avoid-generalised-outages.html).

A public ledger helps only when it stays available under faults. Solana, another blockchains that does not offer the same properties as Redbelly,
is known to have experienced nine outages between September 2021 and February 2023, lasting 154.5 hours [1]. Availability sat below 99 
percent, which fails to reach two nines. Traditional cloud services, like the ones that lost data, quote at least three nines. 
The same study showed Solana unable to recover from transient node failures. The empirical comparison of blockchain fault tolerance [1] led us to call 
Redbelly the *fault tolerant blockchain* in this previous [post](https://gramoli.github.io/2024/09/25/the-fault-tolerant-blockchain.html).

### Redbelly disaster recovery in action

Redbelly treats a destroyed region as a fault the protocol is specified to survive. Democratic BFT, the core consensus protocol of the 
blockchain that has been formally verified with model checking [2], keeps committing even in these adversarial contexts. Production 
replicas sit with independent operators across continents and across clouds. On 
13 June 2025 Google Cloud failed globally for up to three hours. Redbelly replicas were then on AWS, GCP and OVH. At the trough, 
95 of 108 probes still answered, and the chain kept committing superblocks. Among the five chains STABL tested, only Redbelly 
stayed insensitive to isolated crashes, in part due to its fully decentralised (a.k.a., *leaderless*) design as we explained 
[previously](https://gramoli.github.io/2024/01/19/why-blockchains-were-actually-centralised.html). 

Availability is a copy of state that still answers after the building is gone.

[1] [STABL: The Sensitivity of Blockchains to Failures](https://gramoli.github.io/pubs/2025-Middleware-Stabl.pdf). V. Gramoli, R. Guerraoui, A. Lebedev, G. Voron. 
26th ACM/IFIP International Middleware Conference (Middleware), 2025, Best Student Paper Award.

[2] [Holistic Verification of Blockchain Consensus](https://gramoli.github.io/pubs/formal-verif.pdf). N. Bertrand, V. Gramoli, M. Lazić, I. Konnov, P. Tholoniat, 
J. Widder. 36th International Symposium on Distributed Computing (DISC), 2022.
