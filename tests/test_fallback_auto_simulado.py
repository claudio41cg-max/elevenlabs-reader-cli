"""O modo auto deve permanecer no Reader e nunca chamar a API oficial."""
import asyncio
import unittest
from unittest.mock import AsyncMock

from elevenlabs_tts_client import ElevenLabsTTSClient


class AutomaticReaderOnlyTest(unittest.TestCase):
    def test_vazio_nao_chama_metodos_oficiais(self):
        client = ElevenLabsTTSClient("token-simulado")
        client._stream_reader_websocket_flows = AsyncMock(return_value=None)
        client._stream_http_direct = AsyncMock(return_value=b"audio-oficial")
        client._stream_direct_websocket = AsyncMock(return_value=b"audio-oficial-ws")
        result = asyncio.run(client.stream_with_websocket(
            text="Teste", voice_id="voz-simulada", method="auto"
        ))
        self.assertIsNone(result)
        client._stream_reader_websocket_flows.assert_awaited_once()
        client._stream_http_direct.assert_not_awaited()
        client._stream_direct_websocket.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
