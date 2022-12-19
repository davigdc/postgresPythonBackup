# postgersPythonBackup
Este projeto é parte do curso "Introduction to Python Development" da plataforma "A Cloud Guru". A finalidade é criar um CLI "pgbackup" que nos permite realizar o dump de um banco de dados postgresSQL e exportar para um diretório local ou para um bucket S3 na AWS.

---
## pgbackup
CLI for backing up remote PostgreSQL databases locally or to AWS S3.

---
## Usage
Pass in a full database URL, the storage driver, and destination.
S3 Example w/ bucket name:
```
$ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups
```

Local Example w/ local path:
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
## Installation From Source

To install the package after you've cloned the repository, you'll
want to run the following command from within the project directory:
```
$ pip install --user -e .
```

---
## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:davigdc/postgersPythonBackup`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`

---
