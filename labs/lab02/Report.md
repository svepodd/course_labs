<div align="center">
<h1><a id="intro">Лабораторная работа №2</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Поддоскина С.К.-8b9aff" alt="Contributor Badge"></a></div>

- [x] 1. Выведите на терминале и проанализируйте следующие команды консоли

 `who | wc -l` показывает количество активных пользовательских сессий.

```bash
svepodd@svepodd-VirtualBox:~$ who | wc -l
2
```

`id` выводит идентификатор пользователя (`uid`), основную группу (`gid`) и список дополнительных групп.

```bash
svepodd@svepodd-VirtualBox:~$ id
uid=1000(svepodd) gid=1000(svepodd) groups=1000(svepodd),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),114(lpadmin),984(docker)
```

`whoami` выводит имя текущего пользователя.

```bash
svepodd@svepodd-VirtualBox:~$ whoami
svepodd
```

`hostnamectl` показывает информацию о хосте и системе.

```bash
svepodd@svepodd-VirtualBox:~$ hostnamectl
 Static hostname: svepodd-VirtualBox
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 0e38ef746f8e4e0b8c1dc40d39ede5a1
         Boot ID: e14b08d6056140e48157feff15ec444d
  Virtualization: oracle
Operating System: Ubuntu 24.04.1 LTS              
          Kernel: Linux 6.14.0-35-generic
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
Firmware Version: VirtualBox
   Firmware Date: Fri 2006-12-01
    Firmware Age: 19y
```

- [x] 2. Выведите утилитой `tree` список вложенности дерева директорий для каталога своего пользователя. Далее используйте `ls -a` и укажите отличие от `ls -l`.

`tree` показывает иерархию каталогов в виде дерева

```bash
svepodd@svepodd-VirtualBox:~$ tree
.
├── course_labs
│   ├── artifacts
│   │   ├── cheetsheet
│   │   │   ├── Docker_Image_Security_Best_Practices.pdf
│   │   │   └── gitscm.jpg
│   │   ├── exmpls
│   │   │   ├── Аналитический отчет по уязвимости PrintNightmare.pdf
│   │   │   ├── Пример - Multisignature - Безопасности криптовалютных платежей.pdf
│   │   │   └── Пример_аналитических_отчетов_по_задачам_ИБ.pdf
│   │   ├── owasp
│   │   │   ├── OWASP_Top_10_CICD_Risks.pdf
│   │   │   ├── Авторизация (Authorization).pdf
│   │   │   ├── Атаки на клиентов (Client-side Attacks).pdf
│   │   │   ├── Аутентификация (Authentication).pdf
│   │   │   ├── Выполнение кода (Command Execution).pdf
│   │   │   ├── Логические атаки (Logical Attacks).pdf
│   │   │   └── Разглашение информации (Information Disclosure).pdf
│   │   └── ppt
│   │       └── Лекция_Управление Рисками ИБ_intro.pdf
│   ├── assets
│   │   ├── logotype
│   │   │   └── logo.jpg
│   │   └── style
│   │       └── style.css
│   ├── CODE_OF_CONDUCT.md
│   ├── CONTRIBUTING.md
│   ├── labs
│   │   ├── lab01
│   │   │   ├── README.md
│   │   │   └── typersteel.py
│   │   ├── lab02
│   │   │   ├── exmpl_hello.py
│   │   │   ├── pygamesteel.py
│   │   │   └── README.md
│   │   ├── lab03
│   │   │   ├── exmp_targets.txt
│   │   │   └── README.md
│   │   ├── lab04
│   │   │   └── README.md
│   │   ├── lab05
│   │   │   ├── client
│   │   │   │   ├── client.py
│   │   │   │   ├── Dockerfile
│   │   │   │   └── requirements.txt
│   │   │   ├── docker-compose.yml
│   │   │   ├── README.md
│   │   │   ├── server
│   │   │   │   ├── app.py
│   │   │   │   ├── Dockerfile
│   │   │   │   └── requirements.txt
│   │   │   └── source
│   │   │       ├── Dockerfile
│   │   │       ├── hello.py
│   │   │       └── requirements.txt
│   │   └── lab06
│   │       └── README.md
│   ├── LICENSE.md
│   ├── NOTICE.md
│   ├── README.md
│   └── SECURITY.md
├── Desktop
├── Documents
├── Downloads
│   ├── http_client.zip
│   ├── nmap.zip
│   ├── parallel_cpp.tar.gz
│   └── TMP.zip
├── lab01
│   ├── hello.py
│   └── README.md
├── lab02
│   ├── env
│   │   ├── bin
│   │   │   ├── python -> python3
│   │   │   ├── python3 -> /usr/bin/python3
│   │   │   └── python3.12 -> python3
│   │   ├── include
│   │   │   └── python3.12
│   │   ├── lib
│   │   │   └── python3.12
│   │   │       └── site-packages
│   │   ├── lib64 -> lib
│   │   └── pyvenv.cfg
│   ├── pycache
│   │   └── pygame.cpython-312.pyc
│   └── pygame.py
├── Music
├── Pictures
├── Public
├── screen
├── snap
│   ├── firefox
│   │   ├── 7355
│   │   ├── 7423
│   │   ├── common
│   │   └── current -> 7423
│   ├── firmware-updater
│   │   ├── 127
│   │   ├── 210
│   │   ├── common
│   │   └── current -> 210
│   └── snapd-desktop-integration
│       ├── 178
│       │   ├── Desktop
│       │   ├── Documents
│       │   ├── Downloads
│       │   ├── Music
│       │   ├── Pictures
│       │   ├── Public
│       │   ├── Templates
│       │   └── Videos
│       ├── 315
│       │   ├── Desktop
│       │   ├── Documents
│       │   ├── Downloads
│       │   ├── Music
│       │   ├── Pictures
│       │   ├── Public
│       │   ├── Templates
│       │   └── Videos
│       ├── common
│       └── current -> 315
├── Templates
├── test
│   └── svetikk.md
└── Videos

72 directories, 55 files
```

`ls -a` показывает все файлы, включая скрытые.

