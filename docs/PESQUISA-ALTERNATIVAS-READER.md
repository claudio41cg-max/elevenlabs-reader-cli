# Pesquisa comparativa: clientes não oficiais do ElevenReader

Data da pesquisa: 2026-10-20.

## Base do projeto
- https://github.com/gastonmorixe/elevenlabs-reader-cli
- Código do cliente Reader com Firebase, App Check, catálogo de vozes, criação de leitura e streaming.
- Dependência não resolvida neste fork: acesso autenticado à API privada Reader. Os testes GitHub anteriores são offline/simulados.

## Novo candidato para estudo, sem substituir a base
- https://pypi.org/project/elvenreader/
- Biblioteca `elvenreader`, versão 0.3.0, distribuída com licença MIT.
- Declara funcionalidades de voz, áudio MP3, tempos de palavras, cenas com múltiplas vozes e limpeza de leituras.
- Documenta autenticação com Firebase e App Check obtido durante sessão automatizada do Chrome. Isso não equivale a login oficial destinado a terceiros; não presumir permissão para reutilização de tokens de atestado.
- Requer macOS, Keychain e Chrome para o fluxo documentado; não foi comprovada compatibilidade com Android.
- Página GitHub mencionada pela distribuição não foi encontrada durante esta pesquisa; usar o pacote PyPI somente como referência até verificar a origem do código.
- Nenhum teste de geração real foi executado por nós.

## Outro candidato de comparação
- https://github.com/Microck/elevenlabs-webui-client
- Cliente do serviço ElevenLabs Web UI (não especificamente Reader), com Firebase e geração MP3 descritos pelo autor.
- Não presumir acesso ilimitado ou ausência de cobrança, nem incorporar extração de perfis/sessões para contornar verificações.

## Próximo passo com evidência
Confirmar fonte pública, licenças e compatibilidade de cada implementação; testar somente caminhos autenticados autorizados com conta própria em ambiente privado. Não pedir tokens em chat, não salvar segredos no GitHub. Não trocar o cliente principal antes de uma demonstração real de áudio e verificação dos limites.
