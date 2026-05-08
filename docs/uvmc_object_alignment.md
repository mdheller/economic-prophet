# UVMC Object Alignment Map

This note maps the Unified Value Measurement Calculus (UVMC) onto the existing Economic Prophet object graph. The purpose is to prevent a parallel ontology from emerging. UVMC should enrich the existing class/entity spine with measurement context, dimensions, KPI mappings, knowledge quality, tensors, and governance receipts.

## 1. Alignment principle

Economic Prophet already treats profitability as a typed object-graph problem. UVMC keeps that object graph as the measurement substrate and adds cross-domain semantics around it.

```text
legal_entity
  -> line_of_business
    -> relationship
      -> account
        -> instrument
          -> transaction_event
```

Supporting objects remain part of the graph:

```text
collateral_set
funding_source
hedge_set
scenario
model_version
parameter_set
portfolio
audit_pack
```

UVMC adds the following cross-cutting contracts:

```text
measurement_context
period
discount_curve
industry_overlay
domain
value_driver
kpi
kpi_observation
enterprise_dimension
dimension_level
reference_record
knowledge_quality
tensor_mapping
metric_space
standards_reference
governance_control
calculation_receipt
```

## 2. Existing object alignment

| Existing object | UVMC role | Required UVMC enrichment |
| --- | --- | --- |
| `legal_entity` | Reporting, legal, tax, regulatory, and capital boundary. | `industry_overlay_ref`, `jurisdiction`, `currency`, `accounting_basis`, `standards_profile`, legal-entity dimension membership. |
| `line_of_business` | Management economics boundary and KPI-tree root. | Domain weights, driver weights, strategy owner, management-reporting hierarchy, industry overlay. |
| `relationship` | Customer/counterparty/franchise-economics node. | Customer dimension, relationship dimension, franchise effects, collateral overlap, cross-sell, diversification, relationship-level K. |
| `account` | Account-level container for balances, fees, utilization, and product context. | Product/service dimension, balance facts, utilization facts, fee facts, sign conventions, source lineage. |
| `instrument` | Contract, exposure, position, obligation, or service entitlement. | Cash-flow model, risk model, capital model, option terms, hurdle curve, NOPAT contribution, real-option hooks. |
| `transaction_event` | Event-time observation and EP-delta source. | Event provenance, source-record ID, event timestamp, correction/reversal handling, variance-driver tag. |
| `portfolio` | Aggregation and risk-pooling view. | Portfolio membership rules, concentration factors, diversification adjustment, scenario applicability. |
| `collateral_set` | Capital and exposure mitigant. | Eligible collateral, haircut, overlap rules, reserve adequacy, collateral provenance, release constraints. |
| `funding_source` | FTP, liquidity, and hurdle-rate support object. | Funding curve, term premium, liquidity premium, stress surcharge, stable-funding credit, scenario binding. |
| `hedge_set` | Risk transfer and mitigation object. | Hedge attribution, offset eligibility, basis risk, effectiveness tests, risk-capital impact. |
| `scenario` | Measurement context. | Base/upside/downside/stress mode, assumptions, discount curve, K mode, industry overlay, run controls. |
| `model_version` | Formula and model provenance. | Formula version, tensor version, calibration version, validation status, approval state. |
| `parameter_set` | Runtime parameterization. | Weights, coefficients, spreads, caps, floors, tensor references, effective dates. |
| `audit_pack` | Calculation receipt. | Input hash, output hash, formula version, model version, parameter version, overrides, reconciliation status. |

## 3. UVMC class-to-object placement

| UVMC class | Belongs at | Notes |
| --- | --- | --- |
| `MeasurementContext` | Every run and every measured output. | Binds object, period, horizon, scenario, industry overlay, formula version, model version, and parameter set. |
| `Period` | Global dimension. | Supports event-time, intraday, daily, monthly, quarterly, annual, and close-cycle grains. |
| `DiscountCurve` | Scenario plus currency plus object boundary. | Used for period-safe NPV and hurdle-rate decomposition. |
| `IndustryOverlay` | Legal entity, line of business, portfolio, or external-sector view. | Encodes NAICS, ISIC, domain, regulatory, and sector weighting assumptions. |
| `Domain` | Cross-cutting dimension. | Finance, customer, workforce, supply chain, engineering, program, risk, security, education, governance, etc. |
| `ValueDriver` | KPI tree and variance bridge. | Price, volume, cost, productivity, capital, risk, mix, knowledge. |
| `KPI` | KPI catalog. | Must define unit, sign convention, driver, domain, object type, aggregation behavior, and EP mapping. |
| `KPIObservation` | Fact/event layer. | Must include object, period, source, unit, value, provenance, and dimension coordinates. |
| `EnterpriseDimension` | Shared reference-data layer. | Time, geography, industry, legal entity, LOB, customer, relationship, account, product, supplier, skill, clearance, etc. |
| `DimensionLevel` | Inside `EnterpriseDimension`. | Defines grain, parent level, rollup field, code field, and description field. |
| `ReferenceRecord` | Inside dimension level. | Versioned reference member with status and effective dating. |
| `KnowledgeQuality` | Source, observation, edge, model, calculation, or output. | Stores C/Q/S/P components, score, scoring mode, evidence refs, and credit constraints. |
| `TensorMapping` | Model/parameter layer. | KPI-to-EP, variance, risk-capital, and knowledge-adjustment mappings. |
| `MetricSpace` | Analytics/search layer. | Weighted vector comparison over value, risk, knowledge, domain, and operating features. |
| `StandardsReference` | Governance and semantic layer. | External reporting, risk, industry, control, and classification references. |
| `GovernanceControl` | Policy/control plane. | Validation, access, approval, override, reconciliation, exception, and change control. |
| `CalculationReceipt` | Output layer. | Deterministic evidence for every non-trivial run. |

