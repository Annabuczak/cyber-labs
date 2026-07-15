#!/usr/bin/env python3
"""Beginner-friendly Security+ revision program for Social Engineering."""

from __future__ import annotations

import argparse
import json
import random
import textwrap
from dataclasses import dataclass
from pathlib import Path

RANDOM = random.SystemRandom()
PROGRESS_FILE = Path(__file__).with_name("social_engineering_progress.json")


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
    Topic("Social engineering basics", "Social engineering manipulates people into helping an attack succeed."),
    Topic("Motivational triggers", "Attackers use emotions such as urgency, fear, authority, trust, curiosity, greed, and sympathy."),
    Topic("Phishing types", "Phishing uses fake messages; variants include spear phishing, whaling, smishing, vishing, and angler phishing."),
    Topic("Other attacks", "Social engineering also includes impersonation, pretexting, baiting, tailgating, shoulder surfing, and dumpster diving."),
    Topic("Scams and influence", "Fraud targets money, while influence campaigns try to shape opinions, beliefs, or behaviour."),
    Topic("Prevention", "Prevention combines awareness, verification, reporting, MFA, filtering, and technical controls."),
    Topic("Exam clues", "Security+ questions often reveal the attack through clues such as SMS, voice, senior targets, fake stories, or secure doors."),
)


FLASHCARDS: tuple[Flashcard, ...] = (
    Flashcard("fc_social_engineering", "Social engineering basics", "Social engineering", "Manipulating someone into revealing information, giving access, clicking a link, opening a file, sending money, or breaking normal security procedures.", "Attacking the human."),
    Flashcard("fc_human_target", "Social engineering basics", "Human target", "Social engineering targets people and their behaviour instead of only attacking technology.", "Hack the human."),
    Flashcard("fc_red_flags", "Social engineering basics", "Red flags", "Urgency, fear, secrecy, pressure, unusual payment requests, login-detail requests, MFA-code requests, suspicious links, and unexpected attachments.", "Pause before acting."),
    Flashcard("fc_trigger", "Motivational triggers", "Motivational trigger", "A psychological technique used to influence a victim's behaviour during a social engineering attack.", "Why the victim acts."),
    Flashcard("fc_urgency", "Motivational triggers", "Urgency", "Pressure that tries to make a victim act immediately before thinking or checking.", "You must act now."),
    Flashcard("fc_authority", "Motivational triggers", "Authority", "Pretending a request comes from someone powerful or trusted, such as a manager, bank, or IT support.", "This is from your manager."),
    Flashcard("fc_curiosity", "Motivational triggers", "Curiosity", "Tempting a victim to open a file, click a link, or investigate something interesting.", "Look at this photo."),
    Flashcard("fc_phishing", "Phishing types", "Phishing", "A fake email or message designed to steal details, spread malware, request money, or trick a user into unsafe action.", "Fake message."),
    Flashcard("fc_spear_phishing", "Phishing types", "Spear phishing", "Targeted phishing against a specific person or group.", "Specific target."),
    Flashcard("fc_whaling", "Phishing types", "Whaling", "Targeted phishing against senior people such as executives.", "Big target."),
    Flashcard("fc_smishing", "Phishing types", "Smishing", "Phishing by SMS or text message.", "SMS phishing."),
    Flashcard("fc_vishing", "Phishing types", "Vishing", "Phishing by voice call.", "Voice phishing."),
    Flashcard("fc_angler", "Phishing types", "Angler phishing", "Fake customer support on social media.", "Social-media support scam."),
    Flashcard("fc_impersonation", "Other attacks", "Impersonation", "Pretending to be someone else, such as IT support, a manager, a bank employee, or a trusted vendor.", "Fake identity."),
    Flashcard("fc_pretexting", "Other attacks", "Pretexting", "Creating a fake story or scenario to gain trust and ask for information or access.", "Fake story."),
    Flashcard("fc_baiting", "Other attacks", "Baiting", "Offering something tempting, such as a free USB drive or download, to trick the victim.", "Tempting offer."),
    Flashcard("fc_tailgating", "Other attacks", "Tailgating", "Following someone into a secure area without permission.", "Following inside."),
    Flashcard("fc_shoulder_surfing", "Other attacks", "Shoulder surfing", "Watching someone type or view a password, PIN, or other sensitive information.", "Watching secrets."),
    Flashcard("fc_dumpster_diving", "Other attacks", "Dumpster diving", "Searching rubbish for sensitive information, documents, or media.", "Rubbish searching."),
    Flashcard("fc_quid_pro_quo", "Other attacks", "Quid pro quo", "Offering something in exchange for information or access.", "Something for something."),
    Flashcard("fc_watering_hole", "Other attacks", "Watering hole attack", "Compromising a website commonly visited by the intended target group.", "Target a familiar website."),
    Flashcard("fc_bec", "Scams and influence", "Business email compromise", "Email fraud used to trick a business into sending money or data, often using authority and urgency.", "Fake business request."),
    Flashcard("fc_fraud", "Scams and influence", "Fraud or scam", "A dishonest attempt to trick someone into giving money, information, or access.", "Fake invoice, delivery fee, or refund."),
    Flashcard("fc_influence", "Scams and influence", "Influence campaign", "An attempt to shape opinions, beliefs, or behaviour using tactics such as fake accounts, bots, propaganda, or manipulated content.", "Manipulating beliefs."),
    Flashcard("fc_misinformation", "Scams and influence", "Misinformation", "False information shared without necessarily intending harm.", "False, not necessarily deliberate."),
    Flashcard("fc_disinformation", "Scams and influence", "Disinformation", "False information deliberately shared to mislead.", "Deliberately misleading."),
    Flashcard("fc_safe_response", "Prevention", "Safe response", "Do not click, open, or share. Verify through a trusted route and report the message to IT or security.", "Pause, verify, report."),
    Flashcard("fc_phishing_controls", "Prevention", "Phishing controls", "Spam filtering, email gateways, DNS filtering, attachment sandboxing, MFA, training, simulations, SPF, DKIM, and DMARC.", "Technology plus awareness."),
    Flashcard("fc_campaign", "Prevention", "Anti-phishing campaign", "Training that uses awareness material, simulated emails, reporting buttons, feedback, and measurements to build safer habits.", "Teach and measure."),
    Flashcard("fc_mfa", "Prevention", "MFA against phishing", "MFA reduces the damage caused by a stolen password because the attacker still needs another factor.", "Password plus another factor."),
    Flashcard("fc_exam_smishing", "Exam clues", "SMS clue", "A phishing message sent by SMS or text is smishing.", "SMS equals smishing."),
    Flashcard("fc_exam_vishing", "Exam clues", "Voice clue", "A phishing attempt made by phone call is vishing.", "Voice equals vishing."),
    Flashcard("fc_exam_whaling", "Exam clues", "Executive clue", "A targeted phishing attack against an executive is whaling.", "Big target."),
)


