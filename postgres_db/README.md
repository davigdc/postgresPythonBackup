# Executar PostgresSQL em Container
Para testarmos o projeto, podemos executar o banco de dados postgresSQL facilmente em um container e popularmos com os comandos abaixo. Para isso, é necessário ter docker instaldo.

```
# Dentro desta pasta, execute:
$ docker compose up -d

# Após subir o container, popular com script:
docker exec -ti postgres_container psql -U postgres -d sample -f /tmp/scripts/populate_db.sql

# Pronto para uso!
```