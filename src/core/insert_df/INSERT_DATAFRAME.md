# ADICIONAR DADOS NO BD

Esse módulo tem como objetivo. inserir os dados do `dataframe` em um Banco de Dados

O arquivo principal `index.py`, tem a função `insert_dataframe()`, que recebe o `dataframe` tratado.

Para cada linha ele verifica se existe uma amostra já cadastrada no banco.

Se existe, são atualizados os dados de análise com os valores fornecidos pelas colunas.

Se não, ele insere uma nova amostra e a partir disso, insere novos dados de análise.

**A seguir, como as colunas são representadas em cada ambiente:**

|           Excel           |      Banco de Dados       |
| :-----------------------: | :-----------------------: |
|       _**`Cloro`**_       |  _**`Cloro Residual`**_   |
| _**`Coliformes Totais`**_ | _**`Coliformes Totais`**_ |
|        _**`Cor`**_        |   _**`Cor Aparente`**_    |
|      _**`E Coli`**_       | _**`Escherichia Coli`**_  |
|     _**`Turbidez`**_      |     _**`Turbidez`**_      |