```bash
svepodd@svepodd-VirtualBox:~$ ls -a
.              .bashrc      Desktop     .gnupg    .local    Public  .sudo_as_admin_successful
..             .cache       Documents   lab01     Music     screen  Templates
.bash_history  .config      Downloads   lab02     Pictures  snap    test
.bash_logout   course_labs  .gitconfig  .lesshst  .profile  .ssh    Videos
```

`ls -l` предоставляет список файлов с информацией о правах доступа, владельце, размере и дате изменения, но не показывает скрытые файлы по умолчанию.

```bash
svepodd@svepodd-VirtualBox:~$ ls -l
total 52
drwxrwxr-x 6 svepodd svepodd 4096 Dec  1 00:09 course_labs
drwxr-xr-x 2 svepodd svepodd 4096 Sep 20 09:29 Desktop
drwxr-xr-x 2 svepodd svepodd 4096 Sep 20 09:29 Documents
drwxr-xr-x 2 svepodd svepodd 4096 Nov 11 22:47 Downloads
drwxrwxr-x 3 svepodd svepodd 4096 Nov 23 23:15 lab01
drwxrwxr-x 4 svepodd svepodd 4096 Dec  1 18:51 lab02
drwxr-xr-x 2 svepodd svepodd 4096 Sep 20 09:29 Music
drwxr-xr-x 2 svepodd svepodd 4096 Sep 20 09:29 Pictures
drwxr-xr-x 2 svepodd svepodd 4096 Sep 20 09:29 Public
-rw-rw-r-- 1 svepodd svepodd    0 Dec  1 00:36 screen
drwx------ 5 svepodd svepodd 4096 Sep 20 12:04 snap
drwxr-xr-x 2 svepodd svepodd 4096 Sep 20 09:29 Templates
drwxrwxr-x 3 svepodd svepodd 4096 Nov 24 16:40 test
drwxr-xr-x 2 svepodd svepodd 4096 Sep 20 09:29 Videos
```

- [x] 3. Используйте утилиту `file` и `df` для определения какая файловая система на разделе `/dev/sda1`.

`file -s /dev/sda2` анализирует устройство и определяет тип файловой системы.

```bash
svepodd@svepodd-VirtualBox:~$ sudo file -s /dev/sda2
[sudo] password for svepodd: 
/dev/sda2: Linux rev 1.0 ext4 filesystem data, UUID=8aa628ea-c5e9-4cbd-9753-9daaf1fafe17 (needs journal recovery) (extents) (64bit) (large files) (huge files)
```

`df -T /` показывает тип файловой системы для корневого раздела `/`.

```bash
svepodd@svepodd-VirtualBox:~$ df -T /
Filesystem     Type 1K-blocks     Used Available Use% Mounted on
/dev/sda2      ext4  32909008 16562760  14642312  54% /
```

- [x] 4. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ which vi
$ locate hello.py
$ sudo updatedb
$ locate hello
$ touch screen
$ find ~ -name screen
$ locate screen
$ sudo updated
$ locate screen
```

`which vi` выводит путь к бинарному файлу редактора `vi`, который будет запущен по умолчанию.

```bash
svepodd@svepodd-VirtualBox:~$ which vi
/usr/bin/vi
```

`locate hello.py` ищет файл по имени в заранее построенной базе `mlocate`. До запуска `updatedb` нужных совпадений может не быть.

```bash
svepodd@svepodd-VirtualBox:~$ locate hello.py
/snap/gnome-42-2204/176/usr/lib/x86_64-linux-gnu/peas-demo/plugins/pythonhello/pythonhello.py
```

`sudo updatedb` обновляет базу путей для `locate`

```bash
svepodd@svepodd-VirtualBox:~$ sudo updatedb
```

Повторный `locate hello` с учётом обновлённой базы показывает все файлы и каталоги, в имени которых встречается подстрока `hello`.

```bash
svepodd@svepodd-VirtualBox:~$ locate hello
/boot/grub/i386-pc/hello.mod
/home/svepodd/course_labs/labs/lab02/exmpl_hello.py
/home/svepodd/course_labs/labs/lab05/source/hello.py
/home/svepodd/lab01/hello.py
/snap/core22/2139/usr/lib/python3.10/__phello__.foo.py
/snap/core22/2139/usr/lib/python3.10/__pycache__/__phello__.foo.cpython-310.pyc
/snap/core22/2163/usr/lib/python3.10/__phello__.foo.py
/snap/core22/2163/usr/lib/python3.10/__pycache__/__phello__.foo.cpython-310.pyc
/snap/gnome-42-2204/176/usr/lib/python3.10/__phello__.foo.py
/snap/gnome-42-2204/176/usr/lib/x86_64-linux-gnu/peas-demo/plugins/helloworld
/snap/gnome-42-2204/176/usr/lib/x86_64-linux-gnu/peas-demo/plugins/pythonhello
/snap/gnome-42-2204/176/usr/lib/x86_64-linux-gnu/peas-demo/plugins/helloworld/helloworld.plugin
/snap/gnome-42-2204/176/usr/lib/x86_64-linux-gnu/peas-demo/plugins/helloworld/libhelloworld.so
/snap/gnome-42-2204/176/usr/lib/x86_64-linux-gnu/peas-demo/plugins/pythonhello/pythonhello.plugin
/snap/gnome-42-2204/176/usr/lib/x86_64-linux-gnu/peas-demo/plugins/pythonhello/pythonhello.py
/usr/lib/grub/i386-pc/hello.mod
/usr/lib/python3.12/__hello__.py
/usr/lib/python3.12/__phello__
/usr/lib/python3.12/__phello__/__init__.py
/usr/lib/python3.12/__phello__/__pycache__
/usr/lib/python3.12/__phello__/spam.py
/usr/lib/python3.12/__phello__/__pycache__/__init__.cpython-312.pyc
/usr/lib/python3.12/__phello__/__pycache__/spam.cpython-312.pyc
/usr/lib/python3.12/__pycache__/__hello__.cpython-312.pyc
/usr/lib/x86_64-linux-gnu/open-coarrays/openmpi/bin/OpenCoarrays-2.10.2-tests/asynchronous_hello_world
/usr/lib/x86_64-linux-gnu/open-coarrays/openmpi/bin/OpenCoarrays-2.10.2-tests/hello_multiverse
/usr/share/cmake-3.28/Modules/IntelVSImplicitPath/hello.f
/usr/share/doc/bpfcc-tools/examples/hello_world.py
/usr/share/doc/bpfcc-tools/examples/tracing/hello_fields.py
/usr/share/doc/bpfcc-tools/examples/tracing/hello_perf_output.py
/usr/share/doc/bpfcc-tools/examples/tracing/hello_perf_output_using_ns.py
/usr/share/doc/libevent-dev/examples/hello-world.c
/usr/share/doc/libpmix-dev/examples/hello.c
/usr/share/locale-langpack/en@boldquot/LC_MESSAGES/hello.mo
/usr/share/locale-langpack/en@quot/LC_MESSAGES/hello.mo
/usr/share/locale-langpack/en_AU/LC_MESSAGES/hello.mo
/usr/share/locale-langpack/en_CA/LC_MESSAGES/hello.mo
/usr/share/locale-langpack/en_GB/LC_MESSAGES/hello.mo
```

Пробуем для `hello.py`:

```bash
svepodd@svepodd-VirtualBox:~$ locate hello.py
/home/svepodd/course_labs/labs/lab02/exmpl_hello.py
/home/svepodd/course_labs/labs/lab05/source/hello.py
/home/svepodd/lab01/hello.py
/snap/gnome-42-2204/176/usr/lib/x86_64-linux-gnu/peas-demo/plugins/pythonhello/pythonhello.py
```

`touch screen` создаёт пустой файл `screen`

```bash
svepodd@svepodd-VirtualBox:~$ touch screen
```

`find ~ -name screen` выполняет поиск по файловой системе, проходя дерево каталогов от `~`.

```bash
svepodd@svepodd-VirtualBox:~$ find ~ -name screen
/home/svepodd/screen
```

После `updatedb` система начинает видеть новые файлы. Это демонстрирует разницу между `find` (работает прямо по диску) и `locate` (работает по базе).

```bash
svepodd@svepodd-VirtualBox:~$ locate screen
/snap/core22/2139/usr/lib/terminfo/s/screen
/snap/core22/2139/usr/lib/terminfo/s/screen-256color
/snap/core22/2139/usr/lib/terminfo/s/screen-256color-bce
/snap/core22/2139/usr/lib/terminfo/s/screen-bce
/snap/core22/2139/usr/lib/terminfo/s/screen-s
/snap/core22/2139/usr/lib/terminfo/s/screen-w
/snap/core22/2139/usr/lib/terminfo/s/screen.xterm-256color
/snap/core22/2139/usr/share/bash-completion/completions/gnome-screenshot
/snap/core22/2139/usr/share/bash-completion/completions/screen
/snap/core22/2139/usr/share/subiquity/subiquitycore/screen.py
/snap/core22/2139/usr/share/subiquity/subiquitycore/__pycache__/screen.cpython-310.pyc
...
```

- [x] 5. Используйте конструкцию и вставьте ее в созданный файл ранее. Подключите `pygame` - используем исключительно для стилизации окна.

Используемая конструкция:
```py
import os
import pygame
pygame.init()

