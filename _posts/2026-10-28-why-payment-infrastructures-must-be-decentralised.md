---
layout: post
author: Vincent
tags: centralisation finance finality
---

When a Google Cloud data centre in Europe suffered a major outage recently, millions of Revolut customers abruptly lost access to their own money [[1]](https://www.theguardian.com/business/2026/oct/20/revolut-down-app-cards-service-disruption). Cards were declined at checkout terminals, transfers stalled, and account balances became unreachable. 

The outage was not confined to Europe. Customers in Australia—on the other side of the world from the affected facility—found themselves unable to pay for groceries, commute, or settle bills. A single regional failure in a cloud provider's infrastructure reached across hemispheres and froze daily commerce for people thousands of kilometres away.

Nearly four decades ago, Turing Award laureate Leslie Lamport offered a definition that captures this exact failure mode:

> *"A distributed system is one in which the failure of a computer you didn’t even know existed can render your own computer unusable."*

Modern fintech platforms look borderless on a smartphone screen, yet most rely on centralised cloud architectures or fragile chains of regional dependencies under the hood. When an Australian user taps a card or submits a payment, the request often traverses authentication services, ledger databases, and API gateways hosted in a handful of data centres overseas. If one of those remote facilities goes dark, the user's phone might as well be disconnected. Centralising critical financial state in one provider or region turns a local hardware or network incident into a global payment outage.

### The Structural Flaw in Centralised Payment Rails

Traditional and neo-banking payment rails treat availability as an operational problem to be solved with backup servers and failover scripts. In practice, active-passive database replication and single-cloud deployments share correlated failure points: a misconfigured routing table, a cooling failure in a single availability zone, or a regional cloud control-plane outage brings the service down until engineers intervene.

For a payment system to be genuinely resilient, fault tolerance cannot be an afterthought bolted onto a centralised database. The system must continue processing and settling transactions even while individual nodes, datacentres, or entire cloud regions are offline.

### How Redbelly Network Solves This

At the University of Sydney and Redbelly Network, we spent years researching and building a system designed specifically to eliminate single points of failure without sacrificing the speed and certainty that payments require. Redbelly Network replaces centralised payment ledgers with a purpose-built, decentralised network anchored by two core properties: **true decentralisation** and **instant finality**.


![Centralisation can block cashless payments](/img/revolut.png){: width="500" }

#### 1. Decentralisation Across Geographies and Operators

Redbelly does not depend on any single data centre, cloud vendor or jurisdiction [[2]](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf). The network is maintained by a geographically distributed set of independent governors and candidate nodes spanning multiple regions and infrastructure providers. 

Through our Democratic Byzantine Fault Tolerant (DBFT) consensus protocol [3], the network continues to reach agreement and process transactions seamlessly even if a subset of nodes fails, loses connectivity or behaves maliciously. If a datacentre in Europe goes offline, transactions initiated in Sydney—or anywhere else—continue to execute without interruption. No remote computer you have never heard of can hold your funds hostage.

#### 2. Instant, Deterministic Finality

A common criticism of first-generation blockchains is that they trade centralisation for slow, probabilistic settlement. Waiting minutes for block confirmations—or risking a chain reorganisation that reverses a payment after the customer has walked out of a shop—is unusable for retail and institutional payments.

Redbelly’s DBFT consensus is deterministic and leaderless. Rather than relying on a single leader node (which itself can become a bottleneck or point of failure) or probabilistic proof-of-work forks, collaborative consensus combines valid proposals from participating nodes and finalises transactions in seconds. Once a transaction is committed on Redbelly, it is irrevocable. There are no forks, no rollbacks, and no waiting for "six confirmations". Both the payer and the merchant receive mathematical certainty that the settlement is final at the moment of payment.

### Building Financial Infrastructure That Stays On

Money is public utility infrastructure. A payment rail that stops working in Sydney because a server rack failed in Europe is not fit for a connected global economy. 

By combining Byzantine fault-tolerant decentralisation with deterministic instant finality, Redbelly Network ensures that financial applications stay live, responsive, and final—regardless of which data centre goes dark next.

### References

[1] The Guardian. [Google cloud failure hits millions as UK courts and banks knocked offline](https://www.theguardian.com/business/2026/oct/20/revolut-down-app-cards-service-disruption). 20 October 2026.

[2] [Red Belly: A secure, fair and scalable open blockchain](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf). T Crain, C Natoli, V Gramoli. IEEE Symposium on Security and Privacy (S&P), 466-483, 2021.

[3] DBFT: Efficient Leaderless Byzantine Consensus and its Application to Blockchains. T. Crain, V. Gramoli, M. Larrea and M. Raynal. 2018 IEEE 17th International Symposium on Network Computing and Applications (NCA), Cambridge, MA, USA, 2018, pp. 1-8, doi: 10.1109/NCA.2018.8548057.
