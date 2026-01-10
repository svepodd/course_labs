<div align="center">
<h1><a id="intro">Лабораторная работа №5</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Поддоскина_С._К.-8b9aff" alt="Contributor Badge"></a></div>

## Задание

- [x] 1. Поставьте `Docker` и `buildkit`

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05$ docker version
Client: Docker Engine - Community
 Version:           29.1.1
 API version:       1.52
 Go version:        go1.25.4
 Git commit:        0aedba5
 Built:             Fri Nov 28 11:33:04 2025
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          29.1.1
  API version:      1.52 (minimum version 1.44)
  Go version:       go1.25.4
  Git commit:       9a84135
  Built:            Fri Nov 28 11:33:04 2025
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          v2.2.0
  GitCommit:        1c4457e00facac03ce1d75f7b6777a7a851e5c41
 runc:
  Version:          1.3.4
  GitCommit:        v1.3.4-0-gd6d73eb8
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05$ docker buildx version
github.com/docker/buildx v0.30.1 9e66234aa13328a5e75b75aa5574e1ca6d6d9c01
```

- [x] 2. Перейдите в `source` и выведите на терминале, далее проанализируйте следующие команды консоли

```bash
$ docker buildx build -t hellow-appsec-world .
$ docker run hello-appsec-world
$ docker run --rm -it hello-appsec-world

$ docker save -o hello.tar hello-appsec-world
$ docker load -i hello.tar
$ docker load -i image.tar
```

Команда `docker buildx build -t hello-appsec-world .` осуществляет сборку Docker-образа через BuildKit с именем итогового образа `hello-appsec-world` в текущей папке.

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05/source$ docker buildx build -t hello-appsec-world .
[+] Building 27.6s (13/13) FINISHED                                                                      docker:default
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 443B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                0.9s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load build context                                                                                  0.1s
 => => transferring context: 63B                                                                                   0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db52214cf  0.2s
 => => resolve docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db52214cf9e20696e  0.2s
 => CACHED [builder 2/4] WORKDIR /hello                                                                            0.0s
 => CACHED [builder 3/4] COPY requirements.txt .                                                                   0.0s
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt              16.8s
 => [stage-1 3/6] COPY --from=builder /wheels /wheels                                                              0.1s 
 => [stage-1 4/6] COPY requirements.txt .                                                                          0.1s 
 => [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                              4.4s 
 => [stage-1 6/6] COPY hello.py .                                                                                  0.3s 
 => exporting to image                                                                                             3.0s 
 => => exporting layers                                                                                            1.5s 
 => => exporting manifest sha256:29cf312e5bb11c6e0552d7cbb4b32edb6942750758e8dbf780c019ec775946eb                  0.1s 
 => => exporting config sha256:daf961f1807a58dc05ae6a3d93d1a936742bb22ba1a2f1ce34d21c6b0c4a94e9                    0.0s
 => => exporting attestation manifest sha256:742e81c02e0f1cadfed669f2162b2e4f9a7b7665a7a663acee9d8e5e1940ac84      0.1s
 => => exporting manifest list sha256:8060a970aeea2b2a55dd736df22f4752ffcbb82d3ccbddd10845f278f8f1d20f             0.1s
 => => naming to docker.io/library/hello-appsec-world:latest                                                       0.0s
 => => unpacking to docker.io/library/hello-appsec-world:latest                                                    0.7s
```

При помои команды `docker run hello-appsec-world` запускаем контейнер из образа:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05/source$ docker run hello-appsec-world
hello appsec world
```

При помои команды `docker run --rm -it hello-appsec-world` запускаем контейнер из образа, но с флагами `-i` (оставляет STDIN открытым), `-t` (выделяет псевдо-терминал) и `--rm` (удаляет контейнер сразу после завершения)/

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05/source$ docker run --rm -it hello-appsec-world
hello appsec world
```

Экспорт Docker-образа `hello-appsec-world` в файл-архив `hello.tar`:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05/source$ docker save -o hello.tar hello-appsec-world
```

Импорт образа из архива `hello.tar` обратно в локальное хранилище Docker:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05/source$ docker load -i hello.tar
Loaded image: hello-appsec-world:latest
```

- [x] 3. Откройте `Dockerfile` и сделайте его анализ. Сделайте `commit`

```dockerfile
# Этап 1: сборка зависимостей
FROM python:3.11-slim AS builder
WORKDIR /hello
# Копируем файл с зависимостями
COPY requirements.txt . 
# Устанавливаем зависимости в отдельную директорию wheelhouse для кеширования
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt

# Этап 2: запускаемый образ
FROM python:3.11-slim
WORKDIR /hello
# Копируем файл с зависимостями
COPY --from=builder /wheels /wheels # Копируем собранные wheel-пакеты
COPY requirements.txt . 
# Устанавливаем зависимости из wheel-пакетов
RUN pip install --no-index --find-links=/wheels -r requirements.txt
# Копируем исходный код приложения
COPY hello.py .

# Переменные окружения для улучшенной работы Python
ENV PYTHONUNBUFFERED=1
# Запускаем приложение
CMD ["python", "hello.py"] 
```

Делаем commit:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ git add source/
svepodd@svepodd-VirtualBox:~/lab01$ git commit -S -m "Add hello-appsec-world"

[master 558e20b] Add hello-appsec-world
 4 files changed, 31 insertions(+)
 create mode 100644 source/Dockerfile
 create mode 100644 source/hello.py
 create mode 100644 source/hello.tar
 create mode 100644 source/requirements.txt
```

- [x] 4. Замените в `Dockerfile`значение скрипта на `python` тем, который вы сделали ранее в прошлых лабораторных работах. Вложите свой файл `python` в директорию. Сделайте анализ своего измененного `Dockerfile` и внесите изменения. Сделайте `commit`. 

Измененный `Dockerfile`:

```Dockerfile
# Этап 1: сборка wheel-пакетов
FROM python:3.11-slim AS builder
WORKDIR /app
# Копируем файл с зависимостями
COPY requirements.txt .
# Устанавливаем зависимости в отдельную директорию wheelhouse для кеширования
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt

# Этап 2: запускаемый образ
FROM python:3.11-slim
WORKDIR /app

