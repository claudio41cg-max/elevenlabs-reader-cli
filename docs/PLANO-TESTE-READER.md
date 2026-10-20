# Verificação inicial do ElevenLabs Reader CLI

Este repositório é uma cópia do projeto comunitário original. O código principal foi mantido sem alterações na branch `main`.

## Objetivo do teste

Verificar a listagem de vozes e a geração de áudio **com uma conta própria e acesso autorizado**, usando o cliente existente, antes de construir uma interface de celular.

## Pré-requisitos

- Python e dependências declaradas em `requirements.txt`.
- Conta própria do ElevenLabs Reader.
- Autenticação suportada e permitida pelo serviço. O código original descreve tokens internos do aplicativo que podem expirar. Não publique, cole no chat ou envie para o GitHub nenhum token, sessão, arquivo de captura de tráfego ou credencial.
- Confirmação de que o uso do serviço respeita as permissões da conta. Não tente contornar App Check, bloqueios de acesso ou limites de uso.

## Comandos de diagnóstico, após configurar autenticação válida localmente

```bash
python elevenlabs_tts_client.py --help
./tts --list-voices
```

Somente depois de a listagem funcionar e de confirmarmos as permissões, testar uma frase curta para ouvir e exportar MP3 conforme as instruções originais do README.

## Situação

- Repositório e arquivos analisados: **sim**.
- Dependências executadas e autenticação testada: **não**.
- Vozes reais geradas: **não**.
- Aplicativo Android publicado: **não**.

Não há motor independente incluído aqui: o cliente depende dos servidores do ElevenLabs. A presença do código não garante disponibilidade contínua. O repositório original não apresenta licença explícita; confirmar a autorização para adaptar e redistribuir o código antes de transformá-lo em um aplicativo.