QUESTIONS: tuple[Question, ...] = (
    Question("q_social_engineering", "Social engineering basics", "What is social engineering?", "Manipulating a person into helping an attack succeed", "Social engineering targets human behaviour to gain information, access, money, or unsafe actions.", ("Manipulating a person into helping an attack succeed", "Replacing a broken server", "Encrypting a backup", "Balancing network traffic"), ("manipulat", "person", "attack")),
    Question("q_human_target", "Social engineering basics", "What does social engineering mainly target?", "People", "Social engineering tries to hack the human rather than only hacking technology.", ("People", "Only firewalls", "Only backup servers", "Only encryption keys"), ("people", "human")),
    Question("q_red_flags", "Social engineering basics", "Which combination is a common social engineering warning sign?", "Urgency, secrecy, and a request for an MFA code", "Pressure, secrecy, and requests for credentials or codes should make a user stop and verify.", ("Urgency, secrecy, and a request for an MFA code", "A normal internal meeting invite", "A tested backup schedule", "A routine software update"), ("urgency", "secrecy", "mfa")),
    Question("q_trigger", "Motivational triggers", "What is a motivational trigger?", "A psychological technique used to influence a victim's behaviour", "Attackers use triggers such as fear, urgency, authority, trust, and curiosity.", ("A psychological technique used to influence a victim's behaviour", "A type of firewall rule", "A backup power source", "A hash value"), ("psychological", "influence", "behaviour")),
    Question("q_urgency", "Motivational triggers", "An email says your account will close in 10 minutes unless you click now. Which trigger is being used?", "Urgency", "Urgency pushes the victim to act before thinking or verifying.", ("Urgency", "Availability", "Redundancy", "Segmentation"), ("urgency", "act now")),
    Question("q_authority", "Motivational triggers", "A fake message claims to come from your manager. Which trigger is being used?", "Authority", "Attackers use authority to make requests feel important and difficult to refuse.", ("Authority", "Hashing", "Failover", "Patching"), ("authority", "manager")),
    Question("q_phishing", "Phishing types", "What is phishing?", "A fake email or message designed to trick the victim", "Phishing can steal details, spread malware, request money, or cause unsafe actions.", ("A fake email or message designed to trick the victim", "Following someone through a door", "Searching rubbish", "Watching a PIN"), ("fake", "email", "message")),
    Question("q_spear", "Phishing types", "Which phishing type targets a specific person or group?", "Spear phishing", "Spear phishing is targeted rather than general.", ("Spear phishing", "Smishing", "Vishing", "Dumpster diving"), ("spear", "phishing", "target")),
    Question("q_whaling", "Phishing types", "Which phishing type targets executives or other senior people?", "Whaling", "Whaling targets high-value senior people.", ("Whaling", "Smishing", "Baiting", "Tailgating"), ("whaling", "executive", "senior")),
    Question("q_smishing", "Phishing types", "A fake parcel-delivery text asks for a small fee. What is this?", "Smishing", "Smishing is phishing by SMS or text message.", ("Smishing", "Vishing", "Whaling", "Tailgating"), ("smishing", "sms", "text")),
    Question("q_vishing", "Phishing types", "A fake bank employee phones and asks for security details. What is this?", "Vishing", "Vishing is phishing by voice call.", ("Vishing", "Smishing", "Angler phishing", "Baiting"), ("vishing", "voice", "call")),
    Question("q_angler", "Phishing types", "A fake customer-support account contacts someone on social media. What is this?", "Angler phishing", "Angler phishing uses fake social-media customer support.", ("Angler phishing", "Whaling", "Tailgating", "Dumpster diving"), ("angler", "social media", "support")),
    Question("q_impersonation", "Other attacks", "An attacker pretends to be IT support and asks for a password. What attack is this?", "Impersonation", "Impersonation means pretending to be someone else.", ("Impersonation", "Tailgating", "Shoulder surfing", "Watering hole attack"), ("impersonation", "pretend", "identity")),
    Question("q_pretexting", "Other attacks", "An attacker invents a payroll-update story to ask for bank details. What attack is this?", "Pretexting", "Pretexting uses a fake story to make the request believable.", ("Pretexting", "Smishing", "Dumpster diving", "Whaling"), ("pretexting", "fake", "story")),
    Question("q_baiting", "Other attacks", "Leaving a tempting free USB drive for someone to use is an example of what?", "Baiting", "Baiting offers something tempting to make the victim act.", ("Baiting", "Tailgating", "Vishing", "Disinformation"), ("baiting", "tempt")),
    Question("q_tailgating", "Other attacks", "Following an employee into a secure area without permission is called what?", "Tailgating", "Tailgating bypasses physical entry checks by following an authorised person.", ("Tailgating", "Whaling", "Smishing", "Pretexting"), ("tailgating", "follow", "secure")),
    Question("q_shoulder_surfing", "Other attacks", "Watching someone enter a PIN is called what?", "Shoulder surfing", "Shoulder surfing means observing sensitive information directly.", ("Shoulder surfing", "Dumpster diving", "Baiting", "Vishing"), ("shoulder", "surfing", "watch")),
    Question("q_dumpster", "Other attacks", "Searching rubbish for printed passwords or sensitive documents is called what?", "Dumpster diving", "Dumpster diving looks for useful information in discarded material.", ("Dumpster diving", "Tailgating", "Whaling", "Spear phishing"), ("dumpster", "rubbish", "trash")),
    Question("q_quid_pro_quo", "Other attacks", "Offering technical help in exchange for login details is an example of what?", "Quid pro quo", "Quid pro quo means offering something in exchange for information or access.", ("Quid pro quo", "Whaling", "Shoulder surfing", "Smishing"), ("quid", "pro", "quo", "exchange")),
    Question("q_watering_hole", "Other attacks", "Compromising a website commonly visited by the intended victims is called what?", "Watering hole attack", "A watering hole attack targets a website familiar to the target group.", ("Watering hole attack", "Vishing", "Tailgating", "Dumpster diving"), ("watering", "hole", "website")),
    Question("q_bec", "Scams and influence", "A fake CEO email urgently asks finance to pay an invoice secretly. What is this?", "Business email compromise", "Business email compromise uses email fraud, authority, urgency, and sometimes secrecy to steal money or data.", ("Business email compromise", "Shoulder surfing", "Tailgating", "Misinformation"), ("business", "email", "compromise")),
    Question("q_influence", "Scams and influence", "Fake accounts, bots, propaganda, and manipulated media are used in what kind of campaign?", "Influence campaign", "Influence campaigns try to shape opinions, beliefs, or behaviour.", ("Influence campaign", "Anti-phishing campaign", "Backup campaign", "Patching campaign"), ("influence", "campaign", "belief")),
    Question("q_misinformation", "Scams and influence", "What is misinformation?", "False information shared without necessarily intending harm", "Misinformation may be false even when the person sharing it does not mean to mislead.", ("False information shared without necessarily intending harm", "False information deliberately shared to mislead", "A voice phishing call", "A fake story used for access"), ("false", "without", "intent")),
    Question("q_disinformation", "Scams and influence", "What is disinformation?", "False information deliberately shared to mislead", "Disinformation is intentionally misleading.", ("False information deliberately shared to mislead", "False information shared by mistake", "A secure email gateway", "A backup copy"), ("false", "deliberate", "mislead")),
    Question("q_safe_response", "Prevention", "What should a user do with a suspicious email?", "Do not click; verify through a trusted route and report it", "The safe response is to pause, avoid links and attachments, verify independently, and report the message.", ("Do not click; verify through a trusted route and report it", "Reply with a password", "Forward it to everyone", "Open the attachment to test it"), ("not", "click", "verify", "report")),
    Question("q_mfa", "Prevention", "Why is MFA useful against phishing?", "It reduces damage from a stolen password by requiring another factor", "A stolen password alone may not be enough when MFA is enabled.", ("It reduces damage from a stolen password by requiring another factor", "It makes every email genuine", "It deletes all spam automatically", "It replaces staff training"), ("password", "another", "factor")),
    Question("q_campaign", "Prevention", "What is the goal of an anti-phishing campaign?", "Build safer habits and improve recognition and reporting", "A good campaign teaches users, encourages reporting, and measures improvement without shaming staff.", ("Build safer habits and improve recognition and reporting", "Embarrass staff who click", "Remove all email accounts", "Replace every security control"), ("safer", "habits", "report")),
    Question("q_controls", "Prevention", "Which set contains phishing-prevention controls?", "Email filtering, MFA, training, simulations, SPF, DKIM, and DMARC", "Phishing prevention combines technology, training, and safe user behaviour.", ("Email filtering, MFA, training, simulations, SPF, DKIM, and DMARC", "Only door locks and CCTV", "Only UPS and generators", "Only backups and RAID"), ("filter", "mfa", "training")),
    Question("q_exam_text", "Exam clues", "Which answer should you think of when the clue is SMS or text message?", "Smishing", "Smishing means SMS phishing.", ("Smishing", "Vishing", "Whaling", "Baiting"), ("smishing", "sms")),
    Question("q_exam_voice", "Exam clues", "Which answer should you think of when the clue is a voice call?", "Vishing", "Vishing means voice phishing.", ("Vishing", "Smishing", "Whaling", "Pretexting"), ("vishing", "voice")),
    Question("q_exam_story", "Exam clues", "Which answer should you think of when the clue is a believable fake story?", "Pretexting", "Pretexting means using a fake scenario to gain trust.", ("Pretexting", "Whaling", "Tailgating", "Misinformation"), ("pretexting", "story")),
)


