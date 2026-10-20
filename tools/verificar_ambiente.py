#!/usr/bin/env python3
"""Offline readiness check for the Reader CLI. Does not contact ElevenLabs."""
from __future__ import annotations
import importlib.util
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ("aiohttp", "websockets", "elevenlabs", "dateutil")

def main() -> int:
    print("ElevenLabs Reader CLI — verificação local (sem gerar áudio)")
    print("Python:", sys.version.split()[0])
    missing = [pkg for pkg in REQUIRED if importlib.util.find_spec(pkg) is None]
    print("Dependências:", "OK" if not missing else "Faltando: " + ", ".join(missing))
    required_files = ("elevenlabs_tts_client.py", "token_manager.py", "tts")
    absent = [p for p in required_files if not (ROOT / p).is_file()]
    print("Arquivos originais:", "OK" if not absent else "Faltando: " + ", ".join(absent))
    print("Autenticação Reader: precisa ser realizada localmente e com autorização.")
    print("Tokens e credenciais não devem ser enviados ao chat ou salvos no GitHub.")
    print("Este teste não comprova acesso aos servidores ou funcionamento das vozes.")
    return 1 if missing or absent else 0

if __name__ == "__main__":
    raise SystemExit(main())
