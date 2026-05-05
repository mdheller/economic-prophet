# Heller Mesh Measurement Mechanics

This note adds the Heller flywheel mechanics to Economic Prophet as a measurement layer. The goal is not to turn the Economic Prophet runtime into a token issuer. The goal is to make mesh activity measurable with the same audit discipline already used for economic-profit, object-context, relationship, collateral, funding, hedge, and lineage outputs.

## Purpose

Economic Prophet currently measures profitability across a typed object graph:

```text
legal_entity -> line_of_business -> relationship -> account -> instrument -> transaction_event
```

The Heller mesh layer extends that measurement graph with internal economic flywheels, transfer-pricing edges, triparty release state, and Heller-class supply dynamics.

The measurement objective is:

```text
For each sphere, edge, and triparty face, compute:
- economic-profit delta
- transfer price
- knowledge quality
- momentum change
- credit exposure
- required collateral
- reserve adequacy
- gross-to-net compression
- release/admission/export state
- audit/proof lineage
```

## Non-goals

This specification does not define live money movement, external token issuance, exchange trading, redemption rights, or public-chain settlement. Those require separate legal, regulatory, security, and custody review. The v0.1 scope is auditable internal measurement and simulation.

## Sphere model

The initial Heller mesh uses eleven spheres:

```text
security
forensics
community
attestation
mesh
champion_challenger
packaging
education
federation
governance
developer_platform
```

The names above normalize the working diagrams. `champion_challenger` is the sphere that measures challenger tests, model contests, verification contests, audits, and outcome improvement. `developer_platform` absorbs the duplicated/ambiguous developer-platform node until the system splits developer experience from deployment/platform operations.

Each sphere is a measurable object with:

```text
sphere_id
name
cadence
economic_profit
momentum
knowledge_quality
micro_supply
credit_supply
reserve_supply
risk_charge
capital_charge
```

## Heller classes

### Micro-Heller

Micro-Hellers represent fast-decaying utility, work, learning, internal service consumption, contribution, and participation. They are suitable for measuring internal contribution, education loops, reproducibility work, support response, and mesh participation.

They should be non-transferable in v0.1 measurement mode.

```text
S_micro(t+1) = S_micro(t) + issuance_micro(t) - burn_micro(t) - decay_micro(t)
```

### Credit-Heller

Credit-Hellers represent staked, medium-duration, slashable obligations. They are the correct measurement unit for trade lines, publication bonds, rights warranties, seller obligations, developer obligations, fulfillment promises, challenger stakes, and solver/filler risk.

```text
S_credit(t+1) = S_credit(t) + stake(t) - settle(t) - slash(t) - expire(t)
```

### Reserve-Heller

Reserve-Hellers represent long-duration collateral anchors. They bound Credit-Heller issuance and measure reserve adequacy. Reserve-Hellers should back credit exposure, not every Micro-Heller event.

```text
S_reserve(t+1) = S_reserve(t) + collateral_mint(t) - reserve_release(t) - reserve_impairment(t)
```

## Knowledge functional

Knowledge quality is measured as:

```text
K = C * Q * S * P
```

Where:

```text
C = completeness
Q = quality
S = stability / source strength
P = provenance / proof strength
```

`K` is bounded to `[0, 1]` and should reduce collateral requirements when knowledge is complete, high-quality, stable, and strongly proven.

## Momentum update

The working flywheel equation becomes a measurement equation:

```text
m(t+1) = sigma(W * delta_EP(t) + B * K(t) + A * m(t) - lambda * m(t))
```

Where:

```text
m(t)        = sphere momentum vector
W           = weighted inter-sphere EP influence matrix
B           = knowledge influence matrix
A           = persistence / adjacency matrix
lambda      = decay or drag vector
sigma       = bounded activation function
```

This lets the runtime measure whether a sphere is gaining useful momentum, accumulating bloat, suffering inertia, creating bottlenecks, or reducing system risk.

## Economic-profit delta

Economic Prophet already decomposes object-level EP into revenue, expected loss, expense, funding cost, funding credits, taxes, and capital charge. The Heller mesh layer maps sphere deltas into that same measurement language:

```text
delta_EP_ij ~= beta * delta_volume_ij
            + gamma * delta_productivity_ij
            + delta * delta_capital_ij
            - epsilon * delta_cost_ij
            - risk_charge_ij
```

The exact coefficients are scenario parameters. The key rule is that Heller mechanics must remain measurable through auditable EP components, not through opaque narrative scoring.

## Transfer pricing

Inter-sphere service consumption is priced by transfer-pricing edges.

```text
TransferPrice_ij = CostFloor_ij
                 + MarginalCost_ij
                 + CapitalCharge_ij
                 + RiskCharge_ij
                 + beta * max(delta_EP_ij, 0) * K_ij
                 - Subsidy_ij(policy)
```

