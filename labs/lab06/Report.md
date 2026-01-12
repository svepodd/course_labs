<div align="center">
<h1><a id="intro">Лабораторная работа №6</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Поддоскина_С._К.-8b9aff" alt="Contributor Badge"></a></div>

***
## Задание

- [x] 1. Необходимо установить `Docker Engine` для Linux

```bash
$ sudo apt-get update
$ sudo apt-get install -y docker.io
$ sudo usermod -aG docker "$USER"

$ sudo systemctl start docker
$ docker pull docker/docker-bench-security
```

Docker был установлен ранее:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab06$ docker info
Client: Docker Engine - Community
 Version:    29.1.1
 Context:    default
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.30.1
    Path:     /usr/libexec/docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /usr/libexec/docker/cli-plugins/docker-compose

Server:
 Containers: 22
  Running: 1
  Paused: 0
  Stopped: 21
 Images: 12
 Server Version: 29.1.1
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: active
  NodeID: ua9nf0ufe02rz5rj62jn2t871
  Is Manager: true
  ClusterID: 16jj7bjgg0ur2i7pdw90ayibz
  Managers: 1
  Nodes: 1
  Default Address Pool: 10.0.0.0/8  
  SubnetSize: 24
  Data Path Port: 4789
  Orchestration:
   Task History Retention Limit: 5
  Raft:
   Snapshot Interval: 10000
   Number of Old Snapshots to Retain: 0
   Heartbeat Tick: 1
   Election Tick: 10
  Dispatcher:
   Heartbeat Period: 5 seconds
  CA Configuration:
   Expiry Duration: 3 months
   Force Rotate: 0
  Autolock Managers: false
  Root Rotation In Progress: false
  Node Address: 10.0.2.15
  Manager Addresses:
   10.0.2.15:2377
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 1c4457e00facac03ce1d75f7b6777a7a851e5c41
 runc version: v1.3.4-0-gd6d73eb8
 init version: de40ad0
 Security Options:
  apparmor
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.14.0-37-generic
 Operating System: Ubuntu 24.04.3 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 4
 Total Memory: 3.824GiB
 Name: svepodd-VirtualBox
 ID: 56420892-7b12-4c5b-8027-bfea34cd906e
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Username: svepodd
 Experimental: false
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false
 Firewall Backend: iptables
```

- [x] 2. Проверьте работу докера и сделать скрипт `audit.sh` исполняемым

Проверяем работоспособность Docker запуском `hello-world` образа:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab06$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

Делаем скрипт `audit.sh` исполняемым:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab06$ chmod +x audit.sh
```

- [x] 3. Развернуть уязвимое приложение как отдельные стенды

```bash
$ docker compose up -d # основной web, app, postgres
$ docker-compose -f vulnerable-app.yml up -d # поверх для vulnerable-web, debug-shell
    -f # file
    up # создает и поднимает файлы из compose
    -d # фоновый режим
```

