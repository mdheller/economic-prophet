# Unified Value Measurement Calculus v0.1

The Unified Value Measurement Calculus (UVMC) extends Economic Prophet from a financial-institution profitability engine into a cross-domain, standards-aligned measurement lattice. It preserves Economic Profit as the additive value backbone while adding KPI trees, industry/domain overlays, knowledge quality, tensor mappings, and governed dimensional semantics.

UVMC does not replace the existing Economic Prophet object model. It wraps it with a typed measurement context so every calculated value is attributable to an object, period, scenario, domain, industry overlay, source, formula version, parameter set, and audit receipt.

## 1. Design rules

UVMC follows seven non-negotiable rules.

1. Economic Profit remains the canonical additive value measure.
2. All lower-grain economics must roll up without changing semantic meaning.
3. Knowledge quality may reduce uncertainty penalties, but it may not erase base cost of capital or regulated/economic capital requirements.
4. KPI trees are explanatory bridges into EP, not substitutes for EP.
5. Industry overlays tune weights, KPIs, and risk factors; they do not create incompatible valuation systems.
6. Enterprise dimensions must be versioned, effective-dated, hierarchical, and auditable.
7. Every output must carry lineage, cadence, model version, parameter version, and reproducible run evidence.

## 2. Canonical notation

| Symbol | Meaning |
| --- | --- |
| `t` | Period index. |
| `o` | Measured object, such as legal entity, line of business, relationship, account, instrument, transaction event, sphere, edge, or triparty face. |
| `h` | Measurement horizon. |
| `NOPAT_adj(o,t)` | Adjusted net operating profit after tax for object `o` in period `t`. |
| `Capital_adj(o,t-1)` | Adjusted invested, economic, regulatory, or risk capital assigned to `o` at the start of the period. |
| `HurdleRate_adj(o,t,h)` | Period/horizon-adjusted hurdle rate, including base cost of capital, risk spread, provenance penalty, and governed knowledge credit. |
| `EP(o,t)` | Economic Profit for object `o` in period `t`. |
| `K` | Knowledge quality scalar in `[0,1]`. |
| `DF_t` | Discount factor for period `t`. |
| `W_industry` | Industry/domain weighting matrix. |
| `T` | KPI-to-EP mapping tensor. |
| `M` | EP variance mapping matrix. |
| `R` | Risk exposure tensor. |

## 3. Core equations

### 3.1 Economic Profit

```text
EP(o,t) = NOPAT_adj(o,t) - HurdleRate_adj(o,t,h) * Capital_adj(o,t-1)
```

For banking-style object economics, this reconciles to the existing component form:

```text
EP_hat(o,t,h) = Revenue_hat
              - ExpectedLoss_hat
              - Expense_hat
              - FundingCosts_hat
              + FundingCredits_hat
              - Taxes_hat
              - CapitalCharge_hat

CapitalCharge_hat(o,t,h) = Hurdle_hat(o,t,h) * Capital_hat(o,t,h)
```

### 3.2 Additive value

For a flat equivalent spot rate, the simple form is acceptable:

```text
Value = sum_t EP_t / (1 + HurdleRate_adj)^t
```

For period-varying hurdle rates, UVMC uses discount factors:

```text
DF_t = product_{tau=1..t} (1 + HurdleRate_adj(tau))^-1
Value = sum_t EP_t * DF_t
```

This avoids the common error of applying a single-period rate as if it were a full maturity spot curve.

### 3.3 Knowledge-adjusted hurdle rate

The sign-safe decomposition is:

```text
HurdleRate_UVMC = BaseCostOfCapital
                + RiskSpread
                + ProvenancePenalty
                - KnowledgeCredit
```

with guards:

```text
0 <= KnowledgeCredit <= KnowledgeCreditCap
KnowledgeCredit <= ProvenancePenalty + OperationalUncertaintySpread
HurdleRate_UVMC >= BaseCostOfCapital + NonDiversifiableRiskFloor
```