# Минимальные системные зависимости для pygame/SDL (чтобы импорт/инициализация работали)
RUN apt-get update && apt-get install -y --no-install-recommends libsdl2-2.0-0 \
    libfreetype6 && rm -rf /var/lib/apt/lists/*
# Копируем файл с зависимостями
COPY --from=builder /wheels /wheels
COPY requirements.txt .
# Устанавливаем зависимости из wheel-пакетов
RUN pip install --no-index --find-links=/wheels -r requirements.txt
# Копируем исходный код приложения
COPY py_game.py .

# Переменные окружения для улучшенной работы Python
ENV PYTHONUNBUFFERED=1 \
    SDL_VIDEODRIVER=dummy \
    SDL_AUDIODRIVER=dummy \
    XDG_RUNTIME_DIR=/tmp

# Запускаем приложение
ENTRYPOINT ["python", "py_game.py"]
CMD []
```

`requirements.txt`:

```txt
pygame
typer
```

Делаем commit:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ git add Dockerfile requirements.txt py_game.py 
warning: in the working copy of 'source/Dockerfile', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'source/requirements.txt', LF will be replaced by CRLF the next time Git touches it
svepodd@svepodd-VirtualBox:~/lab01/source$ git commit -S -m "Modified Dockerfile (fix)"
[master fcc6aef] Modified Dockerfile (fix)
 2 files changed, 27 insertions(+), 7 deletions(-)
```

- [x] 5. Выведите на терминале и проанализируйте следующие команды консоли. Сравните хеш сумму вашего архива с `image.tar` из репозитория, выведите на терминал.

```bash
$ docker buildx build -t hellow-appsec-world .
$ docker run hello-appsec-world
$ docker save -o hello_ypur_project.tar hello-appsec-world

$ docker load -i hello_ypur_project.tar
$ docker run hello-appsec-world

$ docker load -i image.tar
$ docker run hello-appsec-world
```

Сборка Docker-образа:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker buildx build -t hello-appsec-world .
[+] Building 148.4s (14/14) FINISHED                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 1.43kB                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                1.3s
 => [internal] load .dockerignore                                                                                  0.1s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load build context                                                                                  0.1s
 => => transferring context: 67B                                                                                   0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db52214cf  0.2s
 => => resolve docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db52214cf9e20696e  0.1s
 => CACHED [builder 2/4] WORKDIR /app                                                                              0.0s
 => [stage-1 3/7] RUN apt-get update && apt-get install -y --no-install-recommends libsdl2-2.0-0     libfreetype  95.5s
 => [builder 3/4] COPY requirements.txt .                                                                          0.5s
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt              17.2s
 => [stage-1 4/7] COPY --from=builder /wheels /wheels                                                              1.0s 
 => [stage-1 5/7] COPY requirements.txt .                                                                          0.3s 
 => [stage-1 6/7] RUN pip install --no-index --find-links=/wheels -r requirements.txt                              8.7s 
 => [stage-1 7/7] COPY py_game.py .                                                                                0.5s 
 => exporting to image                                                                                            39.5s 
 => => exporting layers                                                                                           23.6s 
 => => exporting manifest sha256:ea5aad305ec19fa2aed6cfed8a54ae1f356aaa96df407a42da6f3215f891a64d                  0.0s 
 => => exporting config sha256:32b69dfafc7f996c1cac300c8aece39e778e50f360e9bab1cadb9d5c86928d17                    0.0s 
 => => exporting attestation manifest sha256:abb5a6808d81d77318cf751176073d69023ed64bb1924f2fa22cd0522c36cd99      0.1s 
 => => exporting manifest list sha256:85f420c040c98deca0c5c3f5ae25812b8f8fd066d4dfb2cedaf7bc094de8df60             0.0s 
 => => naming to docker.io/library/hello-appsec-world:latest                                                       0.0s 
 => => unpacking to docker.io/library/hello-appsec-world:latest                                                   15.4s
```

При помои команды `docker run hello-appsec-world` запускаем контейнер из образа:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker run hello-appsec-world
pygame 2.6.1 (SDL 2.28.4, Python 3.11.14)
Hello from the pygame community. https://www.pygame.org/contribute.html
+----------------------------+
| hello appsec world         |
| Who said hello: AppSec     |
| pygame: 2.6.1  uptime: 5ms |
+----------------------------+
svepodd@svepodd-VirtualBox:~/lab01/source$ docker run hello-appsec-world svepodd
pygame 2.6.1 (SDL 2.28.4, Python 3.11.14)
Hello from the pygame community. https://www.pygame.org/contribute.html
+----------------------------+
| hello appsec world         |
| Who said hello: svepodd    |
| pygame: 2.6.1  uptime: 3ms |
+----------------------------+
```

Экспорт Docker-образа `hello-appsec-world` в файл-архив `py_game.tar` и импорт образа из архива `py_game.tar` обратно в локальное хранилище Docker:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker save -o py_game.tar hello-appsec-world
svepodd@svepodd-VirtualBox:~/lab01/source$ docker load -i py_game.tar 
Loaded image: hello-appsec-world:latest
svepodd@svepodd-VirtualBox:~/lab01/source$ docker run hello-appsec-world
pygame 2.6.1 (SDL 2.28.4, Python 3.11.14)
Hello from the pygame community. https://www.pygame.org/contribute.html
+-----------------------------+
| hello appsec world          |
| Who said hello: AppSec      |
| pygame: 2.6.1  uptime: 56ms |
+-----------------------------+
```

Теперь импортируем образ из архива `hello.tar` и запускаем. Видим начальный вывод, как и ожидалось:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker load -i hello.tar 
Loaded image: hello-appsec-world:latest
svepodd@svepodd-VirtualBox:~/lab01/source$ docker run hello-appsec-world
hello appsec world
```

Сравниваем хэш-суммы двух архивов:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ sha256sum hello.tar 
6ee9dbcc55028deb39edffb6ba6dd3e8e61bdff852ea3685325c7f5f4767456e  hello.tar
svepodd@svepodd-VirtualBox:~/lab01/source$ sha256sum py_game.tar 
ea8a19f269dca8b2fc63911607e0d76ba5840ef346da9c388dc44a140926357f  py_game.tar
```

Как и ожидалось, видим разные хэш-суммы у архивов, что подтверждает различие образов.

- [x] 6. Доработайте свой `python` скрипт подключаемыми библиотеками, далее их необходимо разместить в `requirements.txt`. 

Фиксирование версий делает сборку воспроизводимой, а значит при повторной сборке зависимости не сломаются:

```
typer==0.12.3
pygame==2.6.1
```

- [x] 7. Сделайте `commit`. Повторите сборку приложения по вашему `Dockerfile` для доработанного скрипта `python`. Сохраните `image` в виде .`tar` архива. Сделайте `commit`.

Делаем commit:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ git add requirements.txt 
warning: in the working copy of 'source/requirements.txt', LF will be replaced by CRLF the next time Git touches it
svepodd@svepodd-VirtualBox:~/lab01/source$ git commit -S -m "Add modified requirements.txt"
[master 6773924] Add modified requirements.txt
 1 files changed, 2 insertions(+), 2 deletions(-)
```

Повторяем сборку и сохраняем образ в виде архива:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker buildx build -t hello-appsec-world .
[+] Building 48.0s (14/14) FINISHED                                                                      docker:default
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 1.43kB                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                1.5s
 => [internal] load .dockerignore                                                                                  0.1s
 => => transferring context: 2B                                                                                    0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db52214cf  0.1s
 => => resolve docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db52214cf9e20696e  0.1s
 => [internal] load build context                                                                                  0.1s
 => => transferring context: 105B                                                                                  0.1s
 => CACHED [builder 2/4] WORKDIR /app                                                                              0.0s
 => [builder 3/4] COPY requirements.txt .                                                                          0.3s
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt              19.0s
 => CACHED [stage-1 3/7] RUN apt-get update && apt-get install -y --no-install-recommends libsdl2-2.0-0     libfr  0.0s 
 => [stage-1 4/7] COPY --from=builder /wheels /wheels                                                              0.4s 
 => [stage-1 5/7] COPY requirements.txt .                                                                          0.1s 
 => [stage-1 6/7] RUN pip install --no-index --find-links=/wheels -r requirements.txt                              9.5s 
 => [stage-1 7/7] COPY py_game.py .                                                                                0.3s 
 => exporting to image                                                                                            14.3s 
 => => exporting layers                                                                                            8.9s 
 => => exporting manifest sha256:5f3baf90a7405bd7ea17d8e6a6834db3f6f12bf81f3d75273ca3c82743766cce                  0.1s 
 => => exporting config sha256:4bd96d11a952b4facbd5ea7aa4271eb2c663946ee5d9074cde5d38ec374cf52a                    0.0s 
 => => exporting attestation manifest sha256:701b271b3375116558a267f9e50b7ec7ad68b480e03c5e2f82c8f74a948d24d2      0.1s 
 => => exporting manifest list sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7             0.1s
 => => naming to docker.io/library/hello-appsec-world:latest                                                       0.0s
 => => unpacking to docker.io/library/hello-appsec-world:latest                                                    4.8s
svepodd@svepodd-VirtualBox:~/lab01/source$ docker run hello-appsec-world
pygame 2.6.1 (SDL 2.28.4, Python 3.11.14)
Hello from the pygame community. https://www.pygame.org/contribute.html
+----------------------------+
| hello appsec world         |
| Who said hello: AppSec     |
| pygame: 2.6.1  uptime: 4ms |
+----------------------------+
```

Сохраняем образ в виде архива `py_game_v2.tar`:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker save -o py_game_v2.tar hello-appsec-world
svepodd@svepodd-VirtualBox:~/lab01/source$ docker load -i py_game_v2.tar
Loaded image: hello-appsec-world:latest
```

- [x] 8. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ docker login
$ docker tag hello-appsec-world yourusername/hello-appsec-world
$ docker push yourusername/hello-appsec-world
$ docker inspect yourusername/hello-appsec-world
$ docker container create --name first hello-appsec-world # выпишите id контейнера

$ docker image pull geminishkv/hello-appsec-world
$ docker inspect geminishkvdev/hello-appsec-world
$ docker container create --name second hello-appsec-world
``` 

Команда `docker login` позволяет авторизоваться в Docker Hub, чтобы иметь право пушить образы в свой репозиторий:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker login

USING WEB-BASED LOGIN

i Info → To sign in with credentials on the command line, use 'docker login -u <username>'
         

Your one-time device confirmation code is: ...
Press ENTER to open your browser or submit your device code here: https://login.docker.com/activate

Waiting for authentication in the browser…

...

Login Succeeded
```

Команда `docker tag` позволяет задать тег образу:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker tag hello-appsec-world svepodd/hello-appsec-world
```

Команда `docker push svepodd/hello-appsec-world` отправляет образ в Docker Hub:

```
svepodd@svepodd-VirtualBox:~/lab01/source$ docker push svepodd/hello-appsec-world
Using default tag: latest
The push refers to repository [docker.io/svepodd/hello-appsec-world]
165e6c57422f: Pushed 
6079f1b842fb: Pushed 
223f5a70d3ad: Pushed 
06bf62cd5ca2: Pushed 
1473863bb010: Pushed 
7cc13cb22d92: Pushed 
9f359b2c9b15: Pushed 
12e21dd5eef7: Pushed 
02d7611c4eae: Pushed 
654a090213c0: Pushed 
89fd5444eda6: Pushed 
latest: digest: sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7 size: 856
```

Для просмотра метаданных образа используем команду `docker inspect`:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker inspect svepodd/hello-appsec-world
[
    {
        "Id": "sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7",
        "RepoTags": [
            "hello-appsec-world:latest",
            "svepodd/hello-appsec-world:latest"
        ],
        "RepoDigests": [
            "hello-appsec-world@sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7",
            "svepodd/hello-appsec-world@sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7"
        ],
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2026-01-09T13:54:49.860882135+03:00",
        "Config": {
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=...",
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78",
                "PYTHONUNBUFFERED=1",
                "SDL_VIDEODRIVER=dummy",
                "SDL_AUDIODRIVER=dummy",
                "XDG_RUNTIME_DIR=/tmp"
            ],
            "Entrypoint": [
                "python",
                "py_game.py"
            ],
            "WorkingDir": "/app",
            "ArgsEscaped": true
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 163076141,
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:6a7f953ae30c9f480e6eaf7be8b1ba742bce57a3a83c43e927348e763cff7472",
                "sha256:501421e049a171e15631e0b0e231ffd456ee4685f5b5b22cd98163cde83f2c6c",
                "sha256:72533f233c8abf13e297ce15ecbd0ca43a452405a88cb704f3e43a8db89ffe90",
                "sha256:253032e9f52a50fa025102eb1834cb841de4963cbebf37c593c147ccc36f537c",
                "sha256:e9570db72e7d6a625f470b9b96e3d449c73f416177b2b84c7eb602165b7afa20",
                "sha256:948381495740defe539a914020d888405595297122f92801f31e0be5b96f98b7",
                "sha256:126675dc2cf7613bbd9d4e0ebd9ec133995a364fa5c7a1fa41bdcb12e32fbb23",
                "sha256:7db5fedd9d735ae11a12268c686b1c6270183c6cd69c7cb11a404718f5b42d56",
                "sha256:f7a11bb60b539c25412375bf4c0c23cca3b2331a6b39657636efc54bc59f60f2",
                "sha256:6065a09445ca190e104796b737c9da794af80429bdcf05383de2e767ff3eaebd"
            ]
        },
        "Metadata": {
            "LastTagTime": "2026-01-09T11:04:13.470996189Z"
        },
        "Descriptor": {
            "mediaType": "application/vnd.oci.image.index.v1+json",
            "digest": "sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7",
            "size": 856,
            "annotations": {
                "io.containerd.image.name": "docker.io/library/hello-appsec-world:latest",
                "org.opencontainers.image.ref.name": "latest"
            }
        }
    }
]
```

В выводе:
- Entrypoint настроен как `["python", "py_game.py"]
- рабочая директория WorkingDir равна `/app``
- присутствует переменная окружения `PYTHONUNBUFFERED=1`

Команда `docker container create --name first hello-appsec-world` создаёт контейнер, но не запускает:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker container create --name first hello-appsec-world
02f0e529d7e5df7b1e592f5d313a6f0c7a94e0d06dfb59268715e06025637a03
```

Видим неуспешный запуск команды `docker image pull geminishkv/hello-appsec-world`, так как мы не имеем доступа к образу из репозитория geminishkv:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker image pull geminishkv/hello-appsec-world
Using default tag: latest
Error response from daemon: pull access denied for geminishkv/hello-appsec-world, repository does not exist or may require 'docker login'
```

Поэтому установим образ из своего репозитория:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker image pull svepodd/hello-appsec-world
Using default tag: latest
latest: Pulling from svepodd/hello-appsec-world
Digest: sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7
Status: Image is up to date for svepodd/hello-appsec-world:latest
docker.io/svepodd/hello-appsec-world:latest
```

Команда `inspect` выводит практически такие же результаты, как и в предыдущем случае:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker inspect svepodd/hello-appsec-world
[
    {
        "Id": "sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7",
        "RepoTags": [
            "hello-appsec-world:latest",
            "svepodd/hello-appsec-world:latest"
        ],
        "RepoDigests": [
            "hello-appsec-world@sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7",
            "svepodd/hello-appsec-world@sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7"
        ],
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2026-01-09T13:54:49.860882135+03:00",
        "Config": {
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=...",
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78",
                "PYTHONUNBUFFERED=1",
                "SDL_VIDEODRIVER=dummy",
                "SDL_AUDIODRIVER=dummy",
                "XDG_RUNTIME_DIR=/tmp"
            ],
            "Entrypoint": [
                "python",
                "py_game.py"
            ],
            "WorkingDir": "/app",
            "ArgsEscaped": true
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 163076141,
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:6a7f953ae30c9f480e6eaf7be8b1ba742bce57a3a83c43e927348e763cff7472",
                "sha256:501421e049a171e15631e0b0e231ffd456ee4685f5b5b22cd98163cde83f2c6c",
                "sha256:72533f233c8abf13e297ce15ecbd0ca43a452405a88cb704f3e43a8db89ffe90",
                "sha256:253032e9f52a50fa025102eb1834cb841de4963cbebf37c593c147ccc36f537c",
                "sha256:e9570db72e7d6a625f470b9b96e3d449c73f416177b2b84c7eb602165b7afa20",
                "sha256:948381495740defe539a914020d888405595297122f92801f31e0be5b96f98b7",
                "sha256:126675dc2cf7613bbd9d4e0ebd9ec133995a364fa5c7a1fa41bdcb12e32fbb23",
                "sha256:7db5fedd9d735ae11a12268c686b1c6270183c6cd69c7cb11a404718f5b42d56",
                "sha256:f7a11bb60b539c25412375bf4c0c23cca3b2331a6b39657636efc54bc59f60f2",
                "sha256:6065a09445ca190e104796b737c9da794af80429bdcf05383de2e767ff3eaebd"
            ]
        },
        "Metadata": {
            "LastTagTime": "2026-01-09T11:13:46.449399636Z"
        },
        "Descriptor": {
            "mediaType": "application/vnd.oci.image.index.v1+json",
            "digest": "sha256:d9ee6d821a2829928f8e34b47f4d95d1b621b2d58928635522f66c4563b23ba7",
            "size": 856
        }
    }
]
```

Создаем второй контейнер:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker container create --name second hello-appsec-world
a58b7da5ace538d1cf866409f58ef4cc72b024fd60a1c0cc93c2a4d8569de13a
```

- [x] 9. Выведите на терминале и проанализируйте в консоли процессы, которые запущены, владельцев по пользователям

```bash 
 $ docker container run -it ubuntu /bin/bash
``` 

Скачиваем и устанавливаем образ ubuntu. Подключаемся к нему и смотрим запущенные процессы:

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker container run -it ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
20043066d3d5: Pull complete 
06808451f0d6: Download complete 
Digest: sha256:c35e29c9450151419d9448b0fd75374fec4fff364a27f176fb458d472dfc9e54
Status: Downloaded newer image for ubuntu:latest
root@ded57b91f4d1:/# whoami
root
root@ded57b91f4d1:/# id
uid=0(root) gid=0(root) groups=0(root)
root@ded57b91f4d1:/# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.1  0.1   4588  4060 pts/0    Ss   11:11   0:00 /bin/bash
root          11  0.0  0.1   7888  4032 pts/0    R+   11:11   0:00 ps aux
```

Наблюдаем следующее:
- в контейнере по умолчанию пользователь `root`, что видно по `whoami` и `id`.
- `ps aux` показывает процессы внутри контейнера: PID 1 - главный процесс контейнера (`/bin/bash`), а остальное - команды, которые выполняются внутри.
 
- [x] 10. Выведите оба контейнера first и second на терминал

```bash
svepodd@svepodd-VirtualBox:~/lab01/source$ docker ps -a | grep first && docker ps -a | grep second
02f0e529d7e5   hello-appsec-world   "python py_game.py"      12 minutes ago   Created                                first
a58b7da5ace5   hello-appsec-world   "python py_game.py"      3 minutes ago    Created                                second
```

Команда `docker ps -a` показывает все контейнеры, `grep` помогает вывести только необходимые контейнеры. Контейнеры `first` и `second` находятся в статусе `Created`, т.е. они созданы, но не запущены.


- [x] 11. Перейдите в основной корень `lab05` и выведите на терминале, и проанализируйте

```bash 
$ docker-compose up --build
``` 

Выведем содержимое `docker-compose.yml`:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05$ cat docker-compose.yml 
version: "3.8"

networks:
  app_net:

services:
  server:
    build: ./server
    ports:
      - "8000:8000"
    networks:
      - app_net
    command: python app.py

  client:
    build: ./client
    depends_on:
      - server
    networks:
      - app_net
    command: python client.py
```

При помощи команды `docker compose up --build` собираем образы и поднимаем контейнеры:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05$ docker compose up --build
WARN[0000] /home/svepodd/course_labs/labs/lab05/docker-compose.yml: the attribute version is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Building 49.1s (27/27) FINISHED                                                                                     
 => [internal] load local bake definitions                                                                         0.0s
 => => reading from stdin 983B                                                                                     0.0s
 => [server internal] load build definition from Dockerfile                                                        0.2s
 => => transferring dockerfile: 431B                                                                               0.0s
 => [client internal] load build definition from Dockerfile                                                        0.1s
 => => transferring dockerfile: 437B                                                                               0.0s
 => [client internal] load metadata for docker.io/library/python:3.11-slim                                         2.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                      0.0s
 => [server internal] load .dockerignore                                                                           0.2s
 => => transferring context: 2B                                                                                    0.1s
 => [client internal] load .dockerignore                                                                           0.3s
 => => transferring context: 2B                                                                                    0.1s
 => [server internal] load build context                                                                           0.4s
 => => transferring context: 873B                                                                                  0.0s
 => [server builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db  0.4s
 => => resolve docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db52214cf9e20696e  0.4s
 => [client internal] load build context                                                                           0.4s
 => => transferring context: 595B                                                                                  0.0s
 => CACHED [client builder 2/4] WORKDIR /app                                                                       0.0s
 => [client builder 3/4] COPY requirements.txt .                                                                   0.4s
 => [server builder 3/4] COPY requirements.txt .                                                                   0.4s
 => [client builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt       21.2s
 => [server builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt       21.2s
 => [server stage-1 3/6] COPY --from=builder /wheels /wheels                                                       0.5s 
 => [client stage-1 3/6] COPY --from=builder /wheels /wheels                                                       0.6s 
 => [client stage-1 4/6] COPY requirements.txt .                                                                   0.6s 
 => [server stage-1 4/6] COPY requirements.txt .                                                                   0.7s 
 => [client stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                       9.7s 
 => [server stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                       9.6s
 => [server stage-1 6/6] COPY app.py .                                                                             0.8s
 => [client stage-1 6/6] COPY client.py .0.8s
 => [client] exporting to image                                                                                    8.2s
 => => exporting layers                                                                                            3.8s
 => => exporting manifest sha256:bb7d47d116a44b0181edc877b6b7c7331c6f40070f4cc12e132e389f46d99a4f                  0.1s
 => => exporting config sha256:8e4d633261da17c1c64093a3c15966c203781c642edfd5056f9ee177fbaa46bf                    0.2s
 => => exporting attestation manifest sha256:db0650798f0370fa2af73d343649aa4f1d7c40d82de872641d4044dd624f88e1      0.4s
 => => exporting manifest list sha256:54efc81a58c7aee2c6ed2050273c67af38e4e25ae82e9a0c80e73c5173bf9e19             0.1s
 => => naming to docker.io/library/lab05-client:latest                                                             0.4s
 => => unpacking to docker.io/library/lab05-client:latest                                                          2.7s
 => [server] exporting to image                                                                                    9.2s
 => => exporting layers                                                                                            5.0s
 => => exporting manifest sha256:0bcdaae50ad257a505feb3221ead13c423b666abfbc18c967bd20490c19ca66a                  0.1s
 => => exporting config sha256:02dcb8dbf512099dac8a955207d337aea1890f00aae01274d84e8c3ece3cde14                    0.1s
 => => exporting attestation manifest sha256:576c973aad690dafab7a991c4de8909613a957b6b400f99db981841956413942      0.3s
 => => exporting manifest list sha256:8d3ff44784aaba7aabf712db37138ea662fb7f5766b361571033bfa7937eed1a             0.2s
 => => naming to docker.io/library/lab05-server:latest                                                             0.1s
 => => unpacking to docker.io/library/lab05-server:latest                                                          2.8s
 => [client] resolving provenance for metadata file                                                                0.1s
 => [server] resolving provenance for metadata file                                                                0.1s
[+] Running 5/5
 ✔ lab05-server              Built                                                                                 0.0s 
 ✔ lab05-client              Built                                                                                 0.0s 
 ✔ Network lab05_app_net     Created                                                                               0.4s 
 ✔ Container lab05-server-1  Created                                                                               1.7s 
 ✔ Container lab05-client-1  Created                                                                               0.9s 
Attaching to client-1, server-1
server-1  |  * Serving Flask app 'app'
server-1  |  * Debug mode: off
server-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server-1  |  * Running on all addresses (0.0.0.0)
server-1  |  * Running on http://127.0.0.1:8000
server-1  |  * Running on http://172.20.0.2:8000
server-1  | Press CTRL+C to quit
server-1  | 172.20.0.3 - - [09/Jan/2026 11:20:17] "GET / HTTP/1.1" 200 -
client-1  | 
client-1  |     <html>
client-1  |     <head><title>Colorful Output</title></head>
...
```

- [x] 12. Откройте соседнее окно терминала и и выведите на терминале

```bash 
$ open -a "Google Chrome" http://localhost:8000
```

Команда `open -a` предназначена для macOS. Поэтому просто откроем в браузере `http://localhost:8000`:

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_lab05/labs/lab05/img/image-1.png)

- [x] 13. Остановите работу `docker-compose`.

```bash 
$ docker ps -a
$ docker ps -q
$ docker images

$ docker ps -q | xargs docker stop
$ docker-compose down
```

Команда `docker ps -a` выводит список всех контейнеров:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05$ docker ps -a
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS                      PORTS                                         NAMES
3e1e5c7ab611   lab05-client         "python client.py"       24 seconds ago   Up 21 seconds                                                             lab05-client-1
5a28504bf951   lab05-server         "python app.py"          24 seconds ago   Up 21 seconds               0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   lab05-server-1
a58b7da5ace5   hello-appsec-world   "python py_game.py"      11 minutes ago   Created                                                                   second
ded57b91f4d1   ubuntu               "/bin/bash"              14 minutes ago   Exited (0) 12 minutes ago                                                 sad_hawking
02f0e529d7e5   hello-appsec-world   "python py_game.py"      19 minutes ago   Created                                                                   first
a66e7225db0c   hello-appsec-world   "python py_game.py"      29 minutes ago   Exited (0) 29 minutes ago                                                 zen_goldberg
40a9cab4c565   hello-appsec-world   "python py_game.py"      30 minutes ago   Exited (0) 30 minutes ago                                                 unruffled_payne
e05e9bc24456   8060a970aeea         "python hello.py"        42 minutes ago   Exited (0) 42 minutes ago                                                 dreamy_lederberg
2087e70143d3   85f420c040c9         "python py_game.py"      42 minutes ago   Exited (0) 42 minutes ago                                                 focused_haibt
54a257f4eb4e   85f420c040c9         "python py_game.py s…"   44 minutes ago   Exited (0) 44 minutes ago                                                 ecstatic_borg
6338b9b5b755   85f420c040c9         "python py_game.py"      44 minutes ago   Exited (0) 44 minutes ago                                                 funny_cartwright
abd4c9dc3595   8060a970aeea         "python hello.py"        55 minutes ago   Exited (0) 55 minutes ago                                                 funny_pare
680025b4e810   deb1ec609622         "python py_game.py"      55 minutes ago   Exited (0) 55 minutes ago                                                 ecstatic_keller
794ea7d1046e   deb1ec609622         "python py_game.py"      59 minutes ago   Exited (0) 59 minutes ago                                                 nifty_mendel
06ca19421260   38c1f02c2532         "python py_game.py"      2 days ago       Exited (130) 2 days ago                                                   clever_merkle
9988076fa373   registry:2           "/entrypoint.sh /etc…"   2 days ago       Up 2 days                   5000/tcp                                      registry.1.xnaa782c6x7lcl8gaihjzp6dw
6d0cf0a1bd2f   38c1f02c2532         "python py_game.py"      2 days ago       Exited (130) 2 days ago                                                   sweet_lalande
0eab453d6def   8060a970aeea         "python hello.py"        2 days ago       Exited (0) 2 days ago                                                     unruffled_khorana
8d966f2fcbdc   registry:2           "/entrypoint.sh /etc…"   2 days ago       Exited (2) 2 days ago                                                     registry.1.9fqnksvs6cigjq4q1h4l6r8iw
455a6aa04108   registry:2           "/entrypoint.sh /etc…"   3 weeks ago      Exited (2) 2 days ago                                                     registry.1.jjvi31rroolb61yqu0w7d2br7
18204f4b10d7   registry:2           "/entrypoint.sh /etc…"   3 weeks ago      Exited (2) 3 weeks ago                                                    registry.1.jv7vwpfjssivb0esovvilph6c
649f327b047d   registry:2           "/entrypoint.sh /etc…"   3 weeks ago      Exited (2) 3 weeks ago                                                    registry.1.b7frtatcct32rnv9nc3y9mzwu
55bd0095806e   registry:2           "/entrypoint.sh /etc…"   8 weeks ago      Exited (255) 7 weeks ago 5000/tcp                                      
e8c260e4b6ad   hello-world          "/hello"                 8 weeks ago      Exited (0) 8 weeks ago                                                    busy_benz
```

Команда `docker ps -q` выводит ID запущенных контейнеров:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05$ docker ps -q
3e1e5c7ab611
5a28504bf951
9988076fa373
```

Команда `docker images` показывает список локальных Docker-образов:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05$ docker images
                                                                                                    i Info →   U  In Use
IMAGE                                                                   ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-appsec-world:latest                                               d9ee6d821a28        615MB          163MB    U   
hello-world:latest                                                      56433a6be3fd       20.3kB         3.96kB    U   
lab05-client:latest                                                     c25231fe3ff6        208MB         50.9MB    U   
lab05-server:latest                                                     d732543bf630        211MB         51.8MB    U   
registry:2@sha256:a3d8aaa63ed8681a604f1dea0aa03f100d5895b6a58ace528858a7b332415373
                                                                        a3d8aaa63ed8       37.2MB         10.1MB    U   
svepodd/hello-appsec-world:latest                                       d9ee6d821a28        615MB          163MB    U   
ubuntu:latest                                                           c35e29c94501        119MB         31.7MB    U   
```

Команда `docker ps -q | xargs docker stop` останавливает все запущенные контейнеры:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05$ docker ps -q | xargs docker stop
3e1e5c7ab611
5a28504bf951
9988076fa373
```

Команда `docker compose down` останавливает и удаляет ресурсы, созданные `docker-compose up`:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05$ docker compose down
WARN[0000] /home/svepodd/course_labs/labs/lab05/docker-compose.yml: the attribute version is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 3/3
 ✔ Container lab05-client-1  Removed                                                                               0.0s 
 ✔ Container lab05-server-1  Removed                                                                               0.0s 
 ✔ Network lab05_app_net     Removed                                                                               0.4s 
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab05$
```

- [x] 14. Доработайте `docker-compose` и скрипт, который вы подготовили ранее, что бы вы смогли воспроизвести шаги п.11 по п.13 с демонстрацией. Сделайте `commit`.

Запускаем:

```bash
(svepodd_venv) svepodd@svepodd-VirtualBox:~/lab01/docker$ docker compose up --build
[+] Building 68.7s (23/23) FINISHED                                                                                     
 => [internal] load local bake definitions                                                                         0.0s
 => => reading from stdin 947B                                                                                     0.0s
 => [server internal] load build definition from Dockerfile                                                        0.0s
 => => transferring dockerfile: 856B                                                                               0.0s
 => [client internal] load build definition from Dockerfile                                                        0.1s
 => => transferring dockerfile: 140B                                                                               0.0s
 => [client internal] load metadata for docker.io/library/python:3.11-slim                                         1.3s
 => [auth] library/python:pull token for registry-1.docker.io                                                      0.0s
 => [server internal] load .dockerignore                                                                           0.1s
 => => transferring context: 2B                                                                                    0.0s
 => [client internal] load .dockerignore                                                                           0.2s
 => => transferring context: 2B                                                                                    0.0s
 => [client builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db  0.3s
 => => resolve docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db52214cf9e20696e  0.2s
 => [server internal] load build context                                                                           0.1s
 => => transferring context: 125B                                                                                  0.0s
 => [client internal] load build context                                                                           0.1s
 => => transferring context: 31B                                                                                   0.0s
 => CACHED [server builder 2/4] WORKDIR /app                                                                       0.0s
 => CACHED [client 3/3] COPY client.py .                                                                           0.0s
 => [server builder 3/4] COPY requirements.txt .                                                                   0.7s
 => [client] exporting to image                                                                                    1.1s
 => => exporting layers                                                                                            0.0s
 => => exporting manifest sha256:b671bb0a123f5b9141ed68722aab885d9d9fd369806b4d2cc0ac2fdbdd72630c                  0.0s
 => => exporting config sha256:16f0ca3924bdd25696202cb1cb5e39f9986b60a39b6c7d0bc17bb67b05abf4f6                    0.0s
 => => exporting attestation manifest sha256:b28b8f0f00db94b11e87a091d3f18d949e892e2cd46d03c7b85fb159affb6f7e      0.5s
 => => exporting manifest list sha256:e289136184143f8b71ec23574ad6dcfba6b96ea98ed3cd89b691e4ba9f4bace9             0.1s
 => => naming to docker.io/library/docker-client:latest                                                            0.0s
 => => unpacking to docker.io/library/docker-client:latest                                                         0.1s
 => [server builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt       44.7s
 => [client] resolving provenance for metadata file                                                                0.1s
 => CACHED [server stage-1 3/7] RUN apt-get update && apt-get install -y --no-install-recommends     libsdl2-2.0-  0.0s
 => [server stage-1 4/7] COPY --from=builder
 /wheels /wheels                                                       0.5s
 => [server stage-1 5/7] COPY requirements.txt .                                                                   0.3s
 => [server stage-1 6/7] RUN pip install --no-index --find-links=/wheels -r requirements.txt                       8.3s
 => [server stage-1 7/7] COPY app.py .                                                                             0.4s
 => [server] exporting to image                                                                                   10.5s
 => => exporting layers                                                                                            6.6s
 => => exporting manifest sha256:c34589cde06368ed64e0a684f6a40157686bd8f3b521c9b0e3b2b3b9392211e8                  0.1s
 => => exporting config sha256:c0a289ea7c7945467942f19915563b8addb9a699142daec89f4ba5317b2399ed                    0.1s
 => => exporting attestation manifest sha256:49c8ddb06c1850ee2f8e131ff602f236bb6d168e17030e780a9f8d645a742d2d      0.1s
 => => exporting manifest list sha256:dc232c7822454f88b18a56c60c2215b9e47721f754d82ede82eca9949c083487             0.1s
 => => naming to docker.io/library/docker-server:latest                                                            0.0s
 => => unpacking to docker.io/library/docker-server:latest                                                         3.2s
 => [server] resolving provenance for metadata file                                                                0.1s
[+] Running 5/5
 ✔ docker-server              Built                                                                                0.0s 
 ✔ docker-client              Built                                                                                0.0s 
 ✔ Network docker_app_net     Created                                                                              0.2s 
 ✔ Container docker-server-1  Created                                                                              1.7s 
 ✔ Container docker-client-1  Created                                                                              0.3s 
Attaching to client-1, server-1
server-1  |  * Serving Flask app 'app'
server-1  |  * Debug mode: off
...
```

Переходим а браузере на `http://localhost:8000` и видим успешный результат:

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_lab05/labs/lab05/img/image-2.png)

Останавливаем:

```bash
svepodd@svepodd-VirtualBox:~/lab01/docker$ docker ps -a
CONTAINER ID   IMAGE                COMMAND                  CREATED             STATUS                         PORTS                                         NAMES
7259c9c664cb   registry:2           "/entrypoint.sh /etc…"   10 minutes ago      Up 10 minutes                  5000/tcp                                      registry.1.0upzb04blbz4gw1u8f5469xcl
f467c2e646e0   docker-client        "python client.py"       40 minutes ago      Exited (0) 40 minutes ago                                                    docker-client-1
194a9599f9e0   docker-server        "python app.py"          40 minutes ago      Up 40 minutes                  0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   docker-server-1
800ea05b8162   registry:2           "/entrypoint.sh /etc…"   About an hour ago   Exited (2) 10 minutes ago                                                    registry.1.oibfgg4wdmsqmemuh2m3ec8el
b3692b1f9c65   registry:2           "/entrypoint.sh /etc…"   2 hours ago         Exited (2) About an hour ago                                                 registry.1.z0tl0i6ucg7bhkflzm5g2e1id
a58b7da5ace5   hello-appsec-world   "python py_game.py"      2 hours ago         Created                                                                      second
ded57b91f4d1   ubuntu               "/bin/bash"              2 hours ago         Exited (0) 2 hours ago                                                       sad_hawking
02f0e529d7e5   hello-appsec-world   "python py_game.py"      2 hours ago         Created                                                                      first
a66e7225db0c   hello-appsec-world   "python py_game.py"      2 hours ago         Exited (0) 2 hours ago                                                       zen_goldberg
40a9cab4c565   hello-appsec-world   "python py_game.py"      2 hours ago         Exited (0) 2 hours ago                                                       unruffled_payne
e05e9bc24456   8060a970aeea         "python hello.py"        2 hours ago         Exited (0) 2 hours ago                                                       dreamy_lederberg
2087e70143d3   85f420c040c9         "python py_game.py"      2 hours ago         Exited (0) 2 hours ago                                                       focused_haibt
54a257f4eb4e   85f420c040c9         "python py_game.py s…"   2 hours ago         Exited (0) 2 hours ago                                                       ecstatic_borg
6338b9b5b755   85f420c040c9         "python py_game.py"      2 hours ago         Exited (0) 2 hours ago                                                       funny_cartwright
abd4c9dc3595   8060a970aeea         "python hello.py"        3 hours ago         Exited (0) 3 hours ago                                                       funny_pare
680025b4e810   deb1ec609622         "python py_game.py"      3 hours ago         Exited (0) 3 hours ago                                                       ecstatic_keller
794ea7d1046e   deb1ec609622         "python py_game.py"      3 hours ago         Exited (0) 3 hours ago                                                       nifty_mendel
06ca19421260   38c1f02c2532         "python py_game.py"      2 days ago          Exited (130) 2 days ago                                                      clever_merkle
9988076fa373   registry:2           "/entrypoint.sh /etc…"   2 days ago          Exited (2) 2 hours ago                                                       registry.1.xnaa782c6x7lcl8gaihjzp6dw
6d0cf0a1bd2f   38c1f02c2532         "python py_game.py"      2 days ago          Exited (130) 2 days ago                                                      sweet_lalande
0eab453d6def   8060a970aeea         "python hello.py"        2 days ago          Exited (0) 2 days ago                                                        unruffled_khorana
455a6aa04108   registry:2           "/entrypoint.sh /etc…"   3 weeks ago         Exited (2) 2 days ago
svepodd@svepodd-VirtualBox:~/lab01/docker$ docker ps -q
7259c9c664cb
194a9599f9e0
svepodd@svepodd-VirtualBox:~/lab01/docker$ docker images
                                                                                                    i Info →   U  In Use
IMAGE                                                                   ID             DISK USAGE   CONTENT SIZE   EXTRA
docker-client:latest                                                    e28913618414        186MB         45.4MB    U   
docker-server:latest                                                    dc232c782245        622MB          165MB    U   
hello-appsec-world:latest                                               d9ee6d821a28        615MB          163MB    U   
hello-world:latest                                                      56433a6be3fd       20.3kB         3.96kB    U   
lab05-client:latest                                                     c25231fe3ff6        208MB         50.9MB        
lab05-server:latest                                                     d732543bf630        211MB         51.8MB        
registry:2@sha256:a3d8aaa63ed8681a604f1dea0aa03f100d5895b6a58ace528858a7b332415373
                                                                        a3d8aaa63ed8       37.2MB         10.1MB    U   
svepodd/hello-appsec-world:latest                                       d9ee6d821a28        615MB          163MB    U   
ubuntu:latest                                                           c35e29c94501        119MB         31.7MB    U   
svepodd@svepodd-VirtualBox:~/lab01/docker$ docker ps -q | xargs docker stop
7259c9c664cb
194a9599f9e0
svepodd@svepodd-VirtualBox:~/lab01/docker$ docker compose down
[+] Running 3/3
 ✔ Container docker-client-1  Removed                                                                              0.0s 
 ✔ Container docker-server-1  Removed                                                                              0.0s 
 ✔ Network docker_app_net     Removed                                                                              0.2s 
```

- [x] 15. Залейте изменения в свой удаленный репозиторий, проверьте историю `commit`.

Делаем commit:
```bash
svepodd@svepodd-VirtualBox:~/lab01$ git add docker/
warning: in the working copy of 'docker/client/Dockerfile', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docker/client/client.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docker/docker-compose.yaml', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docker/server/Dockerfile', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docker/server/app.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docker/server/requirements.txt', LF will be replaced by CRLF the next time Git touches it
svepodd@svepodd-VirtualBox:~/lab01$ git commit -S -m "New docker-compose.yaml"
[master 88fb2a9] New docker-compose.yaml
 6 files changed, 140 insertions(+)
 create mode 100644 docker/client/Dockerfile
 create mode 100644 docker/client/client.py
 create mode 100644 docker/docker-compose.yaml
 create mode 100644 docker/server/Dockerfile
 create mode 100644 docker/server/app.py
 create mode 100644 docker/server/requirements.txt
```

Смотрим историю:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ git log --oneline --decorate --graph
* 88fb2a9 (HEAD -> master, origin/master, origin/HEAD) New docker-compose.yaml
* 6773924 Add modified requirements.txt
* fcc6aef Modified Dockerfile (fix)
* 558e20b Add hello-appsec-world
* 0511cb2 Add nmapres.txt
* 4a482d3 Add py_game.py
* 087edd2 Merge pull request #2 from svepodd/patch2
|\  
| * 4a045f6 (origin/patch2) Code style was changed
|/  
* 42d853c Comment change #2
* ea39d8d Comment change
*   d7a0ad2 Merge pull request #1 from svepodd/patch1
|\  
| * 713060d New comment in hello.py
| * 6e6930b hello.py in patch1
|/  
* 16a818a Add new hello.py
* 927df8f Add hello.py
* 6a192c1 test #1
```

- [x] 16. Подготовьте отчет `gist`.
 
***

Copyright (c) 2025 Svetlana Poddoskina

