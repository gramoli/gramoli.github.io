---
layout: post
author: Vincent
tags: security RWA 
---

This year, the reproducibility crisis was exacerbated as researchers found that only 50% of 30 highly cited AI studies were reproducible [[1]](https://dl.acm.org/doi/10.1609/aaai.v39i25.34818). By contrast, we made sure that all our experiments showing the superior fault tolerance of Redbelly are judged reproducible by an independent committee of scientists.

### What is Reproducibility?

Reproducibility, the ability for independent researchers to run the same methods and obtain the same results, is one of the bedrock principles of the sciencetific method. Without it, there is no way to understand the factors that lead to the observed results. If a result can’t be reproduced, then what produced it?
- A correct methodology?
- A carefully controlled setup that does notn’t exist in the real world?
- A lucky accident?

### Misleading Results

The race to the most efficient blockchain has led blockchain companies to claim much higher performance than what they could achieve in realistic settings [[2]](https://gramoli.github.io/pubs/Eurosys23-Diablo.pdf). Most results were communicated through online announcements with limited scientific publications, if any, to back them up. And there are barely any results communicated when it comes to their reliability. Finally, we are not aware of any of these experiments that were judged reproducible.

If this trajectory continues, the consequences are easy to imagine:
- blockchains optimized to excel in a benchmark room but not in production,
- critical infrastructure built on foundations that fail under stress,
- and institutions, including governments, basing decisions on results that cannot be verified.
As blockchain becomes the infrastructure for real-world asset tokenisation, reproducibility becomes absolutely essential.


### Blockchain Fault Tolerance

To examine this problem rigorously, we developed Stabl, a framework we designed to evaluate blockchain fault tolerance under realistic and adversarial conditions. 
I introduced Stabl in an earlier [post](https://gramoli.github.io/2025/05/08/evaluating-blockchain-fault-tolerance-with-stabl.html) and the takeaway is straightforward: Redbelly tolerates crashes, churn, partitions, and malicious failures more effectively than the other blockchains evaluated, including Algorand, Aptos, and Solana.

| Blockchain | Attacks | Crash | Churn |  Partition |
|---|---|---|---|---|
| Algorand | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: |
| Aptos | :x: | :heavy_check_mark: | :x: | :x: |
| Avalanche | :heavy_check_mark: | :x: | :x: | :x: |
| Solana | :heavy_check_mark: | :x: | :x: | :x: |
| Redbelly | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |

Not only were these results peer-reviewed before being accepted for publications in the proceedings of the ACM/IFIP Middleware conference 2025 [[3]](https://gramoli.github.io/pubs/2025-Middleware-Stabl.pdf), but the published experimental results have just been independently judged available, functional and reproducible by an independent artifact evaluation committee of scientists.

The scientific article will be presented in the US on December 2025. It shows that Redbelly is better suited to tolerate the experimented partition, churn, crash and malicious failures than other modern blockchains, like Algorand, Aptos and Solana.

### Why This Matters Now

Blockchain is transitioning from an experimental technology to foundational infrastructure. It now underpins assets, markets, and systems that cannot afford ambiguity.
If reproducibility becomes optional, or worse, ignored, the industry risks building systemic infrastructure on unverifiable claims. This is a structural danger.
Reproducibility must become a baseline expectation for blockchain research and performance reporting. Not a “nice to have.”. A requirement.

If this industry wants to be trusted, it must be transparent.
If it wants to scale, it must be scientifically rigorous.
And if it wants to support real-world systems, it must publish results that others can re-run, re-test, and independently verify.

Redbelly has taken that path. And I hope others do as well.

[1] [The Unreasonable Effectiveness of Open Science in AI: A Replication Study](https://dl.acm.org/doi/10.1609/aaai.v39i25.34818). Odd Erik Gundersen, 
Odd Cappelen, Martin Mølnå, Nicklas Grimstad Nilsen.
39th AAAI Conference on Artificial Intelligence (AAAI), 2025.

[2] [Diablo: A Benchmark Suite for Blockchains](https://gramoli.github.io/pubs/Eurosys23-Diablo.pdf). V. Gramoli, R. Guerraoui, A. Lebedev, C. Natoli, G. Voron. 18th ACM European Conference on Computer Systems (EuroSys), 2023.

[3] [STABL: The Sensitivity of Blockchains to Failures](https://gramoli.github.io/pubs/2025-Middleware-Stabl.pdf). V. Gramoli, R. Guerraoui, A. Lebedev, G. Voron. 26th ACM/IFIP International Middleware Conference (Middleware), 2025.

