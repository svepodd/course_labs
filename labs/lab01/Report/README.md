<div align="center">
<h1><a id="intro">Лабораторная работа №1</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Поддоскина_С._К.-8b9aff" alt="Contributor Badge"></a></div>

***

1. Создайте локальный репозиторий на машине

```bash
mkdir lab01
cd lab01/
```

2. Проинициализируйте репозиторий

```bash
git init
```

3. Авторизуйтесь и используйте `GitHub CLI` для создания удаленного репозитория

```bash
gh auth login
gh repo create lab01 --public
```

Ссылка на удалённый репозиторий: https://github.com/svepodd/lab01

4. Создайте пустой README.md 

```bash
touch README.md
```

5. Используйте указание URL своего созданного репозитория для присвоения ветки`master` статуса `origin`

```bash
git remote set-url origin git@github.com:svepodd/lab01.git
```

6. В локальном репозитории и сделайте `commit`

```bash
git add README.md
git commit -S -m "test #1"
```

**ID коммита:** 6a192c1

7. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий

```bash
git push -u origin master
```
![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/4.png)

8. Создайте файл `hello.py` в локальном репозитории. Реализуйте **Hello appsec world** на языке python используя несколько интерпретаторов с "грязным" кодом

```python
import sys
import os

def main():
	v = sys.version_info[0]
	if v==2:
		exec('print "Hello appsec world"')
	elif v==3:
		print("Hello appsec world")
	else:
		print("Unknown python version")

if __name__ == "__main__":
	main()
```

9. Сделайте `commit` с флагом `-S`

```bash
git add hello.py
git commit -S -m "Add hello.py"
```

**ID коммита:** 927df8f

10. Измените исходный код, что бы скрипт запрашивал имя пользователя и выводил `Helloappsec world from @name`

```python
def main():
	v = sys.version_info[0]
	if v==2:
		name = raw_input("Enter your name: ").strip()
		exec('print "Hello appsec world from" + name')
	elif v==3:
		name = input("Enter your name: ")
		print("Hello appsec world from" + name)
	else:
		print("Unknown python version")
```

11. Сделайте `commit` с флагом `-S` и сделайте публикацию в удаленный репозиторий. Проверьте вывод истории изменений

Публикация коммита:
```bash
git add hello.py
git commit -S -m "Add new hello.py"
git push origin master
```

**ID коммита:** 16a818a

Вывод истории:
```bash
git log --graph --decorate --all
```

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/9.png)

12. В локальном репозитории создайте ветку `patch1` и внесите изменения исправлению кода и модернизации до следующего вида, что бы код был рабочим. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий.

Создание ветки:
```bash
git checkout -b patch1
```

Изменение кода:
```python
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
```

Публикация коммита:
```bash
git add hello.py
git commit -S -m "hello.py in patch1"
git push origin master
git log --graph --decorate --all
```

**ID коммита:** 6e6930b

13. Проверьте, что ветка `patch1` в удалённом репозитории

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/13.png)

14. Создайте `pull-request` в виде `patch1 -> master`

```bash
gh pr create --base master --head patch1 --title "hello.py improve" --body "hello.py improve"
```

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/14.png)

15. В ветке `patch1` добавьте в исходный код комментарии и убедитесь, что есть указанные изменения в `pull-request`

Добавление комментария в код:
```python
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    # New comment from SvePodd
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
```

Публикация коммита:
```bash
git add hello.py
git commit -S -m "New comment in hello.py"
git push origin patch1
```

**ID коммита:** 713060d

Указанные изменения есть в `pull-request`:

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/17.png)

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/18.png)

16. В удалённый репозитории выполните слияние `pull-request` для `patch1 -> master` и удалите ветку `patch1`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/19.png)

**ID коммита:** d7a0ad2

17. Стяните последние актуальные изменения и просмотрите историю изменений для `master`

```bash
git pull origin master
```

18. Удалите локальную ветку `patch1`

```bash
git branch -d patch1
```

19. Создайте новую локальную ветку `patch2`.

```bash
git checkout -b patch2
```

20. Измените *code style* по своему усмотрению

```python
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
```

21. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий и создайте pull-request `patch2 -> master`

Публикация коммита:
```bash
git add hello.py
git commit -S -m "Code style was changed"
git push -u origin patch2
```

**ID коммита:** d90f48d

Создание pull-request `patch2 -> master`:
```bash
gh pr create --base master --hesd patch2 --title "Code style was changed" --body "Code style was changed" 
```

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/24.png)

22. В ветке **master** удаленного репозитория явно измените комментарий

```python
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    # New comment from SvePodd
    """
    Говорит "Привет" пользователю
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
```

Публикация коммита:
```bash
git add hello.py
git commit -S -m "Comment change #2"
git push origin master
```

**ID коммита:** 42d853c

23. Увидите, что в `pull-request` появились расхождения

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/27.png)

24. Локально сделайте **rebase** и исправьте расхождения (это называется **конфликт**)

```bash
git rebase --continue
```

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/28.png)

25. Сделайте `commit` и опубликуйте изменения в ветке `patch2`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/29.png)

**ID коммита:** 4a045f6

26. Убедитеcь, что пропали конфликты. 

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/30.png)

27. Сделайте `merge` для `pull-request` `patch2 -> master`.

**ID коммита:** 087edd2

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/31.png)

28. Подготовьте отчет `gist`.

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/34.png)

29. Продемонстрируйте в материалах отчета историю коммитов на локальном и удаленном репозитории.

**Локально:**

```bash
git log --oneline --graph --decorate --all
```

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/32.png)

**Удаленно:**

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/33.png)

***
Copyright (c) 2025 Svetlana Poddoskina