Knowledge can reduce uncertainty load; it cannot eliminate the cost of capital, legal capital, regulatory capital, or hard risk floors.

### 3.4 Knowledge quality

Strict gate mode:

```text
K_strict = C * Q * S * P
```

where:

```text
C = coverage or completeness
Q = quality or coherence
S = stability or source strength
P = provenance or proof strength
```

Weighted continuous mode:

```text
K_geo = C^w_C * Q^w_Q * S^w_S * P^w_P
sum(w_i) = 1
```

Strict mode is appropriate for promotion gates. Weighted geometric mode is appropriate for continuous scoring and ranking.

### 3.5 EP variance decomposition

```text
Delta_EP = Delta_Price
         + Delta_Volume
         + Delta_Cost
         + Delta_Productivity
         + Delta_Capital
         + Delta_Risk
         + Delta_Mix
         + Delta_Knowledge
```

The first five terms preserve the core EP bridge. `Delta_Risk`, `Delta_Mix`, and `Delta_Knowledge` are explicit extension terms and must never be hidden inside generic narrative scores.

### 3.6 KPI-to-EP mapping tensor

```text
Delta_EP = sum_{i,d,o,k} T_{i,d,o,k} * Delta_KPI_{i,d,o,k}
```

where:

```text
i = industry or overlay
 d = domain
 o = object type
 k = KPI leaf
```

The tensor must declare units, sign conventions, calibration method, applicability conditions, and confidence for each populated mapping.

### 3.7 Risk-capital tensor

```text
CapitalCharge = sum_{i,r,t} alpha_{i,r,t} * R_{i,r,t}
```

where `R` is an exposure or risk measurement and `alpha` is a governed coefficient. The tensor can represent credit, market, liquidity, operational, cyber, supply-chain, model, legal, regulatory, and concentration risk.

### 3.8 Metric space

```text
g(u,v) = sum_i w_i * u_i * v_i
```

with constraints:

```text
w_i >= 0
u and v are normalized or explicitly unit-compatible
zero-norm vectors are invalid
```

Cosine distance is:

```text
d(u,v) = arccos(clamp(g(u,v) / sqrt(g(u,u) * g(v,v)), -1, 1))
```

### 3.9 Hypergraph diffusion

```text
phi_t = exp(-t * L_H) * s
```

where `L_H` is a governed hypergraph Laplacian and `s` is a seed vector. Use this for propagation analysis, not as a replacement for measured EP.

## 4. UVMC class catalog

| Class | Purpose |
| --- | --- |
| `uvmc:MeasurementContext` | Declares object, period, scenario, horizon, industry overlay, formula version, model version, parameter set, and governance context. |
| `uvmc:Period` | Represents calendar, fiscal, event-time, intraday, daily, monthly, quarterly, annual, and close-cycle grains. |
| `uvmc:DiscountCurve` | Stores period-safe discount factors and hurdle-rate components. |
| `uvmc:IndustryOverlay` | Encodes NAICS, ISIC, sector, regulatory, and domain-specific measurement weights. |
| `uvmc:Domain` | Represents finance, customer, workforce, supply chain, engineering, program, risk, security, or other value domain. |
| `uvmc:ValueDriver` | Represents price, volume, cost, productivity, capital, risk, mix, and knowledge drivers. |
| `uvmc:KPI` | Defines a KPI leaf, including unit, sign convention, domain, object type, and EP mapping behavior. |
| `uvmc:KPIObservation` | Records observed KPI values or deltas with source, period, object, dimension coordinates, and provenance. |
| `uvmc:EnterpriseDimension` | Defines shared dimensions such as time, geography, legal entity, line of business, customer, relationship, industry, program, skill, supplier, product, and control. |
| `uvmc:DimensionLevel` | Defines hierarchy levels and rollup semantics inside a dimension. |
| `uvmc:ReferenceRecord` | Versioned dimension record with status and effective dating. |
| `uvmc:NOPATAdjustment` | Bridges accounting profit to EP-compatible NOPAT. |
| `uvmc:CapitalAdjustment` | Bridges book capital, invested capital, risk capital, economic capital, regulatory capital, and intangible adjustments. |
| `uvmc:HurdleRateComponent` | Represents base cost, risk spread, provenance penalty, knowledge credit, floors, and caps. |
| `uvmc:KnowledgeQuality` | Stores K components, scoring mode, score, credit cap, and evidence references. |
| `uvmc:VarianceComponent` | Stores EP movement attribution by driver. |
| `uvmc:TensorMapping` | Defines KPI-to-EP, risk-capital, knowledge-adjustment, and variance mapping tensors. |
| `uvmc:MetricSpace` | Declares vector dimensions, weights, normalization method, and distance semantics. |
| `uvmc:HypergraphDiffusion` | Declares diffusion runs over value, risk, knowledge, or operating hypergraphs. |
| `uvmc:StandardsReference` | Attaches standards, controls, classifications, or reporting references to formulas and outputs. |
| `uvmc:GovernanceControl` | Defines validation, approval, access, override, reconciliation, and exception controls. |
| `uvmc:CalculationReceipt` | Emits deterministic run evidence: input hash, output hash, scenario, model version, parameter version, overrides, and reconciliation status. |

