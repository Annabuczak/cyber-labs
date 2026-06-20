#!/usr/bin/env python3
"""Beginner-friendly Security+ revision program from Notion notes."""

from __future__ import annotations

import argparse
import json
import random
import textwrap
from dataclasses import dataclass
from pathlib import Path

RANDOM = random.SystemRandom()
PROGRESS_FILE = Path(__file__).with_name("security_progress.json")


@dataclass(frozen=True)
class Topic:
    name: str
    summary: str


@dataclass(frozen=True)
class Flashcard:
    id: str
    topic: str
    term: str
    answer: str
    hint: str = ""


@dataclass(frozen=True)
class Question:
    id: str
    topic: str
    prompt: str
    answer: str
    explanation: str
    options: tuple[str, ...] = ()
    keywords: tuple[str, ...] = ()


TOPICS: tuple[Topic, ...] = (
    Topic("CIA triad", "Confidentiality protects secrecy, integrity protects accuracy, and availability keeps systems usable."),
    Topic("AAA", "Authentication proves identity, authorisation decides access, and accounting records activity."),
    Topic("Accounting", "Accounting tracks user activity with logs, audit trails, monitoring, SIEM, and syslog."),
    Topic("Authentication", "Authentication proves a user, device, or entity is who they claim to be."),
    Topic("Authorisation", "Authorisation happens after authentication and decides what the user can access or do."),
    Topic("Redundancy", "Redundancy improves availability by using backup components and removing single points of failure."),
    Topic("Controls", "Security controls may be technical safeguards or control types such as preventative, detective, and corrective."),
    Topic("Zero Trust", "Zero Trust verifies every request using control-plane decisions and data-plane enforcement."),
    Topic("Gap Analysis", "Gap analysis compares the current state with the desired state and creates a plan to fix what is missing."),
    Topic("Risk basics", "Risk exists when a threat can exploit a vulnerability."),
)


