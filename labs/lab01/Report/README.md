1. Создайте локальный репозиторий на машине

2. Проинициализируйте репозиторий

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/1.png)

3. Авторизуйтесь и спользуйте `GitHub CLI` для создания удаленного репозитория

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/2.png)

4. Создайте пустой README.md 

5. Используйте указание URL своего созданного репозитория для присвоения ветки `master` статуса `origin`

```bash
git remote set-url origin git@github.com:svepodd/lab01.git
```

6. В локальном репозитории и сделайте `commit`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/3.png)

7. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/4.png)

8. Создайте файл `hello.py` в локальном репозитории. Реализуйте `Hello appsecworld` на языке python используя несколько интерпретаторов с "грязным" кодом

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/5.png)

9. Сделайте `commit` с флагом `-S`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/6.png)

10. Измените исходный код, что бы скрипт запрашивал имя пользователя и выводил `Hello appsec world from @name`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/7.png)

11. Сделайте `commit` с флагом `-S` и сделайте публикацию в удаленный репозиторий. Проверьте вывод истории изменений

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/8.png)

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/9.png)

12. В локальном репозитории создайте ветку `patch1` и внесите изменения исправлению кода и модернизации до следующего вида, что бы код был рабочим. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий:

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/10.png)

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/11.png)

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/12.png)

13. Проверьте, что ветка `patch1` в удалённом репозитории

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/13.png)

14. Создайте `pull-request` в виде `patch1 -> master`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/14.png)

15. В ветке `patch1` добавьте в исходный код комментарии и убедитесь, что есть указанные изменения в `pull-request`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/16.png)

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/17.png)

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/18.png)

16. В удалённый репозитории выполните слияние `pull-request` для `patch1 -> master` и удалите ветку `patch1`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/19.png)

17. Стяните последние актуальные изменения и просмотрите историю изменений для `master`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/20.png)

18. Удалите локальную ветку `patch1`
19. Создайте новую локальную ветку `patch2`.

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/21.png)

20. Измените *code style* по своему усмотрению

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/22.png)

21. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий исоздайте pull-request `patch2 -> master`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/23.png)

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/24.png)

22. В ветке **master** удаленного репозитория явно измените комментарий

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/25.png)

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/26.png)

23. Увидите, что в `pull-request` появились расхождения

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/27.png)

24. Локально сделайте **rebase** и исправьте расхождения (это называется **конфликт**)

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/28.png)

25. Сделайте `commit` и опубликуйте изменения в ветке `patch2`

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/29.png)

26. Убедитель, что пропали конфликты. 

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/30.png)

27. Сделайте `merge` для `pull-request` `patch2 -> master`.

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/31.png)

28. Подготовьте отчет `gist`.

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/34.png)

29. Продемонстрируйте в материалах отчета историю коммитов на локальном и удаленном репозитории.

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/32.png)

![alt text](https://raw.githubusercontent.com/svepodd/course_labs/svepodd_labs/labs/lab01/Report/img/33.png)
