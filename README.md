# News Summary – make.fun, news‑summary‑01

This repository contains the entry for the **make.fun**
competition *news‑summary‑01*, which requires a single file
containing a summary of the world's news for Wednesday, 11
November 2026.

The bundled summary is stored in `summary.txt`. The program
`main.py` copies this file to the location requested by
make.fun – the directory specified by the environment
variable `MAKEFUN_OUTPUT_DIR` (defaults to `/output`) – as
`entry.txt`.  It performs a byte‑for‑byte copy, so the output is
indistinguishable from the source.

Run the program with:

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Afterwards your entry will be in `out/entry.txt`.

---
**Commit**: `News summary entry: 11 November 2026 summary and copier program`

