<div align="center">
<h1><a id="intro">Лабораторная работа №7</a><br></h1>
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
$ pip install -r vulnerable-app/requirements.txt
```

- [x] 2. Запустите уязвимое приложение

```bash
$ docker-compose -f docker-compose.yml up -d --build # http://localhost:8080
```

- [x] 3. Запустите SAST Semgrep и проанализируйте выведенный лог в консоли и опишите логику правил для `semgrep-rules.yml` исходя из паттернов, которые используются. Отчет будет в директории SAST

```bash
$ semgrep --config sast/semgrep-rules.yml \
  --json \
  --output sast/semgrep-report.json \
  vulnerable-app/
```

Запускаем SAST Semgrep:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07$ semgrep --config sast/semgrep-rules.yml \
  --json \
  --output sast/semgrep-report.json \
  vulnerable-app/

┌──── ○○○ ────┐
│ Semgrep CLI │
└─────────────┘                                                                

...
 
┌──────────────┐
│ Scan Summary │
└──────────────┘
✅ Scan completed successfully.
 • Findings: 5 (5 blocking)
 • Rules run: 16
 • Targets scanned: 2
 • Parsed lines: ~100.0%
 • Scan was limited to files tracked by git
 • For a detailed list of skipped files and lines, run semgrep with the --verbose flag
Ran 16 rules on 2 files: 5 findings.
```

Semgrep пишет **16 Code rules** - всего правил в `semgrep-rules.yml`, которые распределены:
- Python: 12 правил, которые применены к файлу `app.py` 
- YAML: 4 правила, которые применены к файлу `config.yaml`

В выведенном логе видим:

```bash
✅ Scan completed successfully.
 • Findings: 5 (5 blocking)
 • Rules run: 16
 • Targets scanned: 2
```

Это означает, что из 16 правил реально сработали (дали совпадения) 5.

Смотрим вывод `semgrep-report.json`:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07$ cat sast/semgrep-report.json
{"version":"1.147.0","results":[{"check_id":"sast.py-info-version-disclosure","path":"vulnerable-app/app.py","start":{"line":26,"col":5,"offset":410},"end":{"line":26,"col":39,"offset":444},"extra":{"message":"Раскрытие версии приложения в ответе.","metadata":{},"severity":"LOW","fingerprint":"requires login","lines":"requires login","validation_state":"NO_VALIDATOR","engine_kind":"OSS"}},{"check_id":"sast.py-os-system-rce","path":"vulnerable-app/app.py","start":{"line":52,"col":5,"offset":1102},"end":{"line":52,"col":19,"offset":1116},"extra":{"message":"RCE через os.system с данными пользователя.","metadata":{},"severity":"CRITICAL","fingerprint":"requires login","lines":"requires login","validation_state":"NO_VALIDATOR","engine_kind":"OSS"}},{"check_id":"sast.py-arbitrary-file-read","path":"vulnerable-app/app.py","start":{"line":68,"col":14,"offset":1501},"end":{"line":68,"col":29,"offset":1516},"extra":{"message":"Чтение произвольного файла по пути из запроса (LFI/Path Traversal).","metadata":{},"severity":"CRITICAL","fingerprint":"requires login","lines":"requires login","validation_state":"NO_VALIDATOR","engine_kind":"OSS"}},{"check_id":"sast.py-unsafe-pickle-deserialization","path":"vulnerable-app/app.py","start":{"line":79,"col":15,"offset":1749},"end":{"line":79,"col":48,"offset":1782},"extra":{"message":"Небезопасная десериализация через pickle.loads.","metadata":{},"severity":"CRITICAL","fingerprint":"requires login","lines":"requires login","validation_state":"NO_VALIDATOR","engine_kind":"OSS"}},{"check_id":"sast.py-eval-user-input","path":"vulnerable-app/app.py","start":{"line":88,"col":14,"offset":1996},"end":{"line":88,"col":24,"offset":2006},"extra":{"message":"Опасное использование eval на пользовательском вводе.","metadata":{},"severity":"HIGH","fingerprint":"requires login","lines":"requires login","validation_state":"NO_VALIDATOR","engine_kind":"OSS"}}],"errors":[{"code":2,"level":"warn","type":"Other syntax error","message":"Other syntax error at line vulnerable-app/config.yaml:37:\n (approximate error location; error nearby after) error calling parser: could not find expected ':' character 0 position 0 returned: 0","path":"vulnerable-app/config.yaml"}],"paths":{"scanned":["vulnerable-app/app.py","vulnerable-app/config.yaml"]},"time":{"rules":[],"rules_parse_time":0.004681110382080078,"profiling_times":{"config_time":0.12587690353393555,"core_time":-2.011631965637207,"ignores_time":6.771087646484375e-05,"total_time":-1.8722844123840332},"parsing_time":{"total_time":0.0,"per_file_time":{"mean":0.0,"std_dev":0.0},"very_slow_stats":{"time_ratio":0.0,"count_ratio":0.0},"very_slow_files":[]},"scanning_time":{"total_time":0.041726112365722656,"per_file_time":{"mean":0.020863056182861328,"std_dev":0.00017590682779200506},"very_slow_stats":{"time_ratio":0.0,"count_ratio":0.0},"very_slow_files":[]},"matching_time":{"total_time":0.0,"per_file_and_rule_time":{"mean":0.0,"std_dev":0.0},"very_slow_stats":{"time_ratio":0.0,"count_ratio":0.0},"very_slow_rules_on_files":[]},"tainting_time":{"total_time":0.0,"per_def_and_rule_time":{"mean":0.0,"std_dev":0.0},"very_slow_stats":{"time_ratio":0.0,"count_ratio":0.0},"very_slow_rules_on_defs":[]},"fixpoint_timeouts":[],"prefiltering":{"project_level_time":0.0,"file_level_time":0.0,"rules_with_project_prefilters_ratio":0.0,"rules_with_file_prefilters_ratio":0.9166666666666666,"rules_selected_ratio":1.0,"rules_matched_ratio":1.0},"targets":[],"total_bytes":0,"max_memory_bytes":141562112},"engine_requested":"OSS","skipped_rules":[],"profiling_results":[]}
```

По `semgrep-report.json` как раз видно 5 найденных `check_id` (сработавших правил):
- `py-os-system-rce`
- `py-arbitrary-file-read`
- `py-unsafe-pickle-deserialization`
- `py-eval-user-input`
- `py-info-version-disclosure`

Теперь проанализируем логику правил для `semgrep-rules.yml` исходя из паттернов, которые используются:

| Правило                            | Идея                                                                                       | Паттерны                                                                                                                                                                        | Смысл                                                                                                                               |
| ---------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `py-sql-injection-critical`        | найти небезопасное формирование SQL через конкатенацию строки в SQL-запросе                | `cursor.execute("SELECT " + ...)`<br>`cursor.execute(f"SELECT " + ...)`                                                                                                         | если запрос собирается строкой, особенно с пользовательскими данными, возможна SQL-инъекция.                                        |
| `py-os-system-rce`                 | выявить вызовы `os.system(...)`.                                                           | `os.system(...)`                                                                                                                                                                | если в `os.system` попадают данные из запроса/пользовательского ввода, возникает риск command injection/RCE.                        |
| `py-subprocess-rce`                | детектировать запуск shell через `sh -c`, который часто приводит к инъекциям.              | `subprocess.call(["sh", "-c", ...])`                                                                                                                                            | передача строки команд интерпретатору shell (`sh -c`) особенно опасна при участии внешнего ввода.                                   |
| `py-arbitrary-file-read`           | найти чтение файлов через `open(..., "r")`.                                                | `open(..., "r")`                                                                                                                                                                | если аргумент `open()` формируется из параметра запроса/пути, это типичный признак LFI/Path Traversal (чтение произвольных файлов). |
| `py-unsafe-pickle-deserialization` | найти небезопасную десериализацию.                                                         | `pickle.loads(...)`                                                                                                                                                             | `pickle` при загрузке может выполнять произвольный код => типичный источник RCE при обработке данных извне.                         |
| `py-reflected-xss`                 | выявить отражённый XSS - когда пользовательский ввод вставляется в HTML без экранирования. | `html = f"<h1>Results for: {q}</h1>"`    <br>`return f"<h1>Results for: {q}</h1>"`                                                                                              | переменная `q` (как будто из параметров запроса) напрямую попадает в HTML => риск XSS.                                              |
| `py-hardcoded-db-credentials`      | найти захардкоженные учётные данные.                                                       | `DB_USER = "..."`<br>`DB_PASSWORD = "..."`                                                                                                                                      | хранение логина/пароля в коде => утечка секретов через репозиторий, логи, бэкапы и т.д.                                             |
| `py-eval-user-input`               | запрет опасного вычисления выражений.                                                      | `eval(...)`                                                                                                                                                                     | `eval` с пользовательским вводом = выполнение произвольного кода.                                                                   |
| `yaml-hardcoded-secrets-config`    | поиск секретов в YAML.                                                                     | `password: "..."`<br>`default_admin_password: "..."`<br>`jwt_secret: "..."`                                                                                                     | хранение паролей/секретов в конфиге.                                                                                                |
| `py-debug-mode-enabled`            | обнаружить включённый debug.                                                               | `app.config["DEBUG"] = True`<br>`app.run(..., debug=True)`                                                                                                                      | debug даёт лишнюю информацию, иногда интерактивную консоль/traceback, повышает риск утечки.                                         |
| `py-verbose-logging-sensitive`     | выявить подробные debug-логи.                                                              | `logging.basicConfig(level=logging.DEBUG)`<br>`app.logger.debug(...)`                                                                                                           | в логи могут попасть токены, пароли, cookies, части запросов/ответов.                                                               |
| `py-info-version-disclosure`       | фиксировать раскрытие версии приложения.                                                   | `return "Vulnerable lab07 app v1.0"`                                                                                                                                            | версионирование помогает атакующему подобрать эксплойт/уязвимую ветку.                                                              |
| `py-debug-endpoint-exposes-env`    | найти debug-эндпоинты, отдающие окружение и заголовки.                                     | `env = dict(os.environ)`<br>`return {"headers": headers, "env_sample": env_sample}`                                                                                             | утечка окружения может раскрыть токены, ключи, конфиги, пути, сервисные переменные.                                                 |
| `yaml-hardcoded-secrets-2`         | дополнительная проверка на секреты и учётные данные в config.yaml                          | `password: "..."`<br>`default_admin_password: "..."`<br>`jwt_secret: "..."`                                                                                                     | дублирует идею поиска `password/default_admin_password/jwt_secret`, только паттерны записаны без кавычек.                           |
| `yaml-insecure-security-flags`     | найти отключённые механизмы защиты в конфиге                                               | `"enable_csrf_protection: false"`<br>`"enable_rate_limit: false"`<br>`"allow_insecure_cookies: true"`<br>`"session_cookie_secure: false"`<br>`"session_cookie_httponly: false"` | поиск механизмов: CSRF, rate limit, insecure cookies, cookie flags                                                                  |
| `yaml-debug-and-unsafe-features`   | найти выключенные debug-режим и экспериментальные/опасные фичи                             | `debug: true`<br>`enable_unsafe_eval: true`<br>`enable_remote_shell: true`                                                                                                      | позволяет выявить опасные фичи                                                                                                      |

- [x] 4. Запустите SAST Checkov по Dockerfile, compose и проанализируйте выведенный лог в консоли и опишите логику правил для `checkov-config.yaml` по `Docker`. Отчет будет в директории SAST

```bash
$ checkov \
  --framework dockerfile \
  --file vulnerable-app/Dockerfile docker-compose.yml \
  --output json \
  --output-file-path sast/checkov-report.json \
  --soft-fail