Разворачиваем:

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab06$ docker compose up -d
WARN[0000] /home/svepodd/course_labs/labs/lab06/docker-compose.yml: the attribute version is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] Found orphan containers ([debug-shell]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
[+] Running 3/3
 ✔ Container insecure-db                    Started                                                                1.1s 
 ✔ Container vulnerable-app                 Started                                                                2.3s 
 ✔ Container 516c602120a9_vulnerable-nginx  Started                                                                2.5s 
```

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab06$ docker compose -f vulnerable-app.yml up -d
WARN[0000] /home/svepodd/course_labs/labs/lab06/vulnerable-app.yml: the attribute version is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] Found orphan containers ([vulnerable-app insecure-db]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
[+] Running 3/3
 ✔ Container 516c602120a9_vulnerable-nginx  Recreated                                                              1.4s 
 ✔ Container debug-shell                    Started                                                                0.9s 
 ✔ Container vulnerable-web                 Started                                                                1.0s
```

- [x] 4. Запустите скрипт из `venv` и проанализируйте то, что вывело на терминале и что вывело при конвертировании

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install openpyxl odfpy
$ ./audit.sh
$ deactivate # или $ deactivate 2>/dev/null || true
```

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab06$ python3 -m venv venv
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab06$ source venv/bin/activate
(venv) svepodd@svepodd-VirtualBox:~/course_labs/labs/lab06$ pip install openpyxl odfpy
Collecting openpyxl
  Downloading openpyxl-3.1.5-py2.py3-none-any.whl.metadata (2.5 kB)
Collecting odfpy
  Downloading odfpy-1.4.1.tar.gz (717 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 717.0/717.0 kB 2.5 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting et-xmlfile (from openpyxl)
  Downloading et_xmlfile-2.0.0-py3-none-any.whl.metadata (2.7 kB)
Collecting defusedxml (from odfpy)
  Downloading defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)
Downloading openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 250.9/250.9 kB 3.7 MB/s eta 0:00:00
Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Downloading et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
Building wheels for collected packages: odfpy
  Building wheel for odfpy (pyproject.toml) ... done
  Created wheel for odfpy: filename=odfpy-1.4.1-py2.py3-none-any.whl size=160717 sha256=230cd86ad2ee838733b4901e2ebb9598070ad6ca586b0f25d0e5c990e52646bf
  Stored in directory: /home/svepodd/.cache/pip/wheels/36/5d/63/8243a7ee78fff0f944d638fd0e66d7278888f5e2285d7346b6
Successfully built odfpy
Installing collected packages: et-xmlfile, defusedxml, openpyxl, odfpy
Successfully installed defusedxml-0.7.1 et-xmlfile-2.0.0 odfpy-1.4.1 openpyxl-3.1.5
```

Запускаем скрипт:

```bash
(venv) svepodd@svepodd-VirtualBox:~/course_labs/labs/lab06$ ./audit.sh
Starting Docker CIS & Image Security Audit
==========================================
Detected platform: Linux
Using docker-bench-security image: docker/docker-bench-security:latest
Reports will be saved to: ./audit_reports/

Running Trivy scan for docker/docker-bench-security:latest...
2026-01-11T17:34:18+03:00       INFO    [vuln] Vulnerability scanning is enabled
2026-01-11T17:34:18+03:00       INFO    [secret] Secret scanning is enabled
2026-01-11T17:34:18+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-01-11T17:34:18+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2026-01-11T17:34:18+03:00       INFO    Detected OS     family="alpine" version="3.8.2"
2026-01-11T17:34:18+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.8" repository="3.8" pkg_num=25
2026-01-11T17:34:18+03:00       INFO    Number of language-specific files       num=0
2026-01-11T17:34:18+03:00       WARN    This OS version is no longer supported by the distribution      family="alpine" version="3.8.2"
2026-01-11T17:34:18+03:00       WARN    The vulnerability detection may be insufficient because security updates are not provided
Saved to: ./audit_reports/json/docker-bench-security-trivy.json

Scanning lab images for vulnerabilities...

=== Trivy scan for nginx:alpine ===
2026-01-11T17:34:18+03:00       INFO    [vuln] Vulnerability scanning is enabled
2026-01-11T17:34:18+03:00       INFO    [secret] Secret scanning is enabled
2026-01-11T17:34:18+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-01-11T17:34:18+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2026-01-11T17:34:18+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2026-01-11T17:34:18+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2026-01-11T17:34:18+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=71
2026-01-11T17:34:18+03:00       INFO    Number of language-specific files       num=0
Saved to: ./audit_reports/json/nginx-alpine-trivy.json

=== Trivy scan for python:3.11-alpine ===
2026-01-11T17:34:18+03:00       INFO    [vuln] Vulnerability scanning is enabled
2026-01-11T17:34:18+03:00       INFO    [secret] Secret scanning is enabled
2026-01-11T17:34:18+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-01-11T17:34:18+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2026-01-11T17:34:18+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2026-01-11T17:34:18+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2026-01-11T17:34:18+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=38
2026-01-11T17:34:18+03:00       INFO    Number of language-specific files       num=1
2026-01-11T17:34:18+03:00       INFO    [python-pkg] Detecting vulnerabilities...
Saved to: ./audit_reports/json/python-3.11-alpine-trivy.json

=== Trivy scan for postgres:16-alpine ===
2026-01-11T17:34:18+03:00       INFO    [vuln] Vulnerability scanning is enabled
2026-01-11T17:34:18+03:00       INFO    [secret] Secret scanning is enabled
2026-01-11T17:34:18+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-01-11T17:34:18+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2026-01-11T17:34:18+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2026-01-11T17:34:18+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2026-01-11T17:34:18+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=45
2026-01-11T17:34:18+03:00       INFO    Number of language-specific files       num=1
2026-01-11T17:34:18+03:00       INFO    [gobinary] Detecting vulnerabilities...
2026-01-11T17:34:18+03:00       WARN    Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/docs/v0.68/guide/scanner/vulnerability#severity-selection for details.
Saved to: ./audit_reports/json/postgres-16-alpine-trivy.json

Linux host detected – configuring mounts for CIS Docker Benchmark coverage

Mounting /usr/lib/systemd
Mounting /var/log
Running Docker Bench Security container (CIS host audit)

# ------------------------------------------------------------------------------
# Docker Bench for Security v1.3.4
#
# Docker, Inc. (c) 2015-
#
# Checks for dozens of common best-practices around deploying Docker containers in production.
# Inspired by the CIS Docker Community Edition Benchmark v1.1.0.
# ------------------------------------------------------------------------------

Initializing Sun Jan 11 14:34:18 UTC 2025


[INFO] 1 - Host Configuration
[WARN] 1.1  - Ensure a separate partition for containers has been created
[NOTE] 1.2  - Ensure the container host has been Hardened
[PASS] 1.3  - Ensure Docker is up to date
[INFO]      * Using 28.5.1 which is current
[INFO]      * Check with your operating system vendor for support and security maintenance for Docker
[INFO] 1.4  - Ensure only trusted users are allowed to control Docker daemon
[INFO]      * docker:x:1001:svepodd
[WARN] 1.5  - Ensure auditing is configured for the Docker daemon
[INFO] 1.6  - Ensure auditing is configured for Docker files and directories - /var/lib/docker
[INFO]      * Directory not found
[INFO] 1.7  - Ensure auditing is configured for Docker files and directories - /etc/docker
[INFO]      * Directory not found
[INFO] 1.8  - Ensure auditing is configured for Docker files and directories - docker.service
[INFO]      * File not found
[INFO] 1.9  - Ensure auditing is configured for Docker files and directories - docker.socket
[INFO]      * File not found
[INFO] 1.10  - Ensure auditing is configured for Docker files and directories - /etc/default/docker
[INFO]      * File not found
[INFO] 1.11  - Ensure auditing is configured for Docker files and directories - /etc/docker/daemon.json
[INFO]      * File not found
[INFO] 1.12  - Ensure auditing is configured for Docker files and directories - /usr/bin/docker-containerd
[INFO]      * File not found
[INFO] 1.13  - Ensure auditing is configured for Docker files and directories - /usr/bin/docker-runc
[INFO]      * File not found


[INFO] 2 - Docker daemon configuration
[WARN] 2.1  - Ensure network traffic is restricted between containers on the default bridge
[PASS] 2.2  - Ensure the logging level is set to 'info'
[PASS] 2.3  - Ensure Docker is allowed to make changes to iptables
[PASS] 2.4  - Ensure insecure registries are not used
[PASS] 2.5  - Ensure aufs storage driver is not used
[WARN] 2.6  - Ensure TLS authentication for Docker daemon is configured
[WARN]      * Docker daemon currently listening on TCP without TLS
[INFO] 2.7  - Ensure the default ulimit is configured appropriately
[INFO]      * Default ulimit doesn't appear to be set
[WARN] 2.8  - Enable user namespace support
[PASS] 2.9  - Ensure the default cgroup usage has been confirmed
[PASS] 2.10  - Ensure base device size is not changed until needed
[WARN] 2.11  - Ensure that authorization for Docker client commands is enabled
[WARN] 2.12  - Ensure centralized and remote logging is configured
[INFO] 2.13  - Ensure operations on legacy registry (v1) are Disabled (Deprecated)
[PASS] 2.14  - Ensure live restore is Enabled (Incompatible with swarm mode)
[WARN] 2.15  - Ensure Userland Proxy is Disabled
[INFO] 2.16  - Ensure daemon-wide custom seccomp profile is applied, if needed
[PASS] 2.17  - Ensure experimental features are avoided in production
[WARN] 2.18  - Ensure containers are restricted from acquiring new privileges


[INFO] 3 - Docker daemon configuration files
[INFO] 3.1  - Ensure that docker.service file ownership is set to root:root
[INFO]      * File not found
[INFO] 3.2  - Ensure that docker.service file permissions are set to 644 or more restrictive
[INFO]      * File not found
[INFO] 3.3  - Ensure that docker.socket file ownership is set to root:root
[INFO]      * File not found
[INFO] 3.4  - Ensure that docker.socket file permissions are set to 644 or more restrictive
[INFO]      * File not found
[INFO] 3.5  - Ensure that /etc/docker directory ownership is set to root:root
[INFO]      * Directory not found
[INFO] 3.6  - Ensure that /etc/docker directory permissions are set to 755 or more restrictive
[INFO]      * Directory not found
[INFO] 3.7  - Ensure that registry certificate file ownership is set to root:root
[INFO]      * Directory not found
[INFO] 3.8  - Ensure that registry certificate file permissions are set to 444 or more restrictive
[INFO]      * Directory not found
[INFO] 3.9  - Ensure that TLS CA certificate file ownership is set to root:root
[INFO]      * No TLS CA certificate found
[INFO] 3.10  - Ensure that TLS CA certificate file permissions are set to 444 or more restrictive
[INFO]      * No TLS CA certificate found
[INFO] 3.11  - Ensure that Docker server certificate file ownership is set to root:root
[INFO]      * No TLS Server certificate found
[INFO] 3.12  - Ensure that Docker server certificate file permissions are set to 444 or more restrictive
[INFO]      * No TLS Server certificate found
[INFO] 3.13  - Ensure that Docker server certificate key file ownership is set to root:root
[INFO]      * No TLS Key found
[INFO] 3.14  - Ensure that Docker server certificate key file permissions are set to 400
[INFO]      * No TLS Key found
[PASS] 3.15  - Ensure that Docker socket file ownership is set to root:docker
[PASS] 3.16  - Ensure that Docker socket file permissions are set to 660 or more restrictive
[INFO] 3.17  - Ensure that daemon.json file ownership is set to root:root
[INFO]      * File not found
[INFO] 3.18  - Ensure that daemon.json file permissions are set to 644 or more restrictive
[INFO]      * File not found
[INFO] 3.19  - Ensure that /etc/default/docker file ownership is set to root:root
[INFO]      * File not found
[INFO] 3.20  - Ensure that /etc/default/docker file permissions are set to 644 or more restrictive
[INFO]      * File not found


[INFO] 4 - Container Images and Build File
[WARN] 4.1  - Ensure a user for the container has been created
[WARN]      * Running as root: registry.1.ux6q3c95n42tue0b9xirrkrwg
[NOTE] 4.2  - Ensure that containers use trusted base images
[NOTE] 4.3  - Ensure unnecessary packages are not installed in the container
[NOTE] 4.4  - Ensure images are scanned and rebuilt to include security patches
[WARN] 4.5  - Ensure Content trust for Docker is Enabled
[WARN] 4.6  - Ensure HEALTHCHECK instructions have been added to the container image
[WARN]      * No Healthcheck found: [course_lab1-hello:latest]
[WARN]      * No Healthcheck found: [lab05-server:latest]
[WARN]      * No Healthcheck found: [lab05-client:latest]
[WARN]      * No Healthcheck found: [nginx:alpine]
[WARN]      * No Healthcheck found: [python:3.11-alpine]
[WARN]      * No Healthcheck found: [postgres:16-alpine]
[WARN]      * No Healthcheck found: [alpine:latest]
[WARN]      * No Healthcheck found: [my-hello-appsec:latest]
[WARN]      * No Healthcheck found: [hellow-appsec-world:latest]
[WARN]      * No Healthcheck found: [svepodd/hello-appsec-world:latest hello-appsec-world:latest svepodd/hello-appsec-world:latest]
[WARN]      * No Healthcheck found: [svepodd/hello-appsec-world:latest hello-appsec-world:latest svepodd/hello-appsec-world:latest]
[WARN]      * No Healthcheck found: [ghcr.io/digininja/dvwa:latest]
[WARN]      * No Healthcheck found: [hadoop/submit:3.4.2]
[WARN]      * No Healthcheck found: [nginx:latest]
[WARN]      * No Healthcheck found: [hadoop/basic:3.4.2]
[WARN]      * No Healthcheck found: [jupyterlab/core:4.4.9]
[WARN]      * No Healthcheck found: [spark/core:3.5.7]
[WARN]      * No Healthcheck found: [127.0.0.1:5000/mpi:latest@sha256:7c4617d46f34f515c97cc84b060fa24b22142970c76dadc250d5552c4e330c2e]
[WARN]      * No Healthcheck found: [127.0.0.1:5000/mpi:latest]
[WARN]      * No Healthcheck found: [mariadb:10]
[WARN]      * No Healthcheck found: [structurizr/onpremises:latest]
[WARN]      * No Healthcheck found: [ubuntu:latest]
[WARN]      * No Healthcheck found: [voice_recognizer-asr:latest]
[WARN]      * No Healthcheck found: [registry:2@sha256:a3d8aaa63ed8681a604f1dea0aa03f100d5895b6a58ace528858a7b332415373]
[INFO] 4.7  - Ensure update instructions are not use alone in the Dockerfile
[INFO]      * Update instruction found: [course_lab1-hello:latest]
[INFO]      * Update instruction found: [lab05-server:latest]
[INFO]      * Update instruction found: [lab05-client:latest]
[INFO]      * Update instruction found: [my-hello-appsec:latest]
[INFO]      * Update instruction found: [hellow-appsec-world:latest]
[INFO]      * Update instruction found: [svepodd/hello-appsec-world:latest hello-appsec-world:latest svepodd/hello-appsec-world:latest]
[INFO]      * Update instruction found: [svepodd/hello-appsec-world:latest hello-appsec-world:latest svepodd/hello-appsec-world:latest]
[INFO]      * Update instruction found: [ghcr.io/digininja/dvwa:latest]
[INFO]      * Update instruction found: [hadoop/submit:3.4.2]
[INFO]      * Update instruction found: [hadoop/historyserver:3.4.2]
[INFO]      * Update instruction found: [hadoop/nodemanager:3.4.2]
[INFO]      * Update instruction found: [hadoop/resourcemanager:3.4.2]
[INFO]      * Update instruction found: [hadoop/datanode:3.4.2]
[INFO]      * Update instruction found: [hadoop/namenode:3.4.2]
[INFO]      * Update instruction found: [hadoop/basic:3.4.2]
[INFO]      * Update instruction found: [jupyterlab/core:4.4.9]
[INFO]      * Update instruction found: [spark/core:3.5.7]
[INFO]      * Update instruction found: [structurizr/onpremises:latest]
[INFO]      * Update instruction found: [structurizr/lite:latest]
[INFO]      * Update instruction found: [voice_recognizer-asr:latest]
[NOTE] 4.8  - Ensure setuid and setgid permissions are removed in the images
[INFO] 4.9  - Ensure COPY is used instead of ADD in Dockerfile
[INFO]      * ADD in image history: [nginx:alpine]
[INFO]      * ADD in image history: [python:3.11-alpine]
[INFO]      * ADD in image history: [postgres:16-alpine]
[INFO]      * ADD in image history: [alpine:latest]
[INFO]      * ADD in image history: [hadoop/submit:3.4.2]
[INFO]      * ADD in image history: [hadoop/historyserver:3.4.2]
[INFO]      * ADD in image history: [hadoop/nodemanager:3.4.2]
[INFO]      * ADD in image history: [hadoop/resourcemanager:3.4.2]
[INFO]      * ADD in image history: [hadoop/datanode:3.4.2]
[INFO]      * ADD in image history: [hadoop/namenode:3.4.2]
[INFO]      * ADD in image history: [hadoop/basic:3.4.2]
[INFO]      * ADD in image history: [jupyterlab/core:4.4.9]
[INFO]      * ADD in image history: [spark/core:3.5.7]
[INFO]      * ADD in image history: [127.0.0.1:5000/mpi:latest@sha256:7c4617d46f34f515c97cc84b060fa24b22142970c76dadc250d5552c4e330c2e]
[INFO]      * ADD in image history: [127.0.0.1:5000/mpi:latest]
[INFO]      * ADD in image history: [mariadb:10]
[INFO]      * ADD in image history: [structurizr/onpremises:latest]
[INFO]      * ADD in image history: [structurizr/lite:latest]
[INFO]      * ADD in image history: [ubuntu:latest]
[INFO]      * ADD in image history: [registry:2@sha256:a3d8aaa63ed8681a604f1dea0aa03f100d5895b6a58ace528858a7b332415373]
[INFO]      * ADD in image history: [docker/docker-bench-security:latest]
[NOTE] 4.10  - Ensure secrets are not stored in Dockerfiles
[NOTE] 4.11  - Ensure verified packages are only Installed


[INFO] 5 - Container Runtime
[WARN] 5.1  - Ensure AppArmor Profile is Enabled
[WARN]      * No AppArmorProfile Found: vulnerable-web
[WARN]      * No AppArmorProfile Found: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.2  - Ensure SELinux security options are set, if applicable
[WARN]      * No SecurityOptions Found: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.3  - Ensure Linux Kernel Capabilities are restricted within containers
[WARN]      * Capabilities added: CapAdd=[ALL] to vulnerable-web
[WARN] 5.4  - Ensure privileged containers are not used
[WARN]      * Container running in Privileged mode: vulnerable-web
[PASS] 5.5  - Ensure sensitive host system directories are not mounted on containers
[PASS] 5.6  - Ensure ssh is not run within containers
[PASS] 5.7  - Ensure privileged ports are not mapped within containers
[NOTE] 5.8  - Ensure only needed ports are open on the container
[WARN] 5.9  - Ensure the host's network namespace is not shared
[WARN]      * Container running with networking mode 'host': vulnerable-web
[WARN] 5.10  - Ensure memory usage for container is limited
[WARN]      * Container running without memory restrictions: vulnerable-web
[WARN]      * Container running without memory restrictions: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.11  - Ensure CPU priority is set appropriately on the container
[WARN]      * Container running without CPU restrictions: vulnerable-web
[WARN]      * Container running without CPU restrictions: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.12  - Ensure the container's root filesystem is mounted as read only
[WARN]      * Container running with root FS mounted R/W: vulnerable-web
[WARN]      * Container running with root FS mounted R/W: registry.1.ux6q3c95n42tue0b9xirrkrwg
[PASS] 5.13  - Ensure incoming container traffic is binded to a specific host interface
[WARN] 5.14  - Ensure 'on-failure' container restart policy is set to '5'
[WARN]      * MaximumRetryCount is not set to 5: vulnerable-web
[WARN]      * MaximumRetryCount is not set to 5: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.15  - Ensure the host's process namespace is not shared
[WARN]      * Host PID namespace being shared with: vulnerable-web
[PASS] 5.16  - Ensure the host's IPC namespace is not shared
[PASS] 5.17  - Ensure host devices are not directly exposed to containers
[INFO] 5.18  - Ensure the default ulimit is overwritten at runtime, only if needed
[INFO]      * Container no default ulimit override: vulnerable-web
[INFO]      * Container no default ulimit override: registry.1.ux6q3c95n42tue0b9xirrkrwg
[PASS] 5.19  - Ensure mount propagation mode is not set to shared
[PASS] 5.20  - Ensure the host's UTS namespace is not shared
[WARN] 5.21  - Ensure the default seccomp profile is not Disabled
[WARN]      * Default seccomp profile disabled: vulnerable-web
[NOTE] 5.22  - Ensure docker exec commands are not used with privileged option
[NOTE] 5.23  - Ensure docker exec commands are not used with user option
[PASS] 5.24  - Ensure cgroup usage is confirmed
[WARN] 5.25  - Ensure the container is restricted from acquiring additional privileges
[WARN]      * Privileges not restricted: vulnerable-web
[WARN]      * Privileges not restricted: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.26  - Ensure container health is checked at runtime
[WARN]      * Health check not set: vulnerable-web
[WARN]      * Health check not set: registry.1.ux6q3c95n42tue0b9xirrkrwg
[INFO] 5.27  - Ensure docker commands always get the latest version of the image
[WARN] 5.28  - Ensure PIDs cgroup limit is used
[WARN]      * PIDs limit not set: vulnerable-web
[WARN]      * PIDs limit not set: registry.1.ux6q3c95n42tue0b9xirrkrwg
[PASS] 5.29  - Ensure Docker's default bridge docker0 is not used
[PASS] 5.30  - Ensure the host's user namespaces is not shared
[WARN] 5.31  - Ensure the Docker socket is not mounted inside any containers
[WARN]      * Docker socket shared: vulnerable-web


[INFO] 6 - Docker Security Operations
[INFO] 6.1  - Avoid image sprawl
[INFO]      * There are currently: 33 images
[INFO] 6.2  - Avoid container sprawl
[INFO]      * There are currently a total of 30 containers, with only 3 of them currently running


[INFO] 7 - Docker Swarm Configuration
[WARN] 7.1  - Ensure swarm mode is not Enabled, if not needed
[PASS] 7.2  - Ensure the minimum number of manager nodes have been created in a swarm
[WARN] 7.3  - Ensure swarm services are binded to a specific host interface
[WARN] 7.4  - Ensure data exchanged between containers are encrypted on different nodes on the overlay network
[WARN]      * Unencrypted overlay network: ingress (swarm)
[INFO] 7.5  - Ensure Docker's secret management commands are used for managing secrets in a Swarm cluster
[WARN] 7.6  - Ensure swarm manager is run in auto-lock mode
[NOTE] 7.7  - Ensure swarm manager auto-lock key is rotated periodically
[INFO] 7.8  - Ensure node certificates are rotated as appropriate
[INFO] 7.9  - Ensure CA certificates are rotated as appropriate
[INFO] 7.10  - Ensure management plane traffic has been separated from data plane traffic

[INFO] Checks: 105
[INFO] Score: -9

CIS audit output saved to: ./audit_reports/text/docker-bench-security-cis.txt

Converting Trivy JSON reports to XLSX/ODT formats...
✓ Saved to XLSX: ./audit_reports/xlsx/postgres-16-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/postgres-16-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/docker-bench-security-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/docker-bench-security-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/nginx-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/nginx-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/python-3.11-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/python-3.11-alpine-trivy.odt

==========================================
Audit complete!
Reports directory structure:
   ./audit_reports/
   ├── json/          (Trivy JSON outputs)
   ├── text/          (CIS audit text outputs)
   ├── xlsx/          (Excel spreadsheets)
   └── odt/           (OpenDocument Text files)

For CIS Docker Benchmark details, see:
https://www.cisecurity.org/benchmark/docker
```

В итоге было проведено 105 проверок, а общая оценка безопасности составила -9 очков:

```bash
[INFO] Checks: 105
[INFO] Score: -9
```

- [x] 5. Проведите анализ уязвимостей, опишите их причину возникновения

**5.1. Уязвимости уровня образов (Trivy)**

**Проблема: EOL-образ внутри docker-bench-security (Alpine 3.8.2)**  
В логе Trivy видим:

```bash
2026-01-11T17:34:18+03:00       WARN    This OS version is no longer supported by the distribution      family="alpine" version="3.8.2"
```

Это означает, что базовая ОС образа устарела, security updates не поставляются, поэтому часть уязвимостей может оставаться неисправленной и даже не полностью детектироваться.

**Причина:** использование старой версии базового образа/слоя, который больше не поддерживается дистрибутивом.  

**Следствие:** рост вероятности эксплуатации известных CVE в системных пакетах, снижение достоверности скана (обновления баз безопасности для EOL могут быть неполными).

**5.2. Уязвимости уровня конфигурации daemon/хоста**

**Separate partition for containers**  
- Причина: `/var/lib/docker` расположен не на отдельном разделе.  
- Риск: при "разрастании" образов/логов можно забить диск хоста => отказ в обслуживании.

**Docker daemon listening on TCP without TLS**  
- Причина: демон доступен по TCP без TLS.  
- Риск: перехват управления Docker => полный контроль над контейнерами и потенциально хостом.

**Enable user namespace support**  
- Причина: userns-изоляция не включена.  
- Риск: процессы root в контейнере ближе по привилегиям к root на хосте (хуже работает принцип least privilege).

**Restrict containers from acquiring new privileges**  
- Причина: не включён `no-new-privileges`.  
- Риск: внутри контейнера проще повышать привилегии через setuid/setcap и цепочки уязвимостей.

**Аудит файлов Docker не настроен**  
- Причина: отсутствуют правила auditd для docker-файлов/директорий.  
- Риск: хуже расследование инцидентов (нет событий доступа/изменений), ниже наблюдаемость.

**5.3. Уязвимости уровня runtime контейнеров**

**AppArmor profile отсутствует**
- Причина: контейнер запущен без AppArmor-профиля.
- Риск: меньше барьеров на доступ контейнера к системным ресурсам => повышается вероятность побега из контейнера при эксплуатации RCE и уязвимостей ядра/сервисов.

**CapAdd=[ALL] (выданы все Linux capabilities)**
- Причина: в `vulnarable-app.yml` задано `cap_add: [ALL]`, что расширяет права процесса в контейнере. 
- Риск: контейнер получает привилегии, близкие к root на хосте => проще повысить привилегии и обойти ограничения namespaces/seccomp/LSM.

**Privileged mode**
- Причина: включён `privileged: true`. Это фактически максимальные права контейнера.
- Риск: высокая вероятность компрометации хоста при наличии RCE в приложении. Любая уязвимость внутри контейнера становится значительно опаснее, потому что контейнер почти не изолирован.

**Host network (network_mode: host)**
- Причина: контейнер подключён к сетевому стеку хоста (`network_mode: host`). 
- Риск: теряется сетевой периметр контейнера. Возможны: перехват/прослушка локальных сервисов хоста, обход ограничений публикации портов, рост последствий сканирования внутренней сети.

**Host PID namespace (pid: host)**
- Причина: задано `pid: host`.
- Риск: процессы в контейнере видят процессы хоста => упрощается разведка и атаки на хостовые сервисы, повышается риск закрепления/скрытности вредоносной активности.

**Seccomp по умолчанию отключён**
- Причина: задано `security_opt: ["seccomp=unconfined"]`. 
- Риск: контейнеру доступны потенциально опасные системные вызовы. Это повышает вероятность эксплуатации: уязвимостей ядра, техник обхода изоляции, вредоносных действий, которые seccomp обычно ограничивает.

**Docker socket смонтирован в контейнер**
- Причина: в volumes проброшен `/var/run/docker.sock:/var/run/docker.sock`.
- Риск: это почти прямой root-доступ к хосту, потому что внутри контейнера можно управлять Docker daemon.

**Нет лимитов на RAM/CPU/PIDs**
- Причина: не заданы `mem_limit`, `cpus`/`cpu_quota`, `pids_limit`. 
- Риск: DoS на хост: контейнер может занять всю память => падение сервисов, может выжечь CPU => деградация, может исчерпать PID’ы => проблемы запуска процессов на хосте и в других контейнерах.

**Root filesystem доступна на запись (R/W)**
- Причина: не включено `read_only: true` и не настроены tmpfs/volume для временных данных.
- Риск: упрощается закрепление атакующего внутри контейнера, подмена файлов приложения, сокрытие следов, изменение конфигов.

 **Нет healthcheck**
- **Причина:** отсутствует `healthcheck`.
- **Риск:** снижение наблюдаемости и устойчивости.

**Дополнительно: контейнер registry.1.***
- **Причина:** сервис запущен с ослаблениями (нет лимитов, healthcheck, seccomp/AppArmor и т.д.).
- **Риск:** если атакующий доберётся до registry-сервиса, последствия - компрометация supply chain (подмена/выдача образов).

- [x] 6. Опишите влияния уязвимостей, их сценарий атаки

**6.1. Сценарий атаки "Container => Host" (побег из контейнера / захват хоста)**

**Условия:** `privileged + cap_add ALL + seccomp unconfined + pid: host + network_mode host` дают контейнеру почти хост-уровень.

**Сценарий:**
1. атакующий получает выполнение кода в `vulnerable-web`;
2. из-за `privileged` и расширенных capabilities он получает доступ к устройствам/ядру/монтированиям;
3. через уязвимости ядра или неправильные монтирования может закрепиться на хосте;
4. дальше - компрометация всех контейнеров и данных.

**6.2. Сценарий атаки через Docker socket (`/var/run/docker.sock`)**

**Условия:** в `vulnerable-web` проброшен сокет Docker: `- /var/run/docker.sock:/var/run/docker.sock`. Контейнер получает возможность обращаться к Docker API хоста.

**Сценарий:**
1. атакующий получает выполнение кода в `vulnerable-web` (RCE/команда в контейнере);
2. внутри контейнера обращается к Docker API через `/var/run/docker.sock` (например, с помощью `docker`/curl к API);
3. запускает новый контейнер с повышенными правами и монтированием файловой системы хоста (например, `/` в `/host`);
4. читает/изменяет файлы хоста (ssh-ключи, конфиги, учётные данные), добавляет постоянный доступ;
5. получает полный контроль над хостом и всеми контейнерами (просмотр других томов, сетей, образов, секретов).

**6.3. Сценарий DoS из-за отсутствия лимитов ресурсов**

**Условия:** у контейнеров `vulnerable-web` и `registry.1.*` отсутствуют ограничения CPU/RAM/PIDs. Хост ограничивает только "физическая" мощность и настройки ОС.

**Сценарий:**
1. атакующий получает возможность запускать команды внутри контейнера (RCE, shell, уязвимый endpoint);
2. запускает нагрузку: массовое создание процессов (fork bomb), бесконечные вычисления, выделение памяти, активную запись на диск;
3. контейнер начинает потреблять непропорционально много ресурсов (CPU/RAM/PIDs/IO), вытесняя другие сервисы;
4. на хосте возникают симптомы: OOM-killer, зависания, невозможность создать новые процессы, деградация сети/диска;
5. сервисы контейнеров становятся недоступны, стенд частично/полностью падает => отказ в обслуживании.

**6.4. Supply-chain риск из-за EOL образов**

**Условия:** используется образ с EOL-базой (Trivy: `alpine 3.8.2` в `docker/docker-bench-security`). Для EOL дистрибутива часть CVE остаётся непатченной.

**Сценарий:**
1. в инфраструктуре используется образ на базе устаревшего (EOL) дистрибутива, где известные уязвимости не закрываются обновлениями;
2. атакующий находит способ взаимодействовать с компонентом внутри контейнера (сервис/утилита/библиотека) или добивается выполнения кода (через уязвимость приложения, небезопасный скрипт, цепочку зависимостей);
3. эксплуатирует известную уязвимость в системном пакете/библиотеке, для которой уже есть публичный эксплойт, но патчей для EOL-ветки нет;
4. получает повышение привилегий внутри контейнера, доступ к данным/конфигам, возможность закрепления;
5. при наличии дополнительных ослаблений (privileged, docker.sock, host namespaces) сценарий развивается до компрометации хоста/других контейнеров.

- [x] 7. Оцените риски ИБ и предложите меры для их снижения: 
> - Следует разобрать `.yaml` описав, что в них считается не безопасным и почему
> - Опишите сценарии реализации рисков CR, DL
> - Предложили исправленные `.yaml`

**7.1. Разбор `docker-compose.yaml`**

**1) База данных опубликована наружу**