FLASHCARDS: tuple[Flashcard, ...] = (
    Flashcard("fc_cia", "CIA triad", "CIA triad", "Confidentiality keeps data secret, integrity keeps data accurate, and availability keeps systems and data accessible.", "Confidentiality, Integrity, Availability."),
    Flashcard("fc_confidentiality", "CIA triad", "Confidentiality", "Protecting information from unauthorised access and disclosure.", "Think: encryption and privacy."),
    Flashcard("fc_integrity", "CIA triad", "Integrity", "Keeping data accurate, unchanged, and trustworthy unless an authorised change is made.", "Think: hashing and checksums."),
    Flashcard("fc_availability", "CIA triad", "Availability", "Making sure systems and data are accessible to authorised users when needed.", "Think: uptime and access."),
    Flashcard("fc_aaa", "AAA", "AAA", "Authentication proves who you are, authorisation controls what you can access, and accounting records what you did.", "Identity, access, activity."),
    Flashcard("fc_accounting", "AAA", "Accounting", "Recording user activity through logs and audit trails.", "What did you do?"),
    Flashcard("fc_accounting_topic", "Accounting", "Accounting", "A security measure that tracks and records user activities during communications or transactions.", "Logging, monitoring, tracking, recording."),
    Flashcard("fc_audit_trail", "Accounting", "Audit trail", "A chronological record of user activities showing what happened, when it happened, and who was involved.", "A timeline of activity."),
    Flashcard("fc_siem", "Accounting", "SIEM", "Security Information and Event Management collects logs and alerts from many systems and analyses them in real time.", "Central security event analysis."),
    Flashcard("fc_syslog", "Accounting", "Syslog server", "A server that collects logs from network devices, servers, applications, firewalls, and security devices.", "Central log collection."),
    Flashcard("fc_forensic_analysis", "Accounting", "Forensic analysis", "Investigating what happened during a security incident using evidence such as logs and event records.", "Incident investigation."),
    Flashcard("fc_authentication", "Authentication", "Authentication", "A security measure that proves a user, device, or entity is who they claim to be.", "Who are you?"),
    Flashcard("fc_auth_factors", "Authentication", "Authentication factors", "The five factor categories are something you know, something you have, something you are, something you do, and somewhere you are.", "Know, have, are, do, where."),
    Flashcard("fc_mfa", "Authentication", "Multi-factor authentication", "MFA uses two or more different authentication factor categories together.", "Password plus PIN is not true MFA."),
    Flashcard("fc_authorisation", "Authorisation", "Authorisation", "Deciding what a user or entity is allowed to access after they have been authenticated.", "What are you allowed to do?"),
    Flashcard("fc_permissions", "Authorisation", "Permissions", "Actions a user can perform on a resource, such as read, write, modify, delete, or execute.", "Actions on a resource."),
    Flashcard("fc_privileges", "Authorisation", "Privileges", "Higher-level rights, such as installing software, changing security settings, or managing accounts.", "Admin-style rights."),
    Flashcard("fc_least_privilege", "Authorisation", "Least privilege", "Users should only receive the minimum access needed to do their job.", "Minimum necessary access."),
    Flashcard("fc_redundancy", "Redundancy", "Redundancy", "Duplicating critical parts of a system so another part can take over if one fails.", "Removes single points of failure."),
    Flashcard("fc_load_balancing", "Redundancy", "Load balancing", "Spreading user traffic across multiple servers so one server does not become overloaded.", "Availability helper."),
    Flashcard("fc_failover", "Redundancy", "Failover", "Automatically switching to a backup system when the main system fails.", "Backup takes over."),
    Flashcard("fc_controls", "Controls", "Security controls", "Safeguards used to protect systems, data, people, and assets.", "Reduce risk."),
    Flashcard("fc_technical_controls", "Controls", "Technical controls", "Security measures that use technology, hardware, or software to manage and reduce risk.", "Firewalls, encryption, MFA, IDS."),
    Flashcard("fc_preventative", "Controls", "Preventative controls", "Controls designed to stop a security incident before it happens.", "Stop it before it happens."),
    Flashcard("fc_deterrent", "Controls", "Deterrent controls", "Controls designed to discourage attackers from attempting an attack.", "Scare them off."),
    Flashcard("fc_detective", "Controls", "Detective controls", "Controls that identify when something suspicious or unwanted has happened.", "Logs, SIEM alerts, CCTV monitoring."),
    Flashcard("fc_corrective", "Controls", "Corrective controls", "Controls that fix or reduce damage after an incident.", "Backups, recovery, malware removal."),
    Flashcard("fc_compensating", "Controls", "Compensating controls", "Alternative controls used when the preferred control cannot be used.", "Backup option for control gaps."),
    Flashcard("fc_directive", "Controls", "Directive controls", "Controls that tell people what they should or should not do.", "Policies and procedures."),
    Flashcard("fc_zero_trust", "Zero Trust", "Zero Trust", "A model based on 'never trust, always verify'. Every request must prove it should be trusted.", "Verify explicitly, least privilege, assume breach."),
    Flashcard("fc_control_plane", "Zero Trust", "Control Plane", "The decision-making and policy-management part of Zero Trust.", "The brain of Zero Trust."),
    Flashcard("fc_data_plane", "Zero Trust", "Data Plane", "The part of Zero Trust where access actually happens and decisions are carried out.", "The hands of Zero Trust."),
    Flashcard("fc_policy_engine", "Zero Trust", "Policy Engine", "The part of the Control Plane that checks a request against policies and decides allow, deny, or limit.", "Decides yes or no."),
    Flashcard("fc_policy_admin", "Zero Trust", "Policy Administrator", "The part of the Control Plane that manages and applies the access decision.", "Applies policy decisions."),
    Flashcard("fc_pep", "Zero Trust", "Policy Enforcement Point", "The point where the access decision is enforced by allowing, blocking, or limiting the request.", "Security guard at the door."),
    Flashcard("fc_adaptive_identity", "Zero Trust", "Adaptive Identity", "Identity checks that adapt to risk using real-time context such as device, location, behaviour, and time.", "Identity checks that adapt."),
    Flashcard("fc_gap_analysis", "Gap Analysis", "Gap analysis", "Comparing where an organisation is now with where it wants to be to identify what is missing.", "Current state vs desired state."),
    Flashcard("fc_gap_steps", "Gap Analysis", "Gap analysis steps", "Define scope, gather current-state data, identify gaps, and develop a plan to bridge the gaps.", "Scope, current state, gaps, plan."),
    Flashcard("fc_technical_gap", "Gap Analysis", "Technical gap analysis", "Checks technology, infrastructure, tools, and configurations against security needs.", "Checking the technology."),
    Flashcard("fc_business_gap", "Gap Analysis", "Business gap analysis", "Checks business processes, operations, responsibilities, training, and readiness.", "Checking how the organisation works."),
    Flashcard("fc_poam", "Gap Analysis", "POA&M", "Plan of Action and Milestones: a fix-it plan for weaknesses with actions, owners, resources, timelines, and status.", "Fix-it plan with deadlines."),
    Flashcard("fc_threat", "Risk basics", "Threat", "Anything that could cause harm, loss, damage, or compromise to IT systems.", "Cyber attacks, breaches, disasters."),
    Flashcard("fc_vulnerability", "Risk basics", "Vulnerability", "A weakness in system design or implementation, such as bugs, misconfiguration, or missing patches.", "Weakness that could be exploited."),
    Flashcard("fc_risk", "Risk basics", "Risk", "Risk exists when a threat can exploit a vulnerability.", "Threat plus vulnerability."),
)


