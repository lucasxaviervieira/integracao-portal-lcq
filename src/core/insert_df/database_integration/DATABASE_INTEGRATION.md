# INTEGRAÇÃO AO BANCO DE DADOS

Esse módulo tem como objetivo. integrar o BD à esse sistema.

A partir da classe `PainelBordoDB`, temos:

- 1 (um) `método construtor` para conectar se ao BD;
- 3 (três) `métodos GET's` sendo esses:
  - id_amostra;
  - id_ponto_analise;
  - id_parametro;
- 2 (dois) `métodos POST's` sendo esses:
  - LAB_Amostra;
  - LAB_Dado_Analise;
- 1 (um) `método PUT` para atualizar os dados de análise;

## Variavéis de Ambiente

Para utilizar essa classe, são necessárias variavéis de ambiente, exemplo a seguir:

| Váriaveis de Ambiente     | Valor            |
| ------------------------- | ---------------- |
| _**`DATABASE_SERVER`**_   | localhost        |
| _**`DATABASE_NAME`**_     | example_db       |
| _**`DATABASE_USERNAME`**_ | example_username |
| _**`DATABASE_PASSWORD`**_ | example_password |
