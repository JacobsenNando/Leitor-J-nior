
## Leitor Júnior - Portal de Resumos e Notas para Livros

Bem-vindo ao Leitor Júnior, um portal desenvolvido para inserir resumos e notas para livros, projetado para ser utilizado em escolas.

## Guia de Configuração

Este é um guia básico para configurar e iniciar o projeto Leitor Júnior com Django.

## Configuração do Ambiente Virtual

```bash
python -m venv venv
```

## Ativar o Ambiente Virtual

- No Windows:

```bash
./venv/Scripts/activate.ps1
```

- No Linux/Mac:

```bash
source venv/bin/activate
```

## Instalação de requerimentos

```bash
pip install requirements.txt
```
## Criação de Databases

 Em seu servidor MySQL, execute o seguinte comando para criar a database:
 ```bash
create database leitor_junior
```

## Migração do Banco de Dados

Execute o seguinte comando para criar as tabelas no banco de dados:

```bash
python manage.py migrate
```
## Popular as Tabelas

Execute os comandos encontrados no arquivo [popular bd.sql](https://github.com/JacobsenNando/PIA3/blob/main/popular%20bd.sql)

## Criação de um Superusuário

Para criar um usuário administrativo no Django, execute o seguinte comando e siga as instruções:

```bash
python manage.py createsuperuser
```

Isso abrirá uma série de prompts. Você pode usar "admin" como nome de usuário e definir uma senha de sua escolha. O email pode ser deixado em branco, apenas pressione Enter para continuar.

## Executar servidor local

Para executar o serviço localmente:

```bash
python manage.py runserver
```
```

Este README.md fornece instruções básicas para configurar um ambiente de desenvolvimento Django e iniciar o projeto Leitor Júnior.
