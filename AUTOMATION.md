# Automation disclosure

## Scheduled worksheet generation

`.github/workflows/daily-research.yml` runs Monday and Thursday at 02:17 UTC and supports manual dispatch. It is part of a portfolio-wide rotation: secure-code validation runs Tuesday/Friday, dependency monitoring Wednesday/Saturday, and detection validation Sunday.

This workflow:

1. checks out this repository;
2. installs the pinned test dependency;
3. runs all local tests;
4. chooses a curated topic deterministically from the UTC date;
5. creates `research/YYYY/YYYY-MM-DD-slug.md` with status `Planned`;
6. commits only if that tracked file is new or materially different.

The workflow does not scan networks, contact targets, use repository secrets, or claim that the worksheet was executed. It uses the built-in `GITHUB_TOKEN` with `contents: write` only. All other permissions are disabled by default.

Commits use the transparent `github-actions[bot]` identity with a subject derived from the selected topic. A no-change run exits without a commit. Generated plans require manual evidence and review before their status can change.
