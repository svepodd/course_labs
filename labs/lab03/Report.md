<div align="center">
<h1><a id="intro">Лабораторная работа №3</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Поддоскина С. К.-8b9aff" alt="Contributor Badge"></a></div>


- [x] 1. Опишите используемые методы по их назначению, как они функционируют и какие результаты могут дать для оценки. Используйте сноску из материалов выше по флагам команд.

| Метод                                        | Описание                                                                                                                                                                                                     |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **TCP Connect scan <br>(`-sT`)**             | Полное установление TCP-соединения, nmap выполняет полный TCP-handshake (SYN → SYN/ACK → ACK). Надёжно, но более заметно (полный handshake фиксируется сервисом/логами).                                     |
| **TCP SYN scan <br>(`-sS`)**                 | Отправляется SYN и анализируется ответ (SYN/ACK → порт открыт; RST → закрыт). Соединение обычно не завершается до конца (нет финального ACK), поэтому способ менее шумный.                                   |
| **UDP scan<br>(`-sU`)**                      | UDP-порты сложнее диагностировать: часто тишина означает либо фильтрацию, либо **open\|filtered**. Для уточнения Nmap смотрит ICMP Port Unreachable и поведение сервиса.                                     |
| **FIN (`-sF`), NULL (`-sN`), Xmas (`-sX`)**  | Нетипичные TCP-флаги для обхода простых фильтров. Исторически могли помогать отличать open/closed по реакции стека, но сегодня результаты часто **open\|filtered** из-за файрволов/IDS.                      |
| **ACK scan (`-sA`)**                         | Не определяет open/closed напрямую. Используется для понимания, есть ли фильтрация (stateful firewall): ответы RST обычно трактуются как unfiltered.                                                         |
| **ICMP ping / ping-scan <br>(`-sn`, `-sP`)** | Определение живых хостов (host discovery) без сканирования портов.                                                                                                                                           |
| **Idle scan (`-sI`)**                        | Невидимое сканирование через "зомби"-хост с предсказуемым IPID. Позволяет скрыть реальный источник сканирования, но требует специфических условий и корректного выбора "зомби".                              |
| **FTP-proxy scan (`-b`)**                    | Сканирование через FTP bounce (устаревающая техника): если FTP-сервер позволяет PORT-команды к третьим хостам, можно проксировать сканирование. На практике редко встречается из-за современных ограничений. |

- [x] 2. Выведите на терминале и проанализируйте следующие команды консоли

Базовое сканирование TCP-портов:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ nmap localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 00:50 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00016s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE
631/tcp  open  ipp
5000/tcp open  upnp

Nmap done: 1 IP address (1 host up) scanned in 0.05 seconds
```

Запуск стандартного набора NSE-скриптов:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ nmap -sC localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 00:58 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000077s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE
631/tcp  open  ipp
| http-robots.txt: 1 disallowed entry 
|_/
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=svepodd-VirtualBox/organizationName=svepodd-VirtualBox/stateOrProvinceName=Unknown/countryName=US
| Subject Alternative Name: DNS:svepodd-VirtualBox, DNS:svepodd-VirtualBox.local, DNS:localhost
| Not valid before: 2025-12-14T21:58:42
|_Not valid after:  2035-12-12T21:58:42
|_http-title: Home - CUPS 2.4.7
5000/tcp open  upnp

Nmap done: 1 IP address (1 host up) scanned in 1.94 seconds
```

По порту 631 получены дополнительные сведения (включая заголовок web-интерфейса CUPS и информацию TLS-сертификата).

 Опция `-p` ожидает номера портов или сервисы, кторые необходимо просканировать:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ nmap -p localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 01:01 MSK
Found no matches for the service mask 'localhost' and your specified protocols
QUITTING!
```

Команда `nmap -O localhost` без `sudo` корректно завершилась сообщением о необходимости root-привилегий для OS fingerprinting:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ nmap -O localhost
TCP/IP fingerprinting (for OS scan) requires root privileges.
QUITTING!
```

Cкан 80 порта:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ nmap -p 80 localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 01:02 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000081s latency).

PORT   STATE  SERVICE
80/tcp closed http

Nmap done: 1 IP address (1 host up) scanned in 0.04 seconds
```

Cкан 443 порта:
```bash
svepodd@svepodd-VirtualBox:~/lab01$ nmap -p 443 localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 01:02 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000075s latency).

PORT    STATE  SERVICE
443/tcp closed https

Nmap done: 1 IP address (1 host up) scanned in 0.04 seconds
```

Cкан 8443 порта:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ nmap -p 8443 localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 01:02 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000077s latency).

PORT     STATE  SERVICE
8443/tcp closed https-alt

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds
```

Командой `nmap -p "*" localhost` выполнен перебор большого диапазона портов, и дополнительно обнаружен **2377/tcp (swarm)**, что типично для Docker Swarm manager-port:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ nmap -p "*" localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 01:03 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000069s latency).
Not shown: 8365 closed tcp ports (conn-refused)
PORT     STATE SERVICE
631/tcp  open  ipp
2377/tcp open  swarm
5000/tcp open  upnp

Nmap done: 1 IP address (1 host up) scanned in 0.27 seconds
```

Командой `nmap -sV -p 22,8080 localhost` проверены типичные порты SSH/HTTP-proxy — оба закрыты:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ nmap -sV -p 22,8080 localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 01:05 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00022s latency).

PORT     STATE  SERVICE    VERSION
22/tcp   closed ssh
8080/tcp closed http-proxy

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.35 seconds
```

Выполнен ping-scan подсети: `nmap -sP 10.238.179.0/24` (аналог современного `-sn`). Найдены 4 активных узла (включая шлюз и VM):

```bash
svepodd@svepodd-VirtualBox:~$ nmap -sP 10.238.179.0/24
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 17:25 MSK
Nmap scan report for 10.238.179.1
Host is up (0.079s latency).
Nmap scan report for svepodd-VirtualBox (10.238.179.78)
Host is up (0.0018s latency).
Nmap scan report for _gateway (10.238.179.240)
Host is up (0.0062s latency).
Nmap scan report for 10.238.179.250
Host is up (2.9s latency).
Nmap done: 256 IP addresses (4 hosts up) scanned in 16.37 seconds
```

Для хоста `10.238.179.1` применено `nmap --open`, выявлены открытые порты 135, 139, 445, 5357 (характерно для Windows-служб: RPC/NetBIOS/SMB/WSD):

```bash
svepodd@svepodd-VirtualBox:~$ nmap --open 10.238.179.1 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 17:26 MSK
Nmap scan report for 10.238.179.1
Host is up (0.064s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
5357/tcp open  wsdapi

Nmap done: 1 IP address (1 host up) scanned in 1.75 seconds
```

Для `10.238.179.1` и `scanme.nmap.org` использован `--packet-trace`, что позволило увидеть попытки соединений к множеству портов и ответы (refused/no-response), а также DNS-резолвинг целей

