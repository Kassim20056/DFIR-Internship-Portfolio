# Case 5 — Wazuh SIEM Deployment & Configuration

**Goal:** Stand up a centralized SIEM and onboard a Windows endpoint end-to-end.
**Platform:** Wazuh all-in-one on a VPS + Windows agent.

## Objectives

- Install a centralized SIEM platform on a VPS.
- Access the Wazuh dashboard through a web browser.
- Deploy a Wazuh agent on a Windows endpoint.
- Connect the Windows endpoint to the Wazuh manager.
- Verify that endpoint logs and alerts appear in the dashboard.
- Use the dashboard to monitor security events, vulnerabilities, and endpoint status.
- Document all steps for internship reporting and future reference.

## Deployment Steps

1. **Server preparation** — provision the VPS and satisfy Wazuh prerequisites.
2. **All-in-one installation** — deploy Wazuh manager, indexer, and dashboard.
3. **Dashboard access** — reach the web UI and complete post-installation verification.
4. **Firewall configuration** — open the required service ports.
5. **Windows agent deployment** — install and register the agent, verify the Windows service.
6. **Connection verification** — confirm the agent appears active in the dashboard.
7. **Dashboard exploration, testing & monitoring** — validate that logs and alerts flow.

## Firewall / Service Ports

| Port | Purpose |
|---|---|
| 443 | Wazuh dashboard (HTTPS web UI) |
| 1514 | Agent event data to manager |
| 1515 | Agent enrollment / registration |
| 9200 | Wazuh indexer (Elasticsearch API) |
| 55000 | Wazuh manager REST API |

## Outcome

A working single-node Wazuh SIEM with a connected Windows agent reporting live security events, plus documented troubleshooting (path/port/enrollment issues) and security-hardening considerations. This exercise complements the forensic casework by demonstrating the **detection and continuous-monitoring** side of the DFIR lifecycle.
