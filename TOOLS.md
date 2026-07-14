# Tool Reference & Command Index

## Tools Used

| Tool | Version | Purpose | Notes |
|---|---|---|---|
| Arsenal Image Mounter | 3.11.307 | Mount E01 disk image read-only | GUI + CLI (`aim_cli.exe`) |
| LECmd | 1.5.1.0 | Parse Windows LNK shortcut files | CSV export |
| PECmd | 1.5.1.0 | Parse Windows Prefetch (.pf) | CSV + Timeline CSV |
| AppCompatCacheParser | 1.5.1.0 | Parse ShimCache from SYSTEM hive | Offline hive parsing |
| MFTECmd | 1.3.0.0 | Parse $MFT | Requires extracted $MFT / admin |
| KAPE | Latest | Triage artefact collection | Requires admin for raw collection |
| DumpIt | — | Live RAM acquisition | Raw memory image |
| FTK Imager | — | Full disk imaging (E01) | Chain-of-custody metadata |
| Volatility 3 | 3.x | Memory forensics | Process/network/injection/persistence |
| Hayabusa | — | Sigma event-log timeline | Core+ rule set |
| Wazuh | — | SIEM / EDR monitoring | All-in-one + Windows agent |
| Python 3.12 | 3.12 | xlrd (XLS), sqlite3 (Firefox), re (carving) | Inline scripts |
| Detect It Easy / capa / YARA / ssdeep | — | Static malware analysis | Typing, capabilities, signatures |

## Representative Command Reference

### Integrity & Acquisition
```text
certutil -hashfile MEM SHA256
```

### Memory Forensics (Volatility 3)
```text
vol.py -f MEM windows.info
vol.py -f MEM windows.pslist | psscan | pstree
vol.py -f MEM windows.cmdline
vol.py -f MEM windows.netscan
vol.py -f MEM windows.malfind --dump
vol.py -f MEM windows.ldrmodules ; windows.vadinfo
vol.py -f MEM windows.svcscan ; windows.registry.printkey
vol.py -f MEM windows.filescan ; windows.dumpfiles
```

### Static Malware Triage
```text
sha256sum sample.exe ; ssdeep sample.exe
file sample.exe ; die sample.exe
strings -n 8 sample.exe ; strings -el sample.exe
capa sample.exe
yara64 -r rules.yar <path>
```

### Disk Artefact Parsing (EZ Tools)
```text
LECmd.exe -d <lnk_dir> --csv <out>
PECmd.exe -d <prefetch_dir> --csv <out>
AppCompatCacheParser.exe -f SYSTEM --csv <out>
```

### Event-Log Timeline
```text
hayabusa csv-timeline -d <evtx_dir>\evidence\ -o event_timeline.csv
```