QUESTIONS: tuple[Question, ...] = (
    Question("q_confidentiality", "CIA triad", "Which CIA principle is about keeping information secret from unauthorised people?", "Confidentiality", "Confidentiality protects information from unauthorised access and disclosure.", ("Confidentiality", "Integrity", "Availability", "Accounting"), ("confidentiality",)),
    Question("q_integrity", "CIA triad", "Which CIA principle keeps data accurate, unchanged, and trustworthy?", "Integrity", "Integrity protects accuracy and makes sure data is not changed unless authorised.", ("Confidentiality", "Integrity", "Availability", "Authorisation"), ("integrity",)),
    Question("q_availability", "CIA triad", "Which CIA principle makes sure authorised users can access systems and data when needed?", "Availability", "Availability is about keeping systems and data accessible when needed.", ("Availability", "Integrity", "Accounting", "Data masking"), ("availability",)),
    Question("q_hashing", "CIA triad", "Which method helps prove whether a downloaded file has been changed?", "Hashing", "A changed file produces a different hash value, so hashing helps detect alteration.", ("Hashing", "Data masking", "CCTV", "Authorisation"), ("hashing", "hash")),
    Question("q_aaa", "AAA", "What does AAA stand for?", "Authentication, Authorisation, Accounting", "AAA means authentication, authorisation, and accounting.", ("Authentication, Authorisation, Accounting", "Access, Alerts, Audits", "Availability, Authentication, Access", "Assets, Accounts, Authorisation"), ("authentication", "authorisation", "authorization", "accounting")),
    Question("q_accounting", "AAA", "What does accounting record in the AAA framework?", "What you did", "Accounting records user activity through logs and audit trails.", ("Who you are", "What you did", "What you are allowed to access", "How data is encrypted"), ("what you did", "activity", "logs", "audit")),
    Question("q_audit_trail", "Accounting", "What is an audit trail?", "A chronological record of user activities", "An audit trail shows what happened, when it happened, and who was involved.", ("A chronological record of user activities", "A backup copy of a database", "A method for encrypting passwords", "A list of approved software"), ("chronological", "record", "activity")),
    Question("q_siem", "Accounting", "What does a SIEM help security teams do?", "Collect and analyse security events in real time", "A SIEM collects logs and alerts from many systems and analyses them to detect suspicious activity.", ("Collect and analyse security events in real time", "Replace all passwords", "Create physical barriers", "Restore files from backup"), ("security events", "logs", "analyse", "real time")),
    Question("q_syslog", "Accounting", "Which technology collects logs from routers, switches, firewalls, servers, and applications?", "Syslog server", "A syslog server centralises logs from many devices and systems.", ("Syslog server", "Load balancer", "Policy engine", "UPS"), ("syslog", "logs")),
    Question("q_forensics", "Accounting", "Which process investigates what happened during a security incident?", "Forensic analysis", "Forensic analysis uses evidence such as logs, source IPs, accessed files, and unusual activity to understand an incident.", ("Forensic analysis", "Data masking", "Load balancing", "Authorisation"), ("forensic", "investigat")),
    Question("q_password_factor", "Authentication", "Which authentication factor category does a password belong to?", "Something you know", "Passwords, PINs, passphrases, and security question answers are knowledge factors.", ("Something you know", "Something you have", "Something you are", "Somewhere you are"), ("something you know", "knowledge")),
    Question("q_phone_factor", "Authentication", "Which authentication factor category does a phone used for a login code belong to?", "Something you have", "A phone, smart card, token, or security key is a possession factor.", ("Something you know", "Something you have", "Something you do", "Somewhere you are"), ("something you have", "possession")),
    Question("q_mfa", "Authentication", "Which pair is true multi-factor authentication?", "Password and fingerprint", "MFA must combine different factor categories. Password is something you know; fingerprint is something you are.", ("Password and PIN", "Password and security question", "Password and fingerprint", "PIN and passphrase"), ("password", "fingerprint")),
    Question("q_location", "Authentication", "A system checks whether a user is logging in from the office network. Which factor is this?", "Somewhere you are", "Location factors use evidence such as GPS, IP address, Wi-Fi network, or geofencing.", ("Something you have", "Something you do", "Somewhere you are", "Something you know"), ("somewhere you are", "location")),
    Question("q_authz_after_authn", "Authorisation", "What happens first: authentication or authorisation?", "Authentication happens before authorisation", "A user first proves identity, then the system decides permissions and privileges.", ("Authentication happens before authorisation", "Authorisation happens before authentication", "They are the same thing", "Accounting happens first"), ("authentication", "before", "authorisation", "authorization")),
    Question("q_authorisation", "Authorisation", "A user can view files but cannot delete them. Which concept is this?", "Authorisation", "Authorisation decides what an authenticated user is allowed to do.", ("Authentication", "Authorisation", "Accounting", "Non-repudiation"), ("authorisation", "authorization")),
    Question("q_execute", "Authorisation", "Which permission allows a user to run a program or command?", "Execute", "Execute permission allows a user to run a program or command.", ("Read", "Modify", "Execute", "Delete"), ("execute",)),
    Question("q_least_privilege", "Authorisation", "Which principle says users should only receive the minimum access needed for their job?", "Least privilege", "Least privilege reduces data leaks, accidental changes, insider threats, malware damage, and system misuse.", ("Zero knowledge", "Least privilege", "Non-repudiation", "Failover"), ("least privilege", "minimum access")),
    Question("q_load_balancing", "Redundancy", "Which availability method spreads user traffic across multiple servers?", "Load balancing", "A load balancer spreads traffic across multiple servers so one server does not become overloaded.", ("Load balancing", "Hashing", "Data masking", "Digital signatures"), ("load balancing", "load balancer")),
    Question("q_failover", "Redundancy", "What is failover?", "Automatically switching to a backup system when the main one fails", "Failover helps maintain availability by moving service to a backup system after failure.", ("Converting data into a hash", "Automatically switching to a backup system when the main one fails", "Recording user activity in logs", "Hiding sensitive data"), ("backup", "fails", "switching")),
    Question("q_redundancy", "Redundancy", "Which phrase best describes redundancy?", "Having backup critical components if something fails", "Redundancy duplicates critical components and removes single points of failure.", ("Proof that someone did something", "Having backup critical components if something fails", "Deciding what a user may access", "Obscuring sensitive data"), ("backup", "critical", "fails", "single point")),
    Question("q_technical_control", "Controls", "Which control category uses technology, hardware, or software to reduce risk?", "Technical controls", "Technical controls include firewalls, antivirus, encryption, access control lists, MFA, and IDS.", ("Technical controls", "Directive controls", "Business gap analysis", "Accounting"), ("technical", "technology", "hardware", "software")),
    Question("q_preventative", "Controls", "Which control type is designed to stop an incident before it happens?", "Preventative", "Preventative controls reduce the chance of a threat becoming a real problem.", ("Preventative", "Detective", "Corrective", "Compensating"), ("preventative", "preventive", "stop")),
    Question("q_deterrent", "Controls", "Warning signs, visible guards, fences, and legal warnings are examples of which control type?", "Deterrent", "Deterrent controls discourage attackers by making them think twice.", ("Deterrent", "Corrective", "Directive", "Technical"), ("deterrent", "discourage")),
    Question("q_detective", "Controls", "Audit logs, SIEM alerts, and file integrity monitoring are examples of which control type?", "Detective", "Detective controls identify when suspicious or unwanted activity has happened.", ("Preventative", "Detective", "Corrective", "Directive"), ("detective",)),
    Question("q_corrective", "Controls", "Backups, malware removal, and system recovery are examples of which control type?", "Corrective", "Corrective controls fix or reduce damage after an incident.", ("Corrective", "Deterrent", "Preventative", "Compensating"), ("corrective",)),
    Question("q_compensating", "Controls", "If an old system cannot support MFA, stricter monitoring and IP restrictions may be used instead. What type of control is this?", "Compensating", "Compensating controls are alternative controls used when the preferred control cannot be used.", ("Compensating", "Detective", "Directive", "Corrective"), ("compensating", "alternative")),
    Question("q_directive", "Controls", "Policies, procedures, standards, and training instructions are examples of which control type?", "Directive", "Directive controls tell people what they should or should not do.", ("Directive", "Preventative", "Detective", "Technical"), ("directive", "policy", "procedure")),
    Question("q_zero_trust", "Zero Trust", "Which phrase best describes Zero Trust?", "Never trust, always verify", "Zero Trust requires every access request to be checked, even inside the network.", ("Trust internal users only", "Never trust, always verify", "Encrypt everything only", "Allow access after first login"), ("never trust", "always verify", "verify")),
    Question("q_control_plane", "Zero Trust", "In Zero Trust Architecture, which plane makes access decisions and manages policies?", "Control Plane", "The Control Plane is the decision-making and policy-management part of Zero Trust.", ("Control Plane", "Data Plane", "Power Plane", "Audit Plane"), ("control plane", "decision")),
    Question("q_data_plane", "Zero Trust", "In Zero Trust Architecture, which plane carries out the access decision?", "Data Plane", "The Data Plane is where access actually happens and the decision is enforced.", ("Data Plane", "Control Plane", "Business Plane", "Scope Plane"), ("data plane", "carries out", "enforce")),
    Question("q_policy_engine", "Zero Trust", "Which Zero Trust component checks the request against policies and decides allow, deny, or limit?", "Policy Engine", "The Policy Engine makes the access decision.", ("Policy Engine", "Syslog server", "Load balancer", "Audit trail"), ("policy engine", "decides")),
    Question("q_pep", "Zero Trust", "Which Zero Trust component enforces the access decision?", "Policy Enforcement Point", "The Policy Enforcement Point allows, blocks, or limits the request.", ("Policy Enforcement Point", "Policy Engine", "SIEM", "Technical gap analysis"), ("policy enforcement", "pep", "enforce")),
    Question("q_adaptive_identity", "Zero Trust", "What does Adaptive Identity mean?", "Identity checks adapt to real-time risk context", "Adaptive Identity looks at context such as normal device, location, behaviour, time, and device health.", ("Identity checks adapt to real-time risk context", "Every user gets permanent admin access", "Only passwords are checked", "Logs are deleted automatically"), ("adaptive", "identity", "risk", "context")),
    Question("q_gap_analysis", "Gap Analysis", "What does gap analysis compare?", "Current state and desired state", "Gap analysis compares where the organisation is now with where it wants to be.", ("Current state and desired state", "Threats and passwords", "Logs and hashes", "Users and IP addresses"), ("current state", "desired state")),
    Question("q_gap_steps", "Gap Analysis", "Which set best describes the basic gap analysis steps?", "Define scope, gather current-state data, identify gaps, develop a fix plan", "The notes describe scope, current-state data, gaps, and a plan to bridge the gaps.", ("Define scope, gather current-state data, identify gaps, develop a fix plan", "Encrypt data, delete logs, add users, remove backups", "Authenticate, authorise, account, archive", "Detect, deter, deny, destroy"), ("scope", "current", "gaps", "plan")),
    Question("q_technical_gap", "Gap Analysis", "Which gap analysis type checks systems, tools, infrastructure, patching, MFA, logging, and configurations?", "Technical Gap Analysis", "Technical gap analysis focuses on technology and infrastructure capability.", ("Technical Gap Analysis", "Business Gap Analysis", "Audit Trail", "Data Plane"), ("technical", "technology", "infrastructure")),
    Question("q_business_gap", "Gap Analysis", "Which gap analysis type checks processes, responsibilities, workflows, readiness, and training?", "Business Gap Analysis", "Business gap analysis focuses on how the organisation works, not just technology.", ("Business Gap Analysis", "Technical Gap Analysis", "Policy Engine", "Syslog"), ("business", "process", "training")),
    Question("q_poam", "Gap Analysis", "What is a POA&M?", "A fix-it plan with actions, owners, resources, timelines, milestones, and status", "A Plan of Action and Milestones turns gap analysis findings into a practical remediation plan.", ("A fix-it plan with actions, owners, resources, timelines, milestones, and status", "A password-only authentication method", "A backup power source", "A firewall rule set"), ("plan of action", "milestones", "fix", "timeline")),
    Question("q_risk_pair", "Risk basics", "Which pair is required for security risk to exist?", "Threat and vulnerability", "Threat with no vulnerability is no risk, and vulnerability with no threat is no risk.", ("Threat and vulnerability", "Threat and encryption", "Vulnerability and training", "Availability and masking"), ("threat", "vulnerability")),
    Question("q_non_repudiation", "Risk basics", "What does non-repudiation help prove?", "That someone cannot deny an action later", "Non-repudiation provides evidence linking a person to an action, message, or transaction.", ("That data is always available", "That someone cannot deny an action later", "That passwords are strong", "That a network is segmented"), ("cannot deny", "proof", "action")),
)


