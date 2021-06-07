# Tesztautomatizálás oktatás

## Docker

```shell
net localgroup docker-users OKTATAS\T360-v3-ITSH-o /add
```

## Alkalmazás indítása

A `locations` könyvtárban létre kell hozni `docker-compose.yml` fájlt, majd a 
következő paranccsal indítható az alkalmazás:

```shell
docker compose up
```

Ezután elérhető a [http://localhost:8080](http://localhost:8080) címen.


