# Case 1 — Jimmy Wilson Disk Forensics

**Scenario:** Simulated incident response — suspected identity theft and document fraud.
**Evidence:** E01 forensic disk image attributed to suspect *Jimmy Wilson*.
**Environment:** Isolated training lab; image mounted read-only.

> Training scenario. All names and data are fictional practice datasets.

## Executive Summary

This forensic examination was conducted on a disk image (E01 format) attributed to suspect Jimmy Wilson. The image was mounted read-only using **Arsenal Image Mounter** and analysed using industry-standard tools. The evidence establishes an active identity-theft and potential document-fraud operation.

Key findings:

- **Victim PII spreadsheet** — 4 victims with full name, date of birth, and Social Security Number.
- **Encrypted communications** — BCTextEncoder used to create encrypted messages referencing co-conspirators *Jose Badguy* and *Robert Ripoff*.
- **Criminal intent in browser history** — searches for *"how to steal identities"* and *"identity theft jail time"* on 2014-02-11.
- **Counterfeiting equipment research** — Zebra ZXP Series 8 ID-card printers (equipment for producing counterfeit identity documents).
- **Encryption in use** — TrueCrypt actively used; additional encrypted volumes on a separate `M:\` drive (BillyBob).
- **Removable media** — BCTextEncoder executed from USB drive `G:\` (not present in this image).
- **Anti-forensics** — deliberate deletion of a *'New Prices'* folder containing an encoded file.
- **Recovery potential** — Volume Shadow Copy confirmed, potentially allowing recovery of deleted artefacts.

The combined weight of these artefacts establishes criminal intent, active offending, and deliberate evidence concealment.

## Examination Methodology (9 Phases)

| Phase | Focus | Tool |
|---|---|---|
| 1 | Evidence mounting & drive verification | Arsenal Image Mounter |
| 2 | Suspect profile enumeration | Filesystem review |
| 3 | LNK (shortcut) file analysis | LECmd |
| 4 | Prefetch analysis (program execution) | PECmd |
| 5 | ShimCache / AppCompatCache analysis | AppCompatCacheParser |
| 6 | Browser history analysis (Firefox SQLite) | Python `sqlite3` |
| 7 | MFT extraction attempts | MFTECmd |
| 8 | Document metadata extraction | Python (xlrd, re) |
| 9 | Additional artefact collection | Manual review |

Each phase produced CSV output that was reviewed for indicators of criminal activity, program execution, and anti-forensic behaviour. LNK and Prefetch artefacts confirmed execution of encryption utilities from removable media; ShimCache corroborated the execution timeline; and Firefox history reconstructed the suspect's research and intent sequence.

## Key Evidence Findings

- **`name that need addresses.xls`** — legacy Excel spreadsheet parsed with Python `xlrd`, containing four victims' PII (name, DOB, SSN, address).
- **BCTextEncoder artefacts** — encoded `.txt` files recovered, keyed from filenames, evidencing encrypted co-conspirator communications.
- **Deleted 'New Prices' folder** — recovered MFT entry showing intentional deletion of an encoded file.
- **TrueCrypt** — presence and active use confirmed via LNK/Prefetch and mounted-volume evidence.
- **Browser criminal-intent sequence** — timestamped searches demonstrating premeditation.

## Investigative Recommendations (selected)

- Recover deleted artefacts from Volume Shadow Copies.
- Seize and image the removable `G:\` USB device and the `M:\` (BillyBob) encrypted volume.
- Pursue TrueCrypt/BCTextEncoder key recovery under legal authority.
- Cross-reference victim PII against known fraud reports.

See the full report and complete command reference in [`TOOLS.md`](TOOLS.md) and [`DFIR_Internship_Report_Kassim_Galeb.docx`](DFIR_Internship_Report_Kassim_Galeb.docx).
