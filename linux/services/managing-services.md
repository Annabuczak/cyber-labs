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
```

## Stopping a Service

```bash
sudo systemctl stop cups
```

## Verifying Service Closure

```bash
nmap 127.0.0.1
nmap -p 631 127.0.0.1
```

## What I Learned

- `systemctl status` shows whether a service is active, inactive, or failed.
- Stopping an unnecessary service can reduce exposed local services.
- Nmap can help verify whether a service port is still reachable after stopping the service.