```bash
svepodd@svepodd-VirtualBox:~$ nmap --packet-trace 10.238.179.1 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 17:26 MSK
CONN (0.0765s) TCP localhost > 10.238.179.1:80 => Operation now in progress
CONN (0.0773s) TCP localhost > 10.238.179.1:443 => Operation now in progress
CONN (0.2045s) TCP localhost > 10.238.179.1:80 => Connection refused
NSOCK INFO [0.2040s] nsock_iod_new2(): nsock_iod_new (IOD #1)
NSOCK INFO [0.2040s] nsock_connect_udp(): UDP connection requested to 127.0.0.53:53 (IOD #1) EID 8
NSOCK INFO [0.2040s] nsock_read(): Read request from IOD #1 [127.0.0.53:53] (timeout: -1ms) EID 18
NSOCK INFO [0.2040s] nsock_write(): Write request for 43 bytes to IOD #1 EID 27 [127.0.0.53:53]
NSOCK INFO [0.2040s] nsock_trace_handler_callback(): Callback: CONNECT SUCCESS for EID 8 [127.0.0.53:53]
NSOCK INFO [0.2040s] nsock_trace_handler_callback(): Callback: WRITE SUCCESS for EID 27 [127.0.0.53:53]
NSOCK INFO [0.2210s] nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 18 [127.0.0.53:53] (43 bytes): .............1.179.238.10.in-addr.arpa.....
NSOCK INFO [0.2210s] nsock_read(): Read request from IOD #1 [127.0.0.53:53] (timeout: -1ms) EID 34
NSOCK INFO [0.2210s] nsock_iod_delete(): nsock_iod_delete (IOD #1)
NSOCK INFO [0.2210s] nevent_delete(): nevent_delete on event #34 (type READ)
CONN (0.2223s) TCP localhost > 10.238.179.1:5900 => Operation now in progress
CONN (0.2226s) TCP localhost > 10.238.179.1:113 => Operation now in progress
CONN (0.2228s) TCP localhost > 10.238.179.1:111 => Operation now in progress
CONN (0.2231s) TCP localhost > 10.238.179.1:3389 => Operation now in progress
CONN (0.2234s) TCP localhost > 10.238.179.1:443 => Operation now in progress
CONN (0.2236s) TCP localhost > 10.238.179.1:1723 => Operation now in progress
CONN (0.2432s) TCP localhost > 10.238.179.1:587 => Operation now in progress
CONN (0.2486s) TCP localhost > 10.238.179.1:110 => Operation now in progress
CONN (0.2490s) TCP localhost > 10.238.179.1:3306 => Operation now in progress
CONN (0.2494s) TCP localhost > 10.238.179.1:21 => Operation now in progress
CONN (0.2495s) TCP localhost > 10.238.179.1:5900 => Connection refused
CONN (0.2495s) TCP localhost > 10.238.179.1:113 => Connection refused
CONN (0.2495s) TCP localhost > 10.238.179.1:111 => Connection refused
CONN (0.2495s) TCP localhost > 10.238.179.1:3389 => Connection refused
CONN (0.2495s) TCP localhost > 10.238.179.1:443 => Connection refused
CONN (0.2495s) TCP localhost > 10.238.179.1:1723 => Connection refused
CONN (0.2495s) TCP localhost > 10.238.179.1:587 => Connection refused
CONN (0.2499s) TCP localhost > 10.238.179.1:80 => Operation now in progress
...
CONN (1.5526s) TCP localhost > 10.238.179.1:19 => Connection refused
CONN (1.5526s) TCP localhost > 10.238.179.1:389 => Connection refused
CONN (1.5526s) TCP localhost > 10.238.179.1:1185 => Connection refused
CONN (1.5526s) TCP localhost > 10.238.179.1:1021 => Connection refused
CONN (1.5526s) TCP localhost > 10.238.179.1:24 => Connection refused
CONN (1.5526s) TCP localhost > 10.238.179.1:5004 => Connection refused
CONN (1.5526s) TCP localhost > 10.238.179.1:2003 => Connection refused
CONN (1.5526s) TCP localhost > 10.238.179.1:7025 => Connection refused
CONN (1.5526s) TCP localhost > 10.238.179.1:49400 => Connection refused
CONN (1.5526s) TCP localhost > 10.238.179.1:2492 => Connection refused
CONN (1.5526s) TCP localhost > 10.238.179.1:2038 => Connection refused
Nmap scan report for 10.238.179.1
Host is up (0.034s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
5357/tcp open  wsdapi

Nmap done: 1 IP address (1 host up) scanned in 1.55 seconds
```

Это иллюстрирует, как Nmap строит картину портов на основе сетевых реакций.