def wrap(text: str) -> str:
    return textwrap.fill(text, width=88)


def load_progress() -> dict[str, dict[str, int]]:
    if not PROGRESS_FILE.exists():
        return {}
    try:
        raw_progress = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return {
        key: {
            "correct": int(value.get("correct", 0)),
            "incorrect": int(value.get("incorrect", 0)),
        }
        for key, value in raw_progress.items()
        if isinstance(value, dict)
    }


def save_progress(progress: dict[str, dict[str, int]]) -> None:
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2, sort_keys=True), encoding="utf-8")


def record_answer(progress: dict[str, dict[str, int]], question: Question, correct: bool) -> None:
    stats = progress.setdefault(question.id, {"correct": 0, "incorrect": 0})
    if correct:
        stats["correct"] += 1
    else:
        stats["incorrect"] += 1


def weighted_questions(questions: tuple[Question, ...], topic: str | None) -> list[Question]:
    progress = load_progress()
    pool = [question for question in questions if topic is None or question.topic == topic]
    weighted_pool: list[Question] = []
    for question in pool:
        stats = progress.get(question.id, {"correct": 0, "incorrect": 0})
        weight = 1 + min(stats["incorrect"], 4)
        if stats["incorrect"] > stats["correct"]:
            weight += 2
        weighted_pool.extend([question] * weight)
    RANDOM.shuffle(weighted_pool)
    return weighted_pool