```yaml
insecure-db:
  ports:
    - "5432:5432"
```

- **Почему небезопасно:** база становится доступна с хоста/внешней сети, что увеличивает поверхность атаки (подбор пароля, эксплуатация уязвимостей Postgres, утечки).
- **Риск:** **DL высокий** (утечка данных БД при доступе извне), **CR средний** (через доступ к БД можно развить атаку на приложение/учётки).

**2) Слабые/предсказуемые учётные данные БД**

```yaml
- POSTGRES_PASSWORD=root
- POSTGRES_USER=vulnuser
- DB_URL=postgresql://vulnuser:root@insecure-db:5432/vulnapp
```

- **Почему небезопасно:** секреты в открытом виде (утечки через git, `docker inspect`, логи), слабый пароль.
- **Риск:** **DL высокий** (прямой доступ к данным), **CR средний** (компрометация БД даёт плацдарм для дальнейших атак на сервисы).

**3) Секреты и флаги в переменных окружения**

```yaml
- APP_SECRET_KEY=hardcoded-in-env
```

- **Почему небезопасно:** env читается через `docker inspect`, может попадать в логи/дампы, хранится в compose/репозитории. Это прямой канал утечки.
-  **Риск:** **DL высокий** (утечка ключей/токенов), **CR средний/высокий** (секреты могут использоваться для подписи cookie/JWT/сессий => захват админки/выполнение действий)

