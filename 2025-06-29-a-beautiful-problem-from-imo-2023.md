---
title: "A Beautiful Problem from IMO 2023"
date: June 29, 2025
math: true
---

Today I want to share one of my favorite problems from the 2023 International Mathematical Olympiad. It's a beautiful combination of **number theory** and **geometry** that really showcases the elegance of mathematical thinking.

## Problem Statement

Let $n \geq 2$ be a positive integer. Find the number of ways to place $n$ rooks on an $n \times n$ chessboard such that there is exactly one rook in each row and each column, and the sum of the numbers of the squares occupied by the rooks is divisible by $n$.

## Initial Observations

At first glance, this might seem like a straightforward counting problem, but there's more depth here than meets the eye.

The key insight is to think about *permutations*. If we place exactly one rook in each row and column, we're essentially creating a permutation $\sigma$ of $\{1, 2, \ldots, n\}$.

For a permutation $\sigma$, the rook in row $i$ is placed in column $\sigma(i)$. If we number the squares from 1 to $n^2$ row by row, then the square occupied by the rook in row $i$ has number:

$$n(i-1) + \sigma(i)$$

## The Mathematical Core

The sum of all occupied squares is:

$$S(\sigma) = \sum_{i=1}^n [n(i-1) + \sigma(i)] = n \sum_{i=1}^n (i-1) + \sum_{i=1}^n \sigma(i)$$

Since $\sigma$ is a permutation of $\{1, 2, \ldots, n\}$, we have:
$$\sum_{i=1}^n \sigma(i) = 1 + 2 + \cdots + n = \frac{n(n+1)}{2}$$

Therefore:
$$S(\sigma) = n \cdot \frac{(n-1)n}{2} + \frac{n(n+1)}{2} = \frac{n^2(n-1) + n(n+1)}{2} = \frac{n(n^2-1+n+1)}{2} = \frac{n^3}{2}$$

## The Surprising Result

Wait! This means $S(\sigma) = \frac{n^3}{2}$ for *every* permutation $\sigma$.

The answer depends on the parity of $n$:

- If $n$ is **even**: Every valid rook placement works, so there are $n!$ ways.
- If $n$ is **odd**: No valid rook placement works, so there are $0$ ways.

## Why This Problem is Beautiful

What I love about this problem is how it initially appears to be about counting complex arrangements, but the key insight transforms it into a simple parity argument. The "aha moment" comes when you realize that all permutations give the same sum!