def choose_topic() -> str | None:
    print("\nTopics")
    print("0. All topics")
    for index, topic in enumerate(TOPICS, start=1):
        print(f"{index}. {topic.name}")

    while True:
        choice = input("Choose a topic: ").strip()
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(TOPICS):
            return TOPICS[int(choice) - 1].name
        print(f"Enter a number from 0 to {len(TOPICS)}.")


def show_topics() -> None:
    print("\nSecurity+ Topics")
    for topic in TOPICS:
        print(f"\n{topic.name}")
        print(wrap(topic.summary))


def run_flashcards(topic: str | None, shuffled: bool) -> None:
    cards = [card for card in FLASHCARDS if topic is None or card.topic == topic]
    if shuffled:
        RANDOM.shuffle(cards)

    print("\nFlashcards")
    print("Press Enter to reveal each answer. Type q then Enter to stop.\n")

    for index, card in enumerate(cards, start=1):
        print(f"{index}. [{card.topic}] {card.term}")
        if card.hint:
            print(f"Hint: {card.hint}")
        command = input("> ")
        if command.strip().lower() == "q":
            break
        print(wrap(card.answer))
        print()


def run_quiz(question_count: int, topic: str | None) -> None:
    progress = load_progress()
    selected = pick_questions(question_count, topic)
    score = 0

    print("\nMultiple-Choice Quiz")
    print("Weak questions appear more often. Answers are randomised each time.\n")

    for index, question in enumerate(selected, start=1):
        options = list(question.options)
        RANDOM.shuffle(options)
        print_question_header(index, question)
        for option_index, option in enumerate(options, start=1):
            print(f"   {option_index}. {option}")

        chosen_answer = options[read_option(len(options)) - 1]
        correct = chosen_answer == question.answer
        score += int(correct)
        record_answer(progress, question, correct)
        explain_answer(question, correct)

    save_progress(progress)
    show_session_score(score, len(selected))


