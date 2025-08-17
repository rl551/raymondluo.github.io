---
title: "Running it twice"
date: August 17, 2025
math: true
---

In poker, when two or more players are all in before the river is revealed and there is no more action, they can choose to run it multiple times. Formally, there are $N=\min(n_1, n_2, \dots, n_k)$ runouts, where $n_i$ is the number of times player $i$ wants to run it, until the deck is depleted. On every run, cards are dealt without replacement from the deck and the winner of each run wins $\tfrac{1}{N}$ of the total pot.

When I first learned how to play poker, I was told running it multiple times is an attractive method for some because it keeps the EV the same but reduces variance. For a while, I never fully convinced myself why the EV stays the same but it turns out this is just a simple exercise in conditional expectation.

For simplificity, I will assume hero is all in on the turn (so there is one river card to be revealed) against a single villain and they run it twice. Let $X$ be the event that hero win a runout, $P$ be the size of the pot, $D$ be the deck of cards, and $S$ be the set of revealed cards. Hero's expected value is
$$
    \frac{P}{2}\cdot\mathbb{P}[X\mid S]+\frac{P}{2}\sum_{r\in D\backslash S, |r|=1}\mathbb{P}[X\mid S\cup\{r\}]\cdot\mathbb{P}[r]=\frac{P}{2}\cdot\mathbb{P}[X\mid S]+\frac{P}{2}\cdot\mathbb{E}[\mathbb{E}[(X\mid S)\mid r]].
$$
Since $\mathbb{E}[\mathbb{E}[(X\mid S)\mid r]]=\mathbb{E}[X\mid S]=\mathbb{P}[X\mid S]$, the expression simplifes to $P\cdot\mathbb{P}[X\mid S]$, as desired. It is easy to see that you can easily generalize this calculation to multiple players and runouts.