---
layout: post
author: Vincent
tags: security RWA 
---

This year, the reproducibility crisis was exacerbated as researchers found that only 50% of 30 highly cited AI studies were reproducible [1].
By contrast, we make sure that all our experiments showing the superior fault tolerance of Redbelly are judged reproducible by an independent artifact evaluation committee of scientists. 

### What is Reproducibility?

Reproducibility, which is the ability for different researchers to obtain the same results using the same methods, is vital for scientific advances. Without it, there is no way to understand the factors that lead to the observed results. The documentation cannot explain the results and the results could be equally resulting from an accident. 

### Misleading Results

The race to the most efficient blockchain have led blockchain companies to claim much higher performance than what they could achieve in realistic settings [2]. Most results were communicated through online announcements with limited scientific publications, if any, to back them up. And there is barely any results communicated when it comes to their reliability. Finally, we are not aware of any of these experiments that were judged reproducible.

### Blockchain Fault Tolerance

We recently published Stabl, a framework to evaluate the fault tolerance of blockchains in realistic scenarios. It was described in a previous [blog post](https://gramoli.github.io/2025/05/08/evaluating-blockchain-fault-tolerance-with-stabl.html). 
It shows the following comparison when blockchains are subject to different failure patterns: 

| Blockchain | Attacks | Crash | Churn |  Partition |
|---|---|---|---|---|
| Algorand | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
| Aptos | :x: | :heavy_check_mark: | :x: | :x: |
| Avalanche | :heavy_check_mark: | :x: | :x: | :x: |
| Solana | :heavy_check_mark: | :x: | :x: | :x: |
| Redbelly | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |

Not only were these results peer-reviewed before being accepted for publications in the proceedings of the ACM/IFIP Middleware conference 2025 [3], but the published experimental results have just been judged available, functional and reproducible by an independent artifact evaluation committee of scientists.

The scientific article will be presented in the US on December 2025. It shows that Redbelly is better suited to tolerate the experimented partition, churn, crash and malicious failures than other modern blockchains, like Algorand, Aptos and Solana.

We have of course disclosed the vulnerabilities we found to the developers of the other blockchains. 
Now that blockchain is being used to tokenise real world assets, it is now time for reproducibility to become a de facto principle when communicating experimental results of this technology.

[1] [The Unreasonable Effectiveness of Open Science in AI: A Replication Study](https://dl.acm.org/doi/10.1609/aaai.v39i25.34818) Odd Erik Gundersen, 
Odd Cappelen, Martin Mølnå, Nicklas Grimstad Nilsen
AAAI’25

[2] [Diablo: A Benchmark Suite for Blockchains](https://gramoli.github.io/pubs/Eurosys23-Diablo.pdf) V. Gramoli, R. Guerraoui, A. Lebedev, C. Natoli, G. Voron. 18th ACM European Conference on Computer Systems (EuroSys), 2023.

[3] [STABL: The Sensitivity of Blockchains to Failures](https://gramoli.github.io/pubs/2025-Middleware-Stabl.pdf) V. Gramoli, R. Guerraoui, A. Lebedev, G. Voron. 26th ACM/IFIP International Middleware Conference (Middleware), 2025.