def run_short_answer(question_count: int, topic: str | None) -> None:
    progress = load_progress()
    selected = pick_questions(question_count, topic)
    score = 0

    print("\nShort-Answer Practice")
    print("Type a short answer. Do not worry about perfect wording.\n")

    for index, question in enumerate(selected, start=1):
        print_question_header(index, question)
        user_answer = input("Your answer: ").strip()
        correct = is_short_answer_correct(user_answer, question)
        score += int(correct)
        record_answer(progress, question, correct)
        explain_answer(question, correct)

    save_progress(progress)
    show_session_score(score, len(selected))


def pick_questions(question_count: int, topic: str | None) -> list[Question]:
    selected: list[Question] = []
    seen_ids: set[str] = set()
    for question in weighted_questions(QUESTIONS, topic):
        if question.id in seen_ids:
            continue
        selected.append(question)
        seen_ids.add(question.id)
        if len(selected) == question_count:
            break
    return selected


def print_question_header(index: int, question: Question) -> None:
    print(f"{index}. [{question.topic}] {wrap(question.prompt)}")


def read_option(option_count: int) -> int:
    while True:
        raw_value = input("Your answer: ").strip()
        if raw_value.isdigit() and 1 <= int(raw_value) <= option_count:
            return int(raw_value)
        print(f"Enter a number from 1 to {option_count}.")


