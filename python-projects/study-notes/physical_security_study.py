#!/usr/bin/env python3
"""Beginner-friendly Security+ revision program for Physical Security."""

from __future__ import annotations

import argparse
import json
import random
import textwrap
from dataclasses import dataclass
from pathlib import Path

RANDOM = random.SystemRandom()
PROGRESS_FILE = Path(__file__).with_name("physical_security_progress.json")


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
    Topic("Physical security basics", "Physical security protects people, facilities, devices, media, and supporting infrastructure."),
    Topic("Access controls", "Physical access controls limit who can enter restricted areas or touch important equipment."),
    Topic("Monitoring", "Monitoring controls help detect, record, and investigate physical security events."),
    Topic("Environmental controls", "Environmental controls keep equipment available by protecting against fire, heat, humidity, and power loss."),
    Topic("Physical attacks", "Attackers may use tailgating, shoulder surfing, dumpster diving, theft, or tampering."),
    Topic("Secure areas", "Server rooms, wiring closets, data centres, and reception areas need layered physical controls."),
    Topic("Control types", "Physical controls can be deterrent, preventive, detective, corrective, or compensating."),
    Topic("Exam clues", "Security+ questions often describe the control by its purpose: discourage, stop, detect, or recover."),
)


FLASHCARDS: tuple[Flashcard, ...] = (
    Flashcard("fc_physical_security", "Physical security basics", "Physical security", "Protecting people, buildings, equipment, media, and infrastructure from physical access, damage, or disruption.", "Real-world protection."),
    Flashcard("fc_physical_cia", "Physical security basics", "Physical security and CIA", "Physical security supports confidentiality by blocking access, integrity by preventing tampering, and availability by protecting equipment.", "CIA still applies."),
    Flashcard("fc_badge", "Access controls", "Badge reader", "An electronic access control that checks an ID card or token before allowing entry.", "Tap or scan to enter."),
    Flashcard("fc_biometrics", "Access controls", "Biometrics", "Authentication based on physical or behavioural traits such as fingerprint, face, iris, voice, or gait.", "Something you are or do."),
    Flashcard("fc_mantrap", "Access controls", "Mantrap", "A small controlled area with two doors that helps ensure only one authorised person enters at a time.", "Two-door controlled entry."),
    Flashcard("fc_turnstile", "Access controls", "Turnstile", "A physical barrier that controls one-person-at-a-time entry, often using a badge or ticket.", "Controlled flow."),
    Flashcard("fc_tailgating", "Physical attacks", "Tailgating", "Following an authorised person into a restricted area without authenticating.", "Walking in behind someone."),
    Flashcard("fc_shoulder_surfing", "Physical attacks", "Shoulder surfing", "Watching someone enter or view sensitive information, such as a password or PIN.", "Looking over a shoulder."),
    Flashcard("fc_dumpster_diving", "Physical attacks", "Dumpster diving", "Searching rubbish for sensitive information, documents, badges, storage media, or hardware.", "Trash can leak data."),
    Flashcard("fc_cctv", "Monitoring", "CCTV", "Video monitoring used to deter activity, detect incidents, and provide evidence.", "Cameras and recordings."),
    Flashcard("fc_visitor_log", "Monitoring", "Visitor log", "A record of who visited, when they arrived, who they met, and when they left.", "Reception evidence."),
    Flashcard("fc_tamper_seal", "Monitoring", "Tamper-evident seal", "A seal that shows visible evidence if equipment, packaging, or media has been opened.", "Shows signs of tampering."),
    Flashcard("fc_ups", "Environmental controls", "UPS", "An uninterruptible power supply gives short-term backup power and helps prevent sudden shutdowns.", "Battery backup."),
    Flashcard("fc_generator", "Environmental controls", "Backup generator", "A longer-term backup power source used when utility power is unavailable.", "Longer power outage support."),
    Flashcard("fc_hvac", "Environmental controls", "HVAC", "Heating, ventilation, and air conditioning helps maintain safe temperature and airflow for equipment.", "Temperature and airflow."),
    Flashcard("fc_fire_suppression", "Environmental controls", "Fire suppression", "Systems that detect or extinguish fire while reducing damage to people and equipment.", "Fire protection."),
    Flashcard("fc_wiring_closet", "Secure areas", "Wiring closet", "A room or cabinet containing network equipment and cabling that should be locked and monitored.", "Network gear lives here."),
    Flashcard("fc_data_centre", "Secure areas", "Data centre controls", "Data centres use layered controls such as guards, badges, cameras, cages, HVAC, UPS, and fire suppression.", "Layers around critical systems."),
    Flashcard("fc_deterrent", "Control types", "Deterrent control", "A control that discourages unwanted activity, such as signs, lights, visible guards, or cameras.", "Discourage."),
    Flashcard("fc_preventive", "Control types", "Preventive control", "A control that blocks or reduces the chance of an incident, such as locks, fences, and badge readers.", "Stop before it happens."),
    Flashcard("fc_detective", "Control types", "Detective control", "A control that identifies or records an event, such as CCTV recordings, alarms, and access logs.", "Notice and record."),
    Flashcard("fc_corrective", "Control types", "Corrective control", "A control that helps recover after an incident, such as replacing hardware or restoring from backup.", "Fix after."),
)