def wrap(text: str) -> str:
    return textwrap.fill(text, width=88)


def load_progress() -> dict[str, dict[str, int]]:
    if not PROGRESS_FILE.exists():
        return {}
    try:
        raw = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return {
        key: {"correct": int(value.get("correct", 0)), "incorrect": int(value.get("incorrect", 0))}
        for key, value in raw.items()
        if isinstance(value, dict)
    }


def save_progress(progress: dict[str, dict[str, int]]) -> None:
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2, sort_keys=True), encoding="utf-8")


def record_answer(progress: dict[str, dict[str, int]], question: Question, correct: bool) -> None:
    stats = progress.setdefault(question.id, {"correct": 0, "incorrect": 0})
    stats["correct" if correct else "incorrect"] += 1


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
    print("\nSocial Engineering Topics")
    for topic in TOPICS:
        print(f"\n{topic.name}")
        print(wrap(topic.summary))


def run_flashcards(topic: str | None, shuffled: bool) -> None:
    cards = [card for card in FLASHCARDS if topic is None or card.topic == topic]
    if shuffled:
        RANDOM.shuffle(cards)
    print("\nSocial Engineering Flashcards")
    print("Press Enter to reveal each answer. Type q then Enter to stop.\n")
    for index, card in enumerate(cards, start=1):
        print(f"{index}. [{card.topic}] {card.term}")
        if card.hint:
            print(f"Hint: {card.hint}")
        if input("> ").strip().lower() == "q":
            break
        print(wrap(card.answer))
        print()


