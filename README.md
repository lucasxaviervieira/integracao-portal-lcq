# integracao-portal-lcq

Esse projeto tem como objetivo, integrar os dados de análises mensais das planilhas recebidas pelo LCQ com os pontos de análise no _`website`_ -> [Portal CAJ](http://portal/) (acesso apenas pela _intranet_).

## Documentação

O projeto foi documentado com arquivos `.md` (markdown) explicando cada diretório/arquivo.

Exemplo:

![MD example](/assets/md_example.png)

Veja a documentação do sistema, a partir daqui: [Documentation »](/src/core/CORE.md)

## Instalação e Configuração

### Rodar o Projeto

Clone o projeto

```bash
  git clone https://github.com/lucasxaviervieira/integracao-portal-lcq
```

Entre no diretório do projeto

```bash
  cd integracao-portal-lcq
```

Instale as dependências

**Utilize o gerenciador de pacotes** `PDM`

_Obs.: você pode utilizar também o `PIP`_

```bash
  pdm add
```

Inicie o servidor

```bash
  pdm run streamlit run .\src\app.py
```

#### Obs.: Inicie após configurar as variáveis de ambiente

### Configurar as Variáveis de Ambiente

Para rodar esse projeto, é necessário ter um arquivo `.env` na raiz do diretório, com as seguintes variáveis de ambiente:

```text
LDAP_SERVER="ldap://example.com"
LDAP_PORT=389
LDAP_DN="cn=admin,dc=example,dc=com"
DATABASE_SERVER="localhost"
DATABASE_NAME="example_db"
DATABASE_USERNAME="example_username"
DATABASE_PASSWORD="example_passowrd"
```

## Funcionalidades

- Autorização integrada a um servidor LDAP
- Leitura de arquivo `.xlsx` (excel)

## Tecnologias Usadas

- [PDM](https://pdm-project.org/en/latest/) Gerenciador de pacotes e ambiente virtual para Python.

- [streamlit](https://streamlit.io/) Framework para fornecer aplicações de dados interactivas.

- [pandas](https://pandas.pydata.org/) Ferramenta de análise e manipulação de dados para Python.

- [openpyxl](https://pypi.org/project/openpyxl/) Dependência para a biblioteca pandas ler arquivos `.xlsx` (excel).

- [ldap3](https://pypi.org/project/ldap3/) Biblioteca de cliente LDAP V3 em Python em conformidade com o RFC 4510

- [python-dotenv](https://pypi.org/project/ldap3/) Biblioteca para ler e definir como variável de ambiente, dados a partir de um arquivo `.env`.

- [pyodbc](https://pypi.org/project/pyodbc/) Módulo python que simplifica o acesso a bases de dados ODBC.

##

![Logo](/assets/logo.png)