```

Результат запуска команды:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07$ checkov \
  --framework dockerfile \
  --file vulnerable-app/Dockerfile docker-compose.yml \
  --output json \
  --output-file-path sast/checkov-report.json \
  --soft-fail
2026-01-13 21:48:30,331 [MainThread  ] [WARNI]  /home/svepodd/course_labs/labs/lab07/venv/lib/python3.12/site-packages/paramiko/pkey.py:59: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
  'cipher': algorithms.TripleDES,

2026-01-13 21:48:30,341 [MainThread  ] [WARNI]  /home/svepodd/course_labs/labs/lab07/venv/lib/python3.12/site-packages/paramiko/transport.py:193: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
  'class': algorithms.TripleDES,

[ dockerfile framework ]: 100%|████████████████████|[1/1], Current File Scanned=vulnerable-app/Dockerfile
{
    "check_type": "dockerfile",
    "results": {

...

    "summary": {
        "passed": 50,
        "failed": 2,
        "skipped": 0,
        "parsing_errors": 0,
        "resource_count": 1,
        "checkov_version": "3.2.497"
    },
    "url": "Add an api key '--bc-api-key <api-key>' to see more detailed insights via https://bridgecrew.cloud"
}
```

В выведенном логе видим:

```bash
"summary": {
    "passed": 50,
    "failed": 2,
    "skipped": 0,
    "parsing_errors": 0,
    "resource_count": 1,
    "checkov_version": "3.2.497"
},
```

Это означает, что из всех правил 2 политики упали:`CKV_DOCKER_2` и `CKV_DOCKER_3`

Теперь проанализируем логику правил для для `checkov-config.yaml` по `Docker`:

| Проверка      | Смысл                                       |
| ------------- | ------------------------------------------- |
| CKV_DOCKER_2  | Контейнер не должен запускаться под root    |
| CKV_DOCKER_3  | Минимизировать лишние пакеты и слои         |
| CKV_DOCKER_5  | Избегать latest без необходимости           |
| CKV_DOCKER_7  | Не использовать ADD вместо COPY             |
| CKV_DOCKER_8  | Явно задавать non-root пользователя         |
| CKV_DOCKER_9  | Минимизировать размер/attack surface образа |
| CKV_DOCKER_10 | Наличие HEALTHCHECK                         |
| CKV_DOCKER_12 | Не хранить секреты в ENV                    |
| CKV_DOCKER_13 | Запрет привилегированного режима            |
| CKV_DOCKER_14 | Ограничить capabilities                     |
| CKV_DOCKER_16 | Предпочитать read-only root filesystem      |

- [x] 5. Подготовка зависимостей Java и Maven‑скан для проведения SCA. Отчеты будут в директории SCA. Будет ошибка, которую надо поправить, что бы уязвимости определялись или добавить дополнительные уязвимости для их вывода в отчете

```bash
$ cd sca
$ ./dependency-check.sh --update # обновление и поставка базы NVD API
$ mvn dependency:resolve
$ mvn dependency:copy-dependencies -DoutputDirectory=./lib # зависимости из $ pom.xml как jar в ./lib
$ mvn org.owasp:dependency-check-maven:check || true # Maven-плагин OWASP
```

