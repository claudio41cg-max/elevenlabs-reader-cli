"""Testes de tratamento de erro do catálogo Reader, sem chamadas de rede."""
import asyncio
import unittest
from unittest.mock import patch

from elevenlabs_tts_client import ElevenLabsTTSClient


class FakeResponse:
    status = 401
    async def __aenter__(self):
        return self
    async def __aexit__(self, *args):
        return False
    async def text(self):
        return "Acesso não autorizado"


class FakeSession:
    def __init__(self, *args, **kwargs):
        pass
    async def __aenter__(self):
        return self
    async def __aexit__(self, *args):
        return False
    def get(self, url, headers):
        assert url == "https://api.elevenlabs.io/v1/reader/voices"
        return FakeResponse()


class AuthenticationErrorTests(unittest.TestCase):
    def test_catalogo_rejeita_autenticacao_invalida_sem_expor_token(self):
        token = "token-falso-nao-publicar"
        client = ElevenLabsTTSClient(token)
        with patch("elevenlabs_tts_client.aiohttp.ClientSession", FakeSession):
            with self.assertRaises(Exception) as error:
                asyncio.run(client.get_voices())
        self.assertIn("401", str(error.exception))
        self.assertNotIn(token, str(error.exception))


if __name__ == "__main__":
    unittest.main()
