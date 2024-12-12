# MÓDULOS DO SISTEMA

O núcleo do sistema tem como objetivo, realizar a limpeza do `Excel` tratar seus dados a partir de um `dataframe` - da biblioteca `Pandas` - e, então se conectar a um Banco de Dados para inserir as novas informações.

O núcleo está divido em 3 etapas;

## Etapa I {#AUTH}

Esse módulo tem como objetivo, implementar um meio de autorização para o uso do sistema;

Ir para o módulo: [Auth »](/src/core/auth/AUTH.md)

## Etapa II {#CLEAN_XL}

Esse módulo tem como objetivo higienizar o `Excel` importado;

Ir para o módulo: [Clean XL »](/src/core/clean_xl/CLEAN_EXCEL.md)

## Etapa III {#INSERT_DF}

Esse módulo tem como objetivo inserir o `dataframe` em um BD;

Ir para o módulo: [Insert DF »](/src/core/insert_df/INSERT_DATAFRAME.md)
