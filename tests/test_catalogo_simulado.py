"""Teste isolado: confirma a leitura do catálogo sem acessar a rede ou usar tokens."""
import asyncio
import unittest
from unittest.mock import patch

from elevenlabs_tts_client import ElevenLabsTTSClient


class FakeResponse:
    status = 200
    async def __aenter__(self):
        return self
    async def __aexit__(self, *args):
        return False
    async def json(self):
        return {"voices": [{"voice_id": "demo", "name": "Voz de teste"}]}


class FakeSession:
    def __init__(self, *args, **kwargs):
        pass
    async def __aenter__(self):
        return self
    async def __aexit__(self, *args):
        return False
    def get(self, url, headers):
        assert url.endswith("/v1/reader/voices")
        assert headers["Authorization"] == "Bearer token-de-teste"
        return FakeResponse()


class VoiceCatalogTest(unittest.TestCase):
    def test_listagem_simulada(self):
        client = ElevenLabsTTSClient("token-de-teste")
        with patch("elevenlabs_tts_client.aiohttp.ClientSession", FakeSession):
            result = asyncio.run(client.get_voices())
        self.assertEqual(result["voices"][0]["name"], "Voz de teste")


if __name__ == "__main__":
    unittest.main()
