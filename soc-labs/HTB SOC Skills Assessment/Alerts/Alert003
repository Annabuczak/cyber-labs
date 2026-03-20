# Alert 003 - Failed Admin Logons Outside PAW

## Summary

Failed logon attempts for administrative accounts observed from non-PAW systems.

## Observations

- Accounts: Administrator/administrator
- Source Systems:
    - DC1 ❗
    - DC2 ❗
    - PAW ✅
- Logon Type: Interactive
- Attempts: Multiple

## Analysis

Administrative activity is required to be performed exclusively from the PAW.

Failed logon attempts from DC1 and DC2 indicate:

- Potential policy violations
- Possible credential misuse
- Unauthorised admin login attempts from non-approved systems

## Hypothesis

Most likely:

- Admins not adhering to PAW usage policy

Possible:

- Unauthorised attempts using admin credentials

## Action Taken

Consult with IT Operations to verify:

- Whether the activity is legitimate
- Whether the PAW policy is being enforced

## Verdict

❗ Suspicious – Requires IT validation

## Mistake Learned - Admin Logons

### What I did

Assumed failed admin logons were normal human error

### What I missed

Admin activity must ONLY occur on PAW

### Correct reasoning

Admin logons from DC1/DC2 violate policy → suspicious

### Takeaway

Always validate activity against environment rules
