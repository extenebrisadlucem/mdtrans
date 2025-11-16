import requests
from typing import Optional

class LibreTranslator:
    def __init__(self, api_url: str):
        self.api_url = api_url.rstrip("/")

    def translate_text(
        self,
        text: str,
        source: str = "auto",
        target: str = "fr",
        format: str = "text",
        api_key: Optional[str] = None,
    ) -> str:
        """
        Translate arbitrary text using the LibreTranslate API.
        Raises RuntimeError for API-level failures.
        """
        payload = {
            "q": text,
            "source": source,
            "target": target,
            "format": format,
        }
        if api_key:
            payload["api_key"] = api_key

        try:
            resp = requests.post(self.api_url, json=payload, timeout=60)
        except requests.RequestException as e:
            raise RuntimeError(f"HTTP error contacting LibreTranslate: {e}")

        if resp.status_code != 200:
            raise RuntimeError(f"LibreTranslate returned {resp.status_code}: {resp.text}")

        data = resp.json()
        if "translatedText" not in data:
            raise RuntimeError(f"Unexpected API response: {data}")

        return data["translatedText"]
