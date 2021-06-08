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

## Selenium Grid

* Létrehozunk egy `selenium-grid-demo` könyvtárban egy `docker-compose.yaml` állományt
* `docker compose up` parancsot a `selenium-grid-demo` könyvtárban
* Elérhető a `http://localhost:4444/`

### Ha VNC-n nézni akarjátok

* VNC kliens feltelepítése: https://www.realvnc.com/en/connect/download/viewer/
* VNC csatlakozás a `localhost:5900`-as címre

### Ha Side runnert akartok

* Selenium IDE teszteset létrehozása
* Mentsük el `Python.side` néven

* Létrehoztam a `Dockerfile-side-runner` fájlt
* Parancs: `docker build -t side-runner --file Dockerfile-side-runner .`
* Futtatás: `docker run --network selenium-grid-network side-runner`

### Ha fejlesztőeszközből

* El kell indítani a `python_selenium_task` fájlt