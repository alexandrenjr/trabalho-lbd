# Trabalho Prático de Laboratório de Banco de Dados

Este projeto foi desenvolvido para a disciplina de Laboratório de Banco de Dados do curso de Engenharia de Computação da Faculdade de Computação da Universidade Federal de Mato Grosso do Sul.

## Tutorial de Instalação

Clone este repositório:

```bash
git clone <url-repo>
```

Em um terminal, crie um ambiente virtual no Python com o seguinte comando:

```bash
python -m venv env
```

Ative tal ambiente:

```bash
env\Scripts\activate
```

Instale as dependências com o seguinte comando:

```bash
pip install -r requirements.txt
```

## Executando a Aplicação

Execute a aplicação com:

```bash
python main.py
```

## Visualizando a Aplicação

Finalemten, aá para [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Observação

A *string* que inicializa um *database* no *PostgreSQL* em [`__init__.py`](webapp/__init__.py) (linha 6) é a seguinte:

```bash
postgresql+psycopg2://postgres:postgres@localhost:5432/trabalhodb
```

onde possui o seguinte formato:

```bash
postgresql+psycopg2://usuario:senha@localhost:porta/database
```
Definido tais campos, a aplicação irá criar um *database* com nome *database*, caso ela não
exista, de forma automática.