**4) DEBUG=true**

```yaml
- DEBUG=true
```

- **Почему небезопасно:** debug-режим часто раскрывает стек-трейсы, конфиги, окружение, иногда включает интерактивный дебаггер => повышает риск RCE/утечек.
- **Риск:** **DL высокий** (выдача конфигов/переменных/трассировок), **CR средний/высокий** (в ряде фреймворков debug может привести к RCE/обходу аутентификации)

**5) RW bind-mount кода приложения**

```yaml
volumes:   
  - ./app:/app:rw
```

- **Почему небезопасно:** при компрометации контейнера атакующий может менять файлы на хосте в каталоге проекта (подмена кода, закладки), что бьёт по целостности и может привести к компрометации окружения разработчика.
- **Риск:** **CR высокий** (закладка/персистентность через изменение кода на хосте), **DL средний** (утечка исходников/конфигов)

**6) Нет ограничений ресурсов / healthcheck**

- **Почему небезопасно:** без лимитов CPU/RAM/PIDs контейнер может "съесть" ресурсы и положить хост; без healthcheck труднее мониторинг.
- **CR низкий/средний** (напрямую не даёт root, но облегчает атаки через деградацию/хаос), **DL низкий** (косвенно).

**7) Порты опубликованы на всех интерфейсах**

