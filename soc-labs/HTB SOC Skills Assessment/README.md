# SOC Skills Assessment – HTB

## Overview
This repository contains my investigation and analysis of security alerts during a simulated SOC Tier 1 assessment.

## Objectives
- Analyse alerts from SIEM dashboards
- Apply SOC triage methodology
- Escalate or validate based on context

## Environment Highlights
- Cloud-based infrastructure
- PAW required for admin activity
- Service accounts follow "-svc" naming
- Linux systems have minimal activity
- Root login disabled remotely

## Methodology
Each alert is analysed using:
- Observations
- Context validation
- Risk assessment
- Final verdict

## Alerts Covered
1. Service account failed logon
2. Disabled user login attempt
3. Admin logon outside PAW
4. Service account RDP usage
5. Admin group modification
6. Root SSH login attempts

## Key Takeaways
- Context is critical in SOC analysis
- Not all suspicious activity is malicious
- Privileged account misuse is high risk

## Status
✅ Completed

