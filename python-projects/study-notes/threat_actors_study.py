#!/usr/bin/env python3
"""Beginner-friendly Security+ revision program for Threat Actors."""

from __future__ import annotations

import argparse
import json
import random
import textwrap
from dataclasses import dataclass
from pathlib import Path

RANDOM = random.SystemRandom()
PROGRESS_FILE = Path(__file__).with_name("threat_actors_progress.json")


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
    Topic("Threat actor basics", "A threat actor is a person or group that can cause harm to systems, data, or organisations."),
    Topic("Types of actors", "Security+ commonly groups actors by who they are and how capable they are."),
    Topic("Motivation", "Actors may be motivated by money, politics, revenge, ideology, curiosity, or competitive advantage."),
    Topic("Capability", "Actors differ by skill, funding, time, tools, and access."),
    Topic("Location", "Threat actors may be internal, external, or a partner/third party."),
    Topic("Insider threats", "Insiders may be malicious, negligent, or compromised."),
    Topic("Threat vectors", "A threat vector is the route, path, or method used to reach a target."),
    Topic("Attack surface", "Attack surface means all the possible points an attacker could target."),
    Topic("Defences", "Good defence uses layers such as MFA, patching, logging, segmentation, backups, and least privilege."),
    Topic("Exam clues", "Security+ questions often reveal the actor through clues such as money, ideology, espionage, or authorised access."),
)