# Размеры окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello appsec world")

# Цвет фона
bg_color = (255, 255, 255)

# Текст
font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world :)", True, (255, 0, 0))
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height), 1)
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()
```

Запускаем:

```bash
(svepodd_venv) svepodd@svepodd-VirtualBox:~/lab02$ python3 py_game.py 
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
```

- [x] 6. Сделайте `commit` и `push` в свой репозиторий с изменениями в `master branch`. На следующих лабораторных работах мы вернемся к этому файлу.

```bash
svepodd@svepodd-VirtualBox:~/lab01$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
 py_game.py

nothing added to commit but untracked files present (use "git add" to track)
svepodd@svepodd-VirtualBox:~/lab01$ git add py_game.py 
warning: in the working copy of 'py_game.py', LF will be replaced by CRLF the next time Git touches it
svepodd@svepodd-VirtualBox:~/lab01$ git commit -S -m "Add py_game.py"
[master e066304] Add py_game.py
 1 file changed, 30 insertions(+)
 create mode 100755 py_game.py
```

- [x] 7. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ groups
$ useradd smallman
$ userdel smallman -rf
$ useradd smallman
$ passwd smallman
$ usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33'
$ passwd smallman
$ id smallman
$ groupadd -g 1500 readgroup
$ usermod -aG readgroup smallman
$ chmod 666 screen 
```

`groups` показывает, в какие группы входит текущий пользователь.
```bash
svepodd@svepodd-VirtualBox:~/lab01$ groups
svepodd adm cdrom sudo dip plugdev users lpadmin docker
```

`useradd smallman` создаёт нового пользователя `smallman`. `userdel smallman -rf` удаляет пользователя и его ресурсы:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ sudo useradd smallman

svepodd@svepodd-VirtualBox:~/lab01$ sudo userdel smallman -rf
userdel: smallman mail spool (/var/mail/smallman) not found
userdel: smallman home directory (/home/smallman) not found
```

`passwd smallman` задаёт или изменяет пароль пользователя `smallman`.

```bash
svepodd@svepodd-VirtualBox:~/lab01$ sudo useradd smallman

svepodd@svepodd-VirtualBox:~/lab01$ sudo passwd smallman
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: password updated successfully
```

`usermod smallman -c '...'` добавляет комментарий к записи пользователя в `/etc/passwd`. При помощи `passwd smallman` изменили пароль пользователя `smallman`.

```bash
svepodd@svepodd-VirtualBox:~/lab01$ sudo usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33'

