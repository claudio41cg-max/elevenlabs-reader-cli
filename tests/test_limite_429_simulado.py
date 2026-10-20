"""Confirma que o Reader respeita HTTP 429 sem repetição automática."""
import asyncio
import unittest
from unittest.mock import patch
from elevenlabs_tts_client import ElevenLabsTTSClient

class Response:
    status = 429
    headers = {"Retry-After": "45"}
    async def __aenter__(self): return self
    async def __aexit__(self, *args): return False

class Session:
    calls = 0
    def __init__(self, **kwargs): pass
    async def __aenter__(self): return self
    async def __aexit__(self, *args): return False
    def get(self, url, headers):
        self.__class__.calls += 1
        return Response()

class Tests(unittest.TestCase):
    def test_limite_sem_repetir_consultas(self):
        Session.calls = 0
        with patch("elevenlabs_tts_client.aiohttp.ClientSession", Session):
            with self.assertRaisesRegex(RuntimeError, "HTTP 429.*45"):
                asyncio.run(ElevenLabsTTSClient("token-simulado").get_voices())
        self.assertEqual(Session.calls, 1)

if __name__ == "__main__":
    unittest.main()
