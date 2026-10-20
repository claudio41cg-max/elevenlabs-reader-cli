#!/usr/bin/env python3
"""Diagnóstico local do Reader. Nunca envia tokens ou faz chamadas de rede."""
import importlib.util
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def main():
    print("Diagnóstico de autenticação do ElevenLabs Reader")
    required = ("aiohttp", "websockets", "elevenlabs", "dateutil")
    missing = [name for name in required if importlib.util.find_spec(name) is None]
    print("Dependências:", "OK" if not missing else "Faltam: " + ", ".join(missing))
    files = ("elevenlabs_tts_client.py", "token_manager.py", "tts")
    absent = [name for name in files if not (ROOT / name).is_file()]
    print("Arquivos:", "OK" if not absent else "Faltam: " + ", ".join(absent))
    print("Credencial oficial opcional configurada:", "sim" if os.getenv("ELEVENLABS_API_KEY") else "não")
    print("Este diagnóstico não acessa nem valida sessões privadas do Reader.")
    print("O Reader exige autenticação e verificação App Check aceitas pelo serviço.")
    print("Não envie senhas, tokens, cookies ou capturas de sessão ao GitHub ou ao chat.")
    if missing or absent:
        return 1
    print("Código preparado para análise local. Vozes reais ainda não verificadas.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
