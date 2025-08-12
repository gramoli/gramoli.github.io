---
layout: post
author: Vincent
tags: frontrunning MEV finance security cryptography
---

As much as I admire the cypherpunk community and the impact they had on censorship resistance, 
I believe that the privacy they demanded has now become detrimental to the adoption of blockchain.  
Instead, safer systems should prevent from trespassing on one another’s freedom. 

### Privacy is overrated

Privacy is an important right up to some extent.
By reciprocity, the privacy that you may enjoy while using the blockchain technology is also given to your peers. 
The drawback is that this privacy can backlash on someone else: without revealing our identify we feel less accountable. 

### Private PII

It is one thing to promote your privacy on personal data, it is another to promote privacy on the actions 
you commit that impact other’s life. 
In fact, it is crucial that you control the access to your personal identifiable information (PII) as long 
as it does not hamper the freedom of others.

### Pseudonymity

Blockchain is often referred to as a technology offering anonymity or pseudonymity at best. The users are not identified with 
their PII but rather a public key, typically a sequence of 64 bytes that pairs with a private key used to sign cryptograpically 
transactions.
The term "pseudonymity" stems from the fact that the key can be viewed as a pseudonym, and publicly associating a key to a PII 
would no longer ensure anonymity.

![Tragedy](/img/hacks.png){: width="500" }[https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2025/](.)

### The lack of accountability

The privacy offered through pseudonymity hampers the adoption of blockchain.
In general, no one is made accountable for the losses and the theft of crypto assets.
As depicted in the Figure above, the lack of accountability has led to a dramatic increase in the number of hacks over the years.

It is not in the interest of nation A for another nation B to launder the money that will balance a diplomatic agreement in 
nation B's favour. It is neither fair for a layman’s transactions to be frontrun by a tech-savvy trader (take a loot at 
[a previous post](https://gramoli.github.io/2024/01/07/fair-resource-sharing-using-crypto.html) for more detail on frontrunning). 
And it is not right for a hacker to steal my friend’s rightly earned assets.
Yet, the blockchain technology is being constantly used to these ends and there are too few safeguards in place to protect the 
number of users that multiply by the day.  

### Polygraph

Back in 2019, we defined the Accountable Agreement problem [1], where we aim at not only solving consensus when possible 
but also identifying participants responsible for a disagreement. This identification simply means that the computers
actively trying at making participants disagree on the next block of the blockchain, have their identifier 
exposed cryprographically. 
This result in an undeniable proof-of-fraud that can then be propagated to the system, making participants accountable 
for their actions. We gave the name "Polygraph" to the first solution to this problem, because it helps detects the liars 
in the system.

### Zero Loss Blockchain

Building upon Polygraph, we then designed a Zero Loss Blockchain system [2]. This work debunked the myth that it was impossible
for a blockchain to tolerate a colluding majority. It thus received the Best Paper Award at the conference, IEEE/IFIP DSN, where 
it was published. The key idea was to reimburse the potential victims of a disagreement with the assets of the liars.  

### Towards Deterrence

The beauty in this solution [2] is that it has a built-in mechanism, which can be view as the 
Sword of Damocles, that does not aim at being used. 
We need more of this deterrence mechanisms for blockchain to be safely adopted. 
This is why Redbelly requires all its users to be real wolrd adults by using identity providers before they can 
join the network.

[1] [Polygraph: Accountable byzantine agreement](https://eprint.iacr.org/2019/587.pdf). P Civit, S Gilbert, V Gramoli. 
IEEE 41st International Conference on Distributed Computing Systems (ICDCS), 2021.

[2] [ZLB: A Blockchain to Tolerate Colluding Majorities](https://gramoli.github.io/pubs/DSN24-ZLB.pdf). 
A. Ranchal-Pedrosa, V. Gramoli. 54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN), 2024.