FLASHCARDS: tuple[Flashcard, ...] = (
    Flashcard("fc_threat_actor", "Threat actor basics", "Threat actor", "A person, group, or organisation that can cause harm to systems, data, people, or assets.", "Who could attack or cause harm?"),
    Flashcard("fc_attack_vector", "Threat actor basics", "Attack vector", "The path or method a threat actor uses to attack, such as phishing, malware, stolen credentials, or exploiting a vulnerability.", "How the attack gets in."),
    Flashcard("fc_threat", "Threat actor basics", "Threat", "Anything that could cause harm, loss, damage, or compromise to IT systems.", "The danger."),
    Flashcard("fc_nation_state", "Types of actors", "Nation-state actor", "A government-backed actor with strong funding, advanced tools, patience, and strategic goals.", "Highly resourced and often stealthy."),
    Flashcard("fc_apt", "Types of actors", "Advanced Persistent Threat", "A skilled threat actor that gains access and remains hidden for a long time to spy, steal, or prepare future attacks.", "Advanced, patient, persistent."),
    Flashcard("fc_organised_crime", "Types of actors", "Organised crime", "Criminal groups that usually attack for financial gain, such as fraud, ransomware, and data theft.", "Money-focused."),
    Flashcard("fc_hacktivist", "Types of actors", "Hacktivist", "An attacker motivated by political, social, or ideological beliefs.", "Activism plus hacking."),
    Flashcard("fc_insider", "Types of actors", "Insider threat", "A trusted person inside an organisation who misuses access or accidentally causes harm.", "Employee, contractor, or partner."),
    Flashcard("fc_script_kiddie", "Types of actors", "Script kiddie", "An unskilled attacker who uses tools or scripts created by others.", "Low skill, borrowed tools."),
    Flashcard("fc_competitor", "Types of actors", "Competitor", "A rival organisation that may try to gain business advantage by stealing information or disrupting services.", "Business advantage."),
    Flashcard("fc_shadow_it", "Types of actors", "Shadow IT", "Systems, apps, or services used without official approval, creating security risk even without malicious intent.", "Unapproved technology."),
    Flashcard("fc_financial", "Motivation", "Financial motivation", "Attacking to make money through fraud, ransomware, extortion, theft, or selling data.", "Follow the money."),
    Flashcard("fc_ideology", "Motivation", "Ideological motivation", "Attacking to support a political, social, or religious belief.", "Common with hacktivists."),
    Flashcard("fc_revenge", "Motivation", "Revenge motivation", "Attacking because of anger, resentment, or a personal grievance.", "Often linked to insider threats."),
    Flashcard("fc_curiosity", "Motivation", "Curiosity motivation", "Attacking to learn, explore, test skills, or see what is possible.", "Often lower sophistication."),
    Flashcard("fc_espionage", "Motivation", "Espionage", "Spying or stealing confidential information such as trade secrets, government secrets, intellectual property, or research data.", "The attacker wants information."),
    Flashcard("fc_disruption", "Motivation", "Disruption", "Attacking to stop normal operations, such as through DDoS, deleting data, disabling systems, or damaging infrastructure.", "Stop services working."),
    Flashcard("fc_notoriety", "Motivation", "Notoriety or ego", "Attacking to gain attention, status, recognition, or bragging rights.", "Showing off."),
    Flashcard("fc_capability", "Capability", "Capability", "How able a threat actor is, based on skill, resources, funding, tools, time, and access.", "How strong are they?"),
    Flashcard("fc_sophistication", "Capability", "Sophistication", "The actor's level of skill, planning, stealth, and technical ability.", "Skill and planning level."),
    Flashcard("fc_resources", "Capability", "Resources", "The money, people, time, tools, infrastructure, and access available to an actor.", "What can they spend or use?"),
    Flashcard("fc_skill_level", "Capability", "Skill level", "How technically capable the attacker is, from low-skill tool use to advanced custom malware and stealth.", "How capable are they?"),
    Flashcard("fc_intent", "Capability", "Intent", "What the attacker wants to achieve, such as money, data theft, spying, disruption, access, or reputation damage.", "What do they want?"),
    Flashcard("fc_internal", "Location", "Internal threat actor", "An actor inside the organisation, such as an employee, contractor, or trusted partner.", "Already has some access."),
    Flashcard("fc_external", "Location", "External threat actor", "An actor outside the organisation who must break in or trick someone to gain access.", "Outside attacker."),
    Flashcard("fc_third_party", "Location", "Third-party threat", "Risk from suppliers, vendors, contractors, or partners connected to the organisation.", "Trusted connection can create risk."),
    Flashcard("fc_malicious_insider", "Insider threats", "Malicious insider", "A trusted person who intentionally causes harm, such as stealing data, deleting files, leaking information, or sabotaging systems.", "Intentional harm."),
    Flashcard("fc_negligent_insider", "Insider threats", "Negligent insider", "A trusted person who accidentally creates risk through careless actions, such as clicking phishing links or sending data to the wrong person.", "Accidental harm."),
    Flashcard("fc_compromised_insider", "Insider threats", "Compromised insider", "A legitimate user account or device that is controlled by an attacker without the real user knowing.", "Trusted account, attacker controlled."),
    Flashcard("fc_email_vector", "Threat vectors", "Email vector", "An attack route using phishing, malicious attachments, fake invoices, credential links, or business email compromise.", "Very common way in."),
    Flashcard("fc_web_vector", "Threat vectors", "Web vector", "An attack route targeting websites, web apps, browsers, fake login pages, or vulnerable applications.", "Websites and web apps."),
    Flashcard("fc_wireless_vector", "Threat vectors", "Wireless vector", "An attack route using Wi-Fi, Bluetooth, NFC, rogue access points, evil twin Wi-Fi, or wireless man-in-the-middle attacks.", "Wi-Fi and wireless tech."),
    Flashcard("fc_removable_media", "Threat vectors", "Removable media vector", "An attack route using USB drives, memory cards, external drives, or unauthorised data copying.", "USB risk."),
    Flashcard("fc_supply_chain", "Threat vectors", "Supply chain vector", "An attack route targeting a trusted vendor, supplier, software provider, third-party service, or software update.", "Trusted supplier risk."),
    Flashcard("fc_social_engineering", "Threat vectors", "Social engineering vector", "An attack route that targets people using phishing, vishing, smishing, pretexting, impersonation, baiting, quid pro quo, or tailgating.", "Attacking people."),
    Flashcard("fc_attack_surface", "Attack surface", "Attack surface", "The total collection of points that an attacker could target.", "Everything that could be attacked."),
    Flashcard("fc_digital_surface", "Attack surface", "Digital attack surface", "Technology exposed to attackers, such as web apps, open ports, APIs, cloud storage, public IPs, and login portals.", "Online or technical exposure."),
    Flashcard("fc_physical_surface", "Attack surface", "Physical attack surface", "Physical ways attackers could gain access, such as unlocked doors, server rooms, USB ports, lost laptops, and printed documents.", "Physical access points."),
    Flashcard("fc_human_surface", "Attack surface", "Human attack surface", "People who can be tricked, pressured, manipulated, or bribed.", "People can be targeted."),
    Flashcard("fc_surface_reduction", "Attack surface", "Attack surface reduction", "Removing or securing unnecessary exposure, such as closing unused ports, removing old accounts, patching, MFA, segmentation, and hardening.", "Fewer ways in."),
    Flashcard("fc_defence_depth", "Defences", "Defence in depth", "Using multiple layers of security so if one control fails, another can still help.", "Layered protection."),
    Flashcard("fc_defence_least_privilege", "Defences", "Least privilege", "Users and systems only get the access they need to do their job.", "Only necessary access."),
    Flashcard("fc_defence_patching", "Defences", "Patching", "Fixing known vulnerabilities through operating system, application, firmware, browser, and security updates.", "Closing known holes."),
    Flashcard("fc_defence_logging", "Defences", "Monitoring and logging", "Monitoring detects suspicious behaviour, while logs provide evidence of what happened.", "Evidence and early warning."),
    Flashcard("fc_segmentation", "Defences", "Network segmentation", "Dividing the network into separate areas to limit lateral movement if an attacker gets in.", "Limits attacker movement."),
    Flashcard("fc_backups", "Defences", "Backups", "Copies of data that help recovery after ransomware, deletion, corruption, or system failure.", "Recovery after damage."),
    Flashcard("fc_exam_money", "Exam clues", "Money clue", "Money, fraud, ransom, stolen cards, crypto theft, or profit usually points to organised crime.", "Follow the money."),
    Flashcard("fc_exam_cause", "Exam clues", "Cause clue", "Cause, protest, politics, activism, or ideology usually points to a hacktivist.", "Cause equals hacktivist."),
    Flashcard("fc_exam_government", "Exam clues", "Government clue", "Government-backed, espionage, sabotage, military advantage, or long-term stealth usually points to a nation-state actor.", "Government-backed attacker."),
    Flashcard("fc_exam_access", "Exam clues", "Authorised access clue", "Employee, contractor, vendor, partner, or authorised access usually points to an insider threat.", "Trusted access."),
)