`- "8080:80" - "5001:5000"`

- **Почему небезопасно:** сервисы доступны из сети (если VM/хост в bridged/host-only и т.д.).
- **Риск:** **DL средний/высокий** (доступ к API/вебу извне), **CR средний** (удалённая эксплуатация уязвимостей приложения становится возможной)

Исправленный `docker-compose.yaml`:

```yaml
version: "3.8"

services:
  web:
    image: nginx:alpine
    container_name: web
    depends_on:
      - app
    ports:
      - "127.0.0.1:8080:80"
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    read_only: true
    tmpfs:
      - /tmp
      - /run
    user: "nginx"
    networks:
      - front_net
      - back_net
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://localhost/ >/dev/null 2>&1 || exit 1"]
      interval: 30s
      timeout: 5s
      retries: 3

  db:
    image: postgres:16-alpine
    container_name: db
    environment:
      POSTGRES_DB: vulnapp
      POSTGRES_USER: vulnuser
      POSTGRES_PASSWORD: "${POSTGRES_PASSWORD}"
    volumes:
      - db_data:/var/lib/postgresql/data
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    networks:
      - back_net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U vulnuser -d vulnapp || exit 1"]
      interval: 10s
      timeout: 5s
      retries: 5

  app:
    image: python:3.11-alpine
    container_name: app
    depends_on:
      - db
    working_dir: /app
    volumes:
      - ./app:/app:ro
    command: ["python", "app.py"]
    environment:
      APP_SECRET_KEY: "${APP_SECRET_KEY}"
      DB_HOST: "db"
      DB_NAME: "vulnapp"
      DB_USER: "vulnuser"
      DB_PASSWORD: "${POSTGRES_PASSWORD}"
      DEBUG: "false"
    ports:
      - "127.0.0.1:5001:5000"
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    read_only: true
    tmpfs:
      - /tmp
      - /run
    pids_limit: 200
    mem_limit: 512m
    cpus: 0.5
    networks:
      - back_net
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://localhost:5000/health >/dev/null 2>&1 || exit 1"]
      interval: 30s
      timeout: 5s
      retries: 3

volumes:
  db_data:

networks:
  front_net:
    driver: bridge
  back_net:
    driver: bridge
```

