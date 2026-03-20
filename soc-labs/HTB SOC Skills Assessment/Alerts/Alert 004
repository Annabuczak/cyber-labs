# Alert 004 - RDP Logon Using Service Account

## Summary

An RDP logon was performed using a service account `svc-sql1`.

## Observations

- Account: svc-sql1 (service account)
- Target Host: PKI
- Source IP: 192.168.28.130 (internal)
- Logon Type: RDP (interactive)
- Attempts: 2

## Analysis

Service accounts are designed for automated processes and should not perform interactive logons such as RDP.

The observed behavior indicates:

- Misuse of service account credentials
- Potential credential compromise
- Possible lateral movement attempt

## Hypothesis

Most likely:

- Service account credentials have been compromised and are being used interactively

## Risk Level

Critical

## Action Taken

Escalated to Tier 2/3 for immediate investigation.

## Verdict

🚨 Malicious / Highly Suspicious – Escalation required
