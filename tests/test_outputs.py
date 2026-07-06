import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_is_valid_json():
    """Criterion 1: /app/report.json exists and is valid JSON."""
    assert REPORT.exists(), "/app/report.json not found"
    data = json.loads(REPORT.read_text())
    assert isinstance(data, dict), "report.json root must be a JSON object"


def test_total_requests():
    """Criterion 2: total_requests equals the exact number of requests in the log."""
    data = json.loads(REPORT.read_text())
    assert data.get("total_requests") == 6, (
        f"expected total_requests=6, got {data.get('total_requests')}"
    )


def test_unique_ips():
    """Criterion 3: unique_ips equals the exact number of distinct source IPs."""
    data = json.loads(REPORT.read_text())
    assert data.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {data.get('unique_ips')}"
    )


def test_top_path():
    """Criterion 4: top_path equals the request path with the highest frequency."""
    data = json.loads(REPORT.read_text())
    assert data.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {data.get('top_path')}"
    )
