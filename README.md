# Security Research Daily

Reproducible defensive security notes, controlled-lab worksheets, and research observations maintained by **Rohit Dixit — Cybersecurity Researcher**.

[rohitdixit.dev](https://rohitdixit.dev) 

## Scope

This repository supports disciplined, legal security research in systems owned by the researcher or explicitly authorized lab environments. It does not scan external targets or provide operational offensive tooling.

The scheduled workflow selects one topic from a curated local library and creates a dated **Planned** worksheet. A worksheet is a research plan—not evidence that hands-on testing occurred. Researchers must manually add observations, evidence, sources, and status changes.

## Quick start

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
python scripts/generate_worksheet.py --date 2026-09-15
```

Generation is deterministic for a given date. If that day's worksheet already exists with identical content, the script makes no change.

## Structure

- `topics/topics.json` — curated defensive research questions and lab guidance
- `scripts/generate_worksheet.py` — deterministic worksheet generator
- `research/` — dated worksheets
- `tests/` — generator and content-policy tests
- `.github/workflows/` — CI and scheduled maintenance
- `AUTOMATION.md` — exact automation behavior and limitations
- `SECURITY.md` — private reporting guidance

## Research record standard

Completed work should identify the controlled environment, commands or fixtures used, relevant versions, raw evidence location, expected versus observed behavior, and authoritative references. Unsupported conclusions should not be recorded as findings.

## License

Code is available under the MIT License. Written research material is provided under the same terms unless a file states otherwise.