def is_short_answer_correct(user_answer: str, question: Question) -> bool:
    normalised_answer = normalise(user_answer)
    if not normalised_answer:
        return False
    if normalise(question.answer) in normalised_answer:
        return True
    matched_keywords = {
        normalise(keyword)
        for keyword in question.keywords
        if normalise(keyword) in normalised_answer
    }
    needed_matches = 1 if len(set(question.keywords)) <= 2 else 2
    return len(matched_keywords) >= needed_matches


def normalise(text: str) -> str:
    return (
        text.lower()
        .replace("authorization", "authorisation")
        .replace("-", " ")
        .strip()
    )


def explain_answer(question: Question, correct: bool) -> None:
    if correct:
        print("Correct.")
    else:
        print(f"Not quite. Good answer: {question.answer}")
    print(wrap(question.explanation))
    print()


def show_session_score(score: int, total: int) -> None:
    print(f"Session score: {score}/{total} ({score / total:.0%})")
    print("Progress saved.")


def show_progress() -> None:
    progress = load_progress()
    print("\nProgress By Topic")
    for topic in TOPICS:
        questions = [question for question in QUESTIONS if question.topic == topic.name]
        correct = sum(progress.get(question.id, {}).get("correct", 0) for question in questions)
        incorrect = sum(progress.get(question.id, {}).get("incorrect", 0) for question in questions)
        total = correct + incorrect
        score = f"{correct / total:.0%}" if total else "Not started"
        print(f"{topic.name}: {score} ({correct} correct, {incorrect} incorrect)")

    weak = weakest_questions(progress)
    if weak:
        print("\nWeak Questions")
        for question in weak:
            stats = progress.get(question.id, {"correct": 0, "incorrect": 0})
            print(f"- [{question.topic}] {question.prompt} ({stats['incorrect']} incorrect)")


