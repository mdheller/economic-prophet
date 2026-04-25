# Canonical Profitability Object Model

The Economic Prophet runtime treats profitability as a typed object-graph problem, not as a spreadsheet column.

## Object hierarchy

The first canonical hierarchy is:

```text
legal_entity
  -> line_of_business
    -> relationship
      -> account
        -> instrument
          -> transaction_event
```

Supporting objects attach to this hierarchy:

```text
collateral_set
funding_source
hedge_set
scenario
model_version
parameter_set
```

## Required design properties

1. **Additivity**: lower-level economics must roll up into higher-level views without changing the underlying economic meaning.
2. **Lineage**: each measure must preserve object identity, source system, model version, parameter version, and timestamp.
3. **Cadence awareness**: each object declares whether it is streaming, intraday, daily, or close-cycle.
4. **Auditability**: every run emits an audit record with input hash, output hash, scenario, framework version, and override metadata.
5. **Relationship context**: relationship profitability is not a blind sum of instrument profitability. It must account for collateral overlap, utilization interaction, diversification, and franchise economics.

## Canonical objects

### legal_entity
A regulated or legally accountable reporting boundary.

### line_of_business
A management reporting boundary that owns strategy, pricing, revenue, cost, and risk-taking choices.

### relationship
A client or counterparty relationship that can contain multiple accounts, instruments, exposures, services, and collateral dependencies.

### account
An account-level container for balances, fees, utilization, and product context.

### instrument
A contract or position with cash-flow, funding, loss, capital, option, and recovery behavior.

### transaction_event
An observed event that changes balances, exposure, utilization, fees, collateral, or risk state.

### collateral_set
Collateral supporting one or more exposures. Overlap matters because the same collateral cannot be independently counted across exposures.

### funding_source
The funding curve or funding bucket used by the FTP engine.

### hedge_set
A set of hedges or transfers used to centralize or neutralize market and balance-sheet risks.

## Runtime implication

The reference implementation should eventually expose all objects through schemas and normalize each run through this graph before computing Economic Profit.
