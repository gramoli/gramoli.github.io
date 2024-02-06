[Home](../index) | [Research](../research) | [Software](../software) | [Publications](../publications) | [Blog](blog)

## Diablo

[Diablo](https://diablobench.github.io/) is a benchmark to evaluate blockchain systems on the same ground. It was developed in a partnership 
between University of Sydney and the Swiss Federal Institute of Technology Lausanne (EPFL) to evaluate blockchain and distributed ledger 
technologies when running realistic applications. The name Diablo stems from DIstributed Analytical BLOckchain benchmark. If you use Diablo, 
please mention the reference:

[Diablo: A Benchmark Suite for Blockchains](../pubs/Eurosys23-Diablo.pdf). 
V. Gramoli, R. Guerraoui, A. Lebedev, C. Natoli, G. Voron. 18th ACM European Conference on Computer Systems (EuroSys), 2023.

## Redbelly Blockchain

[Redbelly](https://redbelly.network) is a blockchain system that offers security and performance for [UTXO](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf) and [account](https://gramoli.github.io/pubs/IPDPS23-SmartRedbelly.pdf) models. Its security stems from its deterministic consensus protocol, called Democratic BFT (DBFT), that prevents forks, its [formal verification](https://gramoli.github.io/pubs/DISC22-holistic-verification.pdf) with parameterized model checking and its [accountability](https://eprint.iacr.org/2019/587.pdf) property, allowing to generate undeniable proofs-of-fraud against misbehaving participants. Its performance comes from its superblock optimization that combines proposed blocks instead of selecting only one and discarding the other, and its lightweight validation. On the [Diablo](https://gramoli.github.io/pubs/Eurosys23-Diablo.pdf) benchmarking framework, [Redbelly outperforms 6 mainstream blockchains](https://gramoli.github.io/pubs/IPDPS23-SmartRedbelly.pdf).

[Red Belly: A secure, fair and scalable open blockchain](https://gramoli.github.io/pubs/redbellyblockchain-oakland21.pdf). T Crain, C Natoli, V Gramoli. IEEE Symposium on Security and Privacy (S&P), 466-483, 2021

## Synchrobench

[Synchrobench](https://sites.google.com/site/synchrobench/) is a micro-benchmark suite used to evaluate synchronization techniques 
on data structures. Synchrobench is written in C/C++ and Java and currently includes arrays, binary trees, hash tables, linked lists, 
queues and skip lists that are synchronized with copy-on-write, locks, read-copy-update, compare-and-swap and transactional memory. 
A non-synchronized version of these data structures is proposed in each language as a baseline to measure the performance gain on 
multi-(/many-)core machines.

[More than you ever wanted to know about synchronization: Synchrobench, measuring the impact of the synchronization on concurrent 
algorithms](https://gramoli.github.io/pubs/gramoli-synchrobench.pdf). 
V Gramoli. Proceedings of the 20th ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming (PPoPP), 2015.

