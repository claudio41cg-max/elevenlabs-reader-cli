# Primeira geração real de voz: opção autorizada

O cliente Reader original permanece **intacto**. Sua autenticação privada requer Firebase Reader e App Check do aplicativo, sem login público/documentado para ferramentas independentes. O acesso pela conta no aplicativo oficial não autentica automaticamente o cliente copiado.

A ElevenLabs documenta uma alternativa autorizada: API oficial via chave pessoal. A função abaixo é **opcional**, pertence ao mesmo repositório, não substitui o mecanismo Reader e não é um bypass. A API oficial consome os créditos da conta, inclusive do plano gratuito. O programa começa em modo simulação para evitar consumo acidental.

1. Crie uma chave com permissão apenas de text-to-speech, limites de uso e sem divulgar a chave: https://elevenlabs.io/app/settings/api-keys
2. Salve em variável de ambiente **somente no seu computador/ambiente privado**, como ELEVENLABS_API_KEY. Nunca publique em GitHub Actions, prints ou mensagens.
3. Faça pré-verificação sem consumo:

```bash
python tools/gerar_voz_oficial.py --voice-id JBFqnCBsd6RMkjVDRZzb
```

4. Se autorizar expressamente o consumo de créditos da conta, acrescente `--confirm`:

```bash
python tools/gerar_voz_oficial.py --voice-id JBFqnCBsd6RMkjVDRZzb --confirm
```

Saída: `teste-elevenlabs.mp3`. Texto limitado a 200 caracteres por execução. Nenhuma execução remota com chave foi realizada e a compatibilidade real ainda precisa ser confirmada.

**Importante:** o plano gratuito não libera necessariamente a biblioteca completa de vozes pela API; os recursos disponíveis dependem da conta. A alternativa Reader via interface privada continua em estudo, sem tentar contornar medidas de segurança. Não inclua tokens privados Reader em repositórios públicos.
