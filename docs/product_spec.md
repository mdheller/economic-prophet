# Open Auditable Economic Profit Framework: Product Specification v0.1

## 1. Purpose

Build a near-real-time profitability intelligence product that measures forward-looking Economic Profit
for every relevant object in a financial institution:
- legal entity
- line of business
- relationship
- account
- portfolio
- instrument
- transaction

## 2. Canonical profitability equation

For object `o` at time `t` and horizon `h`:

EP_hat(o,t,h) =
  Revenue_hat(o,t,h)
  - ExpectedLoss_hat(o,t,h)
  - Expense_hat(o,t,h)
  - FundingCosts_hat(o,t,h)
  + FundingCredits_hat(o,t,h)
  - Taxes_hat(o,t,h)
  - CapitalCharge_hat(o,t,h)

CapitalCharge_hat(o,t,h) = Hurdle_hat(o,t,h) * Capital_hat(o,t,h)

ExpectedLoss_hat(o,t,h) = PD_hat(o,t,h) * LGD_hat(o,t,h) * EAD_hat(o,t,h)

## 3. Latency tiers

Not everything updates at the same speed. The runtime must support four measurement cadences.

### 3.1 Streaming / event-time
- market prices
- curve shifts
- collateral marks
- counterparty exposure changes
- utilization changes

### 3.2 Intraday
- FTP shadow price updates
- intraday NII/NIM attribution
- hedge transfer impacts

### 3.3 Daily
- PIT PD nowcasts
- LGD and EAD updates
- capital shadow prices
- stress overlays

### 3.4 Close (monthly/quarterly)
- accounting adjustments
- tax close
- governance checkpoints
- full reconciliation

## 4. Canonical object model

The system must maintain a typed object graph:
- entity -> LOB -> portfolio -> relationship -> instrument -> transaction
- collateral sets and hedges attach to instruments and relationships

## 5. FTP model

FTP is Treasury’s internal shadow price of funding and liquidity scarcity.

FTP(t,h) = base_matched_maturity + term_premium + liquidity_premium + optionality_charge + draw_charge + stress_surcharge - stable_funding_credit - franchise_credit

## 6. Recovery surface (Ross / Arrow–Debreu)

Recovery is modeled as a state-contingent surface, not a scalar.

Distinguish:
- planning recovery RR^P
- market-implied recovery RR^Q
- wedge ΔRR = RR^Q - RR^P

## 7. Zero-EP pricing solver

For any pricing object, solve the minimum customer rate / spread such that EP_hat = 0.

## 8. Attribution

Every run must emit attribution explaining EP movement by:
- price
- volume
- utilization
- FTP
- EL
- recovery
- capital
- tax
- cost
- hedge
- mix

## 9. Audit pack

Every run produces a deterministic audit record containing:
- run_id, timestamp
- model version, parameter version
- input hash and output hash
- overrides
- reconciliation summary

## 10. Deliverables

- docs/whitepaper.md
- docs/product_spec.md
- schemas/
- src/open_ep_framework/
- examples/
- tests/
