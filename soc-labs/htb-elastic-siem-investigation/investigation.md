# Elastic SIEM Investigation – Disabled Account Analysis
## Objective

The goal of this investigation was to analyse Windows event logs in an Elastic SIEM environment and identify security-relevant account activity.
The analysis focused on detecting disabled accounts and investigating authentication events.

## Environment

Platform: Hack The Box  
SIEM: Elastic Stack  
Interface: Kibana Discover  
Index Pattern: windows*

## Investigation Process

The Elastic Discover interface was used to analyse Windows security logs.
The investigation focused on identifying account management events using KQL queries.
event.code:4725
Windows Event ID 4725 – A user account was disabled
## Findings
The investigation revealed that the following account was disabled:
Username: anni
The value was identified in the field:
winlog.event_data.TargetUserName

## Wildcard Query Investigation
A wildcard search was executed to identify administrative usernames.
Query:
user.name: admin*
Result:
The query returned 8 matching results.

## Conclusion
The SIEM investigation successfully identified a disabled user account and multiple administrative username patterns.
This exercise demonstrates how SOC analysts use log analysis and KQL queries to investigate security events within enterprise environments.

## MITRE ATT&CK Mapping

Technique: T1098  
Technique Name: Account Manipulation
Description:
Account changes, such as disabling users, may indicate an attacker's attempts to manipulate identities or remove access.
