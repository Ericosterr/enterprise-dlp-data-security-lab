# Data Classification Model

This lab uses four labels.

## PUBLIC

Information intentionally available to the public.

Examples:
- published marketing content
- public website text
- public documentation

Default handling:
- sharing allowed

## INTERNAL

Non-public information intended for normal internal use.

Examples:
- internal procedures
- routine project notes

Default handling:
- external sharing may require review depending on context

## CONFIDENTIAL

Sensitive business or personal information where disclosure could cause harm.

Examples:
- customer contact records
- commercial agreements
- employee records
- financial reports

Default handling:
- restricted access
- monitored sharing
- external transfer normally requires an approved business reason

## RESTRICTED

Highest sensitivity level in the lab.

Examples:
- payment-card data
- authentication secrets
- high-risk identity data
- encryption keys

Default handling:
- least-privilege access
- strong technical protection
- external sharing blocked by default
- high-severity monitoring

## Important design principle

Classification and enforcement are separate.

A label answers:

> How sensitive is this data?

A DLP policy answers:

> Given the sensitivity, user, destination and business context, what action should the system take?
