# Chain of Custody & Evidence Inventory

> Training-lab evidence. Originals kept read-only; analysis performed on working copies. Every access recorded in `chain_of_custody.csv` and `case_notes.md`.

## Maryam Case — Acquired Evidence

| # | Evidence Item | Description | Acquisition Tool |
|---|---|---|---|
| E-01 | `DESKTOP-2Q2EPKM-20260607-163245.raw` | Physical memory (RAM) image, acquired 2026-06-07 16:32:45 (+03:00) | DumpIt |
| E-02 | `Host_C_Drive_Image_mayram.E01` | Full forensic disk image (EnCase E01) of system drive | FTK Imager |
| E-03 | KapeTriage artefact set (1,003 files) | Registry hives, event logs, prefetch, LNK, browser data | KAPE |

## Integrity Verification

| Evidence | Algorithm | Value | Status |
|---|---|---|---|
| E-01 (memory) | SHA-256 | `7c93c1a808c4cc8021ae95e1526495ff4d38da0d82d5d2adbd808e646d60996c` | Recorded |
| E-02 (disk) | MD5 | `74313aabb222d81b9eec44a6e0199b6f` | MATCH |
| E-02 (disk) | SHA-1 | `e871c8e1abe694c00f0565c3eeffd4de30b3b122` | MATCH |

## Source Package Hashes

| Evidence | SHA-256 | MD5 | Size (bytes) |
|---|---|---|---|
| `tools.zip` | `434b8cc3354b4ffd6ba8c713e52e531af516de8d1282fda120e276570fcf6fe9` | `d8dc74f19685554342e9d135bd3db2e8` | 3,420,326,145 |
| `analyse case.zip` | `e764dd821dc6e83091c64edbb619d48e47192c591cd4d74df834776194ac8bb3` | `f58b7447611015d019b5ba555f6f3fce` | 7,022,737,174 |

## Handling Rule

Original ZIPs remained in place and read-only. Analysis was performed inside a dedicated working-copy directory. No original evidence was modified at any point.
