"""Integration test: needs a live LM Studio (or compatible) server at LocalLLMService's base_url.

Run with `pytest -m integration` while the local server is running; skipped otherwise.
"""

import socket
from urllib.parse import urlparse

import pytest

from ai_exercises.services import LocalLLMService


def _local_server_is_up(base_url):
    parsed = urlparse(base_url)
    try:
        with socket.create_connection((parsed.hostname, parsed.port), timeout=0.5):
            return True
    except OSError:
        return False


pytestmark = pytest.mark.integration


@pytest.fixture
def llm():
    service = LocalLLMService()
    if not _local_server_is_up(str(service.client.base_url)):
        pytest.skip("Local LLM server is not running")
    return service


def test_generate_json_returns_categorized_fruits(llm):
    prompt = "Categorize these fruits by color."
    data = ["apple", "banana", "cherry"]

    result = llm.generate_json(prompt, data)

    assert result
