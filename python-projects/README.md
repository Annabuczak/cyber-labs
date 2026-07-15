# Security-Focused Python Projects

Small Python scripts and study exercises used to practise cybersecurity concepts, automation, and defensive thinking.

This folder is intentionally limited to security-related Python work. General coursework exercises live in the separate `bsc-cybersecurity` repository.

## Structure

```text
python-projects/
├── tools/
│   ├── log_analyzer.py
│   ├── password_audit.py
│   ├── password_generator.py
│   └── port_scanner.py
├── simulators/
│   ├── login_firewall.py
│   └── soc_analyst_simulator.py
├── study-notes/
│   ├── malware_study.py
│   ├── physical_security_study.py
│   ├── security_fundamentals_study.py
│   ├── social_engineering_study.py
│   └── threat_actors_study.py
└── sample-logs/
    └── server.log
```

## Tools

- `tools/password_audit.py` - Checks password strength against length, uppercase, lowercase, number, and symbol criteria.
- `tools/password_generator.py` - Generates random passwords with configurable complexity.
- `tools/port_scanner.py` - Basic TCP port scanner for networking practice.
- `tools/log_analyzer.py` - Parses a sample server log and counts failed logins, errors, warnings, and info messages.

## Simulators

- `simulators/login_firewall.py` - Demonstrates failed login tracking and account lockout logic.
- `simulators/soc_analyst_simulator.py` - Small command-line simulation of SOC alert review and response.

## Study Notes

- `study-notes/malware_study.py`
- `study-notes/physical_security_study.py`
- `study-notes/security_fundamentals_study.py`
- `study-notes/social_engineering_study.py`
- `study-notes/threat_actors_study.py`

These files are learning exercises and revision prompts, not production tools.

## Next Improvements

- Add docstrings to each script.
- Replace hard-coded examples with safer command-line arguments.
- Add small test cases for the tools.
- Keep filenames lowercase and descriptive.
