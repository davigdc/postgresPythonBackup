# 💡 postgresPythonBackup
Este projeto é parte do curso "Introduction to Python Development" da plataforma "A Cloud Guru". A finalidade é criar um CLI "pgbackup" que nos permite realizar o dump de um banco de dados postgresSQL e exportar para um diretório local ou para um bucket S3 na AWS.

---
## pgbackup
CLI para realizar backup remoto do banco de dados PostgreSQL localmente ou para AWS S3.

---
## Uso
Ajuda do comando:
```
$ pgbackup --help
usage: pgbackup [-h] --driver DRIVER DESTINATION url

Back up PostgreSQL databases locally or to AWS S3.

positional arguments:
  url                   URL of the database to backup

options:
  -h, --help            show this help message and exit
  --driver DRIVER DESTINATION, -d DRIVER DESTINATION
                        how & where to store backup
```

Passe a URL do banco de dados completo, o driver de armazenamento e o destino:
Exemplo S3:
```
$ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups
```

Exemplo local:
```
$ pgbackup postgres://bob@example.com:5432/db_one --driver local /
var/local/db_one/backups
```

---
## 📋 Pré-requisitos
- Python

- Banco de dados PostgresSQL acessível e com dados. Na pasta 'postgres_db' a um tutorial de como configurar utilizando docker e o popular com um script.

- AWS CLI
    ```
    # Comandos da documentação oficial
    $ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    $ unzip awscliv2.zip
    $ sudo ./aws/install
    ```

- Binário 'pg_dump'
    ```
    # Create the file repository configuration:
    $ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

    # Import the repository signing key:
    $ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

    # Update the package lists:
    $ sudo apt update

    # Install the latest version of postgres-client (contains pg_dump binarie). 
    $ sudo apt install postgresql-client
    ```

---
## Instalar da fonte

Para instalar o package depois de clonar o repositório:
```
$ pip install --user -e .
```

---
## Preparar para Desenvolvimento

Siga estes passos:

1. Garanta `pip` e `pipenv` estão instalados
2. Clone o repositório: `git clone git@github.com:davigdc/postgresPythonBackup`
3. `cd` para o diretório
4. Ative o virtualenv: `pipenv shell`
5. Instale as dependências: `pipenv install`

---
