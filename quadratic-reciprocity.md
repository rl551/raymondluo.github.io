---
title: "An elegant proof of quadratic reciprocity"
date: June 29, 2025
math: true
---

The law of quadratic reciprocity is an important result from elementary number theory. For odd primes $p$ and $q$, it states:

$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2} \cdot \frac{q-1}{2}},$$

where $\left(\frac{a}{p}\right)$ is the [Legendre Symbol](https://en.wikipedia.org/wiki/Legendre_symbol).

For odd primes $p$, we first define $\mathcal{S}_a=\{(r,s)\in\mathbb{Z}_p^2\mid r^2+s^2\equiv a\pmod{p}\}.$

**Lemma 1**: $\sum_{k=0}^{p-1}|\mathcal{S}_k|=p^2$.

*Proof*: Both expressions count the number of ordered pairs $(r,s)\in\mathbb{Z}_p^2$.

**Lemma 2**: $|\mathcal{S}_0|=p+(p-1)\left(\frac{-1}{p}\right)$.

*Proof*: Suppose $\left(\tfrac{-1}{p}\right)=-1$ and $r^2+s^2\equiv 0\pmod{p}$ for nonzero $r,s$. Then, note that we have
    $$1=\left(\frac{r^2}{p}\right)=\left(\frac{-s^2}{p}\right)=\left(\frac{-1}{p}\right)\left(\frac{s^2}{p}\right)=(-1)(1)=-1,$$
contradiction. Hence, when $\left(\tfrac{-1}{p}\right)=-1$, the only solution to $r^2+s^2\equiv 0\pmod{p}$ is $r=s=0$, so $|\mathcal{S}_0|=1$ in this case.

Now suppose $\left(\tfrac{-1}{p}\right)=1$ and $r^2+s^2\equiv 0\pmod{p}$ for nonzero $r,s$.

Fix $r$. Then, we have $s^2\equiv -r^2\pmod{p}$. There are two solutions to this equation: $s\equiv \pm r\sqrt{-1}\pmod{p}$. Therefore, every nonzero $r$ yields two solutions. This means there are $2\cdot(p-1)+1=2p-1$ solutions in this case.

**Lemma 3**
If $p\nmid a$, then $|\mathcal{S}_a|=p-\left(\tfrac{-1}{p}\right)$.

*Proof*: We first prove that there exists a bijection $\mathcal{S}_1\to\mathcal{S}_a$. 