## 5. Enterprise dimensions

UVMC treats dimensions as first-class objects. A dimension is not just a label; it is a governed hierarchy with level semantics, parent rollups, reference records, effective dating, status, source lineage, and business-facing views.

Initial canonical dimensions:

```text
time_period
legal_entity
line_of_business
relationship
customer
account
instrument
transaction_event
portfolio
geography
industry
sector
function
business_measurement_unit
program
project
workforce
skill
clearance
supplier
opportunity
pipeline
engineering_artifact
quality_event
knowledge_source
standard
control
scenario
model_version
parameter_set
```

## 6. Universal measured-entity contract

Every measured entity should carry or inherit:

```text
id
type
label
description
object_ref
period_ref
scenario_ref
industry_overlay_ref
dimension_coordinates
unit
currency
cadence
source_system
source_record_id
provenance_evidence_ref
model_version
parameter_set
formula_version
owner
status
active_date
inactive_date
created_at
updated_at
input_hash
output_hash
```

Every measured value must also declare:

```text
value
sign_convention
normalization_method
missingness_policy
confidence
knowledge_quality_ref
standard_mapping_ref
lineage_parent_refs
```

## 7. Computation flow

1. Normalize source observations into object graph and enterprise dimensions.
2. Validate status, effective dates, units, sign conventions, and source provenance.
3. Bind period, scenario, model version, parameter set, and industry overlay.
4. Compute EP components at the lowest reliable grain.
5. Map KPI deltas into EP variance components using governed tensors.
6. Compute knowledge quality and apply bounded hurdle-rate adjustment.
7. Aggregate through object hierarchy and enterprise dimensions.
8. Discount period EP with period-safe discount factors.
9. Emit lineage-aware outputs and calculation receipts.
10. Publish business-facing wide and normalized views.

## 8. Invariant gates

A UVMC run is invalid unless these invariants hold:

```text
K is bounded to [0,1]
knowledge credit is bounded and sign-safe
industry/domain weights sum to 1 within declared scopes
metric weights are non-negative
zero-norm vector distances are rejected
period-varying discount factors are compounded period by period
EP components reconcile to economic_profit
KPI observations include object, period, unit, source, and provenance
enterprise dimensions include status and effective dating when versioned
calculated outputs include lineage and model/parameter/formula versions
```

## 9. Relationship to Economic Prophet

Economic Prophet remains the measurement engine. UVMC is the cross-domain calculus and semantic contract around that engine. Banking EP, Heller mesh measurement, enterprise KPI trees, industry overlays, and standards mappings become projections over one governed measurement graph rather than separate spreadsheets or unrelated scoring systems.