## 4. Heller mesh alignment

The Heller mesh layer remains an internal measurement extension, not a token, money-movement, or public-settlement layer. It maps cleanly onto UVMC:

| Heller object | Economic Prophet object | UVMC class alignment |
| --- | --- | --- |
| `sphere` | `line_of_business` or domain cluster. | `Domain`, `MeasurementContext`, `KnowledgeQuality`, `VarianceComponent`. |
| `edge` | Relationship or internal service flow. | `TensorMapping`, `KPIObservation`, `RiskCapitalCharge`, `TransferPrice`. |
| `triparty_face` | Governed release/control surface. | `GovernanceControl`, `CalculationReceipt`, `ReferenceRecord`, `KnowledgeQuality`. |
| `Micro-Heller` | Internal activity/utility measurement. | Fast-decay KPI/fact stream; non-transferable in v0.1. |
| `Credit-Heller` | Slashable obligation measurement. | Exposure, collateral, reserve, and risk-capital measurement. |
| `Reserve-Heller` | Collateral anchor. | `collateral_set`, reserve adequacy, eligibility schedule. |

## 5. Enterprise-dimension alignment

The enterprise-dimension pattern should be adopted directly:

```text
source reference data
  -> ETL/integration
    -> enterprise dimensions
      -> domain datamarts
        -> business-facing wide and normalized views
```

Each dimension should support:

```text
dimension_id
name
level_count
levels[]
reference_records[]
rollup_field
code_field
description_field
status
active_date
inactive_date
source_system
source_record_id
view_wide
view_normalized
```

This is the bridge from legacy enterprise findings to executable measurement infrastructure. If we do not encode dimensions as governed classes, UVMC collapses back into spreadsheet math.

## 6. Domain/entity coverage matrix

| Domain | Primary objects | Dimensions | KPI examples | EP bridge |
| --- | --- | --- | --- | --- |
| Finance | legal_entity, LOB, account, instrument. | time, legal entity, LOB, account, product, currency. | NOPAT, capital, hurdle, margin, cost, tax. | Revenue, cost, tax, capital charge. |
| Customer/relationship | relationship, account, instrument. | customer, geography, industry, segment. | retention, cross-sell, wallet share, utilization. | Price, volume, mix, capital, franchise effect. |
| Workforce/talent | LOB, program, workforce, skill. | role, skill, clearance, geography, program. | staffing gap, time-to-fill, retention, productivity. | Productivity, cost, risk, delivery capacity. |
| Supply chain | supplier, program, instrument/event. | supplier, part, geography, contract, program. | lead time, defect rate, fill rate, concentration. | Cost, productivity, risk, capital. |
| Engineering/quality | engineering artifact, quality event, program. | artifact, system, requirement, defect, program. | rework, defect escape, cycle time, root cause. | Cost, productivity, risk, capital. |
| Business development | opportunity, customer, relationship. | opportunity, pipeline, customer, sector, geography. | win probability, pipeline quality, pursuit cost. | Volume, price, cost, real option. |
| Governance/risk | control, standard, scenario, model. | control, standard, jurisdiction, risk factor. | control coverage, exceptions, unresolved risk. | Risk spread, capital charge, provenance penalty. |
| Knowledge/provenance | source, evidence, model, output. | source, model, evidence type, freshness. | C/Q/S/P, contradiction rate, freshness. | Knowledge credit, risk reduction, decision confidence. |

## 7. Required schema slice

The first implementation slice should add schemas for:

```text
uvmc_measurement_context.schema.json
uvmc_knowledge_quality.schema.json
uvmc_dimension.schema.json
uvmc_tensor_mapping.schema.json
uvmc_calculation_receipt.schema.json
```

The first executable tests should check:

```text
K score bounds
strict and geometric K scoring
knowledge-credit sign discipline
discount-factor compounding
metric-space non-negative weights
cosine clamp behavior
EP component reconciliation shape
```

## 8. Promotion rule

No new UVMC concept should be promoted into runtime code until it has:

1. A class or schema definition.
2. A clear object-graph attachment point.
3. Unit/sign/cadence semantics.
4. Provenance and lineage requirements.
5. At least one synthetic fixture.
6. At least one invariant test.

This keeps the calculus mathematical, auditable, and implementation-ready.