svepodd@svepodd-VirtualBox:~/lab01$ sudo passwd smallman
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: password updated successfully
```

`id smallman` показывает UID/GID и группы пользователя `smallman`.

```bash
svepodd@svepodd-VirtualBox:~/lab01$ id smallman
uid=1001(smallman) gid=1001(smallman) groups=1001(smallman)
```

`groupadd -g 1500 readgroup` создаёт новую группу `readgroup` с GID=1500. `usermod -aG readgroup smallman` добавляет пользователя `smallman` в группу `readgroup`.

```bash
svepodd@svepodd-VirtualBox:~/lab01$ sudo groupadd -g 1500 readgroup
svepodd@svepodd-VirtualBox:~/lab01$ sudo usermod -aG readgroup smallman
```

`chmod 666 /home/svepodd/screen` временно даёт права чтения и записи всем пользователям к файлу `/home/svepodd/screen`.

```bash
svepodd@svepodd-VirtualBox:~/lab01$ chmod 666 /home/svepodd/screen
```

- [x] 8. Выведите группу прав для `screen` и измените, что бы файл был доступен только для чтения созданному пользователю и выведите права этого пользователя для измененного файла только используя `readgroup`.

```bash
svepodd@svepodd-VirtualBox:~$ ls -l screen
-rw-rw-rw- 1 svepodd svepodd 0 Dec  1 00:36 screen
svepodd@svepodd-VirtualBox:~$ sudo chown smallman:smallman screen
svepodd@svepodd-VirtualBox:~$ sudo chmod 400 screen 
svepodd@svepodd-VirtualBox:~$ ls -l screen
-r-------- 1 smallman smallman 0 Dec  1 00:36 screen
```

- [x] 9. Используйте `POSIX ACL`. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ touch nmapres.txt
$ setfacl -m u:smallman:rw nmapres.txt
$ setfacl -m g:readgroup:r nmapres.txt
$ getfacl nmapres.txt
```

```bash
svepodd@svepodd-VirtualBox:~/lab01$ touch nmapres.txt
svepodd@svepodd-VirtualBox:~/lab01$ setfacl -m u:smallman:rw nmapres.txt 
svepodd@svepodd-VirtualBox:~/lab01$ setfacl -m g:readgroup:r nmapres.txt 
svepodd@svepodd-VirtualBox:~/lab01$ getfacl nmapres.txt 
# file: nmapres.txt
# owner: svepodd
# group: svepodd
user::rw-
user:smallman:rw-
group::rw-
group:readgroup:r--
mask::rw-
other::r--
```
При помощи `setfacl` мы задаем ACL-записи:
- пользователю smallman разрешено читать и писать файл
- группе readgroup разрешено только чтение файла

`getfacl` показывает текущие ACL-записи для файла.

- [x] 10. Сохраните файл внутри локального репозитория, так как следующая работа будет подразумевать запись в нее данных о nmap.
```bash
svepodd@svepodd-VirtualBox:~/lab01$ git add nmapres.txt 
svepodd@svepodd-VirtualBox:~/lab01$ git commit -S -m "Add nmapres.txt"
[master 158bc35] Add nmapres.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 nmapres.txt
```

- [x] 11. Для закрепления выведите все списки групп пользователей на вашей ОС и права на верхнеуровневые каталоги.

```bash
svepodd@svepodd-VirtualBox:~/lab01$ cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,svepodd
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:
fax:x:21:
voice:x:22:
cdrom:x:24:svepodd
floppy:x:25:
tape:x:26:
sudo:x:27:svepodd
audio:x:29:
dip:x:30:svepodd
www-data:x:33:
backup:x:34:
operator:x:37:
list:x:38:
irc:x:39:
src:x:40:
shadow:x:42:
utmp:x:43:
video:x:44:
sasl:x:45:
plugdev:x:46:svepodd
staff:x:50:
games:x:60:
users:x:100:svepodd
nogroup:x:65534:
systemd-journal:x:999:
systemd-network:x:998:
crontab:x:997:
systemd-timesync:x:996:
input:x:995:
sgx:x:994:
kvm:x:993:
render:x:992:
messagebus:x:101:
syslog:x:102:
systemd-resolve:x:991:
uuidd:x:103:
_ssh:x:104:
tss:x:105:
ssl-cert:x:106:
systemd-oom:x:990:
bluetooth:x:107:
rdma:x:108:
whoopsie:x:109:
netdev:x:110:
avahi:x:111:
tcpdump:x:112:
sssd:x:113:
lpadmin:x:114:svepodd
fwupd-refresh:x:989:
scanner:x:115:saned
saned:x:116:
geoclue:x:117:
pipewire:x:118:
gnome-remote-desktop:x:988:
polkitd:x:987:
rtkit:x:119:
colord:x:120:
gdm:x:121:
nm-openvpn:x:122:
lxd:x:123:
gamemode:x:986:
gnome-initial-setup:x:985:
svepodd:x:1000:
docker:x:984:svepodd
plocate:x:124:
smallman:x:1001:
readgroup:x:1500:smallman
svepodd@svepodd-VirtualBox:~/lab01$ ls -la /
total 4010084
drwxr-xr-x  23 root root       4096 Sep 20 09:21 .
drwxr-xr-x  23 root root       4096 Sep 20 09:21 ..
lrwxrwxrwx   1 root root          7 Apr 22  2024 bin -> usr/bin
drwxr-xr-x   2 root root       4096 Feb 26  2024 bin.usr-is-merged
drwxr-xr-x   3 root root       4096 Dec 14 14:52 boot
dr-xr-xr-x   2 root root       4096 Sep 20 09:11 cdrom
drwxr-xr-x  19 root root       4200 Dec 14 16:01 dev
drwxr-xr-x 144 root root      12288 Dec 15 00:14 etc
drwxr-xr-x   4 root root       4096 Nov 17 16:32 home
lrwxrwxrwx   1 root root          7 Apr 22  2024 lib -> usr/lib
lrwxrwxrwx   1 root root          9 Apr 22  2024 lib64 -> usr/lib64
drwxr-xr-x   2 root root       4096 Apr  8  2024 lib.usr-is-merged
drwx------   2 root root      16384 Sep 20 09:14 lost+found
drwxr-xr-x   2 root root       4096 Aug 27  2024 media
drwxr-xr-x   2 root root       4096 Aug 27  2024 mnt
drwxr-xr-x   3 root root       4096 Nov 11 21:51 opt
dr-xr-xr-x 325 root root          0 Nov 24 19:14 proc
drwx------   7 root root       4096 Nov 23 21:23 root
drwxr-xr-x  40 root root       1160 Dec 14 23:59 run
lrwxrwxrwx   1 root root          8 Apr 22  2024 sbin -> usr/sbin
drwxr-xr-x   2 root root       4096 Mar 31  2024 sbin.usr-is-merged
drwxr-xr-x  12 root root       4096 Aug 27  2024 snap
drwxr-xr-x   2 root root       4096 Aug 27  2024 srv
-rw-------   1 root root 4106223616 Sep 20 09:21 swap.img
dr-xr-xr-x  13 root root          0 Nov 24 19:14 sys
drwxrwxrwt  18 root root       4096 Dec 15 00:23 tmp
drwxr-xr-x  12 root root       4096 Aug 27  2024 usr
drwxr-xr-x  14 root root       4096 Sep 20 09:26 var
```