**Что исправлено:**
- БД не торчит наружу, секреты вынесены в переменные `${...}`, DEBUG выключен.
- RW bind-mount кода заменён на `:ro`.
- Добавлены hardening (`cap_drop ALL`, `read_only`, `tmpfs`, `no-new-privileges`), healthcheck, лимиты ресурсов.

**7.2. Разбор `vulnerable-app.yml`**

**1) `privileged: true`**

- **Почему небезопасно:** контейнер получает почти хост-уровень привилегий (доступ к устройствам, расширенные права).
- **Риск:** **CR критический** (вероятен выход на хост при любом RCE), **DL высокий** (доступ к данным/томам/файлам),

**2) `network_mode: host` и `pid: host`**

- **Почему небезопасно:** исчезает изоляция сети и процессов => контейнер “видит” хост как свою среду.
- **Риск:** **CR высокий** (упрощается атака на хостовые сервисы/процессы), **DL высокий** (перехват/доступ к локальным сервисам, разведка)

**3) `user: "0:0"`**

- **Почему небезопасно:** процессы внутри контейнера идут от root.
- **Риск:** **CR высокий** (любой RCE сразу даёт root в контейнере => легче развить атаку на хост), **DL высокий** (доступ к секретам/файлам внутри контейнера)

**4) Проброс `/` хоста и docker.sock**