```bash
svepodd@svepodd-VirtualBox:~$ nmap --packet-trace scanme.nmap.org
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 17:27 MSK
CONN (5.2283s) TCP localhost > 45.33.32.156:80 => Operation now in progress
CONN (5.2299s) TCP localhost > 45.33.32.156:443 => Operation now in progress
CONN (5.4492s) TCP localhost > 45.33.32.156:80 => Connected
NSOCK INFO [5.4510s] nsock_iod_new2(): nsock_iod_new (IOD #1)
NSOCK INFO [5.4510s] nsock_connect_udp(): UDP connection requested to 127.0.0.53:53 (IOD #1) EID 8
NSOCK INFO [5.4520s] nsock_read(): Read request from IOD #1 [127.0.0.53:53] (timeout: -1ms) EID 18
NSOCK INFO [5.4520s] nsock_write(): Write request for 43 bytes to IOD #1 EID 27 [127.0.0.53:53]
NSOCK INFO [5.4520s] nsock_trace_handler_callback(): Callback: CONNECT SUCCESS for EID 8 [127.0.0.53:53]
NSOCK INFO [5.4520s] nsock_trace_handler_callback(): Callback: WRITE SUCCESS for EID 27 [127.0.0.53:53]
NSOCK INFO [5.6200s] nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 18 [127.0.0.53:53] (72 bytes): .............156.32.33.45.in-addr.arpa..............,...scanme.nmap.org.
NSOCK INFO [5.6200s] nsock_read(): Read request from IOD #1 [127.0.0.53:53] (timeout: -1ms) EID 34
NSOCK INFO [5.6200s] nsock_iod_delete(): nsock_iod_delete (IOD #1)
NSOCK INFO [5.6200s] nevent_delete(): nevent_delete on event #34 (type READ)
CONN (5.6221s) TCP localhost > 45.33.32.156:445 => Operation now in progress
CONN (5.6224s) TCP localhost > 45.33.32.156:139 => Operation now in progress
CONN (5.6226s) TCP localhost > 45.33.32.156:53 => Operation now in progress
CONN (5.6228s) TCP localhost > 45.33.32.156:113 => Operation now in progress
CONN (5.6229s) TCP localhost > 45.33.32.156:587 => Operation now in progress
CONN (5.6230s) TCP localhost > 45.33.32.156:1025 => Operation now in progress
CONN (5.6231s) TCP localhost > 45.33.32.156:80 => Operation now in progress
CONN (5.6232s) TCP localhost > 45.33.32.156:1720 => Operation now in progress
CONN (5.6233s) TCP localhost > 45.33.32.156:443 => Operation now in progress
CONN (5.6234s) TCP localhost > 45.33.32.156:995 => Operation now in progress
CONN (5.8599s) TCP localhost > 45.33.32.156:80 => Connected
CONN (5.8679s) TCP localhost > 45.33.32.156:22 => Operation now in progress
CONN (5.8687s) TCP localhost > 45.33.32.156:8080 => Operation now in progress
CONN (6.1033s) TCP localhost > 45.33.32.156:22 => Connected
CONN (6.1035s) TCP localhost > 45.33.32.156:8888 => Operation now in progress
...
CONN (20.8941s) TCP localhost > 45.33.32.156:667 => Operation now in progress
CONN (20.8944s) TCP localhost > 45.33.32.156:5500 => Operation now in progress
CONN (20.8952s) TCP localhost > 45.33.32.156:5950 => Operation now in progress
CONN (20.8955s) TCP localhost > 45.33.32.156:1301 => Operation now in progress
CONN (20.8957s) TCP localhost > 45.33.32.156:2717 => Operation now in progress
CONN (20.8970s) TCP localhost > 45.33.32.156:54045 => Operation now in progress
CONN (20.8973s) TCP localhost > 45.33.32.156:4006 => Operation now in progress
CONN (20.8978s) TCP localhost > 45.33.32.156:7999 => Operation now in progress
CONN (20.8982s) TCP localhost > 45.33.32.156:5800 => Operation now in progress
CONN (20.8985s) TCP localhost > 45.33.32.156:1666 => Operation now in progress
CONN (20.8988s) TCP localhost > 45.33.32.156:1287 => Operation now in progress
CONN (20.8991s) TCP localhost > 45.33.32.156:5200 => Operation now in progress
CONN (20.8994s) TCP localhost > 45.33.32.156:6101 => Operation now in progress
CONN (20.8996s) TCP localhost > 45.33.32.156:10012 => Operation now in progress
CONN (20.8999s) TCP localhost > 45.33.32.156:2111 => Operation now in progress
CONN (20.9002s) TCP localhost > 45.33.32.156:19842 => Operation now in progress
CONN (20.9004s) TCP localhost > 45.33.32.156:3261 => Operation now in progress
CONN (20.9007s) TCP localhost > 45.33.32.156:12345 => Operation now in progress
CONN (20.9010s) TCP localhost > 45.33.32.156:3546 => Operation now in progress
CONN (20.9013s) TCP localhost > 45.33.32.156:28201 => Operation now in progress
CONN (20.9016s) TCP localhost > 45.33.32.156:38292 => Operation now in progress
CONN (20.9019s) TCP localhost > 45.33.32.156:3011 => Operation now in progress
CONN (20.9021s) TCP localhost > 45.33.32.156:20 => Operation now in progress
CONN (20.9024s) TCP localhost > 45.33.32.156:1040 => Operation now in progress
CONN (20.9027s) TCP localhost > 45.33.32.156:2190 => Operation now in progress
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.25s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 filtered tcp ports (no-response)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
9929/tcp  open  nping-echo
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 21.32 seconds
```

Топология сети:

```bash
svepodd@svepodd-VirtualBox:~$ nmap --iflist
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 17:28 MSK
************************INTERFACES************************
DEV             (SHORT)           IP/MASK                      TYPE     UP MTU   MAC
lo              (lo)              127.0.0.1/8                  loopback up 65536
lo              (lo)              ::1/128                      loopback up 65536
enp0s3          (enp0s3)          10.0.2.15/24                 ethernet up 1500  08:00:27:98:1D:AA
enp0s3          (enp0s3)          fe80::a00:27ff:fe98:1daa/64  ethernet up 1500  08:00:27:98:1D:AA
enp0s8          (enp0s8)          10.238.179.78/24             ethernet up 1500  08:00:27:18:11:F6
enp0s8          (enp0s8)          fe80::3f85:455e:3ca9:4eb6/64 ethernet up 1500  08:00:27:18:11:F6
docker0         (docker0)         172.17.0.1/16                ethernet up 1500  DE:B0:7F:97:B6:DA
docker_gwbridge (docker_gwbridge) 172.18.0.1/16                ethernet up 1500  96:06:A6:28:FA:2E
docker_gwbridge (docker_gwbridge) fe80::9406:a6ff:fe28:fa2e/64 ethernet up 1500  96:06:A6:28:FA:2E
veth9d66118     (veth9d66118)     (none)/0                     ethernet up 1500  76:D4:B5:CE:FF:1C
veth9d66118     (veth9d66118)     fe80::74d4:b5ff:fece:ff1c/64 ethernet up 1500  76:D4:B5:CE:FF:1C
vethdbdc338     (vethdbdc338)     (none)/0                     ethernet up 1500  12:09:72:2A:8F:FC
vethdbdc338     (vethdbdc338)     fe80::1009:72ff:fe2a:8ffc/64 ethernet up 1500  12:09:72:2A:8F:FC

**************************ROUTES**************************
DST/MASK                      DEV             METRIC GATEWAY
10.0.2.0/24                   enp0s3          100
10.238.179.0/24               enp0s8          101
172.17.0.0/16                 docker0         0
172.18.0.0/16                 docker_gwbridge 0
0.0.0.0/0                     enp0s3          100    10.0.2.2
0.0.0.0/0                     enp0s8          101    10.238.179.240
::1/128                       lo              0
fe80::a00:27ff:fe98:1daa/128  enp0s3          0
fe80::1009:72ff:fe2a:8ffc/128 vethdbdc338     0
fe80::3f85:455e:3ca9:4eb6/128 enp0s8          0
fe80::74d4:b5ff:fece:ff1c/128 veth9d66118     0
fe80::9406:a6ff:fe28:fa2e/128 docker_gwbridge 0
fe80::/64                     enp0s3          256
fe80::/64                     veth9d66118     256
fe80::/64                     docker_gwbridge 256
fe80::/64                     vethdbdc338     256
fe80::/64                     enp0s8          1024
ff00::/8                      enp0s3          256
ff00::/8                      enp0s8          256
ff00::/8                      veth9d66118     256
ff00::/8                      docker_gwbridge 256
ff00::/8                      vethdbdc338     256
```

Сканирование `scanme.nmap.org` показало открытые порты:

```bash
svepodd@svepodd-VirtualBox:~$ cat target.txt 
scanme.nmap.org

svepodd@svepodd-VirtualBox:~$ nmap -iL target.txt 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 17:58 MSK
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.23s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 filtered tcp ports (no-response)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
9929/tcp  open  nping-echo
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 15.92 seconds
```

Далее `nmap -A -iL target.txt` дало расширенную информацию: версии сервисов (OpenSSH, Apache), ключи SSH-hostkey, и "Service Info: OS: Linux".

