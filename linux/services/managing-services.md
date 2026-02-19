# Managing Linux Services

## Objective

Understand how to identify, stop, and verify system services on Ubuntu using systemctl.

## Environment

- Ubuntu Desktop (VirtualBox lab)
- Local administrative access

## Identifying Running Services

To check the status of a specific service:

```bash
systemctl status cups

# Stopping a service
sudo systemctl stop cups

# Verifying service closure
nmap 127.0.0.1
nmap -p 631 127.0.0.1
