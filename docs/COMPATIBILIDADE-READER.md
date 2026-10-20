# Diagnóstico de compatibilidade com a engenharia reversa original

## Fluxo documentado pelo autor
1. Autenticação Firebase Reader válida da própria conta, com verificações exigidas pelo serviço.
2. GET no catálogo de vozes Reader.
3. Criação de leitura a partir de texto no fluxo Reader.
4. Streaming via WebSocket da leitura, com acompanhamento da posição e reconexões.
5. Reprodução local ou exportação MP3.

## Comprovações atuais
- Arquivos originais estão preservados em main e no desenvolvimento.
- Pipeline de Python e testes simulados passaram.
- Usuário reproduziu texto no aplicativo oficial Reader, não no cliente não oficial.
- Nenhum áudio real foi gerado pelo cliente copiado.
- Nenhuma autenticação Reader independente foi estabelecida.

## Bloqueio
O README exige sessão Firebase Reader e App Check. O login do aplicativo oficial não fornece automaticamente uma credencial para um programa separado. Não embutir chaves, enviar tokens para GitHub, compartilhar sessões nem burlar verificações de segurança.

## Decisão de engenharia
Não adicionar outra interface ou provedor neste ponto. Somente depois de existir autenticação autorizada, executar uma consulta real ao catálogo de vozes, seguida de criação de um documento curto e geração MP3, confirmando permissões, limites e eventuais custos.

## Pesquisa de contingência
Se o Reader não oferecer integração viável, avaliar, separadamente e antes de incorporar, motores de código aberto como Piper, Chatterbox ou VoiceStudio, com verificação de licenças, português brasileiro e hardware. Estes modelos não dão acesso às vozes proprietárias do ElevenLabs.

**Status:** bloqueado por autenticação externa, não por falha identificada no pipeline automatizado.
