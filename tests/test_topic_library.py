import json
from pathlib import Path

def test_topic_library_has_required_fields_and_breadth():
    topics = json.loads(Path("topics/topics.json").read_text(encoding="utf-8"))
    required = {"title","question","threat_model","lab","method","evidence","controls","follow_up"}
    assert len(topics) >= 15
    assert all(required <= topic.keys() for topic in topics)
    assert len({topic["title"] for topic in topics}) == len(topics)
    assert all(all(topic[key] for key in required - {"title","question","threat_model"}) for topic in topics)
