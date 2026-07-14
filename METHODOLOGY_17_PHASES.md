# Adapted DFIR Methodology — 17 Phases

A repeatable, defensible workflow applied across the internship casework, adapted from standard DFIR practice for Windows host investigations.

| # | Phase | Purpose |
|---|---|---|
| 1 | Case preparation & evidence verification | Confirm scope, verify hashes, set up documented workspace |
| 2 | Evidence organization | Structure evidence, working copies, notes, and chain of custody |
| 3 | Disk image / mounted evidence validation | Mount read-only; confirm volumes and integrity |
| 4 | File system analysis | $MFT, timestamps, deleted files, filesystem metadata |
| 5 | Windows Registry analysis | System/user hives, configuration, persistence keys |
| 6 | Event log analysis | Security/System/Application logs; Sigma timelining (Hayabusa) |
| 7 | User activity analysis | LNK, jump lists, recent docs, shellbags |
| 8 | Executed program analysis | Prefetch, ShimCache/AppCompatCache, Amcache |
| 9 | USB & external device analysis | Removable-media enumeration and correlation |
| 10 | Network artifact analysis | Connections, DNS, C2 indicators (memory netscan) |
| 11 | Browser & download history analysis | History, downloads, search intent (Firefox SQLite) |
| 12 | Persistence mechanism analysis | Services, scheduled tasks, run keys |
| 13 | Malware / suspicious file triage | Static & dynamic analysis; sandbox detonation |
| 14 | Timeline creation | Unified chronological reconstruction of events |
| 15 | Indicators of Compromise extraction | Files, URLs, domains, registry, services → IOCs.csv |
| 16 | Findings summary | Severity-rated findings with interpretation |
| 17 | Final professional forensic report | Defensible, court-ready documentation |

Each phase feeds the next: acquisition and validation establish trust in the evidence; artefact analysis (phases 4–13) produces findings; and phases 14–17 synthesise those findings into IOCs, a timeline, and a professional report.
