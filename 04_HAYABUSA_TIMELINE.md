# Case 4 — Event-Log Timeline Analysis with Hayabusa

**Tool:** Hayabusa (Yamato Security) — Sigma-based Windows event-log analysis.
**Input:** Windows event logs collected from the mounted E01 image.
**Output:** CSV detection timeline for review in a spreadsheet.

## Workflow

1. The E01 disk image was mounted **read-only** with Arsenal Image Mounter to preserve integrity (volumes `E:\`, `G:\`, `H:\`).
2. Hayabusa's `csv-timeline` command was pointed at the collected Windows event-log directory.
3. The first run failed (`No .evtx files were found`); the path was corrected to include the `\evidence\` subfolder.
4. The **Core+** detection rule set (Option 2) was selected in the scan wizard.
5. Results were exported to a CSV timeline for triage.

```text
hayabusa csv-timeline -d <evtx_dir>\evidence\ -o event_timeline.csv
```

## Why Core+ Is the DFIR Sweet Spot

- **Not Option 1 (Core):** fast, but only high/critical alerts — misses medium-severity techniques attackers routinely use (recon commands, scheduled tasks, minor registry persistence tweaks).
- **Option 2 (Core+):** adds crucial medium-severity rules while staying with stable, tested rules — the best signal-to-noise ratio for spotting lateral movement and persistence without drowning in false positives.
- **Skip 3–5:** Option 3 adds experimental rules (noisy); Options 4–5 add low/informational events that bloat a CSV timeline with background noise.

## Value

Hayabusa converted raw event logs into a rule-tagged chronological timeline, letting me correlate persistence, execution, and defence-evasion events discovered in the disk and memory analysis into a single, defensible sequence for the final report.