```bash
svepodd@svepodd-VirtualBox:~$ nmap -A -iL target.txt 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 18:00 MSK
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.25s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 filtered tcp ports (no-response)
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)
|   2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)
|   256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)
|_  256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)
80/tcp    open  http       Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Go ahead and ScanMe!
|_http-favicon: Nmap Project
9929/tcp  open  nping-echo Nping echo
31337/tcp open  tcpwrapped
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.85 seconds
```

Команда `sudo nmap -sA scanme.nmap.org` (ACK scan) показала "unfiltered" (reset) для всех портов, что интерпретируется как отсутствие stateful-фильтрации по ACK-пакетам на пути.

```bash
svepodd@svepodd-VirtualBox:~$ sudo nmap -sA scanme.nmap.org
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 18:02 MSK
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.00022s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
All 1000 scanned ports on scanme.nmap.org (45.33.32.156) are in ignored states.
Not shown: 1000 unfiltered tcp ports (reset)

Nmap done: 1 IP address (1 host up) scanned in 0.33 seconds
```

Команда `nmap -PN scanme.nmap.org` отключает host discovery и считает хост "up", после чего выполняет сканирование портов:

```bash
svepodd@svepodd-VirtualBox:~$ nmap -PN scanme.nmap.org
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 18:09 MSK
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.25s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 filtered tcp ports (no-response)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
9929/tcp  open  nping-echo
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 17.30 seconds
```

Флаг `--script=vuln` в Nmap запускает набор NSE-скриптов (Nmap Scripting Engine), относящихся к категории `vuln` - то есть скрипты, которые проверяют хост на наличие конкретных известных уязвимостей.

Скрипт по открытым портам определил потенциальные уязвимости и проверил их реальное наличие на машине:

```bash
svepodd@svepodd-VirtualBox:~$ nmap --script=vuln 10.238.179.1 -vv
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 18:12 MSK
NSE: Loaded 105 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 18:12
Completed NSE at 18:12, 10.05s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating Ping Scan at 18:12
Scanning 10.238.179.1 [2 ports]
Completed Ping Scan at 18:12, 0.09s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 18:12
Completed Parallel DNS resolution of 1 host. at 18:12, 0.03s elapsed
Initiating Connect Scan at 18:12
Scanning 10.238.179.1 [1000 ports]
Discovered open port 135/tcp on 10.238.179.1
Discovered open port 445/tcp on 10.238.179.1
Discovered open port 139/tcp on 10.238.179.1
Discovered open port 5357/tcp on 10.238.179.1
Completed Connect Scan at 18:12, 1.58s elapsed (1000 total ports)
NSE: Script scanning 10.238.179.1.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 18:12
NSE: [tls-ticketbleed 10.238.179.1:139] Not running due to lack of privileges.
NSE: [firewall-bypass 10.238.179.1] lacks privileges.
Completed NSE at 18:12, 15.76s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Nmap scan report for 10.238.179.1
Host is up, received conn-refused (0.071s latency).
Scanned at 2025-12-15 18:12:23 MSK for 17s
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE      REASON
135/tcp  open  msrpc        syn-ack
139/tcp  open  netbios-ssn  syn-ack
445/tcp  open  microsoft-ds syn-ack
5357/tcp open  wsdapi       syn-ack

Host script results:
|_smb-vuln-ms10-054: false
|_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 27.69 seconds
```

Расширенная проверка уязвимостей шлюза. Флаг `-sV` раскрыл версии и типы сервисов:

```bash
svepodd@svepodd-VirtualBox:~$ nmap -sV --script=vuln -oN nmapres_new.txt localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 18:29 MSK
Stats: 0:08:14 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.48% done; ETC: 18:38 (0:00:12 remaining)
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000096s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
631/tcp  open  ipp     CUPS 2.4
| http-enum: 
|   /admin.php: Possible admin folder (401 Unauthorized)
|   /admin/: Possible admin folder (401 Unauthorized)
|   /admin/admin/: Possible admin folder (401 Unauthorized)
|   /administrator/: Possible admin folder (401 Unauthorized)
|   /adminarea/: Possible admin folder (401 Unauthorized)
|   /adminLogin/: Possible admin folder (401 Unauthorized)
|   /admin_area/: Possible admin folder (401 Unauthorized)
|   /administratorlogin/: Possible admin folder (401 Unauthorized)
|   /admin/account.php: Possible admin folder (401 Unauthorized)
|   /admin/index.php: Possible admin folder (401 Unauthorized)
|   /admin/login.php: Possible admin folder (401 Unauthorized)
|   /admin/admin.php: Possible admin folder (401 Unauthorized)
|   /admin_area/admin.php: Possible admin folder (401 Unauthorized)
|   /admin_area/login.php: Possible admin folder (401 Unauthorized)
|   /admin/index.html: Possible admin folder (401 Unauthorized)
|   /admin/login.html: Possible admin folder (401 Unauthorized)
|   /admin/admin.html: Possible admin folder (401 Unauthorized)
|   /admin_area/index.php: Possible admin folder (401 Unauthorized)
|   /admin/home.php: Possible admin folder (401 Unauthorized)
|   /admin_area/login.html: Possible admin folder (401 Unauthorized)
|   /admin_area/index.html: Possible admin folder (401 Unauthorized)
|   /admin/controlpanel.php: Possible admin folder (401 Unauthorized)
|   /admincp/: Possible admin folder (401 Unauthorized)
|   /admincp/index.asp: Possible admin folder (401 Unauthorized)
|   /admincp/index.html: Possible admin folder (401 Unauthorized)
|   /admincp/login.php: Possible admin folder (401 Unauthorized)
|   /admin/account.html: Possible admin folder (401 Unauthorized)
|   /adminpanel.html: Possible admin folder (401 Unauthorized)
|   /admin/admin_login.html: Possible admin folder (401 Unauthorized)
|   /admin_login.html: Possible admin folder (401 Unauthorized)
|   /admin/cp.php: Possible admin folder (401 Unauthorized)
|   /administrator/index.php: Possible admin folder (401 Unauthorized)
|   /administrator/login.php: Possible admin folder (401 Unauthorized)
|   /admin/admin_login.php: Possible admin folder (401 Unauthorized)
|   /admin_login.php: Possible admin folder (401 Unauthorized)
|   /administrator/account.php: Possible admin folder (401 Unauthorized)
|   /administrator.php: Possible admin folder (401 Unauthorized)
|   /admin_area/admin.html: Possible admin folder (401 Unauthorized)
|   /admin/admin-login.php: Possible admin folder (401 Unauthorized)
|   /admin-login.php: Possible admin folder (401 Unauthorized)
|   /admin/home.html: Possible admin folder (401 Unauthorized)
|   /admin/admin-login.html: Possible admin folder (401 Unauthorized)
|   /admin-login.html: Possible admin folder (401 Unauthorized)
|   /admincontrol.php: Possible admin folder (401 Unauthorized)
|   /admin/adminLogin.html: Possible admin folder (401 Unauthorized)
|   /adminLogin.html: Possible admin folder (401 Unauthorized)
|   /adminarea/index.html: Possible admin folder (401 Unauthorized)
|   /adminarea/admin.html: Possible admin folder (401 Unauthorized)
|   /admin/controlpanel.html: Possible admin folder (401 Unauthorized)
|   /admin.html: Possible admin folder (401 Unauthorized)
|   /admin/cp.html: Possible admin folder (401 Unauthorized)
|   /adminpanel.php: Possible admin folder (401 Unauthorized)
|   /administrator/index.html: Possible admin folder (401 Unauthorized)
|   /administrator/login.html: Possible admin folder (401 Unauthorized)
|   /administrator/account.html: Possible admin folder (401 Unauthorized)
|   /administrator.html: Possible admin folder (401 Unauthorized)
|   /adminarea/login.html: Possible admin folder (401 Unauthorized)
|   /admincontrol/login.html: Possible admin folder (401 Unauthorized)
|   /admincontrol.html: Possible admin folder (401 Unauthorized)
|   /adminLogin.php: Possible admin folder (401 Unauthorized)
|   /admin/adminLogin.php: Possible admin folder (401 Unauthorized)
|   /adminarea/index.php: Possible admin folder (401 Unauthorized)
|   /adminarea/admin.php: Possible admin folder (401 Unauthorized)
|   /adminarea/login.php: Possible admin folder (401 Unauthorized)
|   /admincontrol/login.php: Possible admin folder (401 Unauthorized)
|   /admin2.php: Possible admin folder (401 Unauthorized)
|   /admin2/login.php: Possible admin folder (401 Unauthorized)
|   /admin2/index.php: Possible admin folder (401 Unauthorized)
|   /administratorlogin.php: Possible admin folder (401 Unauthorized)
|   /admin/account.cfm: Possible admin folder (401 Unauthorized)
|   /admin/index.cfm: Possible admin folder (401 Unauthorized)
|   /admin/login.cfm: Possible admin folder (401 Unauthorized)
|   /admin/admin.cfm: Possible admin folder (401 Unauthorized)
|   /admin.cfm: Possible admin folder (401 Unauthorized)
|   /admin/admin_login.cfm: Possible admin folder (401 Unauthorized)
|   /admin_login.cfm: Possible admin folder (401 Unauthorized)
|   /adminpanel.cfm: Possible admin folder (401 Unauthorized)
|   /admin/controlpanel.cfm: Possible admin folder (401 Unauthorized)
|   /admincontrol.cfm: Possible admin folder (401 Unauthorized)
|   /admin/cp.cfm: Possible admin folder (401 Unauthorized)
|   /admincp/index.cfm: Possible admin folder (401 Unauthorized)
|   /admincp/login.cfm: Possible admin folder (401 Unauthorized)
|   /admin_area/admin.cfm: Possible admin folder (401 Unauthorized)
|   /admin_area/login.cfm: Possible admin folder (401 Unauthorized)
|   /administrator/login.cfm: Possible admin folder (401 Unauthorized)
|   /administratorlogin.cfm: Possible admin folder (401 Unauthorized)
|   /administrator.cfm: Possible admin folder (401 Unauthorized)
|   /administrator/account.cfm: Possible admin folder (401 Unauthorized)
|   /adminLogin.cfm: Possible admin folder (401 Unauthorized)
|   /admin2/index.cfm: Possible admin folder (401 Unauthorized)
|   /admin_area/index.cfm: Possible admin folder (401 Unauthorized)
|   /admin2/login.cfm: Possible admin folder (401 Unauthorized)
|   /admincontrol/login.cfm: Possible admin folder (401 Unauthorized)
|   /administrator/index.cfm: Possible admin folder (401 Unauthorized)
|   /adminarea/login.cfm: Possible admin folder (401 Unauthorized)
|   /adminarea/admin.cfm: Possible admin folder (401 Unauthorized)
|   /adminarea/index.cfm: Possible admin folder (401 Unauthorized)
|   /admin/adminLogin.cfm: Possible admin folder (401 Unauthorized)
|   /admin-login.cfm: Possible admin folder (401 Unauthorized)
|   /admin/admin-login.cfm: Possible admin folder (401 Unauthorized)
|   /admin/home.cfm: Possible admin folder (401 Unauthorized)
|   /admin/account.asp: Possible admin folder (401 Unauthorized)
|   /admin/index.asp: Possible admin folder (401 Unauthorized)
|   /admin/login.asp: Possible admin folder (401 Unauthorized)
|   /admin/admin.asp: Possible admin folder (401 Unauthorized)
|   /admin_area/admin.asp: Possible admin folder (401 Unauthorized)
|   /admin_area/login.asp: Possible admin folder (401 Unauthorized)
|   /admin_area/index.asp: Possible admin folder (401 Unauthorized)
|   /admin/home.asp: Possible admin folder (401 Unauthorized)
|   /admin/controlpanel.asp: Possible admin folder (401 Unauthorized)
|   /admin.asp: Possible admin folder (401 Unauthorized)
|   /admin/admin-login.asp: Possible admin folder (401 Unauthorized)
|   /admin-login.asp: Possible admin folder (401 Unauthorized)
|   /admin/cp.asp: Possible admin folder (401 Unauthorized)
|   /administrator/account.asp: Possible admin folder (401 Unauthorized)
|   /administrator.asp: Possible admin folder (401 Unauthorized)
|   /administrator/login.asp: Possible admin folder (401 Unauthorized)
|   /admincp/login.asp: Possible admin folder (401 Unauthorized)
|   /admincontrol.asp: Possible admin folder (401 Unauthorized)
|   /adminpanel.asp: Possible admin folder (401 Unauthorized)
|   /admin/admin_login.asp: Possible admin folder (401 Unauthorized)
|   /admin_login.asp: Possible admin folder (401 Unauthorized)
|   /adminLogin.asp: Possible admin folder (401 Unauthorized)
|   /admin/adminLogin.asp: Possible admin folder (401 Unauthorized)
|   /adminarea/index.asp: Possible admin folder (401 Unauthorized)
|   /adminarea/admin.asp: Possible admin folder (401 Unauthorized)
|   /adminarea/login.asp: Possible admin folder (401 Unauthorized)
|   /administrator/index.asp: Possible admin folder (401 Unauthorized)
|   /admincontrol/login.asp: Possible admin folder (401 Unauthorized)
|   /admin2.asp: Possible admin folder (401 Unauthorized)
|   /admin2/login.asp: Possible admin folder (401 Unauthorized)
|   /admin2/index.asp: Possible admin folder (401 Unauthorized)
|   /administratorlogin.asp: Possible admin folder (401 Unauthorized)
|   /admin/account.aspx: Possible admin folder (401 Unauthorized)
|   /admin/index.aspx: Possible admin folder (401 Unauthorized)
|   /admin/login.aspx: Possible admin folder (401 Unauthorized)
|   /admin/admin.aspx: Possible admin folder (401 Unauthorized)
|   /admin_area/admin.aspx: Possible admin folder (401 Unauthorized)
|   /admin_area/login.aspx: Possible admin folder (401 Unauthorized)
|   /admin_area/index.aspx: Possible admin folder (401 Unauthorized)
|   /admin/home.aspx: Possible admin folder (401 Unauthorized)
|   /admin/controlpanel.aspx: Possible admin folder (401 Unauthorized)
|   /admin.aspx: Possible admin folder (401 Unauthorized)
|   /admin/admin-login.aspx: Possible admin folder (401 Unauthorized)
|   /admin-login.aspx: Possible admin folder (401 Unauthorized)
|   /admin/cp.aspx: Possible admin folder (401 Unauthorized)
|   /administrator/account.aspx: Possible admin folder (401 Unauthorized)
|   /administrator.aspx: Possible admin folder (401 Unauthorized)
|   /administrator/login.aspx: Possible admin folder (401 Unauthorized)
|   /admincp/index.aspx: Possible admin folder (401 Unauthorized)
|   /admincp/login.aspx: Possible admin folder (401 Unauthorized)
|   /admincontrol.aspx: Possible admin folder (401 Unauthorized)
|   /adminpanel.aspx: Possible admin folder (401 Unauthorized)
|   /admin/admin_login.aspx: Possible admin folder (401 Unauthorized)
|   /admin_login.aspx: Possible admin folder (401 Unauthorized)
|   /adminLogin.aspx: Possible admin folder (401 Unauthorized)
|   /admin/adminLogin.aspx: Possible admin folder (401 Unauthorized)
|   /adminarea/index.aspx: Possible admin folder (401 Unauthorized)
|   /adminarea/admin.aspx: Possible admin folder (401 Unauthorized)
|   /adminarea/login.aspx: Possible admin folder (401 Unauthorized)
|   /administrator/index.aspx: Possible admin folder (401 Unauthorized)
|   /admincontrol/login.aspx: Possible admin folder (401 Unauthorized)
|   /admin2.aspx: Possible admin folder (401 Unauthorized)
|   /admin2/login.aspx: Possible admin folder (401 Unauthorized)
|   /admin2/index.aspx: Possible admin folder (401 Unauthorized)
|   /administratorlogin.aspx: Possible admin folder (401 Unauthorized)
|   /admin/index.jsp: Possible admin folder (401 Unauthorized)
|   /admin/login.jsp: Possible admin folder (401 Unauthorized)
|   /admin/admin.jsp: Possible admin folder (401 Unauthorized)
|   /admin_area/admin.jsp: Possible admin folder (401 Unauthorized)
|   /admin_area/login.jsp: Possible admin folder (401 Unauthorized)
|   /admin_area/index.jsp: Possible admin folder (401 Unauthorized)
|   /admin/home.jsp: Possible admin folder (401 Unauthorized)
|   /admin/controlpanel.jsp: Possible admin folder (401 Unauthorized)
|   /admin.jsp: Possible admin folder (401 Unauthorized)
|   /admin/admin-login.jsp: Possible admin folder (401 Unauthorized)
|   /admin-login.jsp: Possible admin folder (401 Unauthorized)
|   /admin/cp.jsp: Possible admin folder (401 Unauthorized)
|   /administrator/account.jsp: Possible admin folder (401 Unauthorized)
|   /administrator.jsp: Possible admin folder (401 Unauthorized)
|   /administrator/login.jsp: Possible admin folder (401 Unauthorized)
|   /admincp/index.jsp: Possible admin folder (401 Unauthorized)
|   /admincp/login.jsp: Possible admin folder (401 Unauthorized)
|   /admincontrol.jsp: Possible admin folder (401 Unauthorized)
|   /admin/account.jsp: Possible admin folder (401 Unauthorized)
|   /adminpanel.jsp: Possible admin folder (401 Unauthorized)
|   /admin/admin_login.jsp: Possible admin folder (401 Unauthorized)
|   /admin_login.jsp: Possible admin folder (401 Unauthorized)
|   /adminLogin.jsp: Possible admin folder (401 Unauthorized)
|   /admin/adminLogin.jsp: Possible admin folder (401 Unauthorized)
|   /adminarea/index.jsp: Possible admin folder (401 Unauthorized)
|   /adminarea/admin.jsp: Possible admin folder (401 Unauthorized)
|   /adminarea/login.jsp: Possible admin folder (401 Unauthorized)
|   /administrator/index.jsp: Possible admin folder (401 Unauthorized)
|   /admincontrol/login.jsp: Possible admin folder (401 Unauthorized)
|   /admin2.jsp: Possible admin folder (401 Unauthorized)
|   /admin2/login.jsp: Possible admin folder (401 Unauthorized)
|   /admin2/index.jsp: Possible admin folder (401 Unauthorized)
|   /administratorlogin.jsp: Possible admin folder (401 Unauthorized)
|   /admin1.php: Possible admin folder (401 Unauthorized)
|   /administr8.asp: Possible admin folder (401 Unauthorized)
|   /administr8.php: Possible admin folder (401 Unauthorized)
|   /administr8.jsp: Possible admin folder (401 Unauthorized)
|   /administr8.aspx: Possible admin folder (401 Unauthorized)
|   /administr8.cfm: Possible admin folder (401 Unauthorized)
|   /administr8/: Possible admin folder (401 Unauthorized)
|   /administer/: Possible admin folder (401 Unauthorized)
|   /administracao.php: Possible admin folder (401 Unauthorized)
|   /administracao.asp: Possible admin folder (401 Unauthorized)
|   /administracao.aspx: Possible admin folder (401 Unauthorized)
|   /administracao.cfm: Possible admin folder (401 Unauthorized)
|   /administracao.jsp: Possible admin folder (401 Unauthorized)
|   /administracion.php: Possible admin folder (401 Unauthorized)
|   /administracion.asp: Possible admin folder (401 Unauthorized)
|   /administracion.aspx: Possible admin folder (401 Unauthorized)
|   /administracion.jsp: Possible admin folder (401 Unauthorized)
|   /administracion.cfm: Possible admin folder (401 Unauthorized)
|   /administrators/: Possible admin folder (401 Unauthorized)
|   /adminpro/: Possible admin folder (401 Unauthorized)
|   /admins/: Possible admin folder (401 Unauthorized)
|   /admins.cfm: Possible admin folder (401 Unauthorized)
|   /admins.php: Possible admin folder (401 Unauthorized)
|   /admins.jsp: Possible admin folder (401 Unauthorized)
|   /admins.asp: Possible admin folder (401 Unauthorized)
|   /admins.aspx: Possible admin folder (401 Unauthorized)
|   /administracion-sistema/: Possible admin folder (401 Unauthorized)
|   /admin108/: Possible admin folder (401 Unauthorized)
|   /admin_cp.asp: Possible admin folder (401 Unauthorized)
|   /admin/backup/: Possible backup (401 Unauthorized)
|   /admin/download/backup.sql: Possible database backup (401 Unauthorized)
|   /robots.txt: Robots file
|   /admin/upload.php: Admin File Upload (401 Unauthorized)
|   /admin/CiscoAdmin.jhtml: Cisco Collaboration Server (401 Unauthorized)
|   /admin-console/: JBoss Console (401 Unauthorized)
|   /admin4.nsf: Lotus Domino (401 Unauthorized)
|   /admin5.nsf: Lotus Domino (401 Unauthorized)
|   /admin.nsf: Lotus Domino (401 Unauthorized)
|   /administrator/wp-login.php: Wordpress login page. (401 Unauthorized)
|   /admin/libraries/ajaxfilemanager/ajaxfilemanager.php: Log1 CMS (401 Unauthorized)
|   /admin/view/javascript/fckeditor/editor/filemanager/connectors/test.html: OpenCart/FCKeditor File upload (401 Unauthorized)
|   /admin/includes/tiny_mce/plugins/tinybrowser/upload.php: CompactCMS or B-Hind CMS/FCKeditor File upload (401 Unauthorized)
|   /admin/includes/FCKeditor/editor/filemanager/upload/test.html: ASP Simple Blog / FCKeditor File Upload (401 Unauthorized)
|   /admin/jscript/upload.php: Lizard Cart/Remote File upload (401 Unauthorized)
|   /admin/jscript/upload.html: Lizard Cart/Remote File upload (401 Unauthorized)
|   /admin/jscript/upload.pl: Lizard Cart/Remote File upload (401 Unauthorized)
|   /admin/jscript/upload.asp: Lizard Cart/Remote File upload (401 Unauthorized)
|   /admin/environment.xml: Moodle files (401 Unauthorized)
|   /classes/: Potentially interesting folder
|   /es/: Potentially interesting folder
|   /help/: Potentially interesting folder
|_  /printers/: Potentially interesting folder
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_      http://ha.ckers.org/slowloris/
| vulners: 
|   CUPS 2.4: 
|     	MSF:EXPLOIT-MULTI-MISC-CUPS_IPP_REMOTE_CODE_EXECUTION-	9.8	https://vulners.com/metasploit/MSF:EXPLOIT-MULTI-MISC-CUPS_IPP_REMOTE_CODE_EXECUTION-	*EXPLOIT*
|     	1337DAY-ID-39819	9.0	https://vulners.com/zdt/1337DAY-ID-39819	*EXPLOIT*
|     	PACKETSTORM:182767	8.6	https://vulners.com/packetstorm/PACKETSTORM:182767	*EXPLOIT*
|     	6D7EB122-6604-5374-B851-DA56ABDA1F34	8.6	https://vulners.com/githubexploit/6D7EB122-6604-5374-B851-DA56ABDA1F34	*EXPLOIT*
|     	34D7D370-3683-5358-9692-BB0B5AF7F412	8.6	https://vulners.com/githubexploit/34D7D370-3683-5358-9692-BB0B5AF7F412	*EXPLOIT*
|     	CVE-2024-47850	7.5	https://vulners.com/cve/CVE-2024-47850
|     	MSF:AUXILIARY-SCANNER-MISC-CUPS_BROWSED_INFO_DISCLOSURE-	5.3	https://vulners.com/metasploit/MSF:AUXILIARY-SCANNER-MISC-CUPS_BROWSED_INFO_DISCLOSURE-	*EXPLOIT*
|     	F5502B30-710E-5D69-B67C-937F75899289	5.3	https://vulners.com/githubexploit/F5502B30-710E-5D69-B67C-937F75899289	*EXPLOIT*
|     	D0B85558-0ED9-5259-A56D-4C807CC07FCF	5.3	https://vulners.com/githubexploit/D0B85558-0ED9-5259-A56D-4C807CC07FCF	*EXPLOIT*
|     	ADDB422D-CF88-55B8-BA36-EC2BAC7507A0	5.3	https://vulners.com/githubexploit/ADDB422D-CF88-55B8-BA36-EC2BAC7507A0	*EXPLOIT*
|     	9DB4B6B1-3FB0-5827-B554-3F3779D23B09	5.3	https://vulners.com/githubexploit/9DB4B6B1-3FB0-5827-B554-3F3779D23B09	*EXPLOIT*
|_    	48FAED93-C711-59A0-B81E-A65D4463C7F0	5.3	https://vulners.com/githubexploit/48FAED93-C711-59A0-B81E-A65D4463C7F0	*EXPLOIT*
|_http-server-header: CUPS/2.4 IPP/2.1
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
| http-method-tamper: 
|   VULNERABLE:
|   Authentication bypass by HTTP verb tampering
|     State: VULNERABLE (Exploitable)
|       This web server contains password protected resources vulnerable to authentication bypass
|       vulnerabilities via HTTP verb tampering. This is often found in web servers that only limit access to the
|        common HTTP methods and in misconfigured .htaccess files.
|              
|     Extra information:
|       
|   URIs suspected to be vulnerable to HTTP verb tampering:
|     /admin [GENERIC]
|   
|     References:
|       http://www.mkit.com.ar/labs/htexploit/
|       http://capec.mitre.org/data/definitions/274.html
|       http://www.imperva.com/resources/glossary/http_verb_tampering.html
|_      https://www.owasp.org/index.php/Testing_for_HTTP_Methods_and_XST_%28OWASP-CM-008%29
5000/tcp open  http    Docker Registry (API: 2.0)
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_      http://ha.ckers.org/slowloris/

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 562.33 seconds
```

