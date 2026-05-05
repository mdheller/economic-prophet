# Human Economic Profit

Status: review-ready documentation and schema seed.

This directory captures the first repository integration surface for the Human Economic Profit manuscript and companion specifications. The full local artifact bundle exists as a generated ZIP from the working session; this repository PR lands the reviewable index, schema contracts, and integration plan first so the work can be inspected and expanded without immediately flooding the repository with a very large manuscript file.

## Purpose

Human Economic Profit reconstructs economic profit as a historical, mathematical, and civic value framework. It generalizes the original banking-centered Economic Profit / RAROC / FTP / economic-capital framework into a broader system for measuring value creation across people, households, projects, portfolios, institutions, communities, and civic systems.

The central identity is:

```text
EP = V_plus - V_minus - EL + FCR - FC - Pi
```

Where:

- `V_plus` is scalarized beneficial value output, while preserving the original value vector.
- `V_minus` is scalarized resource use, cost, burden, or depletion.
- `EL` is expected loss.
- `FCR` is funding or liquidity credit for supplying stable resources.
- `FC` is funding or liquidity cost for drawing on shared resources.
- `Pi` is non-usurious capital reservation, normally `alpha_share * EC_req`.

## What is included in this first repo pass

```text
docs/specs/human-economic-profit/
  README.md
  repo-integration-plan-v0.1.md
  schemas/
    event.schema.json
    ep-record.schema.json
    reputation-event.schema.json
    replay-row.schema.json
    heller-balance.schema.json
    civic-asset.schema.json
```

## Source lineage

The framework descends from the Economic Profit Methodology white paper and later running drafts. Those prior drafts focused on banking, regulatory capital, RAROC/RARORAC, FTP, PD/LGD/EAD, risk capital, and profitability reconciliation. This version preserves that spine while extending it to civic, reputational, labor, and human-value measurement.

## Reconstructed companion specs

The working bundle reconstructs these specs for later full import:

1. Reputation Exchange Framework
2. Heller / DestiHeller Token Specification
3. SocioProphet Value Measurement Platform Specification
4. Formal Value Algebra / HomoSapien OS draft
5. Octonion Equilibria Specification
6. Policy & Employment Mechanics
7. Source Integration Backlog

## Maturity labels

- EP core, Heller records, civic asset records, reputation events, and replay rows are implementation-skeleton ready.
- Formal Value Algebra and Octonion Equilibria are advanced conceptual drafts and should remain appendix-level until mathematically hardened.
- Historical replay rows require source-grade evidence population before being treated as archival estimates.

## Immediate next work

1. Add the full manuscript and spec bundle as Markdown files or import them via local Git.
2. Add invariant tests for schemas.
3. Add fixtures for one event, one EP record, one reputation event, one replay row, one Heller balance, and one civic asset.
4. Create the simulation harness for EP, demurrage, reputation decay, and civic capacity saturation.
5. Add chapter-level source notes and evidence-grade metadata.