QUESTIONS: tuple[Question, ...] = (
    Question("q_physical_security", "Physical security basics", "What does physical security protect?", "People, facilities, equipment, media, and infrastructure", "Physical security protects real-world assets from access, damage, theft, and disruption.", ("People, facilities, equipment, media, and infrastructure", "Only passwords", "Only cloud storage", "Only software code"), ("people", "facilities", "equipment")),
    Question("q_physical_cia", "Physical security basics", "How does physical security support availability?", "It protects equipment and facilities from disruption", "Power, fire, cooling, and access controls help keep systems usable when needed.", ("It deletes old logs", "It protects equipment and facilities from disruption", "It removes all authentication", "It replaces encryption"), ("protects", "equipment", "availability")),
    Question("q_badge_reader", "Access controls", "Which control checks an ID card before allowing entry?", "Badge reader", "A badge reader is a physical access control for doors and restricted areas.", ("Badge reader", "UPS", "Shredder", "Hash function"), ("badge", "reader")),
    Question("q_mantrap", "Access controls", "Which control uses two doors to restrict entry to one authorised person at a time?", "Mantrap", "A mantrap controls movement through a small secured space between two doors.", ("Mantrap", "Firewall", "Dumpster", "Generator"), ("mantrap", "two doors")),
    Question("q_turnstile", "Access controls", "Which physical barrier controls one-person-at-a-time entry?", "Turnstile", "Turnstiles reduce uncontrolled entry and can work with badges or tickets.", ("Turnstile", "SIEM", "UPS", "Hash"), ("turnstile", "one person")),
    Question("q_tailgating", "Physical attacks", "Someone follows an authorised employee through a secure door without using a badge. What is this?", "Tailgating", "Tailgating is entering by following someone who is authorised.", ("Tailgating", "Hashing", "Failover", "Patching"), ("tailgating", "follow")),
    Question("q_shoulder_surfing", "Physical attacks", "Watching someone type a PIN or password is called what?", "Shoulder surfing", "Shoulder surfing is observing sensitive information directly.", ("Shoulder surfing", "Dumpster diving", "Load balancing", "Segmentation"), ("shoulder", "surfing", "watching")),
    Question("q_dumpster_diving", "Physical attacks", "Searching rubbish for sensitive documents or media is called what?", "Dumpster diving", "Dumpster diving can expose printed documents, storage media, badges, or equipment details.", ("Dumpster diving", "Tailgating", "Biometrics", "Failover"), ("dumpster", "rubbish", "trash")),
    Question("q_cctv", "Monitoring", "Which control records video evidence of physical activity?", "CCTV", "CCTV can deter, detect, and provide evidence for investigations.", ("CCTV", "UPS", "HVAC", "Mantrap"), ("cctv", "camera", "video")),
    Question("q_visitor_log", "Monitoring", "Which record tracks who entered a site, when they arrived, and when they left?", "Visitor log", "Visitor logs help account for guests and investigate incidents.", ("Visitor log", "Firewall rule", "Checksum", "Load balancer"), ("visitor", "log")),
    Question("q_tamper_evident", "Monitoring", "Which control shows visible evidence that something has been opened or altered?", "Tamper-evident seal", "Tamper-evident seals do not always stop tampering, but they reveal signs of it.", ("Tamper-evident seal", "Backup generator", "Turnstile", "Data plane"), ("tamper", "seal")),
    Question("q_ups", "Environmental controls", "Which device gives short-term battery power during an outage?", "UPS", "A UPS helps prevent sudden shutdowns and supports availability.", ("UPS", "CCTV", "Mantrap", "Badge reader"), ("ups", "battery")),
    Question("q_generator", "Environmental controls", "Which control provides longer-term backup power during an outage?", "Backup generator", "Generators can support systems during longer power failures.", ("Backup generator", "Visitor log", "Biometric scanner", "Fence"), ("generator", "power")),
    Question("q_hvac", "Environmental controls", "Which system controls temperature, ventilation, and airflow for equipment rooms?", "HVAC", "HVAC helps prevent overheating and environmental damage.", ("HVAC", "MFA", "CCTV", "Turnstile"), ("hvac", "temperature", "airflow")),
    Question("q_fire_suppression", "Environmental controls", "Which environmental control detects or extinguishes fire?", "Fire suppression", "Fire suppression protects people, facilities, and equipment from fire damage.", ("Fire suppression", "Tailgating", "Shoulder surfing", "Access log"), ("fire", "suppression")),
    Question("q_wiring_closet", "Secure areas", "Why should a wiring closet be locked?", "It contains network equipment and cabling that could be tampered with", "Physical access to network gear can allow disruption, rogue connections, or tampering.", ("It contains network equipment and cabling that could be tampered with", "It stores only public posters", "It removes the need for backups", "It encrypts all data automatically"), ("network", "equipment", "cabling")),
    Question("q_data_centre_layers", "Secure areas", "Why do data centres use layered physical controls?", "Critical systems need multiple protections if one control fails", "Layered controls reduce the chance that one failed control leads to full access or outage.", ("Critical systems need multiple protections if one control fails", "Only one lock is always enough", "Layers are only decorative", "They replace all technical controls"), ("layers", "critical", "multiple")),
    Question("q_deterrent", "Control types", "Warning signs, visible cameras, and guards mainly provide which control type?", "Deterrent", "Deterrent controls discourage unwanted activity.", ("Deterrent", "Corrective", "Compensating", "Accounting"), ("deterrent", "discourage")),
    Question("q_preventive", "Control types", "Locks, fences, and badge readers are mainly which control type?", "Preventive", "Preventive controls try to stop an incident before it happens.", ("Preventive", "Detective", "Corrective", "Forensic"), ("preventive", "preventative", "stop")),
    Question("q_detective", "Control types", "CCTV recordings, alarms, and access logs are mainly which control type?", "Detective", "Detective controls identify or record that something happened.", ("Detective", "Preventive", "Directive", "Compensating"), ("detective", "record", "detect")),
    Question("q_corrective", "Control types", "Replacing stolen equipment and restoring data from backup are examples of which control type?", "Corrective", "Corrective controls help recover after an incident.", ("Corrective", "Deterrent", "Preventive", "Biometric"), ("corrective", "recover")),
    Question("q_exam_discourage", "Exam clues", "If the question says a control is meant to discourage attackers, what type is it?", "Deterrent", "Discourage is the keyword for deterrent controls.", ("Deterrent", "Detective", "Corrective", "Availability"), ("deterrent", "discourage")),
    Question("q_exam_detect", "Exam clues", "If the question says a control records or alerts on an event, what type is it?", "Detective", "Record, detect, alert, and identify are clues for detective controls.", ("Detective", "Preventive", "Corrective", "Administrative"), ("detective", "record", "alert")),
    Question("q_exam_recover", "Exam clues", "If the question says a control restores service after an incident, what type is it?", "Corrective", "Restore, recover, repair, and replace are clues for corrective controls.", ("Corrective", "Deterrent", "Preventive", "Directive"), ("corrective", "restore", "recover")),
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
    print("\nPhysical Security Topics")
    for topic in TOPICS:
        print(f"\n{topic.name}")
        print(wrap(topic.summary))


def run_flashcards(topic: str | None, shuffled: bool) -> None:
    cards = [card for card in FLASHCARDS if topic is None or card.topic == topic]
    if shuffled:
        RANDOM.shuffle(cards)

    print("\nPhysical Security Flashcards")
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
        .replace("preventative", "preventive")
        .replace("rubbish", "trash")
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
    parser = argparse.ArgumentParser(description="Simple Security+ Physical Security revision program.")
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
        print("\nPhysical Security Revision Program")
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
