#!/usr/bin/env python3
"""Optional authorized ElevenLabs TTS test. Never sends requests without --confirm."""
import argparse
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request
import json

def main():
    parser = argparse.ArgumentParser(description="Teste de voz por API oficial (opcional)")
    parser.add_argument("--voice-id", required=True)
    parser.add_argument("--text", default="Olá, Cláudio. Este é um teste de voz.")
    parser.add_argument("--output", default="teste-elevenlabs.mp3")
    parser.add_argument("--confirm", action="store_true", help="Autoriza consumir créditos da própria conta")
    args = parser.parse_args()
    if not args.text.strip() or len(args.text) > 200:
        parser.error("Texto deve ter entre 1 e 200 caracteres.")
    if not args.confirm:
        print("Simulação: nenhuma chamada realizada. O teste real pode consumir créditos.")
        print("Para gerar áudio, configure ELEVENLABS_API_KEY localmente e passe --confirm.")
        return 0
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not key:
        print("Falta ELEVENLABS_API_KEY. Não envie a chave ao chat ou ao GitHub.", file=sys.stderr)
        return 2
    if "/" in args.voice_id or "?" in args.voice_id:
        parser.error("ID de voz inválido.")
    output = Path(args.output)
    payload = json.dumps({"text": args.text.strip(), "model_id": "eleven_multilingual_v2"}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.elevenlabs.io/v1/text-to-speech/" + args.voice_id + "?output_format=mp3_44100_128",
        data=payload,
        headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            data = response.read()
        if not data:
            raise ValueError("Resposta de áudio vazia")
        output.write_bytes(data)
        print("Áudio gravado em:", output)
        return 0
    except urllib.error.HTTPError as e:
        print("ElevenLabs recusou a solicitação. Código HTTP:", e.code, file=sys.stderr)
        return 1
    except (OSError, ValueError) as e:
        print("Falha de conexão ou gravação:", type(e).__name__, file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
