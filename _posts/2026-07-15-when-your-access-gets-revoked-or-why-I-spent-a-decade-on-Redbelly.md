---
layout: post
author: Vincent
tags: sovereignty centralisation security
---

On June 12, the US government ordered Anthropic to cut off access to Fable 5 and Mythos 5 for any foreign national, including people inside the United States.
Anthropic could not verify nationality on every API call. The company switched the models off for everyone.

Within hours, organisations around the world lost access to their key AI functionality for reasons they neither chose nor had control over. 
Although this might have been detrimental for some it illustrates a larger problem that affects any nation when relying on externally governed
resources: they cannot assume they will access to them.

### Redbelly is designed to run

I have spent more than a decade working on coping with this problem.  
At the University of Sydney and CSIRO, our team work on making an efficient 
blockchain designed for institutions, regulators and real settlement.
That work became Redbelly: leaderless Democratic Byzantine Fault Tolerance (DBFT), superblock consensus, 
formally verified security, and deterministic finality without forks or probabilistic waiting.

### Cybersecurity dependency

First, Redbelly was designed as a cybersecurity software that cannot rely on protocols that are controlled by others. By inheriting 
a cybersecurity software from someone else, one would expose themselves to the risk of inheriting hidden back doors. 
We all know Homer’s story from around 750 BCE that illustrates this: the Trojans accepted a massive wooden horse as a gift, 
and once it was inside their gates, Greek soldiers hidden within emerged and won the war. 

Our first goal was to design a distributed ledger by building it in Australia but across academia (University of Sydney), 
government (CSIRO) and industry (Redbelly Blockchain and then Redbelly Network). We made sure to implement its most critical part, 
the consensus algorithm, from sratch in Australia rather than inheriting on some external design or implementation.

### Decentralisation for censorship resistance

Second, Redbelly has been designed for no single institution, be it a government or an organisation, to control it.
Today there are hundreds of nodes around the world and they are spread in all continents. Although we do not have nodes in every country, 
we have in theory enough nodes to cover all jurisdictions in the world. The idea behind such a distribution is to prevent
any single country to control sufficiently many nodes so as to stop the ledger, let alone rewrite it.

We published Redbelly in IEEE S&P and stress-tested it at scale across continents. 
In this scientific publication, a property we showed Redbelly offers is censorship-resistance because Redbelly is guaranteed to serve requests
despite isolated malicious entities trying to stop it.

### Stoping AI can be harmful, stoping a country's economy is devastating

If the most advanced AI models can be recalled overnight, what happens 
when the same geopolitical logic meets financial settlement?
Most countries tokenising real-world assets still depend on settlement and custody infrastructure built and governed abroad. 
Compliance rules, sanctions and export-style restrictions do not always arrive with a migration timeline. 
Sometimes they arrive with a directive.
Countries need a fallback that works alongside national security policy.

### Redbelly as a credible alternative

Redbelly mainnet is live. Partners are issuing tokenised bonds, private credit, and structured products on the network. 
The Reserve Bank of Australia selected us for Project Acacia, including exploration of wholesale CBDC settlement on a public blockchain.
When Australia's central bank tested the future of tokenised wholesale markets, it needed a credible infrastructure in the room.

Digital asset infrastrucutre will become more and more strategic. AI learned that in June. Finance will learn it too.
In uncertain times, nations need settlement rails that cannot be censored, still running when someone else flips the 
switch. That is why we built Redbelly.
