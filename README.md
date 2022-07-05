# Trabalho Prático de Laboratório de Banco de Dados

Este projeto foi desenvolvido para a disciplina de Laboratório de Banco de Dados do curso de Engenharia de Computação da Faculdade de Computação da Universidade Federal de Mato Grosso do Sul.

O trabalho proposto era desenvolver uma aplicação *web* que executasse um CRUD básico. Tal projeto modelou um subuniverso do Sistema Único de Saúde (SUS), no qual relaciona pacientes e profissionais da saúde, assim como à Cartilha de Vacinação. Para o desenvolvimento desse, foi usado a linguagem *Python*, com o *Object Relational Mapper* (ORM) *SQL Alchemy*. Para o *front-end*, foi usado o *framework* *Bootstrap*, majoritariamente HTML.
## Tutorial de Instalação

Clone este repositório:

```bash
git clone <url-repo>
```

Em um terminal, crie um ambiente virtual no *Python* com o seguinte comando:

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

Finalmente, vá para [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Observação

A *string* que inicializa um banco de dados no *PostgreSQL* em [`__init__.py`](webapp/__init__.py) (linha 6) é a seguinte:

```bash
postgresql+psycopg2://postgres:postgres@localhost:5432/trabalhodb
```

onde possui o seguinte formato:

```bash
postgresql+psycopg2://usuario:senha@localhost:porta/database
```
Definido tais campos, a aplicação irá criar um banco de dados com nome *database*, caso ela não
exista, de forma automática.
