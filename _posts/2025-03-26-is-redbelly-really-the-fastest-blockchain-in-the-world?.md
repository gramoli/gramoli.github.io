---
layout: post
author: Vincent
tags: performance finality
---


As Chainspect ranked Redbelly as the fastest blockchain they evaluated, it is interesting 
to understand what it means, and why this announcement complements the previous scientific 
publications that already demonstrated Redbelly’s superior performance. 
In retrospect, it is not so surprising given that Redbelly leverages collaboration of 
machines [[2]](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf) rather than adopting the competitive model of traditional blockchains.

![Chainspect dashboard screenshot](/img/chainspect.png){: width="500" }

### The Problem with Performance Claims in Blockchain

Many blockchain projects boast about high-speed performance in marketing materials, 
social posts, and blogs. However, these claims are rarely backed by transparent, 
reproducible data. When researchers attempt to validate these numbers, they often 
find significant discrepancies. In fact, a scientific study found that the actual 
performance of many blockchains was, on average, just 5% of what was publicly claimed [[1]](https://gramoli.github.io/pubs/Eurosys23-Diablo.pdf).

### Scientific Validation of Redbelly’s Performance

Redbelly is one of the rare blockchains whose performance has been rigorously 
documented in peer-reviewed scientific publications. Evaluations were conducted 
using up to 1,000 machines distributed globally and also with workloads based on 
real-world applications. These results have appeared in leading scientific 
conferences [[2](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf),[3]((https://gramoli.github.io/pubs/IPDPS23-SmartRedbelly.pdf))] and journals [[4](https://gramoli.github.io/pubs/2024-SRBB-TC.pdf)], following extensive expert reviews. This 
process ensures credibility and reflects years of dedicated research and testing.

### Why Documentation and Reproducibility Matter

To properly assess blockchain performance, results must be reproducible. That means 
providing detailed documentation — everything from execution parameters to machine 
specs, network bandwidth, and geographic location. The reason is that environmental 
conditions significantly affect performance.

For instance, our team discovered that a warm-up parameter in Solana could cause
system crashes unless explicitly disabled [[5]](https://arxiv.org/pdf/2409.13142). These are the kinds of issues that happen 
when the parameters in use are poorly documented.

### Understanding Blockchain Performance: Latency vs. Throughput

Blockchain performance is typically measured using two key metrics: latency and throughput.

 * Latency is the time it takes to confirm a transaction — from the time it is issued to the time it is committed.
 * Throughput is the volume of transactions processed per unit of time, often expressed in seconds (TPS)

Think of it like cars on a highway. Latency is the time it takes for a car to travel from point A to point B. Throughput is how many cars can be driven on that road every second. Widening the road increases throughput. Shortening the road reduces latency. But one does not necessarily improve the other.

Both metrics matter. A blockchain can have high throughput but still be unusable if its latency exceeds the settlement time of traditional payment systems.

### Redbelly’s Record-Breaking Performance

Redbelly has set performance records that are not only impressive — but also scientifically verified.

* [660,767 TPS with 3,935 ms latency](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf)
* [666,970 TPS with 4,483 ms latency](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf) 
Note that these numbers are documented in a scientific article of the flagship security conference [[2]](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf).

Beyond these scientific performance results:

Redbelly was the only evaluated blockchain to successfully commit all transactions from real-world workloads (e.g., NASDAQ and Uber data) while running decentralized applications [[4]](https://gramoli.github.io/pubs/2024-SRBB-TC.pdf).
A third-party monitoring firm confirmed that Redbelly achieved the highest maximum throughput among all evaluated blockchains in production: [73,158 TPS](https://chainspect.app/dashboard?order=desc&sort=maxTps), with a minimum finality time of 0 seconds.
ChainSpect has verified Redbelly holds the fastest theoretical throughput: [666,970 TPS](https://chainspect.app/dashboard?order=desc&sort=theorTps)—#1 across all evaluated blockchains.

### Conclusion

Now you know what to look for if you hear a new blockchain reaching high performance. Make sure that the 
results are scientifically checked, that the experiments are carefully documented, that 
the workload is realistic, and that both throughput and latency results are provided.

[A copy of this post is available on Medium](https://medium.com/@redbellyblockchain/768157f6309e).

### References

[1] [Diablo: A Benchmark Suite for Blockchains](https://gramoli.github.io/pubs/Eurosys23-Diablo.pdf). V. Gramoli, R. Guerraoui, A. Lebedev, C. Natoli, G. Voron. 18th ACM European Conference on Computer Systems (EuroSys), 2023.

[2] [Red Belly: A secure, fair and scalable open blockchain](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf). T Crain, C Natoli, V Gramoli. IEEE Symposium on Security and Privacy (S&P), 466–483, 2021.

[3] [Smart Redbelly Blockchain: Reducing Congestion for Web3](https://gramoli.github.io/pubs/IPDPS23-SmartRedbelly.pdf). D. Tennakoon, Y. Hua, V. Gramoli. 37th IEEE International Parallel & Distributed Processing Symposium (IPDPS), 2023.

[4] [Deconstructing the Smart Redbelly Blockchain](https://gramoli.github.io/pubs/2024-SRBB-TC.pdf). D. Tennakoon, V. Gramoli. IEEE Transactions on Computers, DOI:10.1109/TC.2024.3475573, 2024.

[5] [Stabl: The Sensitivity of Blockchains to Failures](https://arxiv.org/pdf/2409.13142). Vincent Gramoli, Rachid Guerraoui, Andrei Lebedev, Gauthier Voron. arXiv:2409.13142, 2024.