- [x] 12. Выведите все права для файлов и директорий локального репозитория которые имеют различные пользователи  (без использования длинных путей)

```bash
svepodd@svepodd-VirtualBox:~/lab01$ ls -l
total 8
-rw-rw-r--  1 svepodd  svepodd  454 Nov 23 23:15 hello.py
-rw-rw-r--+ 1 svepodd  svepodd    0 Dec 15 00:26 nmapres.txt
-rwxrwxr-x  1 svepodd  svepodd  768 Dec 14 16:04 py_game.py
-rw-rw-r--  1 svepodd  svepodd    0 Nov 23 21:13 README.md
-r--------  1 smallman smallman   0 Dec  1 00:36 screen
```

- [x] 13. Выведите процессы которые у вас запущены в термине и вне его.

В терминале:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ ps T
    PID TTY      STAT   TIME COMMAND
  28292 pts/0    Ss     0:00 bash
 332953 pts/0    R+     0:00 ps T
```

Вне терминала:

```bash
svepodd@svepodd-VirtualBox:~/lab01$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  1.8  0.3  23516 14568 ?        Ss   Dec14   5:18 /usr/lib/syst
root           2  0.0  0.0      0     0 ?        S    Dec14   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        S    Dec14   0:00 [pool_workque
root           4  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-rc
root           5  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-sy
root           6  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-kv
root           7  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-sl
root           8  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-ne
root          13  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-mm
root          14  0.0  0.0      0     0 ?        I    Dec14   0:00 [rcu_tasks_kt
root          15  0.0  0.0      0     0 ?        I    Dec14   0:00 [rcu_tasks_ru
root          16  0.0  0.0      0     0 ?        I    Dec14   0:00 [rcu_tasks_tr
root          17  0.1  0.0      0     0 ?        S    Dec14   0:23 [ksoftirqd/0]
root          18  0.3  0.0      0     0 ?        R    Dec14   0:53 [rcu_preempt]
root          19  0.0  0.0      0     0 ?        S    Dec14   0:00 [rcu_exp_par_
root          20  1.1  0.0      0     0 ?        S    Dec14   3:08 [rcu_exp_gp_k
root          21  0.0  0.0      0     0 ?        S    Dec14   0:03 [migration/0]
root          22  0.0  0.0      0     0 ?        S    Dec14   0:00 [idle_inject/
root          23  0.0  0.0      0     0 ?        S    Dec14   0:00 [cpuhp/0]
root          24  0.0  0.0      0     0 ?        S    Dec14   0:00 [cpuhp/1]
root          25  0.0  0.0      0     0 ?        S    Dec14   0:00 [idle_inject/
root          26  0.0  0.0      0     0 ?        S    Dec14   0:04 [migration/1]
root          27  0.0  0.0      0     0 ?        S    Dec14   0:14 [ksoftirqd/1]
root          30  0.0  0.0      0     0 ?        S    Dec14   0:00 [cpuhp/2]
root          31  0.0  0.0      0     0 ?        S    Dec14   0:00 [idle_inject/
root          32  0.0  0.0      0     0 ?        S    Dec14   0:04 [migration/2]
root          33  0.0  0.0      0     0 ?        S    Dec14   0:08 [ksoftirqd/2]
root          36  0.0  0.0      0     0 ?        S    Dec14   0:00 [cpuhp/3]
root          37  0.0  0.0      0     0 ?        S    Dec14   0:00 [idle_inject/
root          38  0.0  0.0      0     0 ?        S    Dec14   0:05 [migration/3]
root          39  0.1  0.0      0     0 ?        S    Dec14   0:28 [ksoftirqd/3]
root          46  0.0  0.0      0     0 ?        S    Dec14   0:00 [kdevtmpfs]
root          47  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-in
root          48  0.0  0.0      0     0 ?        S    Dec14   0:00 [kauditd]
root          49  0.0  0.0      0     0 ?        S    Dec14   0:00 [khungtaskd]
root          51  0.0  0.0      0     0 ?        S    Dec14   0:00 [oom_reaper]
root          53  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-wr
root          54  0.0  0.0      0     0 ?        S    Dec14   0:07 [kcompactd0]
root          55  0.0  0.0      0     0 ?        SN   Dec14   0:00 [ksmd]
root          56  0.0  0.0      0     0 ?        SN   Dec14   0:01 [khugepaged]
root          57  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-ki
root          58  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-kb
root          59  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-bl
root          60  0.0  0.0      0     0 ?        S    Dec14   0:00 [irq/9-acpi]
root          61  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-tp
root          62  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-at
root          63  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-md
root          64  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-md
root          65  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-ed
root          66  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-de
root          67  0.0  0.0      0     0 ?        S    Dec14   0:00 [watchdogd]
root          71  0.2  0.0      0     0 ?        S    Dec14   0:45 [kswapd0]
root          72  0.0  0.0      0     0 ?        S    Dec14   0:00 [ecryptfs-kth
root          73  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-kt
root          74  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-ac
root          76  0.0  0.0      0     0 ?        S    Dec14   0:00 [scsi_eh_0]
root          77  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-sc
root          78  0.0  0.0      0     0 ?        S    Dec14   0:00 [scsi_eh_1]
root          79  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-sc
root          84  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-ml
root          86  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-ip
root          97  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-ks
root          99  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/u21:
root         100  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/u22:
root         101  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/u23:
root         102  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/u24:
root         103  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/u25:
root         118  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-ch
root         182  0.0  0.0      0     0 ?        S    Dec14   0:00 [scsi_eh_2]
root         183  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-sc
root         231  0.2  0.0      0     0 ?        S    Dec14   0:37 [jbd2/sda2-8]
root         232  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-ex
root         628  0.0  0.0      0     0 ?        S    Dec14   0:00 [irq/18-vmwgf
root         629  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-tt
root         633  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/R-cr
avahi        711  0.0  0.1   8668  4448 ?        Ss   Dec14   0:11 avahi-daemon:
message+     712  3.4  0.1  12284  7156 ?        Ss   Dec14   9:42 @dbus-daemon 
root         729  0.0  0.1 313292  7336 ?        Ssl  Dec14   0:15 /usr/libexec/
root         731  0.0  0.0   9424  2608 ?        Ss   Dec14   0:00 /usr/sbin/cro
root         732  0.0  0.1 309880  6520 ?        Ssl  Dec14   0:00 /usr/libexec/
root         734  0.1  0.2  18248  8136 ?        Ss   Dec14   0:18 /usr/lib/syst
root         735  0.1  0.2 469484 10652 ?        Ssl  Dec14   0:22 /usr/libexec/
avahi        739  0.0  0.0   8480  1292 ?        S    Dec14   0:00 avahi-daemon:
root        1076  0.0  0.2 112252 10788 ?        Ssl  Dec14   0:00 /usr/bin/pyth
kernoops    1104  0.0  0.0  12744  2412 ?        Ss   Dec14   0:00 /usr/sbin/ker
root        1107  0.0  0.2 314824  8764 ?        Ssl  Dec14   0:00 /usr/sbin/gdm
kernoops    1112  0.0  0.0  12744  2452 ?        Ss   Dec14   0:00 /usr/sbin/ker
rtkit       1231  0.0  0.0  88476  3368 ?        SNsl Dec14   0:01 /usr/libexec/
colord      1621  0.0  0.2 320008  9904 ?        Ssl  Dec14   0:00 /usr/libexec/
root        1665  0.0  0.2 317160  8684 ?        Ssl  Dec14   0:02 /usr/libexec/
root        1905  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/u23:
root       27081  0.0  0.2 390044 10144 ?        Sl   Dec14   0:00 gdm-session-w
svepodd    27136  1.6  0.3  21484 12300 ?        Ss   Dec14   4:01 /usr/lib/syst
svepodd    27145  0.0  0.0  21456  2356 ?        S    Dec14   0:00 (sd-pam)
svepodd    27177  0.1  0.2 116468 10244 ?        Ssl  Dec14   0:26 /usr/bin/pipe
svepodd    27180  0.0  0.1  97736  4864 ?        Ssl  Dec14   0:00 /usr/bin/pipe
svepodd    27189  0.0  0.3 406892 12584 ?        Ssl  Dec14   0:02 /usr/bin/wire
svepodd    27192  0.0  0.5 124828 20944 ?        Ssl  Dec14   0:10 /usr/bin/pipe
svepodd    27197  0.0  0.1  11168  6552 ?        Ss   Dec14   0:06 /usr/bin/dbus
svepodd    27198  0.0  0.2 463972  9384 ?        SLsl Dec14   0:00 /usr/bin/gnom
svepodd    27239  0.0  0.1 685056  6904 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27251  0.0  0.1 309308  5740 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27253  0.0  0.1 235668  5548 tty2     Ssl+ Dec14   0:00 /usr/libexec/
svepodd    27265  0.0  0.3 298212 13452 tty2     Sl+  Dec14   0:00 /usr/libexec/
root       27280  0.0  0.0   2704  1920 ?        Ss   Dec14   0:00 fusermount3 -
svepodd    27351  0.0  0.1 162652  5760 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27352  0.0  0.1  91548  5404 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27378  0.0  0.1 314280  7200 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27391  0.0  0.1 459712  6368 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd    27399  0.0  0.3 799004 15556 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27437  0.0  0.1 382936  7652 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd    27445 13.4  6.9 5048948 278408 ?      Ssl  Dec14  32:44 /usr/bin/gnom
svepodd    27455  0.0  0.1   9612  5012 ?        S    Dec14   0:00 /usr/bin/dbus
svepodd    27500  0.0  0.1 236068  7260 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd    27522  0.0  0.3 654832 14864 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd    27536  0.0  0.6 2662696 24608 ?       Sl   Dec14   0:00 /usr/bin/gjs 
svepodd    27537  0.0  0.7 1272780 29012 ?       Ssl  Dec14   0:00 /usr/libexec/
svepodd    27546  0.1  0.1 388644  7972 ?        Ssl  Dec14   0:14 /usr/bin/ibus
svepodd    27547  0.0  0.1 383516  6392 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27549  0.0  0.4 412896 16596 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27550  0.0  0.2 431664 10820 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27558  0.2  0.1 458992  7328 ?        Ssl  Dec14   0:39 /usr/libexec/
svepodd    27560  0.0  0.4 411764 16344 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27562  0.0  0.5 594140 20072 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27563  0.0  0.5 597260 20108 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27567  0.0  0.2 323628 10012 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27569  0.5  0.1 531084  6400 ?        Ssl  Dec14   1:16 /usr/libexec/
svepodd    27571  0.0  0.1 309560  6260 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27575  1.4  0.2 543316 10704 ?        Ssl  Dec14   3:37 /usr/libexec/
svepodd    27577  0.0  0.1 459548  7076 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27579  0.0  0.2 393636  8436 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27582  0.0  0.4 486460 17264 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27594  0.0  1.1 897572 44960 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd    27603  0.0  0.1 305492  6872 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd    27734  0.5  0.4 546580 17728 ?        Sl   Dec14   1:16 /usr/libexec/
svepodd    27741  0.0  0.3 416208 12676 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd    27747  2.0  0.2 390092  9968 ?        Ssl  Dec14   5:02 /usr/libexec/
svepodd    27751  0.0  0.1 236648  6524 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd    27753  0.0  0.5 421500 21068 ?        Sl   Dec14   0:04 /usr/libexec/
svepodd    27759  0.0  0.1 310428  6480 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd    27797  0.5  0.4 1365900 17180 ?       Ssl  Dec14   1:21 /usr/libexec/
svepodd    27802  0.0  0.2 389128  8052 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd    27809  0.0  0.1 309792  5940 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27818  0.0  0.1 310760  6208 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27823  0.0  0.1 309772  6176 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27836  0.5  0.5 759908 21684 ?        Ssl  Dec14   1:22 /usr/libexec/
svepodd    27837  0.0  0.1 389376  7448 ?        Ssl  Dec14   0:01 /usr/libexec/
svepodd    27868  0.0  0.1 236772  6780 ?        Sl   Dec14   0:04 /usr/libexec/
svepodd    27887  0.0  0.1 230224  5516 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    27897  0.0  0.0  39136  2416 ?        Ss   Dec14   0:00 /snap/snapd-d
svepodd    27995  0.1  0.2 609444  8380 ?        Sl   Dec14   0:26 /usr/libexec/
svepodd    28015  0.0  0.1 429624  6316 ?        Sl   Dec14   0:00 /snap/snapd-d
svepodd    28042  0.5  0.3 701724 12368 ?        Ssl  Dec14   1:26 /usr/libexec/
root       28083  0.0  0.0      0     0 ?        I<   Dec14   0:00 [kworker/u22:
svepodd    28106  0.2  0.5 736332 20440 ?        SNsl Dec14   0:39 /usr/libexec/
svepodd    28107  0.0  0.6 630720 25888 ?        Ssl  Dec14   0:01 /usr/libexec/
svepodd    28164  0.0  0.6 2662596 24376 ?       Sl   Dec14   0:00 /usr/bin/gjs 
svepodd    28182  0.0  0.1 236272  6116 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    28192  0.0  0.5 417752 22240 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd    28282  0.4  1.2 642048 51556 ?        Ssl  Dec14   1:01 /usr/libexec/
svepodd    28292  0.0  0.1  12612  5956 pts/0    Ss   Dec14   0:00 bash
svepodd    28974  0.0  0.7 569256 28208 ?        Sl   Dec14   0:01 /usr/bin/upda
svepodd    30626  0.0  0.0 231444  3784 ?        SLsl Dec14   0:01 /usr/bin/gpg-
svepodd    32126  7.7 15.7 13197360 631460 ?     Sl   Dec14  18:26 /snap/firefox
svepodd    32273  0.0  0.0 1066672 2360 ?        Sl   Dec14   0:00 /snap/firefox
svepodd    32437  0.0  0.6 1348504 24476 ?       S    Dec14   0:00 /snap/firefox
svepodd    32447  0.0  0.7 1362912 31428 ?       Sl   Dec14   0:00 /snap/firefox
svepodd    32463  0.0  2.1 3525344 86788 ?       Sl   Dec14   0:03 /snap/firefox
svepodd    32474  0.0  1.1 1542196 46048 ?       Sl   Dec14   0:03 /snap/firefox
svepodd    32515  0.1  3.1 3555232 125344 ?      Sl   Dec14   0:24 /snap/firefox
svepodd    32565  0.0  0.2 1839928 9960 ?        Sl   Dec14   0:01 /usr/bin/snap
svepodd    32919  0.3  1.9 3505156 78992 ?       Sl   Dec14   0:47 /snap/firefox
svepodd    33138  0.0  1.0 1500564 42564 ?       Sl   Dec14   0:01 /snap/firefox
svepodd    33146  8.6  9.9 21041940 399620 ?     Sl   Dec14  20:37 /snap/firefox
svepodd    33150  0.0  3.7 3616464 151676 ?      Sl   Dec14   0:11 /snap/firefox
root       69857  0.2  0.0      0     0 ?        I    Dec14   0:32 [kworker/u16:
svepodd    70475  0.0  0.1   8432  4592 ?        S    Dec14   0:00 /usr/bin/ssh-
root      156959  0.0  0.0      0     0 ?        I    Dec14   0:00 [kworker/u16:
syslog    181934  0.5  0.1 222564  5556 ?        Ssl  Dec14   0:41 /usr/sbin/rsy
root      182489  0.0  0.1  17380  4552 ?        Ss   Dec14   0:00 /usr/sbin/wpa
root      184891  2.2  1.3 2015064 52592 ?       Ssl  Dec14   2:42 /usr/bin/cont
svepodd   184981  0.1  4.6 3660236 186380 ?      Sl   Dec14   0:14 /snap/firefox
systemd+  186123  0.0  0.1  17560  6996 ?        Ss   Dec14   0:02 /usr/lib/syst
systemd+  186580  0.3  0.2  21912 11700 ?        Ss   Dec14   0:27 /usr/lib/syst
root      189840  0.0  0.1 313376  7128 ?        Ssl  Dec14   0:00 /usr/libexec/
root      191392 16.5  3.1 2405076 127564 ?      Ssl  Dec14  19:43 /usr/bin/dock
root      192278  0.0  0.0      0     0 ?        I    Dec14   0:06 [ipvs-e:13:0]
root      192842  0.0  0.5 554644 21740 ?        Ssl  Dec14   0:00 /usr/libexec/
polkitd   193069  0.0  0.2 391268 11968 ?        Ssl  Dec14   0:01 /usr/lib/polk
root      193129  0.1  0.2 392528  8832 ?        Ssl  Dec14   0:13 /usr/sbin/Mod
root      204254  1.8  0.4 754756 17844 ?        Ssl  Dec14   2:13 /usr/sbin/Net
gnome-r+  204969  0.0  0.3 512808 14408 ?        Ssl  Dec14   0:00 /usr/libexec/
root      205291  0.0  0.0      0     0 ?        S    Dec14   0:00 [psimon]
root      222009  0.0  0.0      0     0 ?        I    Dec14   0:02 [kworker/u20:
root      241480  1.9  0.6 1996660 24596 ?       Ssl  Dec14   1:32 /usr/lib/snap
root      241642  0.5  0.1  29276  6676 ?        Ss   Dec14   0:28 /usr/lib/syst
root      241658  0.0  0.0      0     0 ?        S    Dec14   0:00 [psimon]
root      241826  0.1  0.2 1233324 10720 ?       Sl   Dec14   0:05 /usr/bin/cont
root      241864  1.2  0.3 729832 15704 ?        Ssl  Dec14   0:58 registry serv
root      241959  0.6  0.8  83296 35448 ?        S<s  Dec14   0:32 /usr/lib/syst
systemd+  241963  0.0  0.1  91048  7744 ?        Ssl  Dec14   0:00 /usr/lib/syst
root      247275  0.0  0.0      0     0 ?        I    Dec14   0:02 [kworker/u18:
root      257453  0.0  0.1  29280  4120 ?        S    Dec14   0:03 (udev-worker)
root      257456  0.1  0.1  29280  4120 ?        S    Dec14   0:06 (udev-worker)
root      257457  1.5  0.2  35156 11264 ?        S    Dec14   0:58 (udev-worker)
root      257464  0.0  0.1  29280  4092 ?        S    Dec14   0:00 (udev-worker)
root      257466  0.5  0.1  30696  5608 ?        S    Dec14   0:22 (udev-worker)
root      257467  0.1  0.1  29280  4092 ?        S    Dec14   0:07 (udev-worker)
root      257468  1.0  0.2  35044 11092 ?        S    Dec14   0:40 (udev-worker)
root      257469  0.0  0.0  29280  3964 ?        S    Dec14   0:00 (udev-worker)
root      257827  0.2  0.1  29280  4120 ?        S    Dec14   0:09 (udev-worker)
root      259801  0.1  0.0  29280  3964 ?        S    Dec14   0:05 (udev-worker)
svepodd   260630  0.6  5.1 3785648 205248 ?      Sl   Dec14   0:23 /snap/firefox
svepodd   264954  0.0  1.6 3481364 64820 ?       Sl   Dec14   0:00 /snap/firefox
svepodd   265399  0.0  1.6 3481364 64904 ?       Sl   Dec14   0:00 /snap/firefox
svepodd   265405  0.0  1.6 3481364 64948 ?       Sl   Dec14   0:00 /snap/firefox
svepodd   267339  0.7  1.7 273024 72068 ?        S    Dec14   0:23 /usr/bin/Xway
svepodd   267380  0.0  1.9 640836 79020 ?        Ssl  Dec14   0:00 /usr/libexec/
svepodd   267415  0.0  0.6 267148 24724 ?        Sl   Dec14   0:00 /usr/libexec/
svepodd   267436  0.0  3.1 1516616 127504 ?      Sl   Dec14   0:01 /usr/libexec/
root      274319  0.0  0.0      0     0 ?        I    Dec14   0:00 [kworker/2:1-
root      274496  0.0  0.0      0     0 ?        I    Dec14   0:00 [kworker/u19:
root      274844  0.0  0.0      0     0 ?        I    Dec14   0:02 [kworker/u20:
root      276305  0.0  0.0      0     0 ?        I    Dec14   0:00 [kworker/u17:
root      284379  0.0  0.0      0     0 ?        I    Dec14   0:00 [kworker/u17:
root      287436  0.0  0.0      0     0 ?        I    Dec14   0:00 [kworker/u19:
root      287992  0.1  0.0      0     0 ?        I<   Dec14   0:03 [kworker/2:1H
root      289718  0.0  0.2  38212 11848 ?        Ss   00:00   0:00 /usr/sbin/cup
cups-br+  289729  0.6  0.4 268360 19640 ?        Ssl  00:00   0:13 /usr/sbin/cup
root      289853  0.0  0.0      0     0 ?        I    00:00   0:00 [kworker/u20:
root      300673  0.2  0.0      0     0 ?        I<   00:09   0:03 [kworker/1:0H
root      306628  0.0  0.0      0     0 ?        I    00:14   0:00 [kworker/0:2-
root      308471  0.0  0.0      0     0 ?        I    00:15   0:00 [kworker/u18:
root      309373  0.1  0.0      0     0 ?        I<   00:16   0:01 [kworker/2:2H
root      311880  0.0  0.0      0     0 ?        I<   00:18   0:00 [kworker/0:2H
root      312514  0.0  0.0      0     0 ?        I<   00:19   0:00 [kworker/1:2H
root      313075  0.0  0.0      0     0 ?        I    00:19   0:00 [kworker/0:1-
root      313120  0.0  0.0      0     0 ?        I    00:19   0:00 [kworker/u19:
root      315640  0.0  0.0      0     0 ?        I    00:21   0:00 [kworker/u17:
root      315932  0.1  0.0      0     0 ?        I    00:22   0:00 [kworker/u20:
svepodd   317745  0.1  1.5 2876016 61556 ?       Sl   00:23   0:00 gjs /usr/shar
root      318322  0.2  0.0      0     0 ?        I<   00:23   0:02 [kworker/3:1H
root      319637  0.0  0.0      0     0 ?        I    00:25   0:00 [kworker/3:1-
root      319776  0.0  0.0      0     0 ?        I    00:25   0:00 [kworker/0:0-
root      320360  0.0  0.0      0     0 ?        I    00:25   0:00 [kworker/2:0-
root      322387  0.0  0.0      0     0 ?        I    00:27   0:00 [kworker/u18:
root      323245  0.1  0.0      0     0 ?        I<   00:28   0:00 [kworker/0:1H
root      323653  0.0  0.0      0     0 ?        I    00:28   0:00 [kworker/1:1-
root      324702  0.0  0.0      0     0 ?        I    00:29   0:00 [kworker/1:3-
root      325414  0.0  0.0      0     0 ?        I<   00:29   0:00 [kworker/3:0H
root      326155  0.0  0.0      0     0 ?        I    00:30   0:00 [kworker/3:2-
root      326800  0.0  0.0      0     0 ?        I    00:31   0:00 [kworker/2:2-
root      329065  0.0  0.0      0     0 ?        I    00:33   0:00 [kworker/2:3-
root      329783  0.0  0.0      0     0 ?        I    00:33   0:00 [kworker/u17:
root      330640  0.0  0.0      0     0 ?        I    00:34   0:00 [kworker/1:0-
root      331068  0.0  0.0      0     0 ?        I    00:34   0:00 [kworker/0:3]
root      332194  0.4  0.0      0     0 ?        I<   00:35   0:00 [kworker/3:2H
root      332516  0.0  0.0      0     0 ?        I    00:36   0:00 [kworker/3:0-
root      332803  0.0  0.0      0     0 ?        I    00:36   0:00 [kworker/u20:
svepodd   333060  100  0.1  13748  4704 pts/0    R+   00:36   0:00 ps aux
```

- [x] 14. Оформить `README.md` по аналогии и использовать `shield`, etc.

- [x] 15. Составить `gist` отчет и отправить ссылку личным сообщением

Ссылка на gist: https://gist.github.com/svepodd/0c6953c9bb9d9f26e2e4ae0a2762a4c4 

***

Copyright (c) 2025 Svetlana Poddoskina
