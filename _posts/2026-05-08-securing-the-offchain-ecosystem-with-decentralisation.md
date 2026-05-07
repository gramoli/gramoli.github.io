---
layout: post
author: Vincent
tags: interoperability cross-chain centralisation security
---

As hacks multiply, the Redbelly choice of regulation-compliant decentralisation has proved effective numerous times to cope with trusting off-chain 
sources. This type of problem has been most recently illustrated with the Kelp DAO attack that drained US$ 292M. While this hack involved 
LayerZero that Redbelly uses, it could not have impacted the Redbelly Network thanks to its inherent decentralisation strategy.

### Summary 

On 18 April, US$ 292M were drained from the Kelp DAO that uses LayerZero contracts themselves.
Kelp DAO is a liquid restaking protocol that issues rsETH as a receipt token for ETH routed through EigenLayer.
To move rsETH between chains, Kelp relied on LayerZero’s cross-chain messaging infrastructure, which uses Decentralized Verifier Networks (DVNs)
to verify that a cross-chain message is legitimate before the destination chain acts on it.

Attackers compromised two Remote Procedure Call nodes operated by LayerZero Labs and ran a Distributed Denial-of-Service attack against a 
third, forcing the verifier to fail over onto the compromised nodes. From there, the attackers fed the verifier a forged cross-chain message 
indicating a valid burn on the source chain. The bridge contract on Ethereum, seeing what looked like a legitimate instruction, released 116,500 
rsETH (approximately USD 292 million, around 18% of rsETH’s circulating supply) to an attacker-controlled address. This is not a smart contract
bug but a single point of failure happening during an off-chain verification. 
The exploit was in the off-chain verification infrastructure feeding the bridge, and it was made possible because Kelp’s bridge ran a 1-of-1 
DVN configuration, meaning a single verifier (LayerZero Labs itself) had to sign off on a cross-chain message for the bridge to act.

### The root cause of the problem

This single point of failure problem is as old as the research on distributed systems. 
If you trust a single source, then even a single failure of this source can impact your entire system.

There are multiple examples of this problem. For example, it is well known that a human error led ChainLink to misreport an exchange rate 
between silver and USD that profited hackers [1]. This is to cope with this type of problem that Redbelly exploits multiple sources of exchange 
data feed and extract the median of the medians of values gathered at different nodes as explained in a previous blog post [2]. 

In general, forgetting about replicating the sources that is used by a blockchain defeats the purpose of even using the blockchain.
If you introduce a single point of failure, then why using a distributed ledger technology that is supposed to cope with a single point of 
failure?

### The consequences

#### The blame fight
46 minutes after the hack, Kelp’s emergency multisig paused core contracts, blocking two follow-up drain attempts.
LayerZero’s post-mortem framed the 1-of-1 setup as a fringe choice Kelp made against repeated guidance to adopt multi-DVN redundancy.
Kelp pushed back hard: it argued the compromised infrastructure was LayerZero’s own, that the 1-of-1 configuration had been LayerZero’s 
onboarding default, and that public LayerZero documentation actively prompted developers toward single-source verification. 
What is uncontested is that LayerZero has now announced it will no longer sign messages for any application running a 1-of-1 configuration, 
forcing a protocol-wide migration.

#### The AAVE contagion
Rather than dump the stolen rsETH on the open market, the attackers deposited approximately 89,567 rsETH into AAVE V3 as collateral and 
borrowed roughly USD 190 million in real wrapped ETH and related assets across Ethereum and Arbitrum before markets could freeze. AAVE 
Labs moved within hours to freeze rsETH markets across its deployments, set loan-to-value ratios to zero on the affected asset, and halt 
new borrowing. 

Press estimates AAVE’s potential bad debt exposure between USD 177 million and USD 230 million, depending on how Kelp ultimately handles 
the shortfall. AAVE’s Total Value Locked dropped by around USD 6 billion in the days that followed as users pulled deposits.
AAVE itself was not hacked. AAVE’s contracts behaved exactly as designed. The protocol simply accepted what it was told was good collateral, 
and that collateral turned out to be unbacked because the bridge that minted it had been drained.

#### The Arbitrum freeze
On 20 April, Arbitrum’s 12-member Security Council — elected by ARB token holders every six months — used its emergency powers to transfer 
30,766 ETH (approximately USD 71 million) of attacker-linked funds from the exploiter’s address to an intermediary wallet that can only be 
moved by a further DAO governance vote. Nine of twelve members signed off, after consultation with law enforcement on the exploiter’s identity. 
Arbitrum framed it as a surgical action that did not affect any other user or chain state. Critics argued it set a precedent: if a small 
group can move funds out of one wallet by signing a multisig, that mechanism could in principle be used in other circumstances, 
including under regulatory pressure.


### The take-away message

#### Decentralisation is key
LayerZero, as a protocol, did exactly what it was designed to do. The exploit was not a protocol-level bug; it 
was the consequence of an implementation choice, running a single-verifier configuration on a bridge securing nearly USD 300 million of user 
assets. Redbelly’s own LayerZero implementation uses three external DVN suppliers precisely so that no single point of failure exists.

