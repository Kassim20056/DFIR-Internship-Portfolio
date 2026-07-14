# Case 2 — Maryam Acquisition & Chain-of-Custody

**Scenario:** Structured evidence acquisition on a compromised training host.
**Subject host:** `DESKTOP-2Q2EPKM` — user `maryam.var`.
**Environment:** Isolated training lab (virtual machine).

> Training scenario. All names and data are fictional practice datasets.

## Executive Summary

The evidence package contains a Windows host KAPE-style artifact collection, memory dumps, and a segmented E01 disk image. Automated triage and manual review of timelines, event logs, filesystem metadata, and suspicious-artifact hits indicate a Windows host named **DESKTOP-2Q2EPKM** with user **maryam.var**. The strongest findings are Microsoft Defender detections for **Award Keylogger / ProKAward**, trojan downloads **loder.exe** and **updsto.exe**, **AutoKMS** hacktool persistence, **Defender tampering** indicators, and **DLLInjector / CryptInject** activity.

## Acquisition Methodology — Order of Volatility

| # | Evidence Item | Description | Tool |
|---|---|---|---|
| E-01 | `DESKTOP-2Q2EPKM-20260607-163245.raw` | Physical memory (RAM) image, acquired 2026-06-07 16:32:45 (+03:00) | **DumpIt** |
| E-02 | `Host_C_Drive_Image_mayram.E01` | Full forensic disk image (EnCase E01) of system drive | **FTK Imager** |
| E-03 | KapeTriage artefact set (1,003 files) | Registry hives, event logs, prefetch, LNK, browser data | **KAPE** |

The acquisition followed a defensible sequence: (1) workspace preparation and documentation, (2) live RAM acquisition, (3) KAPE triage collection, (4) full E01 disk image, and (5) hash-integrity verification with chain completion. A reliable time baseline was established and synchronised with an internet time source before acquisition to ensure accurate timestamps.

## Integrity Verification

| Evidence | Algorithm | Value | Status |
|---|---|---|---|
| E-01 (memory) | SHA-256 | `7c93c1a808c4cc8021ae95e1526495ff4d38da0d82d5d2adbd808e646d60996c` | Recorded |
| E-02 (disk) | MD5 | `74313aabb222d81b9eec44a6e0199b6f` | MATCH |
| E-02 (disk) | SHA-1 | `e871c8e1abe694c00f0565c3eeffd4de30b3b122` | MATCH |

Originals were kept read-only; analysis was performed on a working copy, with every access recorded in `chain_of_custody.csv` and `case_notes.md`.

## Key Findings

| ID | Finding | Severity | Interpretation |
|---|---|---|---|
| F-001 | Commercial keylogger / monitoring tool (`ProKAward`, service `SKLProService`, `wap.exe`, `rsasws.exe`) | High | Defender: `MonitoringTool:Win32/AwardKeylogger`, later `Occamy`. Service suggests persistent execution. |
| F-002 | Downloaded trojans `loder.exe`, `updsto.exe` from `weeknews.pro` | High | `maryam.var` downloaded trojan-classified executables to Downloads. |
| F-003 | AutoKMS hacktool with scheduled task/service persistence (`KMSAutoNet`, `KMSEmulator`) | Medium/High | High-risk activation hacktool with persistence artefacts. |
| F-004 | Defender tampering indicator (`DisableOnAccessProtection`) | High | Registry value affecting real-time protection — attempted AV weakening. |
| F-005 | DLL injector `DLLInjector v2.exe` (`Trojan:Win32/CryptInject`) in Downloads | High | Capable of process injection, evasion, or malware execution. |

Deeper static/dynamic analysis and MITRE ATT&CK mapping are in [`03_MALWARE_TRIAGE.md`](03_MALWARE_TRIAGE.md). Indicators are consolidated in [`IOCs.csv`](IOCs.csv).

## Adapted 17-Phase Methodology

This case was analysed using the adapted 17-phase DFIR workflow (case prep → evidence organisation → image validation → filesystem, registry, event-log, user-activity, executed-program, USB, network, browser, persistence, and malware-triage analysis → timeline → IOC extraction → findings → final report). See [`METHODOLOGY_17_PHASES.md`](METHODOLOGY_17_PHASES.md).
