# SOC Assessment – Findings Summary

## Overview
This document summarises the key findings from the SOC dashboard analysis conducted during the HTB Skills Assessment. Each alert was evaluated using environmental context, account behavior, and security best practices.

---

## 🔍 Key Findings

### 1. Service Account Authentication Failures
- Service account `sql-svc1` generated failed logon attempts.
- Service accounts are expected to use static credentials and not fail authentication.

**Assessment:**  
Likely misconfiguration or credential mismatch.  
**Action:** Consult IT Operations

---

### 2. Disabled User Authentication Attempt
- Disabled account `anni` attempted to authenticate.

**Assessment:**  
Highly suspicious, as disabled accounts should not be used.  
Possible credential reuse or compromise.

**Action:** Escalated to Tier 2/3 🚨

---

### 3. Administrative Logons Outside PAW
- Administrator logons observed from non-PAW systems (e.g., DC1, DC2).

**Assessment:**  
Violates privileged access policy requiring use of PAW.  
Activity appears consistent with known IT behavior but still requires validation.

**Action:** Consult IT Operations

---

### 4. Service Account Used for RDP
- Service account `svc-sql1` used for interactive RDP login.

**Assessment:**  
Service accounts must not be used interactively.  
Indicates possible credential compromise or misuse.

**Action:** Escalated to Tier 2/3 🚨

---

### 5. User Added to Local Administrators Group
- Administrator added a user (SID) to the local Administrators group.

**Assessment:**  
High-impact privilege change.  
Legitimacy unclear due to unresolved user identity.

**Action:** Consult IT Operations

---

### 6. Root SSH Login Attempts
- Multiple failed SSH login attempts for the `root` account.

**Assessment:**  
Root login is disabled for remote access.  
Indicates unauthorised access attempt or brute-force activity.

**Action:** Escalated to Tier 2/3 🚨

---

## 🚨 Overall Risk Assessment

The environment shows multiple indicators of:

- Potential credential misuse
- Policy violations (PAW bypass)
- Unauthorised access attempts
- Privileged account targeting

While some activities may be attributed to operational practices, several alerts strongly indicate possible malicious behavior.

---

## 🧠 Key Lessons Learned

- Context is critical when analysing security events  
- Service and privileged accounts require stricter scrutiny  
- Disabled or restricted accounts should never generate activity  
- Not all suspicious activity is malicious, but all must be validated  

---

## 📌 Final Verdict

The environment presents a mix of:
- ⚠️ Misconfigurations/policy violations  
- 🚨 Potential security incidents requiring escalation  

Further investigation by Tier 2/3 analysts is required for high-risk alerts.

---

## 📊 Status

✅ Assessment Completed  
🚨 Escalations Initiated Where Required  
