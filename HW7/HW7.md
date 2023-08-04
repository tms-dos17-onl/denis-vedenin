# 1. Вывести список всех удаленных репозиториев для контекстого.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git remote -v
origin  https://github.com/tms-dos17-onl/denis-vedenin.git (fetch)
origin  https://github.com/tms-dos17-onl/denis-vedenin.git (push) 
```
# 2. Вывести список всех веток.

```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```
# 3. Вывести последние 3 комитета с помощью git log.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git log -3
commit 37e6aff02a69253a253baab0b1f19c7926bda320 (HEAD -> main)
Author: denis-vedenin <denved98@mail.ru>
Date:   Fri Aug 4 19:30:50 2023 +0300

    Task 2 done

commit 8156faf30c652cb73aaf74b712076afdbb3e16e0
Author: denis-vedenin <denved98@mail.ru>
Date:   Fri Aug 4 19:24:56 2023 +0300

    Task 1 done 'remote repositories'

commit 516b422ab9da7cfebf9c6b486996520fb97c7e88 (origin/main, origin/HEAD)
Author: denis-vedenin <64193562+deniskin1998@users.noreply.github.com>
Date:   Fri Aug 4 19:18:24 2023 +0300

    Delete HW7 directory
```
# 4. Создать пустой файл README.mdи сделать коммит.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ touch README.md

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ ll
total 4
-rw-r--r-- 1 Денис DevOps 197121 1288 Aug  4 19:32 HW7.md
-rw-r--r-- 1 Денис DevOps 197121    0 Aug  4 19:33 README.md
```