def pick_questions(question_count: int, topic: str | None) -> list[Question]:
    selected: list[Question] = []
    seen_ids: set[str] = set()
    for question in weighted_questions(topic):
        if question.id not in seen_ids:
            selected.append(question)
            seen_ids.add(question.id)
        if len(selected) == question_count:
            break
    return selected


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
        correct = options[read_option(len(options)) - 1] == question.answer
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
        correct = is_short_answer_correct(input("Your answer: ").strip(), question)
        score += int(correct)
        record_answer(progress, question, correct)
        explain_answer(question, correct)
    save_progress(progress)
    show_session_score(score, len(selected))


def print_question_header(index: int, question: Question) -> None:
    print(f"{index}. [{question.topic}] {wrap(question.prompt)}")


def read_option(option_count: int) -> int:
    while True:
        raw_value = input("Your answer: ").strip()
        if raw_value.isdigit() and 1 <= int(raw_value) <= option_count:
            return int(raw_value)
        print(f"Enter a number from 1 to {option_count}.")


def is_short_answer_correct(user_answer: str, question: Question) -> bool:
    answer = normalise(user_answer)
    if not answer:
        return False
    if normalise(question.answer) in answer:
        return True
    matched = {normalise(keyword) for keyword in question.keywords if normalise(keyword) in answer}
    needed = 1 if len(set(question.keywords)) <= 2 else 2
    return len(matched) >= needed


def normalise(text: str) -> str:
    return text.lower().replace("-", " ").strip()


def explain_answer(question: Question, correct: bool) -> None:
    print("Correct." if correct else f"Not quite. Good answer: {question.answer}")
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple Social Engineering revision program.")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("topics", help="Show organised topics.")
    flashcards = subparsers.add_parser("flashcards", help="Review flashcards.")
    flashcards.add_argument("--topic", choices=[topic.name for topic in TOPICS])
    flashcards.add_argument("--ordered", action="store_true")
    quiz = subparsers.add_parser("quiz", help="Multiple-choice quiz.")
    quiz.add_argument("-n", "--count", type=int, default=10)
    quiz.add_argument("--topic", choices=[topic.name for topic in TOPICS])
    short = subparsers.add_parser("short", help="Short-answer practice.")
    short.add_argument("-n", "--count", type=int, default=10)
    short.add_argument("--topic", choices=[topic.name for topic in TOPICS])
    subparsers.add_parser("progress", help="Show progress by topic.")
    return parser


def run_menu() -> None:
    while True:
        print("\nSocial Engineering Revision Program")
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
            run_quiz(10, choose_topic())
        elif choice == "4":
            run_short_answer(10, choose_topic())
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