```yaml
volumes:
  - /:/hostroot:rw
  - /var/run/docker.sock:/var/run/docker.sock
```

- **Почему небезопасно:** `/hostroot` = прямой доступ к файловой системе хоста на запись; docker.sock = доступ к Docker API хоста (почти root).
- **Риск:** **CR критический** (прямая компрометация хоста), **DL критический** (чтение любых файлов хоста/секретов/БД)

**5) `cap_add: [ALL]`**

- **Почему небезопасно:** выдаются все Linux capabilities => обход ограничений, усиление атак.
- **Риск:** **CR высокий/критический** (почти superuser поведение), **DL высокий** (расширение доступа)

**6) `apparmor:unconfined` и `seccomp:unconfined`**

- **Почему небезопасно:** отключаются ключевые барьеры (LSM и фильтрация syscalls).
- **Риск:** **CR высокий/критический** (проще эксплуатировать kernel/syscall техники), **DL высокий** (обход ограничений доступа),

**7) Секреты и "FLAG" в env + слабые логины**

```yaml
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
FLAG=FLAG{...}
```

- **Почему небезопасно:** утечка через `inspect`, логи, дампы; слабые учётки легко подбираются.
- **Риск:** **DL высокий/критический** (утечка секретов/флага/учёток), **CR высокий** (компрометация админки часто ведёт к выполнению кода)

**8) Команда установки пакетов при старте**

```yaml
apt-get update && apt-get install ...
```

- **Почему небезопасно:** ухудшает воспроизводимость, тянет пакеты на лету”, усложняет контроль supply-chain; плюс расширяет поверхность атаки внутри контейнера.
- **Риск:** **CR средний/высокий** (появляются инструменты для постэксплуатации), **DL средний** (инструменты могут облегчить сбор данных),

Исправленный `vulnerable-app.yml`:

```yaml
version: "3.8"

services:
  vulnerable-web:
    image: nginx:latest
    container_name: vulnerable-web
    depends_on:
      - app
    ports:
      - "127.0.0.1:8080:80"
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
    user: "nginx"
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    read_only: true
    tmpfs:
      - /tmp
      - /run
    networks:
      - front_net
      - back_net
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://localhost/ >/dev/null 2>&1 || exit 1"]
      interval: 30s
      timeout: 5s
      retries: 3

  db:
    image: postgres:16-alpine
    container_name: db
    environment:
      POSTGRES_DB: vulnapp
      POSTGRES_USER: vulnuser
      POSTGRES_PASSWORD: "${POSTGRES_PASSWORD}"
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - back_net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U vulnuser -d vulnapp || exit 1"]
      interval: 10s
      timeout: 5s
      retries: 5

  app:
    image: python:3.11-alpine
    container_name: app
    depends_on:
      - db
    working_dir: /app
    volumes:
      - ./app:/app:ro
    command: ["python", "app.py"]
    environment:
      ADMIN_USERNAME: "${ADMIN_USERNAME}"
      ADMIN_PASSWORD: "${ADMIN_PASSWORD}"
      DB_HOST: "db"
      DB_USER: "vulnuser"
      DB_PASSWORD: "${POSTGRES_PASSWORD}"
      DEBUG: "false"
    ports:
      - "127.0.0.1:5001:5000"
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    read_only: true
    tmpfs:
      - /tmp
      - /run
    pids_limit: 200
    mem_limit: 512m
    cpus: 0.5
    networks:
      - back_net

  debug-shell:
    image: alpine:latest
    container_name: debug-shell
    command: ["sh", "-c", "sleep infinity"]
    networks:
      - back_net
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    read_only: true
    tmpfs:
      - /tmp
      - /run

volumes:
  db_data:

networks:
  front_net:
    driver: bridge
  back_net:
    driver: bridge
```

**Что исправлено:**
- убраны `privileged`, `network_mode: host`, `pid: host`;
- убраны `/hostroot:rw` и `/var/run/docker.sock`;
- убраны `cap_add: ALL`, `seccomp:unconfined`, `apparmor:unconfined`;
- убраны секреты/FLAG в явном виде (теперь берутся из `.env`);
- debug оставлен только как “контейнер для exec”, без SSH, без root-логина.

- [x] 8. Сделайте анализ уязвимостей из сгенерированных файлов .odt, .xslx и опишите их в отчете. Файлы конвертируются в эти директории

```bash
"├── json/          (Trivy JSON outputs)"
"├── text/          (CIS audit text outputs)"
"├── xlsx/          (Excel spreadsheets)"
"└── odt/           (OpenDocument Text files)"
```

По результатам анализа `.xlsx` получены следующие итоги.

1) **`docker-bench-security-trivy.xlsx`**

| Target                                             | Type   | FindingType   | ID             | Severity | Status | Title                                                                      |
| -------------------------------------------------- | ------ | ------------- | -------------- | -------- | ------ | -------------------------------------------------------------------------- |
| docker/docker-bench-security:latest (alpine 3.8.2) | alpine | vulnerability | CVE-2019-9893  | CRITICAL | fixed  | libseccomp: incorrect generation of syscall filters in libseccomp          |
| docker/docker-bench-security:latest (alpine 3.8.2) | alpine | vulnerability | CVE-2019-14697 | CRITICAL | fixed  | musl libc through 1.1.23 has an x87 floating-point stack adjustment im ... |
| docker/docker-bench-security:latest (alpine 3.8.2) | alpine | vulnerability | CVE-2019-14697 | CRITICAL | fixed  | musl libc through 1.1.23 has an x87 floating-point stack adjustment im ... |

**Анализ CVE:**
- **`CVE-2019-9893` (CRITICAL) - `libseccomp`** (ошибка генерации фильтров syscalls). **Решение:** Обновить на alpine 3.18+/3.19+,пересобрать (libseccomp обновится)
- **`CVE-2019-14697` (CRITICAL) - `musl libc`** (дисбаланс x87 floating-point stack adjustment в i386 math-ассемблере musl мог приводить к out-of-bounds write). **Решение:** Обновить на alpine 3.18+/3.19+, пересобрать(musl обновится)

Образ `docker-bench-security`- аудиторский инструмент, но он построен на старой базе (`alpine 3.8.2`). 

**Рекомендация:** не использовать этот образ как runtime-сервис и применять только как одноразовый аудит. Для production-сканирования - обновлённые инструменты/образы и регулярный Trivy в CI.

2) **`nginx-alpine-trivy.xlsx`**

На момент сканирования Trivy не зафиксировал уязвимости для состава пакетов/компонентов в этом образе.

3) **`postgres-16-alpine-trivy.xlsx`**