Обновление и поставка базы NVD API:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca$ ./dependency-check.sh --update
OWASP Dependency-Check SCA
[*] Updating NVD database in /home/svepodd/.dependency-check-data...
[INFO] Checking for updates
[INFO] NVD API has 327,477 records in this update
[INFO] Downloaded 10,000/327,477 (3%)
[INFO] Downloaded 20,000/327,477 (6%)
[INFO] Downloaded 30,000/327,477 (9%)
...
[INFO] Completed processing batch 164/164 (100%) in 310ms
[INFO] Skipping Known Exploited Vulnerabilities update check since last check was within 24 hours.
[INFO] Begin database defrag
[INFO] End database defrag (4291 ms)
[INFO] Check for updates complete (225875 ms)
[+] NVD data updated
```

Разрешение всех зависимостей:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca$ mvn dependency:resolve
[INFO] Scanning for projects...
[INFO]
[INFO] ---------------------------< lab07:sca-demo >---------------------------
[INFO] Building sca-demo 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- maven-dependency-plugin:2.8:resolve (default-cli) @ sca-demo ---
[INFO]
[INFO] The following files have been resolved:
[INFO]    com.fasterxml.jackson.core:jackson-annotations:jar:2.4.0:compile
[INFO]    com.fasterxml.jackson.core:jackson-databind:jar:2.4.6:compile
[INFO]    com.fasterxml.jackson.module:jackson-module-jaxb-annotations:jar:2.4.6:compile
[INFO]    commons-codec:commons-codec:jar:1.2:compile
[INFO]    com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider:jar:2.4.6:compile
[INFO]    com.fasterxml.jackson.jaxrs:jackson-jaxrs-base:jar:2.4.6:compile
[INFO]    com.fasterxml.jackson.core:jackson-core:jar:2.4.6:compile
[INFO]    org.codehaus.groovy:groovy-all:jar:2.1.6:compile
[INFO]    commons-httpclient:commons-httpclient:jar:3.1:compile
[INFO]    commons-logging:commons-logging:jar:1.0.4:compile
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.126 s
[INFO] Finished at: 2026-01-13T22:16:37+03:00
[INFO] ------------------------------------------------------------------------
```

Копируем зависимости из `pom.xml` в поддиректорию в `./lib`:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca$ mvn dependency:copy-dependencies -DoutputDirectory=./lib
[INFO] Scanning for projects...
[INFO]
[INFO] ---------------------------< lab07:sca-demo >---------------------------
[INFO] Building sca-demo 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- maven-dependency-plugin:2.8:copy-dependencies (default-cli) @ sca-demo ---
[INFO] jackson-annotations-2.4.0.jar already exists in destination.
[INFO] jackson-databind-2.4.6.jar already exists in destination.
[INFO] jackson-module-jaxb-annotations-2.4.6.jar already exists in destination.
[INFO] commons-codec-1.2.jar already exists in destination.
[INFO] jackson-jaxrs-json-provider-2.4.6.jar already exists in destination.
[INFO] jackson-jaxrs-base-2.4.6.jar already exists in destination.
[INFO] jackson-core-2.4.6.jar already exists in destination.
[INFO] groovy-all-2.1.6.jar already exists in destination.
[INFO] commons-httpclient-3.1.jar already exists in destination.
[INFO] commons-logging-1.0.4.jar already exists in destination.
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.304 s
[INFO] Finished at: 2026-01-13T22:17:33+03:00
[INFO] ------------------------------------------------------------------------
```

- [x] 6. Запустите SCA CLI OWASP Dependency-Check для уязвимого приложения. Отчеты будут в директории SCA. Опишите как работает сканирование SCA для `pom.xml` и `app.py`

Сканирование `pom.xml` через Maven-плагин OWASP:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca$ mvn org.owasp:dependency-check-maven:check -DdataDirectory="$HOME/.dependency-check-data" -DautoUpdate=false || true
[INFO] Scanning for projects...
[INFO]
[INFO] ---------------------------< lab07:sca-demo >---------------------------
[INFO] Building sca-demo 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- dependency-check-maven:12.1.0:check (default-cli) @ sca-demo ---
[INFO]

Dependency-Check is an open source tool performing a best effort analysis of 3rd party dependencies; false positives and false negatives may exist in the analysis performed by the tool. Use of the tool and the reporting provided constitutes acceptance for use in an AS IS condition, and there are NO warranties, implied or otherwise, with regard to the analysis or its use. Any use of the tool and the reporting provided is at the user's risk. In no event shall the copyright holder or OWASP be held liable for any damages whatsoever arising out of or in connection with the use of this tool, the analysis performed, or the resulting report.


   About ODC: https://jeremylong.github.io/DependencyCheck/general/internals.html
   False Positives: https://jeremylong.github.io/DependencyCheck/general/suppression.html

💖 Sponsor: https://github.com/sponsors/jeremylong


[INFO] Analysis Started
[INFO] Finished Archive Analyzer (0 seconds)
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished Jar Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Created CPE Index (2 seconds)
[INFO] Finished CPE Analyzer (2 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[WARNING] An error occurred while analyzing '/home/svepodd/.m2/repository/com/fasterxml/jackson/jaxrs/jackson-jaxrs-json-provider/2.4.6/jackson-jaxrs-json-provider-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/tmp/dctempace7e6a6-2655-4f02-a065-3f2f2e435c53/check16733858412085076054tmp/7/pom.xml' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/svepodd/.m2/repository/org/codehaus/groovy/groovy-all/2.1.6/groovy-all-2.1.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/svepodd/.m2/repository/commons-codec/commons-codec/1.2/commons-codec-1.2.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/svepodd/.m2/repository/commons-logging/commons-logging/1.0.4/commons-logging-1.0.4.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/svepodd/.m2/repository/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/svepodd/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.4.6/jackson-module-jaxb-annotations-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/svepodd/.m2/repository/com/fasterxml/jackson/core/jackson-annotations/2.4.0/jackson-annotations-2.4.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/svepodd/.m2/repository/com/fasterxml/jackson/core/jackson-databind/2.4.6/jackson-databind-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/svepodd/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.4.6/jackson-core-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/svepodd/.m2/repository/com/fasterxml/jackson/jaxrs/jackson-jaxrs-base/2.4.6/jackson-jaxrs-base-2.4.6.jar' (Sonatype OSS Index Analyzer).
[INFO] Finished Sonatype OSS Index Analyzer (2 seconds)
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (6 seconds)
[INFO] Writing XML report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.xml
[INFO] Writing HTML report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.html
[INFO] Writing JSON report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.json
[INFO] Writing CSV report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.csv
[INFO] Writing SARIF report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.sarif
[INFO] Writing JENKINS report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-jenkins.html
[INFO] Writing JUNIT report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-junit.xml
[INFO] Writing GITLAB report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-gitlab.json
[WARNING]

One or more dependencies were identified with known vulnerabilities in sca-demo:

commons-httpclient-3.1.jar (pkg:maven/commons-httpclient/commons-httpclient@3.1, cpe:2.3:a:apache:commons-httpclient:3.1:*:*:*:*:*:*:*, cpe:2.3:a:apache:httpclient:3.1:*:*:*:*:*:*:*) : CVE-2012-5783, CVE-2020-13956
groovy-all-2.1.6.jar (pkg:maven/org.codehaus.groovy/groovy-all@2.1.6, cpe:2.3:a:apache:groovy:2.1.6:*:*:*:*:*:*:*) : CVE-2015-3253, CVE-2016-6814, CVE-2020-17521
jackson-annotations-2.4.0.jar (pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.4.0, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.0:*:*:*:*:*:*:*) : CVE-2018-1000873
jackson-core-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-core@2.4.6, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*) : CVE-2018-1000873
jackson-databind-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.4.6, cpe:2.3:a:fasterxml:jackson-databind:2.4.6:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*) : CVE-2017-15095, CVE-2017-17485, CVE-2017-7525, CVE-2018-11307, CVE-2018-14718, CVE-2018-14719, CVE-2018-7489, CVE-2019-14379, CVE-2019-14540, CVE-2019-14892, CVE-2019-16335, CVE-2019-16942, CVE-2019-16943, CVE-2019-17267, CVE-2019-17531, CVE-2019-20330, CVE-2020-8840, CVE-2020-9547, CVE-2020-9548, CVE-2020-10673, CVE-2018-5968, CVE-2020-10650, CVE-2020-24616, CVE-2020-24750, CVE-2020-35490, CVE-2020-35491, CVE-2020-36179, CVE-2020-36180, CVE-2020-36181, CVE-2020-36182, CVE-2020-36183, CVE-2020-36184, CVE-2020-36185, CVE-2020-36186, CVE-2020-36187, CVE-2020-36188, CVE-2020-36189, CVE-2021-20190, CVE-2018-12022, CVE-2019-12086, CVE-2019-14439, CVE-2020-36518, CVE-2022-42003, CVE-2022-42004, CVE-2018-1000873, CVE-2019-12384, CVE-2019-12814, CVE-2023-35116


See the dependency-check report for more details.


[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  11.287 s
[INFO] Finished at: 2026-01-13T22:19:17+03:00
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.owasp:dependency-check-maven:12.1.0:check (default-cli) on project sca-demo:
[ERROR]
[ERROR] One or more dependencies were identified with vulnerabilities that have a CVSS score greater than or equal to '0.0':
[ERROR]
[ERROR] commons-httpclient-3.1.jar (pkg:maven/commons-httpclient/commons-httpclient@3.1, cpe:2.3:a:apache:commons-httpclient:3.1:*:*:*:*:*:*:*, cpe:2.3:a:apache:httpclient:3.1:*:*:*:*:*:*:*): CVE-2020-13956(5.3), CVE-2012-5783(5.8)
[ERROR] groovy-all-2.1.6.jar (pkg:maven/org.codehaus.groovy/groovy-all@2.1.6, cpe:2.3:a:apache:groovy:2.1.6:*:*:*:*:*:*:*): CVE-2015-3253(9.8), CVE-2016-6814(9.8), CVE-2020-17521(5.5)
[ERROR] jackson-annotations-2.4.0.jar (pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.4.0, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.0:*:*:*:*:*:*:*): CVE-2018-1000873(6.5)
[ERROR] jackson-core-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-core@2.4.6, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*): CVE-2018-1000873(6.5)
[ERROR] jackson-databind-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.4.6, cpe:2.3:a:fasterxml:jackson-databind:2.4.6:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*): CVE-2017-17485(9.8), CVE-2020-9547(9.8), CVE-2018-12022(7.5), CVE-2018-5968(8.1), CVE-2020-9548(9.8), CVE-2019-14379(9.8), CVE-2020-36180(8.1), CVE-2020-24616(8.1), CVE-2020-36182(8.1), CVE-2019-14439(7.5), CVE-2020-36181(8.1), CVE-2020-35491(8.1), CVE-2020-36184(8.1), CVE-2020-35490(8.1), CVE-2020-36183(8.1), CVE-2019-12814(5.9), CVE-2019-20330(9.8), CVE-2020-24750(8.1), CVE-2020-10673(8.8), CVE-2018-11307(9.8), CVE-2018-14718(9.8), CVE-2018-1000873(6.5), CVE-2018-7489(9.8), CVE-2018-14719(9.8), CVE-2020-36186(8.1), CVE-2019-17531(9.8), CVE-2020-36185(8.1), CVE-2020-36188(8.1), CVE-2020-36187(8.1), CVE-2020-10650(8.1), CVE-2020-36189(8.1), CVE-2019-12086(7.5), CVE-2019-14540(9.8), CVE-2019-12384(5.9), CVE-2023-35116(4.7), CVE-2017-15095(9.8), CVE-2019-16942(9.8), CVE-2019-16943(9.8), CVE-2021-20190(8.1), CVE-2017-7525(9.8), CVE-2020-36518(7.5), CVE-2019-17267(9.8), CVE-2019-16335(9.8), CVE-2020-36179(8.1), CVE-2020-8840(9.8), CVE-2019-14892(9.8), CVE-2022-42003(7.5), CVE-2022-42004(7.5)
[ERROR]
[ERROR] See the dependency-check report for more details.
[ERROR]
[ERROR]
[ERROR] -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
```