Use this for internal services such as:

```text
security -> forensics
packaging -> education
attestation -> app_store
mesh -> marketplace
federation -> marketplace
education -> community
governance -> release_policy
```

The transfer price must be auditable, parameterized, and tied to measurable EP components.

## Collateral and credit exposure

A Credit-Heller obligation creates exposure. Reserve-Hellers bound that exposure.

```text
RequiredCollateral_ij = alpha_ij * CreditExposure_ij
                      + PendingSettlementRisk_ij
                      + DisputeReserve_ij
                      + ChargebackReserve_ij
                      + RightsWarrantyReserve_ij
                      + OperationalRiskCharge_ij
                      + ConcentrationCharge_ij
```

```text
CreditLimit_ij = EligibleReserveCollateral_ij / alpha_ij
```

`alpha_ij` should increase with volatility, operational risk, rights risk, chargeback risk, jurisdiction risk, and concentration risk. It should decrease as `K_ij` improves, but never below a governed floor.

## Triparty release measurement

The Heller layer should not release value simply because a flow exists. Every consequential flow should pass through a governed triparty face when three local systems are involved.

A triparty face is:

```text
[A, B, C]
```

For marketplace/media/AppStore examples:

```text
[buyer_or_fan, creator_or_seller, clearing_agent]
[developer, app_store, security_attestation]
[packaging, attestation, education]
[marketplace, federation, governance]
```

Each face measures:

```text
lambda_evid   = economically visible/nettable quantity
lambda_admit  = quantity that survives claim, authority, and policy predicates
lambda_release = quantity that also survives proof, freshness, replay, and contradiction predicates
residual      = gross flow - released common-mode flow
```

Only `lambda_release` may be treated as constitutionally cleared. Residuals remain explicit.

## State machine

The Heller mesh layer should preserve the triparty release state machine:

```text
Observed
  -> Proposed
  -> Ready | ReviewRequired | Blocked
  -> Escrowed
  -> Filled
  -> Verified
  -> Released
```

Side exits are first-class outcomes:

```text
Cancelled
Expired
Refunded
Revoked
Unmerged
Slashed
CoarsenedExport
RestrictedProof
```

A profitable flow that fails policy, proof, contradiction, or visibility checks is not a successful flow. It is an admitted, blocked, refunded, revoked, or restricted flow with a proof artifact.

## Measurement outputs

A Heller mesh run should emit:

```text
run_id
scenario
as_of
sphere_states[]
edge_measurements[]
triparty_faces[]
heller_supply[]
reserve_adequacy
credit_utilization
gross_to_net_compression
release_correctness
refund_safety
contradiction_containment
export_discipline
replay_completeness
input_hash
output_hash
```

## Mapping to the current Economic Prophet runtime

| Current object | Heller mesh extension |
| --- | --- |
| legal_entity | reserve/governance boundary |
| line_of_business | sphere or sphere cluster |
| relationship | counterparty, creator, developer, vendor, or internal service relationship |
| account | sphere account or participant account |
| instrument | credit obligation, reserve claim, trade line, service entitlement, or tokenized claim |
| transaction_event | Heller event, transfer-price event, triparty state transition, settlement/slash/refund event |
| collateral_set | Reserve-Heller collateral pool and eligibility schedule |
| funding_source | reserve source, treasury source, or internal funding curve |
| hedge_set | risk transfer, insurance, guarantee, or reserve waterfall hedge |
| audit pack | proof artifact / lawful ledger record |

## First implementation boundary

The first implementation should be schema-first:

1. Validate one synthetic Heller mesh measurement fixture.
2. Emit the fixture as an auditable measurement object.
3. Do not introduce external token movement.
4. Do not introduce transferability.
5. Do not introduce public-chain settlement.
6. Do not introduce collateralized external leverage until the measurement mode is stable.

## Acceptance criteria

A v0.1 implementation is acceptable when it can:

```text
1. Represent all eleven spheres.
2. Represent Micro, Credit, and Reserve supplies separately.
3. Compute or ingest delta_EP and K per edge.
4. Compute transfer price per edge.
5. Compute required collateral and reserve adequacy per Credit-Heller obligation.
6. Represent triparty evidential/admitted/releasable quantities.
7. Preserve residual obligations.
8. Emit deterministic audit hashes.
9. Validate a synthetic fixture against schema.
10. Keep measurement separate from external issuance or redemption.
```

## Strategic rule

Economic Prophet remains the measurement engine. Heller remains the internal economic mechanics. The governed triparty fabric remains the constitutional release layer. The marketplace, AppStore, media, and mesh surfaces are projections over this measured object graph, not sovereign sources of truth.
