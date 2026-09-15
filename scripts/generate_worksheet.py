#!/usr/bin/env python3
"""Create a deterministic, planned defensive-research worksheet."""
from __future__ import annotations
import argparse
import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "topics" / "topics.json"

def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")

def topic_for(day: dt.date, topics: list[dict]) -> dict:
    if not topics:
        raise ValueError("topic library is empty")
    return topics[day.toordinal() % len(topics)]

def render(day: dt.date, topic: dict) -> str:
    bullets = lambda values: "\n".join(f"- [ ] {v}" for v in values)
    controls = "\n".join(f"- {v}" for v in topic["controls"])
    return f"""# {topic["title"]}

- Date: {day.isoformat()}
- Status: **Planned**
- Author: Rohit Dixit — Cybersecurity Researcher
- Mode: Controlled defensive lab only

> This worksheet is an automatically prepared plan. It is not evidence that testing or manual analysis occurred.

## Research question

{topic["question"]}

## Threat model

{topic["threat_model"]}

## Controlled-lab setup

{bullets(topic["lab"])}

## Safe methodology

{bullets(topic["method"])}

## Evidence checklist

{bullets(topic["evidence"])}

## Expected defensive controls

{controls}

## Limitations

- Results apply only to the documented local fixture and exact versions tested.
- A passing lab control does not prove that a production deployment is secure.
- No external target, credential, or personal data may be used.

## Follow-up questions

{bullets(topic["follow_up"])}

## Observations

_Not started. Add commands, versions, timestamps, and evidence paths during manual execution._

## Sources

_Add authoritative sources consulted during manual research._
"""

def generate(day: dt.date, root: Path = ROOT) -> tuple[Path, bool, str]:
    topics = json.loads((root / "topics" / "topics.json").read_text(encoding="utf-8"))
    topic = topic_for(day, topics)
    content = render(day, topic)
    path = root / "research" / str(day.year) / f"{day.isoformat()}-{slugify(topic['title'])}.md"
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == content:
        return path, False, topic["title"]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path, True, topic["title"]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", type=dt.date.fromisoformat, default=dt.datetime.now(dt.timezone.utc).date())
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    path, changed, title = generate(args.date, args.root.resolve())
    print(json.dumps({"path": str(path), "changed": changed, "title": title}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