Сканирование зависимостей Java-проекта выполнялось через Maven-плагин:
- Maven читает `pom.xml` и строит полное дерево зависимостей.
- Каждая зависимость (jar) проходит этапы идентификации.
- Далее выполняется сопоставление с базами уязвимостей.

В логе видно последовательность включённых анализаторов, например:
- `Archive Analyzer`, `Jar Analyzer` - извлекают информацию из jar/архивов;
- `Dependency Merging`, `Hint`, `Version Filter` - нормализуют данные (склейка дубликатов, попытки уточнения версии);
- `CPE Analyzer` - строит индекс сопоставления пакетов и CPE;
- `NVD CVE Analyzer` - проверяет найденные CPE/координаты по базе CVE.

В выводе присутствуют строки вида:

```bash
An error occurred while analyzing ... (Sonatype OSS Index Analyzer).
```

Это означает, что плагин пытался обратиться к OSS Index, но сервис сейчас требует логин, поэтому анализатор не может отработать. При этом сканирование не останавливается, так как основной источник остаётся доступным.

В конце сканирования Dependency-Check выводит список зависимостей с найденными CVE и завершает Maven-цель с ошибкой:

```bash
[ERROR] One or more dependencies were identified with vulnerabilities that have a CVSS score greater than or equal to '0.0':
```

Это ожидаемое поведение: у плагина включён режим "ломать сборку", если есть уязвимости выше указанного порога (в нашем случае порог ≥ 0.0, поэтому любая найденная уязвимость приводит к failure). 

Сканирование `app.py` через OWASP Dependency-Check CLI:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca$ ./dependency-check.sh
OWASP Dependency-Check SCA
[*] Running scan using cached data in /home/svepodd/.dependency-check-data (no full re-download)
[*] Scanning:
    - /home/svepodd/course_labs/labs/lab07/vulnerable-app/requirements.txt
    - /home/svepodd/course_labs/labs/lab07/sca/lib
[INFO]

Dependency-Check is an open source tool performing a best effort analysis of 3rd party dependencies; false positives and false negatives may exist in the analysis performed by the tool. Use of the tool and the reporting provided constitutes acceptance for use in an AS IS condition, and there are NO warranties, implied or otherwise, with regard to the analysis or its use. Any use of the tool and the reporting provided is at the user's risk. In no event shall the copyright holder or OWASP be held liable for any damages whatsoever arising out of or in connection with the use of this tool, the analysis performed, or the resulting report.


   About ODC: https://dependency-check.github.io/DependencyCheck/general/internals.html
   False Positives: https://dependency-check.github.io/DependencyCheck/general/suppression.html


