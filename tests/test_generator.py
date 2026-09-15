import datetime as dt
import json
from pathlib import Path
from scripts.generate_worksheet import generate, slugify, topic_for

def make_root(tmp_path: Path) -> Path:
    (tmp_path / "topics").mkdir()
    topic = {
        "title": "Path Traversal",
        "question": "Can input escape the root?",
        "threat_model": "A synthetic path contains parent segments.",
        "lab": ["Use a temporary directory"],
        "method": ["Create a local fixture"],
        "evidence": ["Record expected and observed paths"],
        "controls": ["Canonical containment check"],
        "follow_up": ["Which encodings remain?"],
    }
    (tmp_path / "topics" / "topics.json").write_text(json.dumps([topic]), encoding="utf-8")
    return tmp_path

def test_slugify():
    assert slugify("HTTP Request Smuggling: Fundamentals") == "http-request-smuggling-fundamentals"

def test_topic_selection_is_deterministic():
    topics = [{"title": "a"}, {"title": "b"}]
    day = dt.date(2026, 9, 15)
    assert topic_for(day, topics) == topic_for(day, topics)

def test_generation_is_idempotent_and_planned(tmp_path):
    root = make_root(tmp_path)
    day = dt.date(2026, 9, 15)
    path, changed, title = generate(day, root)
    assert changed and title == "Path Traversal"
    text = path.read_text(encoding="utf-8")
    assert "Status: **Planned**" in text
    assert "not evidence that testing or manual analysis occurred" in text
    assert "rohitdixit.dev" not in text
    _, changed_again, _ = generate(day, root)
    assert changed_again is False

def test_empty_library_rejected():
    try:
        topic_for(dt.date.today(), [])
    except ValueError as exc:
        assert "empty" in str(exc)
    else:
        raise AssertionError("empty library accepted")
