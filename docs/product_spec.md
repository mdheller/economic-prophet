# Open Auditable Economic Profit Framework: Product Specification v1

## Purpose

Build a near-real-time profitability intelligence product that measures forward-looking Economic Profit for every relevant object in a financial institution:
- legal entity
- line of business
- relationship
- account
- portfolio
- instrument
- transaction

## Canonical profitability equation

For object `o` at time `t` and horizon `h`:

```text
EP_hat(o,t,h) = Revenue_hat(o,t,h)
               - ExpectedLoss_hat(o,t,h)
               - Expense_hat(o,t,h)
               - FundingCosts_hat(o,t,h)
               + FundingCredits_hat(o,t,h)
               - Taxes_hat(o,t,h)
               - CapitalCharge_hat(o,t,h)
```

with:

```text
CapitalCharge_hat(o,t,h) = Hurdle_hat(o,t,h) * Capital_hat(o,t,h)
ExpectedLoss_hat(o,t,h)  = PD_hat(o,t,h) * LGD_hat(o,t,h) * EAD_hat(o,t,h)
```

## Latency tiers

### Streaming / event time
- market prices
- curve shifts
- collateral marks
- counterparty exposure changes
- utilization events
- liquidity spread moves

### Intraday
- FTP shadow-price refresh
- NII / NIM contribution refresh
- hedge transfer refresh
- liquidity-buffer consumption

### Daily
- PD / LGD / EAD nowcasts
- recovery surface updates
- economic-capital shadow charges
- stress overlays

### Monthly / quarterly close
- tax accruals
- close-process accounting adjustments
- op-risk allocations
- governance reconciliation

## Core runtime engines
- FTP engine
- expected-loss engine
- recovery surface engine
- capital charge engine
- zero-EP pricing solver
- attribution engine
- audit-pack generator