QUESTIONS: tuple[Question, ...] = (
    Question("q_threat_actor", "Threat actor basics", "What is a threat actor?", "A person, group, or organisation that can cause harm", "A threat actor is the person or group behind a threat or attack.", ("A person, group, or organisation that can cause harm", "A backup copy of data", "A type of encryption key", "A firewall rule"), ("person", "group", "harm")),
    Question("q_attack_vector", "Threat actor basics", "What is an attack vector?", "The path or method used to attack", "Attack vectors include phishing, malware, stolen credentials, and exploiting vulnerabilities.", ("The path or method used to attack", "The final backup server", "A compliance document", "A type of audit log"), ("path", "method", "attack")),
    Question("q_nation_state", "Types of actors", "Which actor is usually government-backed, highly funded, and patient?", "Nation-state actor", "Nation-state actors often have strong resources, advanced tools, and strategic goals.", ("Nation-state actor", "Script kiddie", "Shadow IT", "Accidental insider"), ("nation", "state", "government")),
    Question("q_apt", "Types of actors", "What does APT usually mean?", "Advanced Persistent Threat", "An APT is advanced, stealthy, and persistent, often staying hidden for a long time.", ("Advanced Persistent Threat", "Automatic Password Tool", "Approved Policy Template", "Access Protection Token"), ("advanced", "persistent", "threat")),
    Question("q_organised_crime", "Types of actors", "Which actor type is most commonly motivated by profit?", "Organised crime", "Organised criminal groups often use fraud, ransomware, theft, and extortion to make money.", ("Organised crime", "Hacktivist", "Shadow IT", "Curious learner"), ("organised crime", "organized crime", "profit", "money")),
    Question("q_hacktivist", "Types of actors", "Which actor is motivated by political, social, or ideological beliefs?", "Hacktivist", "Hacktivists attack to support a cause or message.", ("Hacktivist", "Competitor", "Script kiddie", "Third-party supplier"), ("hacktivist", "ideology", "political")),
    Question("q_insider", "Types of actors", "Which actor already has trusted access inside an organisation?", "Insider threat", "Insider threats can be employees, contractors, or partners who misuse access or make mistakes.", ("Insider threat", "External attacker", "Nation-state actor", "Load balancer"), ("insider", "trusted", "access")),
    Question("q_script_kiddie", "Types of actors", "Which actor has low skill and mainly uses tools made by others?", "Script kiddie", "Script kiddies usually rely on existing scripts or tools instead of advanced knowledge.", ("Script kiddie", "APT", "Nation-state actor", "Organised crime"), ("script", "kiddie", "low skill")),
    Question("q_shadow_it", "Types of actors", "What is Shadow IT?", "Unapproved systems, apps, or services used without official approval", "Shadow IT creates risk because the organisation may not monitor, patch, or secure it properly.", ("Unapproved systems, apps, or services used without official approval", "A government-backed attacker", "A backup generator", "A type of encryption"), ("unapproved", "apps", "systems")),
    Question("q_competitor", "Types of actors", "Which actor may attack to gain business advantage?", "Competitor", "Competitors may seek trade secrets, customer data, pricing plans, or service disruption.", ("Competitor", "Script kiddie", "SIEM", "Policy engine"), ("competitor", "business", "advantage")),
    Question("q_financial", "Motivation", "Ransomware and payment fraud usually show which motivation?", "Financial motivation", "Financially motivated actors attack to make money.", ("Financial motivation", "Curiosity", "Pure accident", "Compliance"), ("financial", "money", "profit")),
    Question("q_revenge", "Motivation", "A former employee deletes files because they are angry. What is the likely motivation?", "Revenge", "Revenge is a personal grievance or anger-based motivation.", ("Revenge", "Availability", "Curiosity", "Compliance"), ("revenge", "anger", "grievance")),
    Question("q_espionage", "Motivation", "Which motivation means spying or stealing confidential information?", "Espionage", "Espionage focuses on information such as secrets, intellectual property, research, or diplomatic communications.", ("Espionage", "Notoriety", "Patching", "Shadow IT"), ("espionage", "spying", "secrets")),
    Question("q_disruption", "Motivation", "DDoS attacks and disabling systems usually point to which goal?", "Disruption", "Disruption means the attacker wants to stop normal operations.", ("Disruption", "Curiosity", "Accounting", "Least privilege"), ("disruption", "stop", "operations")),
    Question("q_notoriety", "Motivation", "An attacker defaces a famous website and brags online. What is the likely motivation?", "Notoriety or ego", "Notoriety means the attacker wants attention, status, or recognition.", ("Notoriety or ego", "Regulatory compliance", "Availability", "Data masking"), ("notoriety", "ego", "attention")),
    Question("q_capability", "Capability", "What does threat actor capability describe?", "How able the actor is based on skill, resources, tools, time, and access", "Capability is about how much ability and support the actor has.", ("How able the actor is based on skill, resources, tools, time, and access", "The number of backups an organisation has", "The colour of a warning banner", "A user password length only"), ("skill", "resources", "tools", "time", "access")),
    Question("q_sophistication", "Capability", "What does sophistication describe?", "The actor's skill, planning, stealth, and technical ability", "More sophisticated actors are usually better at planning, hiding, and using advanced techniques.", ("The actor's skill, planning, stealth, and technical ability", "Whether a user has read permission", "How old a server is", "The number of policies in a handbook"), ("skill", "planning", "stealth")),
    Question("q_intent", "Capability", "What does intent describe?", "What the attacker wants to achieve", "Intent is the attacker's goal, such as stealing money, spying, disrupting services, or gaining access.", ("What the attacker wants to achieve", "How many backups exist", "Whether a port is open", "Which colour the alert is"), ("what", "wants", "achieve", "goal")),
    Question("q_internal_external", "Location", "What is the main difference between internal and external threat actors?", "Internal actors already have some trusted access, external actors start outside", "Internal actors may already have accounts, knowledge, or physical access. External actors must get in from outside.", ("Internal actors already have some trusted access, external actors start outside", "External actors are always harmless", "Internal actors never make mistakes", "They are exactly the same"), ("internal", "trusted", "external", "outside")),
    Question("q_third_party", "Location", "Why can third parties create security risk?", "They may have trusted access or connections to the organisation", "Vendors, contractors, and suppliers can create risk because their access or systems may connect to yours.", ("They may have trusted access or connections to the organisation", "They remove all need for monitoring", "They are always more secure", "They cannot access any systems"), ("third party", "trusted", "connection", "vendor")),
    Question("q_malicious_insider", "Insider threats", "Which insider intentionally steals data, deletes files, leaks information, or sabotages systems?", "Malicious insider", "A malicious insider is a trusted person intentionally causing harm.", ("Malicious insider", "Negligent insider", "Compromised insider", "Script kiddie"), ("malicious", "insider", "intentional")),
    Question("q_negligent_insider", "Insider threats", "Which insider accidentally causes risk by clicking phishing links, losing a laptop, or sending data to the wrong person?", "Negligent insider", "A negligent insider is not trying to attack, but careless actions create risk.", ("Negligent insider", "Nation-state actor", "Hacktivist", "Competitor"), ("negligent", "accidental", "careless")),
    Question("q_compromised_insider", "Insider threats", "A legitimate user account is controlled by an attacker. What type of insider threat is this?", "Compromised insider", "A compromised insider is a real account or device controlled by an attacker.", ("Compromised insider", "Malicious insider", "Shadow IT", "Competitor"), ("compromised", "account", "attacker")),
    Question("q_email_vector", "Threat vectors", "Phishing, fake invoices, credential links, and malicious attachments are examples of which vector?", "Email vector", "Email is one of the most common attack vectors because messages can look legitimate and create urgency.", ("Email vector", "Physical attack surface", "Network segmentation", "Backups"), ("email", "phishing")),
    Question("q_supply_chain", "Threat vectors", "A malicious software update from a trusted vendor is an example of which vector?", "Supply chain vector", "Supply chain attacks target trusted vendors, suppliers, software providers, or third-party services.", ("Supply chain vector", "Wireless vector", "Notoriety", "Least privilege"), ("supply chain", "vendor", "supplier")),
    Question("q_social_engineering", "Threat vectors", "Which vector targets people through phishing, vishing, smishing, pretexting, impersonation, baiting, or tailgating?", "Social engineering vector", "Social engineering targets people instead of technology.", ("Social engineering vector", "Web vector", "Digital attack surface", "Patching"), ("social engineering", "people")),
    Question("q_removable_media", "Threat vectors", "Malicious USB drives and infected external drives are examples of which vector?", "Removable media vector", "Removable media includes USB drives, memory cards, and external drives.", ("Removable media vector", "Email vector", "Espionage", "Hacktivism"), ("removable", "usb", "external")),
    Question("q_attack_surface", "Attack surface", "What is attack surface?", "Everything that could be attacked", "The attack surface is the total collection of points an attacker could target.", ("Everything that could be attacked", "Only a password list", "Only a backup file", "A type of nation-state actor"), ("everything", "attacked", "target")),
    Question("q_digital_surface", "Attack surface", "Web apps, APIs, public IPs, cloud storage, open ports, and login portals are part of which attack surface?", "Digital attack surface", "The digital attack surface includes exposed technology attackers could target.", ("Digital attack surface", "Physical attack surface", "Human attack surface", "Financial motivation"), ("digital", "technology")),
    Question("q_human_surface", "Attack surface", "Employees, helpdesk staff, executives, contractors, and customers who can be tricked are part of which attack surface?", "Human attack surface", "The human attack surface includes people who can be tricked, pressured, manipulated, or bribed.", ("Human attack surface", "Physical attack surface", "Digital attack surface", "Compromised insider"), ("human", "people")),
    Question("q_surface_reduction", "Attack surface", "Closing unused ports, removing old accounts, patching, MFA, and hardening are examples of what?", "Attack surface reduction", "Attack surface reduction removes or secures unnecessary exposure, giving attackers fewer ways in.", ("Attack surface reduction", "Notoriety", "Business email compromise", "Espionage"), ("attack surface", "reduction", "fewer")),
    Question("q_defence_depth", "Defences", "What does defence in depth mean?", "Using multiple layers of security", "Defence in depth means if one control fails, another control can still help.", ("Using multiple layers of security", "Using one password everywhere", "Removing all logs", "Giving every user admin rights"), ("multiple", "layers", "security")),
    Question("q_segmentation", "Defences", "Which defence divides the network into separate areas to limit lateral movement?", "Network segmentation", "Segmentation limits how far an attacker can move if they get in.", ("Network segmentation", "Notoriety", "Shadow IT", "Attack vector"), ("network", "segmentation", "lateral")),
    Question("q_patching", "Defences", "Which defence closes known vulnerabilities through updates?", "Patching", "Patching fixes known holes in operating systems, applications, firmware, browsers, and security tools.", ("Patching", "Espionage", "Vishing", "Hacktivism"), ("patching", "updates")),
    Question("q_exam_money", "Exam clues", "Money, fraud, ransom, stolen cards, crypto theft, or profit points to which actor?", "Organised crime", "Financial clues usually point to organised cybercrime.", ("Organised crime", "Hacktivist", "Negligent insider", "Shadow IT"), ("organised crime", "money")),
    Question("q_exam_cause", "Exam clues", "Cause, protest, politics, activism, or ideology points to which actor?", "Hacktivist", "Cause-based clues usually point to hacktivists.", ("Hacktivist", "Competitor", "Compromised insider", "Script kiddie"), ("hacktivist", "cause")),
    Question("q_exam_government", "Exam clues", "Government-backed, espionage, sabotage, military advantage, or long-term stealth points to which actor?", "Nation-state actor", "Government-backed and long-term stealth clues usually point to nation-state actors.", ("Nation-state actor", "Negligent insider", "Shadow IT", "Competitor"), ("nation", "state", "government")),
    Question("q_exam_authorised_access", "Exam clues", "Employee, contractor, vendor, partner, or authorised access points to which actor?", "Insider threat", "Authorised access clues usually point to an insider threat.", ("Insider threat", "External attacker", "Load balancer", "Firewall"), ("insider", "authorised", "access")),
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


def weighted_questions(topic: str | None) -> list[Question]:
    progress = load_progress()
    pool = [question for question in QUESTIONS if topic is None or question.topic == topic]
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
    print("\nThreat Actors Topics")
    for topic in TOPICS:
        print(f"\n{topic.name}")
        print(wrap(topic.summary))


def run_flashcards(topic: str | None, shuffled: bool) -> None:
    cards = [card for card in FLASHCARDS if topic is None or card.topic == topic]
    if shuffled:
        RANDOM.shuffle(cards)

    print("\nThreat Actors Flashcards")
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
    for question in weighted_questions(topic):
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
        .replace("organized", "organised")
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple Security+ Threat Actors revision program.")
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
    return parser


def run_menu() -> None:
    while True:
        print("\nThreat Actors Revision Program")
        print("1. View topics")
        print("2. Flashcards")
        print("3. Multiple-choice quiz")
        print("4. Short-answer practice")
        print("5. Progress")
        print("6. Exit")

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
            return
        else:
            print("Enter a number from 1 to 6.")


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


if __name__ == "__main__":
    main()
