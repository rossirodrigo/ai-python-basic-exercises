import json
from abc import ABC, abstractmethod
from typing import Any


class LLMService(ABC):
    """Common interface for chat-based LLM backends.

    Every service exposes the same OpenAI-style message list for
    `chat_completion` so exercises can swap backends without changing
    call sites.
    """

    @abstractmethod
    def chat_completion(self, messages: list[dict[str, str]], temperature: float = 1.0) -> str:
        """Sends a list of {"role", "content"} messages and returns the reply text."""

    def _parse_json(self, text: str) -> Any:
        return json.loads(text)

    def generate_json(self, prompt: str, data: Any) -> Any:
        full_prompt = f"""
            {prompt}

            STRICT RULES:
            1. Return ONLY the valid JSON. No conversational text or markdown code blocks.
            2. Ensure the output is a valid JSON.

            Payload to process:
            {json.dumps(data)}
        """

        content = self.chat_completion(messages=[{"role": "user", "content": full_prompt}])
        clean_text = content.replace("```json", "").replace("```", "").strip()
        return self._parse_json(clean_text)
