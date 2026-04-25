# economic-prophet

Open, auditable economic-profit framework and near-real-time profitability intelligence engine.

## Purpose

This repository layers the work from the economic-profit white paper into:
- canonical documentation
- machine-readable schemas
- a reference Python implementation
- synthetic examples and audit outputs

## Repository plan

### Phase 1 — framework as documentation
- `docs/whitepaper.md`
- `docs/product_spec.md`
- `docs/architecture.md`
- `docs/integrations.md`
- `schemas/`

### Phase 2 — framework as first-class modeling and simulation platform
- `src/open_ep_framework/`
- zero-EP pricing solver
- FTP engine
- expected-loss engine
- recovery surface engine
- capital charge engine
- attribution engine
- relationship portfolio effects
- audit pack generation

## Quick start

```bash
python -m pip install -e . pytest
python -m pytest -q
python -m open_ep_framework.cli --example examples/synthetic_run.json --audit audit.json
python -m open_ep_framework.cli --mode relationship --example examples/synthetic_relationship_runtime.json --audit relationship_audit.json
```

The instrument CLI emits:
- FTP rate
- expected loss
- planning recovery
- market-implied recovery
- recovery wedge
- capital charge
- zero-EP break-even rate
- audit pack

The relationship CLI emits:
- weighted instrument break-even rate
- capital diversification credit
- collateral overlap charge
- utilization interaction charge
- franchise / cross-sell credit
- relationship required rate
- audit pack

## Canonical object model

The runtime is moving toward a typed profitability graph:

```text
legal_entity -> line_of_business -> relationship -> account -> instrument -> transaction_event
```

Supporting objects include collateral sets, funding sources, hedge sets, scenarios, model versions, and parameter sets. See `docs/object_model.md`, `schemas/canonical_object.schema.json`, and `examples/canonical_object.json`.

## Relationship portfolio effects

The relationship engine demonstrates why relationship profitability is not a blind sum of transactions. It decomposes relationship required rate into:
- weighted instrument break-even rate
- capital diversification credit
- collateral overlap charge
- utilization interaction charge
- franchise / cross-sell credit

See `examples/synthetic_relationship_runtime.json`, `schemas/relationship.schema.json`, and `tests/test_relationship_cli.py`.

## Ecosystem integration

This reference implementation is designed to integrate with:
- **Gaia** for macro regime state and scenario conditioning
- **Ontogenesis** for canonical ontology, lineage, and semantic constraints
- **TritFabric** for typed event transport and simulation orchestration

## First artifacts to land

- integrated white paper draft
- product specification v1
- schema pack v1
- reference implementation skeleton v1
- synthetic audit example
