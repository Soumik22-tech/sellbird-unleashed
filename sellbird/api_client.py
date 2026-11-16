"""API LLM Client for Sellbird.
Supports Groq, NVIDIA NIM, Google Gemini, and generic OpenAI-compatible endpoints.
"""

import os
import json
import logging
import asyncio
import httpx

logger = logging.getLogger("sellbird.api_client")

class ApiBrainClient:
    def __init__(self, provider: str, model: str = ""):
        self.provider = provider.lower()
        self.custom_model = model

    def get_config(self) -> tuple[str, str, str]:
        """Returns (base_url, api_key, model_name) for the configured provider."""
        if self.provider == "groq":
            api_key = os.getenv("GROQ_API_KEY", "").strip()
            base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1").strip()
            model = self.custom_model or os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile").strip()
            return base_url, api_key, model

        elif self.provider == "nvidia":
            api_key = os.getenv("NVIDIA_API_KEY", "").strip()
            base_url = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1").strip()
            model = self.custom_model or os.getenv("NVIDIA_MODEL", "meta/llama-3.3-70b-instruct").strip()
            return base_url, api_key, model

        elif self.provider == "gemini":
            api_key = os.getenv("GEMINI_API_KEY", "").strip()
            # Google AI Studio OpenAI-compatible endpoint
            base_url = os.getenv("GEMINI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/").strip()
            model = self.custom_model or os.getenv("GEMINI_MODEL", "gemini-2.0-flash").strip()
            return base_url, api_key, model

        elif self.provider == "custom":
            api_key = os.getenv("CUSTOM_API_KEY", "").strip()
            base_url = os.getenv("CUSTOM_BASE_URL", "https://api.openai.com/v1").strip()
            model = self.custom_model or os.getenv("CUSTOM_MODEL", "gpt-4o-mini").strip()
            return base_url, api_key, model

        raise ValueError(f"Unknown API provider: {self.provider}")

    def preflight_check(self) -> str:
        """Checks if required API key and configuration exist."""
        try:
            base_url, api_key, model = self.get_config()
            if not api_key:
                env_var = {
                    "groq": "GROQ_API_KEY",
                    "nvidia": "NVIDIA_API_KEY",
                    "gemini": "GEMINI_API_KEY",
                    "custom": "CUSTOM_API_KEY",
                }.get(self.provider, "API_KEY")
                return f"Missing {env_var} in .env file for provider '{self.provider}'"
            return ""
        except Exception as e:
            return f"Configuration error: {e}"

    async def generate(self, prompt: str, timeout: float = 60.0, expect_json: bool = False) -> str:
        """Call the OpenAI-compatible chat completion endpoint."""
        base_url, api_key, model = self.get_config()
        if not api_key:
            logger.error(f"No API key configured for {self.provider}")
            return ""

        url = f"{base_url.rstrip('/')}/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        messages = [
            {"role": "user", "content": prompt}
        ]

        payload = {
            "model": model,
            "messages": messages,
            "temperature": 0.2,
        }

        if expect_json:
            payload["response_format"] = {"type": "json_object"}

        async with httpx.AsyncClient(timeout=timeout) as client:
            try:
                resp = await client.post(url, headers=headers, json=payload)
                if resp.status_code != 200:
                    logger.error(f"{self.provider} API error [{resp.status_code}]: {resp.text[:300]}")
                    return ""
                data = resp.json()
                content = data["choices"][0]["message"]["content"]
                return content.strip()
            except httpx.TimeoutException:
                logger.error(f"{self.provider} API call timed out after {timeout}s")
                return ""
            except Exception as e:
                logger.error(f"Failed to generate text from {self.provider}: {e}")
                return ""