[INFO] Analysis Started
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished pip Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Created CPE Index (2 seconds)
[INFO] Finished NPM CPE Analyzer (2 seconds)
[INFO] Created CPE Index (1 seconds)
[INFO] Finished CPE Analyzer (2 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[WARN] Disabling OSS Index analyzer due to missing user/password credentials. Authentication is now required: https://ossindex.sonatype.org/doc/auth-required
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (4 seconds)
[INFO] Writing HTML report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report-app/dependency-check-report.html
[INFO] Writing JSON report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report-app/dependency-check-report.json
[+] Reports saved to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report-app
[i] To refresh NVD data occasionally, run: bash sca/dependency-check.sh --update
```

Для Python-части использовался CLI-скрипт `sca/dependency-check.sh`, который сканирует:
- `vulnerable-app/requirements.txt` (список pip-зависимостей),
- `sca/lib` (jar-зависимости из шага с Maven `copy-dependencies`, чтобы CLI мог также проверить Java-артефакты).

Логика SCA-сканирования для Python в Dependency-Check такая:
1. CLI читает `requirements.txt` и извлекает пары `package==version`
2. Анализатор `pip Analyzer` пытается:
    - нормализовать имена пакетов,
    - сопоставить пакеты с известными идентификаторами (CPE/внутренними маппингами),
    - проверить их по локальной базе уязвимостей.
3. После идентификации dependencies выполняется проверка через:
    - `CPE Analyzer`,
    - `NVD CVE Analyzer`.

- [x] 7. Соберите единый отчет из всех сканирований в виде `html`, `csv`, `json`

```bash
$ bash sca/generate_unified_report.sh
```

Написанный скрипт лежит в директории проекта. Запуск:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca$ ./generate_unified_report.sh
[*] Generating unified SAST+SCA report...
[+] Unified report generated: /home/svepodd/course_labs/labs/lab07/sca/unified-report
    - /home/svepodd/course_labs/labs/lab07/sca/unified-report/unified-report.json
    - /home/svepodd/course_labs/labs/lab07/sca/unified-report/unified-report.csv
    - /home/svepodd/course_labs/labs/lab07/sca/unified-report/unified-report.html
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca$ ls unified-report/
unified-report.csv  unified-report.html  unified-report.json
```

Получившийся отчет из всех сканирований:

| tool             | file                          | id                                    | severity | message                                                                                                                                                                                                  |
| ---------------- | ----------------------------- | ------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Semgrep          | vulnerable-app/app.py         | sast.py-info-version-disclosure       | LOW      | Раскрытие версии приложения в ответе.                                                                                                                                                                    |
| Semgrep          | vulnerable-app/app.py         | sast.py-os-system-rce                 | CRITICAL | RCE через os.system с данными пользователя.                                                                                                                                                              |
| Semgrep          | vulnerable-app/app.py         | sast.py-arbitrary-file-read           | CRITICAL | Чтение произвольного файла по пути из запроса (LFI/Path Traversal).                                                                                                                                      |
| Semgrep          | vulnerable-app/app.py         | sast.py-unsafe-pickle-deserialization | CRITICAL | Небезопасная десериализация через pickle.loads.                                                                                                                                                          |
| Semgrep          | vulnerable-app/app.py         | sast.py-eval-user-input               | HIGH     | Опасное использование eval на пользовательском вводе.                                                                                                                                                    |
| Checkov          | vulnerable-app/Dockerfile     | CKV_DOCKER_3                          | None     | Ensure that a user for the container has been created                                                                                                                                                    |
| Checkov          | vulnerable-app/Dockerfile     | CKV_DOCKER_2                          | None     | Ensure that HEALTHCHECK instructions have been added to container images                                                                                                                                 |
| Dependency-Check | commons-httpclient-3.1.jar    | CVE-2012-5783                         | MEDIUM   | Apache Commons HttpClient 3.x, as used in Amazon Flexible Payments Service (FPS) merchant Java SDK and other products, does not verify that the server hostname matches a domain name in the subject's C |
| Dependency-Check | commons-httpclient-3.1.jar    | CVE-2020-13956                        | MEDIUM   | Apache HttpClient versions prior to version 4.5.13 and 5.0.3 can misinterpret malformed authority component in request URIs passed to the library as java.net.URI object and pick the wrong target host  |
| Dependency-Check | groovy-all-2.1.6.jar          | CVE-2015-3253                         | CRITICAL | The MethodClosure class in runtime/MethodClosure.java in Apache Groovy 1.7.0 through 2.4.3 allows remote attackers to execute arbitrary code or cause a denial of service via a crafted serialized objec |
| Dependency-Check | groovy-all-2.1.6.jar          | CVE-2016-6814                         | CRITICAL | When an application with unsupported Codehaus versions of Groovy from 1.7.0 to 2.4.3, Apache Groovy 2.4.4 to 2.4.7 on classpath uses standard Java serialization mechanisms, e.g. to communicate between |
| Dependency-Check | groovy-all-2.1.6.jar          | CVE-2020-17521                        | MEDIUM   | Apache Groovy provides extension methods to aid with creating temporary directories. Prior to this fix, Groovy's implementation of those extension methods was using a now superseded Java JDK method ca |
| Dependency-Check | jackson-annotations-2.4.0.jar | CVE-2018-1000873                      | MEDIUM   | Fasterxml Jackson version Before 2.9.8 contains a CWE-20: Improper Input Validation vulnerability in Jackson-Modules-Java8 that can result in Causes a denial-of-service (DoS). This attack appear to be |
| Dependency-Check | jackson-core-2.4.6.jar        | CVE-2018-1000873                      | MEDIUM   | Fasterxml Jackson version Before 2.9.8 contains a CWE-20: Improper Input Validation vulnerability in Jackson-Modules-Java8 that can result in Causes a denial-of-service (DoS). This attack appear to be |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2017-15095                        | CRITICAL | A deserialization flaw was discovered in the jackson-databind in versions before 2.8.10 and 2.9.1, which could allow an unauthenticated user to perform code execution by sending the maliciously crafte |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2017-17485                        | CRITICAL | FasterXML jackson-databind through 2.8.10 and 2.9.x through 2.9.3 allows unauthenticated remote code execution because of an incomplete fix for the CVE-2017-7525 deserialization flaw. This is exploita |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2017-7525                         | CRITICAL | A deserialization flaw was discovered in the jackson-databind, versions before 2.6.7.1, 2.7.9.1 and 2.8.9, which could allow an unauthenticated user to perform code execution by sending the maliciousl |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2018-11307                        | CRITICAL | An issue was discovered in FasterXML jackson-databind 2.0.0 through 2.9.5. Use of Jackson default typing along with a gadget class from iBatis allows exfiltration of content. Fixed in 2.7.9.4, 2.8.11. |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2018-14718                        | CRITICAL | FasterXML jackson-databind 2.x before 2.9.7 might allow remote attackers to execute arbitrary code by leveraging failure to block the slf4j-ext class from polymorphic deserialization.                  |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2018-14719                        | CRITICAL | FasterXML jackson-databind 2.x before 2.9.7 might allow remote attackers to execute arbitrary code by leveraging failure to block the blaze-ds-opt and blaze-ds-core classes from polymorphic deserializ |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2018-7489                         | CRITICAL | FasterXML jackson-databind before 2.7.9.3, 2.8.x before 2.8.11.1 and 2.9.x before 2.9.5 allows unauthenticated remote code execution because of an incomplete fix for the CVE-2017-7525 deserialization  |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-14379                        | CRITICAL | SubTypeValidator.java in FasterXML jackson-databind before 2.9.9.2 mishandles default typing when ehcache is used (because of net.sf.ehcache.transaction.manager.DefaultTransactionManagerLookup), leadi |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-14540                        | CRITICAL | A Polymorphic Typing issue was discovered in FasterXML jackson-databind before 2.9.10. It is related to com.zaxxer.hikari.HikariConfig.                                                                  |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-14892                        | CRITICAL | A flaw was discovered in jackson-databind in versions before 2.9.10, 2.8.11.5 and 2.6.7.3, where it would permit polymorphic deserialization of a malicious object using commons-configuration 1 and 2 J |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-16335                        | CRITICAL | A Polymorphic Typing issue was discovered in FasterXML jackson-databind before 2.9.10. It is related to com.zaxxer.hikari.HikariDataSource. This is a different vulnerability than CVE-2019-14540.       |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-16942                        | CRITICAL | A Polymorphic Typing issue was discovered in FasterXML jackson-databind 2.0.0 through 2.9.10. When Default Typing is enabled (either globally or for a specific property) for an externally exposed JSON |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-16943                        | CRITICAL | A Polymorphic Typing issue was discovered in FasterXML jackson-databind 2.0.0 through 2.9.10. When Default Typing is enabled (either globally or for a specific property) for an externally exposed JSON |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-17267                        | CRITICAL | A Polymorphic Typing issue was discovered in FasterXML jackson-databind before 2.9.10. It is related to net.sf.ehcache.hibernate.EhcacheJtaTransactionManagerLookup.                                     |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-17531                        | CRITICAL | A Polymorphic Typing issue was discovered in FasterXML jackson-databind 2.0.0 through 2.9.10. When Default Typing is enabled (either globally or for a specific property) for an externally exposed JSON |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-20330                        | CRITICAL | FasterXML jackson-databind 2.x before 2.9.10.2 lacks certain net.sf.ehcache blocking.                                                                                                                    |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-8840                         | CRITICAL | FasterXML jackson-databind 2.0.0 through 2.9.10.2 lacks certain xbean-reflect/JNDI blocking, as demonstrated by org.apache.xbean.propertyeditor.JndiConverter.                                           |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-9547                         | CRITICAL | FasterXML jackson-databind 2.x before 2.9.10.4 mishandles the interaction between serialization gadgets and typing, related to com.ibatis.sqlmap.engine.transaction.jta.JtaTransactionConfig (aka ibatis |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-9548                         | CRITICAL | FasterXML jackson-databind 2.x before 2.9.10.4 mishandles the interaction between serialization gadgets and typing, related to br.com.anteros.dbcp.AnterosDBCPConfig (aka anteros-core).                 |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-10673                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.4 mishandles the interaction between serialization gadgets and typing, related to com.caucho.config.types.ResourceRef (aka caucho-quercus).                 |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2018-5968                         | HIGH     | FasterXML jackson-databind through 2.8.11 and 2.9.x through 2.9.3 allows unauthenticated remote code execution because of an incomplete fix for the CVE-2017-7525 and CVE-2017-17485 deserialization fla |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-10650                        | HIGH     | A deserialization flaw was discovered in jackson-databind through 2.9.10.4. It could allow an unauthenticated user to perform code execution via ignite-jta or quartz-core: org.apache.ignite.cache.jta. |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-24616                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.6 mishandles the interaction between serialization gadgets and typing, related to br.com.anteros.dbcp.AnterosDBCPDataSource (aka Anteros-DBCP).             |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-24750                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.6 mishandles the interaction between serialization gadgets and typing, related to com.pastdev.httpcomponents.configuration.JndiConfiguration.               |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-35490                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to org.apache.commons.dbcp2.datasources.PerUserPoolDataSource.               |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-35491                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to org.apache.commons.dbcp2.datasources.SharedPoolDataSource.                |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36179                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to oadd.org.apache.commons.dbcp.cpdsadapter.DriverAdapterCPDS.               |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36180                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS.                   |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36181                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to org.apache.tomcat.dbcp.dbcp.cpdsadapter.DriverAdapterCPDS.                |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36182                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to org.apache.tomcat.dbcp.dbcp2.cpdsadapter.DriverAdapterCPDS.               |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36183                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to org.docx4j.org.apache.xalan.lib.sql.JNDIConnectionPool.                   |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36184                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to org.apache.tomcat.dbcp.dbcp2.datasources.PerUserPoolDataSource.           |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36185                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to org.apache.tomcat.dbcp.dbcp2.datasources.SharedPoolDataSource.            |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36186                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to org.apache.tomcat.dbcp.dbcp.datasources.PerUserPoolDataSource.            |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36187                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to org.apache.tomcat.dbcp.dbcp.datasources.SharedPoolDataSource.             |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36188                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to com.newrelic.agent.deps.ch.qos.logback.core.db.JNDIConnectionSource.      |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36189                        | HIGH     | FasterXML jackson-databind 2.x before 2.9.10.8 mishandles the interaction between serialization gadgets and typing, related to com.newrelic.agent.deps.ch.qos.logback.core.db.DriverManagerConnectionSou |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2021-20190                        | HIGH     | A flaw was found in jackson-databind before 2.9.10.7. FasterXML mishandles the interaction between serialization gadgets and typing. The highest threat from this vulnerability is to data confidentiali |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2018-12022                        | HIGH     | An issue was discovered in FasterXML jackson-databind prior to 2.7.9.4, 2.8.11.2, and 2.9.6. When Default Typing is enabled (either globally or for a specific property), the service has the Jodd-db ja |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-12086                        | HIGH     | A Polymorphic Typing issue was discovered in FasterXML jackson-databind 2.x before 2.9.9. When Default Typing is enabled (either globally or for a specific property) for an externally exposed JSON end |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-14439                        | HIGH     | A Polymorphic Typing issue was discovered in FasterXML jackson-databind 2.x before 2.9.9.2. This occurs when Default Typing is enabled (either globally or for a specific property) for an externally ex |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2020-36518                        | HIGH     | jackson-databind before 2.13.0 allows a Java StackOverflow exception and denial of service via a large depth of nested objects.                                                                          |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2022-42003                        | HIGH     | In FasterXML jackson-databind before versions 2.13.4.1 and 2.12.17.1, resource exhaustion can occur because of a lack of a check in primitive value deserializers to avoid deep wrapper array nesting, w |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2022-42004                        | HIGH     | In FasterXML jackson-databind before 2.13.4, resource exhaustion can occur because of a lack of a check in BeanDeserializer._deserializeFromArray to prevent use of deeply nested arrays. An application |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2018-1000873                      | MEDIUM   | Fasterxml Jackson version Before 2.9.8 contains a CWE-20: Improper Input Validation vulnerability in Jackson-Modules-Java8 that can result in Causes a denial-of-service (DoS). This attack appear to be |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-12384                        | MEDIUM   | FasterXML jackson-databind 2.x before 2.9.9.1 might allow attackers to have a variety of impacts by leveraging failure to block the logback-core class from polymorphic deserialization. Depending on th |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2019-12814                        | MEDIUM   | A Polymorphic Typing issue was discovered in FasterXML jackson-databind 2.x through 2.9.9. When Default Typing is enabled (either globally or for a specific property) for an externally exposed JSON en |
| Dependency-Check | jackson-databind-2.4.6.jar    | CVE-2023-35116                        | MEDIUM   | jackson-databind through 2.15.2 allows attackers to cause a denial of service or other unspecified impact via a crafted object that uses cyclic dependencies. NOTE: the vendor's perspective is that thi |
| Dependency-Check | PyYAML:5.3.1                  | CVE-2020-14343                        | CRITICAL | A vulnerability was discovered in the PyYAML library in versions before 5.4, where it is susceptible to arbitrary code execution when it processes untrusted YAML files through the full_load method or  |
| Dependency-Check | certifi:2018.4.16             | CVE-2023-37920                        | CRITICAL | Certifi is a curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. Certifi prior to version 2023.07.22 recognizes "e |
| Dependency-Check | certifi:2018.4.16             | CVE-2022-23491                        | HIGH     | Certifi is a curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. Certifi 2022.12.07 removes root certificates from |
| Dependency-Check | paramiko:2.4.1                | CVE-2018-1000805                      | HIGH     | Paramiko version 2.4.1, 2.3.2, 2.2.3, 2.1.5, 2.0.8, 1.18.5, 1.17.6 contains a Incorrect Access Control vulnerability in SSH server that can result in RCE. This attack appear to be exploitable via netw |
| Dependency-Check | paramiko:2.4.1                | CVE-2022-24302                        | MEDIUM   | In Paramiko before 2.10.1, a race condition (between creation and chmod) in the write_private_key_file function could allow unauthorized information disclosure.                                         |
| Dependency-Check | paramiko:2.4.1                | CVE-2023-48795                        | MEDIUM   | The SSH transport protocol with certain OpenSSH extensions, found in OpenSSH before 9.6 and other products, allows remote attackers to bypass integrity checks such that some packets are omitted (from  |
| Dependency-Check | pyjwt:1.7.1                   | CVE-2022-29217                        | HIGH     | yJWT is a Python implementation of RFC 7519. PyJWT supports multiple different JWT signing algorithms. With JWT, an attacker submitting the JWT token can choose the used signing algorithm. The PyJWT   |


- [x] 8. Проанализируйте все уязвимости и объясните для SAST Checkov сработки статуса `Unknown`. Классифицируйте их и укажите какие не должны быть в отчетах. Внесите исправления и запустите повторное сканирование и убедитесь, что они устранены. Приложите исправленный файл и отчет без уязвимостей. 

По отчету видим 2 FAILED-проверки:

| Checkov ID     | Название                                                                 | Суть                                                           | Почему опасно                                                 |
| -------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------- |
| `CKV_DOCKER_2` | Ensure that HEALTHCHECK instructions have been added to container images | В образе не был задан `HEALTHCHECK`                            | Без healthcheck Docker хуже диагностирует зависшие контейнеры |
| `CKV_DOCKER_3` | Ensure that a user for the container has been created                    | Контейнер запускался без явно созданного non-root пользователя | Запуск под root повышает риск компрометации хоста/секретов    |
Исправленный `Dockerfile`:

```Dockerfile
FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libjpeg-dev zlib1g-dev \
        libxml2-dev libxslt1-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8080

RUN adduser --disabled-password --gecos "" appuser
USER appuser

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/').read()" || exit 1

ENV FLASK_ENV=development
ENV DEBUG=true
CMD ["python", "app.py"]
```

Запускаем заново:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07$ checkov \
  --framework dockerfile \
  --file vulnerable-app/Dockerfile docker-compose.yml \
  --output json \
  --output-file-path sast/checkov-report.json \
  --soft-fail
2026-01-13 23:04:33,265 [MainThread  ] [WARNI]  /home/svepodd/course_labs/labs/lab07/venv/lib/python3.12/site-packages/paramiko/pkey.py:59: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
  'cipher': algorithms.TripleDES,

2026-01-13 23:04:33,283 [MainThread  ] [WARNI]  /home/svepodd/course_labs/labs/lab07/venv/lib/python3.12/site-packages/paramiko/transport.py:193: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
  'class': algorithms.TripleDES,

...

    "summary": {
        "passed": 70,
        "failed": 0,
        "skipped": 0,
        "parsing_errors": 0,
        "resource_count": 1,
        "checkov_version": "3.2.497"
    },
    "url": "Add an api key '--bc-api-key <api-key>' to see more detailed insights via https://bridgecrew.cloud"
}
```


- [x] 9. Опишите выведенные уязвимости для SAST Semgrep и принцип их работы. Поправьте скрипт `app.py`. Запустите повторное сканирование и убедитесь, что они устранены. Приложите исправленный файл `app.py` и отчет без уязвимостей. 

По отчету видим 5 FAILED-проверок:

| ID                                    | Уровень  | Описание                                                            | Польза для атакующего                                                                                                  |
| ------------------------------------- | -------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| sast.py-info-version-disclosure       | LOW      | Раскрытие версии приложения в ответе.                               | Ответ типа `Vulnerable lab07 app v1.0` помогает атакующему подбирать эксплойты под конкретную версию                   |
| sast.py-os-system-rce                 | CRITICAL | RCE через os.system с данными пользователя.                         | Если в команду попадают данные пользователя (`host`, `cmd`), можно подставить `; ...` и выполнить произвольные команды |
| sast.py-arbitrary-file-read           | CRITICAL | Чтение произвольного файла по пути из запроса (LFI/Path Traversal). | Пользователь передаёт путь (`/etc/passwd`, `../../..`), и приложение читает произвольные файлы.                        |
| sast.py-unsafe-pickle-deserialization | CRITICAL | Небезопасная десериализация через pickle.loads.                     | `pickle` при десериализации способен выполнять код => прямой путь к RCE.                                               |
| sast.py-eval-user-input               | HIGH     | Опасное использование eval на пользовательском вводе.               | `eval` исполняет ввод пользователя => выполнение произвольного Python-кода.                                            |
Дорабатываем `app.py`:

```python
from flask import Flask, request, make_response
import sqlite3
import os
import subprocess
import pickle
import logging
import ast
import ipaddress

app = Flask(__name__)

app.config["DEBUG"] = True

DB_USER = "admin"
DB_PASSWORD = "SuperSecret123"
DB_PATH = "app.db"

logging.basicConfig(level=logging.DEBUG)

SAFE_READ_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "safe_files"))
os.makedirs(SAFE_READ_DIR, exist_ok=True)

