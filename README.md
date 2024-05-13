
# Leitor Júnior - Portal de Resumos e Notas para Livros

Bem-vindo ao Leitor Júnior, um portal desenvolvido para inserir resumos e notas para livros, projetado para ser utilizado em escolas.

## Guia de Configuração

Este é um guia básico para configurar e iniciar o projeto Leitor Júnior com Django no VSCode.

## Configuração do Ambiente Virtual
- No diretório raiz do projeto

```bash
python -m venv venv
```

## Ativar o Ambiente Virtual

- No Windows (PowerShell):

```PowerShell
./venv/Scripts/activate.ps1
```

- No Windows (bash):

```bash
./venv/Scripts/activate.ps1
```

- No Linux/Mac:

```bash
source venv/bin/activate
```

## Instalação de dependências

```bash
pip install -r requirements.txt
```
# Integração com o banco de dados

Há duas possibilidades para integração com banco de dados por padrão neste projeto, a primeira e mais simples é o dbSqlite3 e a segunda o MySQL Workbench.
## dbSqlite3
- Caso opte por usa o dbSqlite3, apenas pule para o passo de "Migraçao do Banco de Dados", apenas lembre-se de conferir Settings.py DATABASES para configurar o dbSqlite3 ao invés do MySQL.

## MySQL

Em seu servidor MySQL, execute o seguinte comando para criar o database:
 ```bash
create database leitor_junior
```
Em seguida, crie um usuário o qual o ORM do Django irá utilizar para acessar o database 
### Dica: 
- Lembre-se de substituir 'novo_usuario' e 'senha' de acordo com o seu projeto, podem ser valores arbitrários, mas devem coincidir com os dados passados para Settings.py DATABASES.
- Se o banco de dados estiver na mesma máquina do servidor Django, pode ser mantido localhost, caso contrário, altere conforme sua necessidade, lembrando de revisar os parametros em Settings.py DATABASES
 ```mysql
CREATE USER 'novo_usuário'@'localhost' IDENTIFIED BY 'senha'; 
```
Em seguida, crie as permissões para o usuário:
 ```mysql
GRANT ALL PRIVILEGES ON * . * TO 'novo_usuario'@'localhost';
```

## Migração do Banco de Dados

Após a criação do banco de dados, no VSCode, execute o seguinte comando para criar as tabelas no banco de dados:

```bash
python manage.py migrate
```
## Popular as Tabelas

Execute os comandos encontrados no arquivo [popular bd.sql](https://github.com/JacobsenNando/PIA3/blob/main/popular%20bd.sql)
- O arquivo contendo os comandos SQL foi gerado de uma adaptaçao de um dataset público, para que atendesse as necessidade do projeto. O dataset orignial está disponível em: https://www.kaggle.com/datasets/diegomariano/tabela-de-livros?resource=download
- Foram ustilizados alguns dados desse dataset e inserido outros de forma arbitrária conforme a necessidade do projeto para realização dos testes.
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
## Finalização
- Neste ponto, o servidor deve estar configurado corretamente pra funcionar de forma local no VSCode, caso encontre alguma dificuldade não deixa de entrar em contato
