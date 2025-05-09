---
layout: post
author: Vincent
tags: performance synchrony finality centralisation
---

Andrei Lebedev, a PhD student I supervise, will present next month a tutorial on STABL [[1]](https://gramoli.github.io/pubs/2025-Middleware-Stabl.pdf) at the [55th Annual IEEE/IFIP International Conference on Dependable Systems and Networks](https://dsn2025.github.io/) in Italy co-authored by my colleagues from EPFL. This will teach scientists how to assess the fault tolerance of their blockchain software. Below I explain why I believe this is such a great scientific initiative.


For researchers to progress, they need to stand on the shoulders of giants. In particular, without the legacy of former researchers in the form of reusable material, progressing science would require first to constantly reinvent the wheel.

### Lower Bounds in Theoretical Science

This is striking in theoretical science where an impossibility result states that no more research efforts need to be spent trying to solve a problem because it has been proven insolvable. This is why publishing an article presenting a lower bound is so appealing for the theoretical scientific community: they help the research community focus their efforts on what truly matters.

### Empirical Evidence for Systems Research

When conducting empirical research, this is also true. But in this case, what matters is no longer a lower bound proof but rather the experimental settings that led to the empirical observations made by the scientists. Other researchers can then stand on these scientists shoulders by replicating the experiments or study which parameter is responsible for the observations made.

In computer science when scientists do systems research, the methodology is also empirical. Not only are the experimental settings crucial but they may not all be documented in a published article. Additional material, like the source code of the system being studied, are often necessary to understand the observations made. For example, the programming language used or the way the program was written will impact the performance observed.

### Artifacts and Teaching Material

In the field of programming languages, conferences started to ask scientists to submit an artifact for evaluation: this allows a committee to assess whether they could reproduce the results presented in a paper using the provided artifact. Not long after this, other conferences (including in systems research) started asking for the same. Even though the artifact submission is not required for publishing the paper, this is a great initiative that allows for more transparency and fosters progress. 

![The sensitivity of Aptos to failures.](/img/STABL.png){: width="500" }

Going one step further requires teaching and organising tutorials at scientific conferences that allows other scientists to learn by practicing. This is why I believe that the tutorial on STABL [[2]](https://gramoli.github.io/pubs/2025-DSN-Stabl.pdf), just like the tutorial on [Diablo](https://diablobench.github.io/) last year [3] will be so important. STABL [[1]](https://gramoli.github.io/pubs/2025-Middleware-Stabl.pdf) will help more blockchain researchers assess the fault tolerance of their blockchain. We have seen so many times [blockchains crashing or being unusable](https://gramoli.github.io/2024/09/25/the-fault-tolerant-blockchain.html) without understanding why. One thing that is sure is that blockchain researchers need to stand on the shoulder of giants to progress faster. 

[1] [STABL: The Sensitivity of Blockchains to Failures](https://gramoli.github.io/pubs/2025-Middleware-Stabl.pdf). V. Gramoli, R. Guerraoui, A. Lebedev and G. Voron. [26th ACM/IFIP International Middleware Conference (Middleware)](https://middleware-conf.github.io/2025/), 2025.

[2] [Evaluating Blockchain Fault Tolerance with STABL](https://gramoli.github.io/pubs/2025-DSN-Stabl.pdf). V. Gramoli, R. Guerraoui, A. Lebedev, G. Voron. [55th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN)](https://dsn2025.github.io/), 2025.

[3] Evaluating Performance and Dependability of Blockchain Protocols with Diablo. A. Lebedev and V. Gramoli. [54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN)](https://dsn2024uq.github.io/), 2024.
