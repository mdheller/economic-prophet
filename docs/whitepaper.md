# Economic Profit Methodology

## Canonical repository edition

This repository captures the current integrated state of the Economic Profit methodology as an open, auditable framework for measuring profitability, pricing, capital consumption, and value creation in banking and financial institutions.

It preserves the original manuscript spine while integrating later work on:
- central banking and monetary regimes
- distribution choice and tail-risk architecture
- bond pricing, duration, convexity, and PDE framing
- Ross recovery, Arrow–Debreu intuition, and state-contingent recovery surfaces
- open schemas, reference code, and audit packs

## Core claim

Economic Profit is the most coherent way to measure whether a banking organization creates value after paying for the full economic cost of:
- funding
- expected loss
- operating expense
- taxes
- regulatory and economic capital
- liquidity and balance-sheet scarcity

The canonical equation is:

```text
EP = Revenue - Expected Loss - Expenses - Funding Costs + Funding Credits - Taxes - Capital Charge
```

with:

```text
Capital Charge = Hurdle Rate × Capital
Expected Loss  = PD × LGD × EAD
```

## What makes banking special

Banking organizations are not ordinary firms. Their funding base, access to deposits, regulatory capital requirements, reserve and liquidity constraints, internal capital markets, and need to maintain credit standing make profitability measurement fundamentally different from ordinary corporate finance.

## Granularity

Profitability must be additive and reconcilable from:

Transaction → Instrument → Account → Relationship → Portfolio → Line of Business → Legal Entity → Parent

## Why this repository exists

The manuscript is necessary but not sufficient. This repository turns the framework into:
- canonical documentation
- machine-readable schemas
- a reference Python implementation
- synthetic examples
- auditable output packs
