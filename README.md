# Enterprise DLP & Data Security Lab

Hands-on Data Security Engineering lab focused on **sensitive-data discovery, classification, DLP policy enforcement, security monitoring, and incident automation**.

The project is designed around realistic fintech-style data-protection scenarios using synthetic data only.

## Why this project exists

Modern organisations need to protect sensitive information across endpoints, cloud platforms, collaboration tools, databases and business systems. This lab demonstrates the engineering workflow behind that protection:

1. Discover sensitive data
2. Classify it
3. Evaluate DLP policy
4. Allow, alert or block
5. Generate a security event
6. Send events to Elastic
7. Detect suspicious behaviour
8. Automate incident handling

## Target capabilities

- PII / PCI / secrets discovery
- PAN detection with Luhn validation
- Data classification: PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED
- Configurable DLP policy engine
- Simulated data-exfiltration scenarios
- Elasticsearch + Kibana
- ES|QL detection logic
- n8n security automation
- Jira-ready incident enrichment
- AWS S3 / IAM / KMS / CloudTrail scenarios
- PostgreSQL access-control and masking examples
- Automated tests and documented playbooks

## Architecture

```text
Files / DB / Cloud Storage
          |
          v
+-------------------------+
| Sensitive Data Scanner  |
| PII / PCI / Secrets     |
+------------+------------+
             |
             v
+-------------------------+
| Classification Engine   |
| PUBLIC                  |
| INTERNAL                |
| CONFIDENTIAL            |
| RESTRICTED              |
+------------+------------+
             |
             v
+-------------------------+
| DLP Policy Engine       |
+----------+--------------+
           |
      +----+----+
      |         |
    Allow    Alert/Block
                |
                v
       +------------------+
       | Security Event   |
       +--------+---------+
                |
                v
       Elasticsearch
                |
                v
             Kibana
                |
                v
              n8n
                |
                v
      Incident / Jira Flow
```

## Repository structure

```text
.
├── src/
│   └── dlp_lab/
│       ├── scanner/
│       ├── classification/
│       ├── policies/
│       └── events/
├── sample-data/
├── policies/
├── elastic/
├── automation/
├── aws/
├── docs/
├── tests/
├── pyproject.toml
├── docker-compose.yml
└── .env.example
```

## Current status

- [x] Repository architecture
- [x] Python package skeleton
- [x] Synthetic data policy
- [x] Threat model
- [x] Classification model
- [x] Initial Docker Compose skeleton
- [x] Sensitive-data detectors
- [ ] Policy evaluator
- [ ] Elastic ingestion
- [ ] Detection rules
- [ ] Automation workflows

## Quick start

Requirements:
- Python 3.12+
- Docker / Docker Compose

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it and install the project:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

Run the scanner against the synthetic sample:

```bash
dlp-scan sample-data/customer_export.txt
```

Or without installing the console script:

```bash
python -m dlp_lab.scanner.cli sample-data/customer_export.txt
```

Expected behaviour:
- valid synthetic PAN candidates are validated with Luhn
- invalid 16-digit references are ignored
- IBAN candidates are validated with MOD-97
- email and secret patterns are detected
- output contains masked values only

## Security principles used

- Least privilege
- Data minimisation
- Defence in depth
- Detect + prevent
- Explicit classification
- Testable policy enforcement
- Observable security controls
- Synthetic test data only

## Safety of repository data

This repository must never contain:
- real customer information
- real cardholder data
- production API keys
- passwords
- private company information
- real access tokens

All examples are synthetic and intended only for defensive security engineering practice.

## Roadmap

See [docs/ROADMAP.md](docs/ROADMAP.md).

## Interview topics demonstrated by this project

- What is DLP and where can controls be enforced?
- How do data discovery and classification differ?
- Why is regex alone insufficient for payment-card detection?
- How do you reduce DLP false positives?
- What is the difference between encryption, masking and tokenisation?
- How should security events reach a SIEM?
- How would you investigate suspected data exfiltration?
- How can cloud storage access be protected and audited?

---

**Status:** active learning and engineering project.
