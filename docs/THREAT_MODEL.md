# Threat Model

## Scope

This lab focuses on accidental and intentional leakage of sensitive data from enterprise systems.

## Protected data

- Personal data / PII
- Payment-related data / PCI
- Authentication secrets
- Confidential business information

## Example assets

- Customer export files
- PostgreSQL tables
- Cloud-storage objects
- Collaboration documents
- Application logs

## Example threat scenarios

### 1. External sharing by mistake

An employee uploads a customer export to a location accessible outside the organisation.

Desired control:
- detect sensitive content
- classify the object
- block or alert based on policy
- log the event

### 2. Email exfiltration

Sensitive financial or personal data is sent to a non-corporate recipient.

Desired control:
- inspect content/context
- evaluate destination
- block or alert
- create evidence for investigation

### 3. Bulk access followed by transfer

A user accesses an unusually large number of customer records and then attempts an external transfer.

Desired control:
- collect activity events
- correlate behaviour
- raise severity
- send to incident workflow

### 4. Exposed secret

An API key or credential appears in a document or exported file.

Desired control:
- detect likely secret
- classify as restricted
- prevent unsafe sharing
- trigger credential rotation workflow

## Trust boundaries

- User endpoint
- Internal applications
- Databases
- Cloud storage
- External destinations
- SIEM / monitoring platform
- Automation / ticketing platform

## Initial assumptions

- Test data is synthetic
- Lab integrations are local or test-only
- DLP actions are simulated before any real enforcement
- Detection quality is measured through repeatable tests

## Out of scope for the first version

- Malware detection
- Network intrusion detection
- Real endpoint agents
- Production Google Workspace enforcement
- Real customer environments