#### Composability and cross-chain reach come with risk that does not disappear by ignoring it
If you want assets that move freely across many chains, the standard pitch for omnichain tokens and wrapped representations — you accept a 
structural exposure: somewhere in that flow there is a bridge, and bridges have been an important category of DeFi losses for years. The 
Kelp incident is yet another a reminder. Bridges that depend on shared off-chain infrastructures or hidden trust assumptions will keep being 
targeted, because the attackers are organised and well-resourced (this attack has been preliminarily attributed to North Korea’s Lazarus Group, 
who have drained more than USD 575 million from DeFi in 18 days through two structurally different vectors).

#### Layer 2s are not what most people think they are
Arbitrum’s freeze illustrates the point cleanly. A 12-person elected council with emergency powers can transfer funds out of an address. That 
may well have been the right call in this specific case, the funds were stolen by a state-sponsored actor, but it is an exercise of centralised
authority over an asset on a network that markets itself as permissionless. The same observation applies to other widely-used networks. Many 
Layer 2s rely on centralised sequencers or key holders simply because Layer 2s are not blockchain but off-chain. 
This is why regulation is now differenciating clearly Public Digital Token Infrastructure from a Digital Asset Platforms [3] - the latter requiring 
licensing.

#### The choke point of accountability should be the regulated issuer, not the network
When stolen assets move through the system, the cleanest place for action is the issuer of the underlying value, the regulated stablecoin 
issuer, the regulated tokenised-asset issuer, the regulated custodian. They are licensed. They are identified. They have legal obligations to 
their customers. They are in the best position to freeze, claw back, or refuse to redeem assets that have been stolen, and to do so under a 
framework where their decisions are reviewable.

### Conclusions

Redbelly is not a general-purpose network that has been retrofitted to host regulated assets. 
It was purpose-built from the protocol upward for tokenised real-world assets, with the architectural choices that 
flow from that mission. Four of those choices speak directly to the failure modes the Kelp incident exposed.

#### Redbelly is genuinely decentralised at the consensus layer
There is no centralised sequencers or key holders on Redbelly. 
Consensus is produced by a distributed validator set, and no group of insiders is in a position to be asked, or pressured, 
to override the ledger. Decentralisation in this sense is not an aesthetic preference, it is what makes the network credibly neutral 
and what keeps the question "who controls this?" from having a meaningful answer. The Arbitrum freeze cannot happen on Redbelly.

#### Redbelly’s cross-chain implementation has no single point of failure
Where Redbelly connects to other networks via LayerZero, it does so through a configuration that requires independent agreement from multiple 
external DVN suppliers. A bridge protected by one verifier is a bridge with one lock. The Kelp exploit is, mechanically, the story of a single 
lock being picked. Redbelly treats single-verifier configurations the way a bank treats a vault with one key — as a thing that simply does not 
get built. The implementation choice that compromised Kelp is one Redbelly made the opposite call on, deliberately, three years ago.

#### Redbelly is purpose-built for regulated assets, not retrofitted to host them
Identity, accountability, and compliance are properties of the Redbelly network, not bolt-ons added at the application layer. The asset issuers 
operating on Redbelly are identified, licensed, and accountable, and Redbelly’s design assumes they are the choke point for freeze, claw-back, 
and reissuance, exactly as a regulated stablecoin issuer or tokenised-asset issuer should be. Privacy is engineered into the protocol for 
participants who legitimately need it, rather than added later through wrappers that themselves become attack surfaces. The architectural 
choices that make AAVE’s contagion exposure possible (bare instruments, anonymous counterparties, no accountable issuer in the loop) are 
choices Redbelly was built specifically to avoid.

#### Redbelly qualifies as Public Digital Token Infrastructure under the new law
Under the regulatory framework now coming into action, the line between Public Digital Token Infrastructure and Digital Asset Platform will determine 
where licensing obligations fall. Redbelly sits cleanly on the public-infrastructure side of that line because it was designed to be genuinely 
decentralised without party able to unilaterally interfere with the ledger. Networks with a centralised council that can transfer 
funds out of an address do not sit there as comfortably. The Kelp aftermath has made this distinction sharper, not softer, and the networks that 
have been quietly building toward it are about to look very different from the ones that have not.

The single point of failure has recently been illustrated by this single-verifier leading to a USD 292 million drain. 
As long as we will use these ill-suited infrastructures, the problem will exacerbate, the loss will increase. 
Redbelly made the opposite call by building the network from the consensus layer up, for exactly this purpose: to be the Public Digital 
Token Infrastructure [3] that regulated real-world assets can rely on.

### References

[1] Redbelly Yellow Paper v1.0. 
https://redbelly.network/research/Redbelly-Network-Yellow-Paper.pdf

[2] How Does Redbelly Achieve Fixed Price. 15 July 2025.
https://gramoli.github.io/2025/07/15/how-does-redbelly-achieve-fixed-price.html

[3] The Parliament of the Commonwealth of Australia. Corporations Amendment (Digital Assets Framework) Bill 2026.
https://parlinfo.aph.gov.au/parlInfo/download/legislation/bills/r7411_aspassed/toc_pdf/25108b01.pdf;fileType=application%2Fpdf