def weakest_questions(progress: dict[str, dict[str, int]]) -> list[Question]:
    attempted = [
        question
        for question in QUESTIONS
        if progress.get(question.id, {}).get("incorrect", 0) > progress.get(question.id, {}).get("correct", 0)
    ]
    return sorted(
        attempted,
        key=lambda question: progress.get(question.id, {}).get("incorrect", 0),
        reverse=True,
    )[:5]


def explain_risk(has_threat: bool, has_vulnerability: bool) -> str:
    if has_threat and has_vulnerability:
        return "Risk exists: a threat can exploit a vulnerability."
    if has_threat:
        return "No risk from this scenario yet: there is a threat, but no matching vulnerability."
    if has_vulnerability:
        return "No risk from this scenario yet: there is a vulnerability, but no active threat."
    return "No risk from this scenario: there is no threat and no vulnerability."


def run_risk_helper() -> None:
    print("\nRisk Helper")
    has_threat = read_yes_no("Is there a threat? ")
    has_vulnerability = read_yes_no("Is there a vulnerability? ")
    print(wrap(explain_risk(has_threat, has_vulnerability)))


def read_yes_no(prompt: str) -> bool:
    while True:
        value = input(prompt).strip().lower()
        if value in {"y", "yes"}:
            return True
        if value in {"n", "no"}:
            return False
        print("Please enter yes or no.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple Security+ revision program.")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("topics", help="Show organised topics.")

    flashcards = subparsers.add_parser("flashcards", help="Review flashcards.")
    flashcards.add_argument("--topic", choices=[topic.name for topic in TOPICS], help="Study one topic.")
    flashcards.add_argument("--ordered", action="store_true", help="Show cards in a fixed order.")

    quiz = subparsers.add_parser("quiz", help="Multiple-choice quiz.")
    quiz.add_argument("-n", "--count", type=int, default=10, help="Number of questions.")
    quiz.add_argument("--topic", choices=[topic.name for topic in TOPICS], help="Quiz one topic.")

    short = subparsers.add_parser("short", help="Short-answer practice.")
    short.add_argument("-n", "--count", type=int, default=10, help="Number of questions.")
    short.add_argument("--topic", choices=[topic.name for topic in TOPICS], help="Practise one topic.")

    subparsers.add_parser("progress", help="Show progress by topic.")
    subparsers.add_parser("risk", help="Check whether a threat/vulnerability scenario creates risk.")
    return parser


def run_menu() -> None:
    while True:
        print("\nSecurity+ Revision Program")
        print("1. View topics")
        print("2. Flashcards")
        print("3. Multiple-choice quiz")
        print("4. Short-answer practice")
        print("5. Progress")
        print("6. Risk helper")
        print("7. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_topics()
        elif choice == "2":
            run_flashcards(choose_topic(), shuffled=True)
        elif choice == "3":
            run_quiz(question_count=10, topic=choose_topic())
        elif choice == "4":
            run_short_answer(question_count=10, topic=choose_topic())
        elif choice == "5":
            show_progress()
        elif choice == "6":
            run_risk_helper()
        elif choice == "7":
            return
        else:
            print("Enter a number from 1 to 7.")


def clean_count(count: int, topic: str | None) -> int:
    available = sum(1 for question in QUESTIONS if topic is None or question.topic == topic)
    return max(1, min(count, available))


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        run_menu()
    elif args.command == "topics":
        show_topics()
    elif args.command == "flashcards":
        run_flashcards(args.topic, shuffled=not args.ordered)
    elif args.command == "quiz":
        run_quiz(clean_count(args.count, args.topic), args.topic)
    elif args.command == "short":
        run_short_answer(clean_count(args.count, args.topic), args.topic)
    elif args.command == "progress":
        show_progress()
    elif args.command == "risk":
        run_risk_helper()


if __name__ == "__main__":
    main()