Обнаружены следующие уязвимости:

```bash
svepodd@svepodd-VirtualBox:~$ grep "VULNERABLE" nmapres_new.txt
|   VULNERABLE:
|     State: LIKELY VULNERABLE
|   VULNERABLE:
|     State: VULNERABLE (Exploitable)
|   VULNERABLE:
|     State: LIKELY VULNERABLE

```

Экспорт в формат отчета:

```bash
svepodd@svepodd-VirtualBox:~$ mkdir -p ~/project/reports
svepodd@svepodd-VirtualBox:~$ nmap -sV -p 8080 --script vuln -oN ~/project/reports/nmapres_new.txt -oX ~/project/reports/nmapres_new.xml localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 18:46 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00011s latency).

PORT     STATE  SERVICE    VERSION
8080/tcp closed http-proxy

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.44 seconds
svepodd@svepodd-VirtualBox:~$ xsltproc ~/project/reports/nmapres_new.xml -o ~/project/reports/nmapres_new.html
```

Сформирован html отчёт результатов скана шлюза:

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/refs/heads/svepodd_lab03/labs/lab03/report.png)

- [x] 3. Используйте команду `tree` и выведите все вложенные файлы по директориям.

```bash
svepodd@svepodd-VirtualBox:~/course_labs$ tree .
.
├── assets
│   └── logotype
│       ├── logo2.jpg
│       └── logo.jpg
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── docs
│   ├── about.md
│   ├── APPENDIX.md
│   ├── appsec_tt.md
│   ├── artifacts
│   │   ├── assets
│   │   │   ├── favicon.ico
│   │   │   ├── logo.png
│   │   │   └── logotypemd.jpg
│   │   ├── cheatsheet
│   │   │   ├── CHEATSHEET_DOCKERIGNORE.md
│   │   │   ├── CHEATSHEET_DOCKER.md
│   │   │   ├── CHEATSHEET_GH_CLI.md
│   │   │   ├── CHEATSHEET_GITIGNORE.md
│   │   │   └── CHEATSHEET_GIT.md
│   │   ├── exmpls
│   │   │   ├── risk-analysis.png
│   │   │   ├── table1.png
│   │   │   └── transaction.png
│   │   ├── owasp
│   │   │   ├── Authentication.pdf
│   │   │   ├── Authorization.pdf
│   │   │   ├── Client-side_Attacks.pdf
│   │   │   ├── Command_Execution.pdf
│   │   │   ├── Information_Disclosure.pdf
│   │   │   ├── Logical_Attacks.pdf
│   │   │   └── OWASP_Top_10_CICD_Risks.pdf
│   │   └── ppt
│   │       └── Лекция_Управление Рисками ИБ_intro.pdf
│   ├── Authentication.md
│   ├── Authorization.md
│   ├── channel.md
│   ├── Client-side Attacks.md
│   ├── Command Execution.md
│   ├── exmpl.md
│   ├── index.md
│   ├── Information Disclosure.md
│   ├── javascripts
│   │   ├── custom-title.js
│   │   └── typewriter-target.js
│   ├── labs
│   │   ├── lab01.md
│   │   ├── lab02.md
│   │   ├── lab03.md
│   │   ├── lab04.md
│   │   ├── lab05.md
│   │   ├── lab06.md
│   │   ├── lab07.md
│   │   ├── lab08.md
│   │   ├── lab09.md
│   │   ├── lab10.md
│   │   └── pet_project.md
│   ├── licenses.md
│   ├── Logical Attacks.md
│   ├── Multisignature.md
│   ├── OWASP_Top_10_CICD_Risks.md
│   ├── PrintNightmare.md
│   ├── RA.md
│   ├── RELEASE_NOTES.md
│   ├── robots.txt
│   ├── Security.md
│   └── stylesheets
│       ├── burger.css
│       ├── footer.css
│       ├── header.css
│       ├── layout.css
│       ├── mobile-logo.css
│       ├── search.css
│       ├── sidebar.css
│       ├── tools-overlay.css
│       └── typeset.css
├── eslint.config.js
├── labs
│   ├── lab01
│   │   ├── README.md
│   │   └── typersteel.py
│   ├── lab02
│   │   ├── exmpl_hello.py
│   │   ├── pygamesteel.py
│   │   ├── README.md
│   │   └── Report.md
│   ├── lab03
│   │   ├── exmp_targets.txt
│   │   └── README.md
│   ├── lab04
│   │   └── README.md
│   ├── lab05
│   │   ├── client
│   │   │   ├── client.py
│   │   │   ├── Dockerfile
│   │   │   └── requirements.txt
│   │   ├── docker-compose.yml
│   │   ├── README.md
│   │   ├── server
│   │   │   ├── app.py
│   │   │   ├── Dockerfile
│   │   │   └── requirements.txt
│   │   └── source
│   │       ├── Dockerfile
│   │       ├── hello.py
│   │       └── requirements.txt
│   ├── lab06
│   │   ├── audit.sh
│   │   ├── config
│   │   │   └── nginx.conf
│   │   ├── docker-compose.yml
│   │   ├── README.md
│   │   └── vulnerable-app.yml
│   ├── lab07
│   │   ├── cheat_check_yuorself.sh
│   │   ├── docker-compose.yml
│   │   ├── README.md
│   │   ├── sast
│   │   │   ├── checkov-config.yaml
│   │   │   └── semgrep-rules.yml
│   │   ├── sca
│   │   │   ├── dependency-check.sh
│   │   │   └── pom.xml
│   │   └── vulnerable-app
│   │       ├── app.py
│   │       ├── config.yaml
│   │       ├── Dockerfile
│   │       └── requirements.txt
│   ├── lab08
│   │   ├── dast
│   │   │   ├── convert_reports.py
│   │   │   ├── zap-baseline.conf
│   │   │   └── zap_scan.sh
│   │   ├── docker-compose.yml
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── vulnerable-app
│   │       ├── app.py
│   │       ├── Dockerfile
│   │       ├── files
│   │       │   └── secret.txt
│   │       └── requirements.txt
│   ├── lab09
│   │   └── README.md
│   ├── lab10
│   │   └── README.md
│   └── pet_project
│       └── README.md
├── LICENSE.md
├── mkdocs.yml
├── mypy.ini
├── NOTICE.md
├── overrides
│   └── material
│       └── partials
│           └── toc.html
├── README.md
├── RELEASE_NOTES.md
├── requirements.txt
├── ruff.toml
├── SECURITY.md
└── stylelint.config.cjs

38 directories, 126 files
```