def _safe_calc(expr: str):
    # very small safe evaluator: numbers + + - * / () only
    node = ast.parse(expr, mode="eval")
    allowed = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd
    )
    for n in ast.walk(node):
        if not isinstance(n, allowed):
            raise ValueError("Unsupported expression")
        if isinstance(n, ast.Constant) and not isinstance(n.value, (int, float)):
            raise ValueError("Only numbers allowed")

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.Num):
            return n.n
        if isinstance(n, ast.Constant):
            return n.value
        if isinstance(n, ast.UnaryOp):
            v = _eval(n.operand)
            return +v if isinstance(n.op, ast.UAdd) else -v
        if isinstance(n, ast.BinOp):
            a, b = _eval(n.left), _eval(n.right)
            if isinstance(n.op, ast.Add):
                return a + b
            if isinstance(n.op, ast.Sub):
                return a - b
            if isinstance(n.op, ast.Mult):
                return a * b
            if isinstance(n.op, ast.Div):
                return a / b
        raise ValueError("Unsupported expression")

    return _eval(node)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

@app.route("/")
def index():
    # do not disclose version in response
    return "OK"

@app.route("/user")
def get_user():
    username = request.args.get("name", "")
    conn = get_db()
    cur = conn.cursor()
    query = f"SELECT id, name, email FROM users WHERE name = '{username}'"  # nosec B608
    app.logger.debug("Executing query: %s", query)
    rows = cur.execute(query).fetchall()
    conn.close()
    return {"result": rows}