| Target             | Type     | FindingType   | ID             | Severity | Status | Title                                                                                                                 |
| ------------------ | -------- | ------------- | -------------- | -------- | ------ | --------------------------------------------------------------------------------------------------------------------- |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-58183 | HIGH     | fixed  | golang: archive/tar: Unbounded allocation when parsing GNU sparse map                                                 |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-61729 | HIGH     | fixed  | crypto/x509: Excessive resource consumption when printing error string for host certificate validation in crypto/x509 |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-47912 | MEDIUM   | fixed  | net/url: Insufficient validation of bracketed IPv6 hostnames in net/url                                               |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-58185 | MEDIUM   | fixed  | encoding/asn1: Parsing DER payload can cause memory exhaustion in encoding/asn1                                       |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-58186 | MEDIUM   | fixed  | golang.org/net/http: Lack of limit when parsing cookies can cause memory exhaustion in net/http                       |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-58187 | MEDIUM   | fixed  | crypto/x509: Quadratic complexity when checking name constraints in crypto/x509                                       |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-58188 | MEDIUM   | fixed  | crypto/x509: golang: Panic when validating certificates with DSA public keys in crypto/x509                           |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-58189 | MEDIUM   | fixed  | crypto/tls: go crypto/tls ALPN negotiation error contains attacker controlled information                             |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-61723 | MEDIUM   | fixed  | encoding/pem: Quadratic complexity when parsing some invalid inputs in encoding/pem                                   |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-61724 | MEDIUM   | fixed  | net/textproto: Excessive CPU consumption in Reader.ReadResponse in net/textproto                                      |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-61725 | MEDIUM   | fixed  | net/mail: Excessive CPU consumption in ParseAddress in net/mail                                                       |
| usr/local/bin/gosu | gobinary | vulnerability | CVE-2025-61727 | MEDIUM   | fixed  | golang: crypto/x509: excluded subdomain constraint does not restrict wildcard SANs                                    |


Все находки относятся к цели `usr/local/bin/gosu` и типу `gobinary`. Это значит, что Trivy нашёл уязвимости в Go-бинарнике (gosu), который присутствует внутри образа.

- **CVE-2025-58183 (HIGH) - `archive/tar`: unbounded allocation (GNU sparse map)**: `tar.Reader` не ограничивал число sparse-регионов в GNU tar pax sparse => атакующий tar может вызвать неограниченные аллокации памяти. **Решение:** обновить компонент/образ до версии с фиксом.
- **CVE-2025-61729 (HIGH) - `crypto/x509`: excessive resource consumption при формировании ошибки HostnameError**: при построении строки ошибки `HostnameError.Error()` нет лимита на число хостов + конкатенация приводит к квадратичной сложности => сертификат злоумышленника может вызвать чрезмерное потребление ресурсов.  **Решение:** обновление Go runtime/пересборка компонента.
- **CVE-2025-47912 (MEDIUM) - `net/url`: неправильная валидация “IPv6 в скобках”**: `Parse` позволял класть не IPv6 значения в квадратные скобки в host-части URL, хотя по RFC так можно только IPv6.  **Решение:** обновить компонент; не строить security-решения только на “строковой” проверке URL.
- **CVE-2025-58185 (MEDIUM) - `encoding/asn1`: DER parsing => memory exhaustion**: разбор специально сделанного DER мог приводить к большим аллокациям => истощение памяти. **Решение:** обновить.
- **CVE-2025-58186 (MEDIUM) - `net/http`: cookies parsing без лимита**: несмотря на лимит размера заголовков, число cookie не было ограничено => много маленьких cookie вызывает большие аллокации структур => memory DoS. **Решение:** обновление + лимиты ресурсов/рейт-лимит на входе.
- **CVE-2025-58187 (MEDIUM) - `crypto/x509`: quadratic complexity при проверке name constraints**: алгоритм проверки name constraints имеет нелинейную (квадратичную) сложность на некоторых входах => CPU DoS при валидации цепочек сертификатов.  **Решение:** обновить; ставить таймауты/ограничения на TLS-рукопожатия.
- **CVE-2025-58188 (MEDIUM) - `crypto/x509`: panic при DSA public keys**: валидация цепочек с DSA-ключами могла приводить к **panic** из-за неверного предположения про `Equal` => удалённый краш. **Решение:** обновить.
- **CVE-2025-58189 (MEDIUM) - `crypto/tls`: ALPN error содержит attacker-controlled данные без escaping**: при провале handshake на этапе ALPN ошибка может включать протоколы, присланные клиентом, без экранирования => риск log injection/подмены логов управляющими символами. **Решение:** обновить; дополнительно - нормализовать/экранировать строки при логировании TLS ошибок.
- **CVE-2025-61723 (MEDIUM) - `encoding/pem`: quadratic complexity на невалидных входах**: разбор некоторых невалидных PEM может быть квадратичным по времени => CPU DoS. **Решение:** обновить; лимитировать размер входных PEM/таймауты.
- **CVE-2025-61724 (MEDIUM) - `net/textproto`: Reader.ReadResponse CPU DoS**: `ReadResponse` строил строку ответа через повторную конкатенацию строк => при большом числе строк **сильный рост CPU**. **Решение:** обновить.
- **CVE-2025-61725 (MEDIUM) - `net/mail`: ParseAddress CPU DoS**: при разборе domain-literal частей адреса использовалась повторная конкатенация => на больших входах **CPU DoS**. **Решение:** обновить.
- **CVE-2025-61727 (MEDIUM) - `crypto/x509`: excluded subdomain constraint не ограничивает wildcard SAN**: исключающее ограничение поддомена (name constraints) могло **не запрещать** wildcard SAN в leaf-сертификате (пример: исключили `test.example.com`, но `*.example.com` всё равно проходит). **Решение:** обновить.

Даже официальные образы могут содержать уязвимые версии встроенных бинарников/библиотек. При этом поле `Status=fixed` означает, что существует версия с исправлением, поэтому решение обычно сводится к обновлению тега образа.

**Рекомендация:** обновить `postgres:16-alpine` до более свежего патч-релиза (или перейти на `-bookworm`/`-bullseye`, если политика допускает), пересканировать.

4) **`python-3.11-alpine-trivy.xlsx`**

| Target | Type       | FindingType   | ID            | Severity | Status | Title                                               |
| ------ | ---------- | ------------- | ------------- | -------- | ------ | --------------------------------------------------- |
| Python | python-pkg | vulnerability | CVE-2025-8869 | MEDIUM   | fixed  | pip: pip missing checks on symbolic link extraction |

**`CVE-2025-8869` (MEDIUM) - pip (tar extraction + symlinks).** При распаковке tar-архива pip может недостаточно проверять symlink, указывающий вне директории распаковки, если используемый модуль/рантайм не даёт "безопасную" реализацию (контекст вокруг PEP 706).

Уязвимости в пакетных менеджерах/инструментах сборки могут быть использованы для атак через цепочку поставки (подмена/извлечение файлов при установке пакетов).

**Рекомендация:** обновить `pip`/зависимости при сборке образа.
   
- [x] 9. Подготовьте отчет `gist`.
- [x] 10. Почистите кеш от `venv` и остановите уязвимостей приложение, почистите контейнера

```bash
$ rm -rf venv
$ docker-compose -f demo-vulnerable-app.yml down
$ docker system prune -ls
```
 
 ***
 
Copyright (c) 2025 Svetlana Poddoskina