- [x] 4.Найдите IP сетевой карты `Ethernet`, которая соответствует вашей виртуальной машине используя `ifconfig` и выполните команду

```bash
nmap -sP inet_addr
```

```bash
svepodd@svepodd-VirtualBox:~/course_labs$ nmap -sP 10.238.179.78
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 19:04 MSK
Nmap scan report for svepodd-VirtualBox (10.238.179.78)
Host is up (0.00013s latency).
Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
```

- [x] 5. Определите ОС, данные ssh, telnet  с помощью `nmap` и выведите о них информацию.

```bash
svepodd@svepodd-VirtualBox:~/course_labs$ sudo nmap -A -p 22,23 10.238.179.78
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-15 19:17 MSK
Nmap scan report for svepodd-VirtualBox (10.238.179.78)
Host is up (0.00018s latency).

PORT   STATE  SERVICE VERSION
22/tcp closed ssh
23/tcp closed telnet
Too many fingerprints match this host to give specific OS details
Network Distance: 0 hops

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1.92 seconds
```

В данном случае порты закрыты, а определить ОС не получилось.

- [x] 6. Результаты из `nmapres_new.txt` надо перенести в `nmapres.txt` и оставить оба файла рядом в локальном репозитории. Желательно использовать `cp` в консоли через редактор.

```bash
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab03$ ls
exmp_targets.txt  nmapres_new.txt  README.md
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab03$ cp nmapres_new.txt nmapres.txt 
svepodd@svepodd-VirtualBox:~/course_labs/labs/lab03$ ls
exmp_targets.txt  nmapres_new.txt  nmapres.txt  README.md
```

- [x] 7. Оформить `README.md` по аналогии и использовать `shield`, etc.

- [x] 8. Составить `gist` отчет и отправить ссылку личным сообщением

***

Copyright (c) 2025 Svetlana Poddoskina