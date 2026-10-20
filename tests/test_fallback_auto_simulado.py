"""Garante que o modo auto tenta o próximo método se o primeiro vier vazio."""
import asyncio
import unittest
from unittest.mock import AsyncMock
from elevenlabs_tts_client import ElevenLabsTTSClient

class AutomaticFallbackTest(unittest.TestCase):
    def test_vazio_avanca_para_o_proximo_metodo(self):
        client = ElevenLabsTTSClient("token-simulado")
        client._stream_reader_websocket_flows = AsyncMock(return_value=None)
        client._stream_http_direct = AsyncMock(return_value=b"audio-simulado")
        client._stream_direct_websocket = AsyncMock(return_value=b"terceira-opcao")
        result = asyncio.run(client.stream_with_websocket(
            text="Teste", voice_id="voz-simulada", method="auto"
        ))
        self.assertEqual(result, b"audio-simulado")
        client._stream_reader_websocket_flows.assert_awaited_once()
        client._stream_http_direct.assert_awaited_once()
        client._stream_direct_websocket.assert_not_awaited()

if __name__ == "__main__":
    unittest.main()
