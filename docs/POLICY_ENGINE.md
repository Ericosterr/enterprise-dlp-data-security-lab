# DLP Policy Engine

The policy engine separates content discovery from enforcement decisions.

## Why context matters

Sensitive content alone should not always produce the same outcome.

- Restricted payment data to an approved payment processor: ALLOW + audit
- Restricted payment data to personal cloud: BLOCK
- Confidential customer export to an external destination: ALERT or BLOCK depending on volume/context

The decision currently uses:
- content findings
- classification
- destination
- source system
- record count
- business justification

## Decision model

The lab supports ALLOW, ALERT and BLOCK.

## Rule precedence

Rules are evaluated from specific/high-risk conditions toward general fallbacks. A generic allow rule must not override a specific high-risk block.

## Default behaviour

If no explicit rule matches, the engine returns ALERT with rule DLP-999. This avoids silently allowing unknown workflows while also avoiding an indiscriminate block-all policy during early tuning.

## Policy tuning considerations

- false-positive rate
- business impact
- destination trust
- approved workflows
- exception governance
- record volume
- user behaviour
- historical incidents
- regulatory requirements

## Policy-as-code

The file policies/policy_catalog.yml documents the intended control set in a human-readable format. The first implementation keeps evaluation logic explicit in Python so it is easy to test and explain; dynamic rule loading can follow later.