# Passo 4

## Limpar dados

Esse módulo tem como objetivo limpar os dados de algumas colunas do `dataframe`.

### Primeira Limpeza

Realizado na coluna `Ponto`.

**Verifica a quantidade de caracteres;**

Se for igual a `4` caracteres, os dados da linha são obtidos

### Segunda Limpeza

Realizado na coluna `Data da Avaliação e Liberação`.

**Verifica se avalidado e liberado;**

Se for não nulo, os dados da linha são obtidos

### Terceira Limpeza

Realizado nas colunas:

|       _**`Cloro`**_       |
| :-----------------------: |
|     _**`Turbidez`**_      |
|        _**`Cor`**_        |
| _**`Coliformes Totais`**_ |
|      _**`E Coli`**_       |

**Modificar tipo de dado;**

Altera os valores de `Object` para `String`

**_POSTERIORMENTE: VERIFICAR SE EXISTE, SE NÃO, NÃO ADICIONA_**

### Quarta Limpeza

Realizado na coluna `Ponto`.

**Separa o sufixo `N` do conjunto;**

Logo após isso, transforma essa coluna no índice do `dataframe`.

Voltar para a **documentação índice**: [Documentation »](/src/core/CORE.md)