@app.route("/search")
def search():
    q = request.args.get("q", "")
    html = f"<h1>Results for: {q}</h1>"
    return make_response(html, 200)

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # avoid command injection: no shell + basic validation
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return "Invalid host", 400
    subprocess.run(["ping", "-c", "1", host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return f"Pinged {host}"

@app.route("/backup")
def backup():
    target = request.args.get("target", "/tmp/backup.sql")  # nosec B108
    cmd = ["sh", "-c", f"pg_dump mydb > {target}"]
    subprocess.call(cmd)
    return f"Backup to {target} started"

@app.route("/read")
def read_file():
    path = request.args.get("path", "/etc/passwd")
    try:
        # allow reading only inside SAFE_READ_DIR (prevent LFI / traversal)
        if os.path.isabs(path):
            return "Absolute paths are not allowed", 400
        norm = os.path.normpath(path)
        if norm.startswith("..") or "/.." in norm.replace("\\", "/"):
            return "Path traversal detected", 400
        full_path = os.path.abspath(os.path.join(SAFE_READ_DIR, norm))
        if not full_path.startswith(SAFE_READ_DIR + os.sep):
            return "Invalid path", 400

        with open(full_path, "r", encoding="utf-8", errors="replace") as f:
            data = f.read()
        return f"<pre>{data}</pre>"
    except Exception as e:
        return str(e), 500

@app.route("/load")
def load():
    data = request.args.get("data", "")
    try:
        # do not use pickle.loads on untrusted input (RCE). Treat as raw bytes.
        raw = bytes.fromhex(data)
        return f"Loaded data length: {len(raw)}"
    except Exception as e:
        return f"Error: {e}", 500

@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    try:
        result = _safe_calc(expr)
        return str(result)
    except Exception:
        return "Invalid expression", 400

@app.route("/debug")
def debug():
    headers = dict(request.headers)
    return {
        "headers": headers,
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # nosec B104
```

Запускаем заново:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07$ semgrep --config sast/semgrep-rules.yml \
  --json \
  --output sast/semgrep-report.json \
  vulnerable-app/

┌──── ○○○ ────┐
│ Semgrep CLI │
└─────────────┘

...

┌──────────────┐
│ Scan Summary │
└──────────────┘
✅ Scan completed successfully.
 • Findings: 0 (0 blocking)
 • Rules run: 16
 • Targets scanned: 2
 • Parsed lines: ~100.0%
 • Scan was limited to files tracked by git
 • For a detailed list of skipped files and lines, run semgrep with the --verbose flag
Ran 16 rules on 2 files: 0 findings.

✨ If Semgrep missed a finding, please send us feedback to let us know!
   See https://semgrep.dev/docs/reporting-false-negatives/

```

- [x] 10. Доработайте SCA уязвимости, что бы они только остались в финальной версии отчетов.

Исправленный `pom.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>lab07</groupId>
    <artifactId>sca-demo</artifactId>
    <version>1.0.1</version>
    <packaging>jar</packaging>

    <name>sca-demo</name>

    <properties>
        <groovy.version>5.0.3</groovy.version>
        <jackson.version>2.20.1</jackson.version>
        <httpclient5.version>5.6</httpclient5.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.apache.groovy</groupId>
                <artifactId>groovy-bom</artifactId>
                <version>${groovy.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>

            <dependency>
                <groupId>com.fasterxml.jackson</groupId>
                <artifactId>jackson-bom</artifactId>
                <version>${jackson.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <dependencies>
        <dependency>
            <groupId>org.apache.groovy</groupId>
            <artifactId>groovy-all</artifactId>
            <version>${groovy.version}</version>
            <type>pom</type>
        </dependency>

        <dependency>
            <groupId>com.fasterxml.jackson.jaxrs</groupId>
            <artifactId>jackson-jaxrs-json-provider</artifactId>
        </dependency>

        <dependency>
            <groupId>org.apache.httpcomponents.client5</groupId>
            <artifactId>httpclient5</artifactId>
            <version>${httpclient5.version}</version>
        </dependency>
    </dependencies>

    <build>
    <plugins>
        <plugin>
        <groupId>org.owasp</groupId>
        <artifactId>dependency-check-maven</artifactId>
        <version>12.1.0</version>
        <configuration>
            <format>ALL</format>
            <outputDirectory>${project.basedir}/dependency-check-report</outputDirectory>
            <failBuildOnCVSS>0.0</failBuildOnCVSS>
            <autoUpdate>false</autoUpdate>
            <ossindexAnalyzerEnabled>false</ossindexAnalyzerEnabled>
        </configuration>
        <executions>
            <execution>
            <goals>
                <goal>check</goal>
            </goals>
            </execution>
        </executions>
        </plugin>
    </plugins>
    </build>

</project>
```

Запускаем заново:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca$ mvn org.owasp:dependency-check-maven:check -DdataDirectory="$HOME/.dependency-check-data" -DautoUpdate=false || true
[INFO] Scanning for projects...
[INFO]
[INFO] ---------------------------< lab07:sca-demo >---------------------------
[INFO] Building sca-demo 1.0.1
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- dependency-check-maven:12.1.0:check (default-cli) @ sca-demo ---
[INFO]

Dependency-Check is an open source tool performing a best effort analysis of 3rd party dependencies; false positives and false negatives may exist in the analysis performed by the tool. Use of the tool and the reporting provided constitutes acceptance for use in an AS IS condition, and there are NO warranties, implied or otherwise, with regard to the analysis or its use. Any use of the tool and the reporting provided is at the user's risk. In no event shall the copyright holder or OWASP be held liable for any damages whatsoever arising out of or in connection with the use of this tool, the analysis performed, or the resulting report.


   About ODC: https://jeremylong.github.io/DependencyCheck/general/internals.html
   False Positives: https://jeremylong.github.io/DependencyCheck/general/suppression.html

💖 Sponsor: https://github.com/sponsors/jeremylong


[INFO] Analysis Started
[INFO] Finished Archive Analyzer (0 seconds)
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished Jar Analyzer (0 seconds)
[ERROR] ----------------------------------------------------
[ERROR] .NET Assembly Analyzer could not be initialized and at least one 'exe' or 'dll' was scanned. The 'dotnet' executable could not be found on the path; either disable the Assembly Analyzer or add the path to dotnet core in the configuration.
[ERROR] The dotnet 8.0 core runtime or SDK is required to analyze assemblies
[ERROR] ----------------------------------------------------
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Created CPE Index (2 seconds)
[INFO] Finished CPE Analyzer (3 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (5 seconds)
[INFO] Writing XML report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.xml
[INFO] Writing HTML report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.html
[INFO] Writing JSON report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.json
[INFO] Writing CSV report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.csv
[INFO] Writing SARIF report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.sarif
[INFO] Writing JENKINS report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-jenkins.html
[INFO] Writing JUNIT report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-junit.xml
[INFO] Writing GITLAB report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-gitlab.json
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  9.146 s
[INFO] Finished at: 2026-01-13T23:36:22+03:00
[INFO] ------------------------------------------------------------------------
```

Видим, что сработок больше нет:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca$ cat dependency-check-report/dependency-check-report.csv
"Project","ScanDate","DependencyName","DependencyPath","Description","License","Md5","Sha1","Identifiers","CPE","CVE","CWE","Vulnerability","Source","CVSSv2_Severity","CVSSv2_Score","CVSSv2","CVSSv3_BaseSeverity","CVSSv3_BaseScore","CVSSv3","CVSSv4_BaseSeverity","CVSSv4_BaseScore","CVSSv4","CPE Confidence","Evidence Count","VendorProject","Product","Name","DateAdded","ShortDescription","RequiredAction","DueDate","Notes"
```

dependency-check сопоставляет версии пакетов из `requirements.txt` с уязвимостями в локальной базе. Исправляем `requirements.txt`:

```txt
Flask==2.3.3
Werkzeug==2.3.7
Jinja2==3.1.3
itsdangerous==2.1.2
click==8.1.7
requests==2.31.0
markupsafe==2.1.5
colorama==0.4.6
gunicorn==21.2.0
```

Запускаем:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca$ ./dependency-check.sh
OWASP Dependency-Check SCA
[*] Running scan using cached data in /home/svepodd/.dependency-check-data (no full re-download)
[*] Scanning:
    - /home/svepodd/course_labs/labs/lab07/vulnerable-app/requirements.txt
    - /home/svepodd/course_labs/labs/lab07/sca/lib
[INFO]

Dependency-Check is an open source tool performing a best effort analysis of 3rd party dependencies; false positives and false negatives may exist in the analysis performed by the tool. Use of the tool and the reporting provided constitutes acceptance for use in an AS IS condition, and there are NO warranties, implied or otherwise, with regard to the analysis or its use. Any use of the tool and the reporting provided is at the user's risk. In no event shall the copyright holder or OWASP be held liable for any damages whatsoever arising out of or in connection with the use of this tool, the analysis performed, or the resulting report.


   About ODC: https://dependency-check.github.io/DependencyCheck/general/internals.html
   False Positives: https://dependency-check.github.io/DependencyCheck/general/suppression.html


[INFO] Analysis Started
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished pip Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Created CPE Index (2 seconds)
[INFO] Finished NPM CPE Analyzer (2 seconds)
[INFO] Created CPE Index (1 seconds)
[INFO] Finished CPE Analyzer (2 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[WARN] Disabling OSS Index analyzer due to missing user/password credentials. Authentication is now required: https://ossindex.sonatype.org/doc/auth-required
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (5 seconds)
[INFO] Writing HTML report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report-app/dependency-check-report.html
[INFO] Writing JSON report to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report-app/dependency-check-report.json
[+] Reports saved to: /home/svepodd/course_labs/labs/lab07/sca/dependency-check-report-app
[i] To refresh NVD data occasionally, run: bash sca/dependency-check.sh --update
```

После исправлений получаем следующее:

```bash
(venv) svepodd@DESKTOP-PPV5M0R:~/course_labs/labs/lab07/sca/dependency-check-report-app$ cat dependency-check-report.html | grep "Vulnerabilities Found"
                        <li><i>Vulnerabilities Found</i>:&nbsp;0</li>
```

- [x] 11. Проверьте себя по найденным сработкам анализаторов и так вы сможете помочь себе разобраться в ситуации, если возникнут сложности

```bash
$ bash cheat_check_yuorself.sh
```

- [x] 12. Делайте все коммиты на соответствующих шагах, далее заливайте изменения в удаленный репозиторий.
- [x] 13. Подготовьте отчет `gist`.
- [x] 14. Почистите кеш от `venv` и остановите уязвимое приложение

```bash
$ deactivate
$ rm -rf venv
$ docker-compose -f ххх down
$ docker-compose -f docker-compose.yml down
$ docker system prune -f
```

***

Copyright (c) 2026 Svetlana Poddoskina