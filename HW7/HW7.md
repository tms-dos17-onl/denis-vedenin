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

# 5. Добавьте фразу «Hello, DevOps» в README.mdфайл и сделайте коммит.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ nano README.md

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ cat README.md
«Hello, DevOps»
```

# 6. Сделать реверт последнего коммита. Вывести последние 3 комитета с помощью git log.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git revert 80fc5d3
[main 626a58b] Revert "Task 5 done'Add Hello, DevOps in README.md'"
 2 files changed, 12 deletions(-)

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git log -3
commit 626a58b089d1a4c7e4345f28267858f447a96266 (HEAD -> main)
Author: denis-vedenin <denved98@mail.ru>
Date:   Fri Aug 4 19:47:06 2023 +0300

    Revert "Task 5 done'Add Hello, DevOps in README.md'"

    This reverts commit 80fc5d3086d6ffa0098090b014df35f7da9b1003.

commit 80fc5d3086d6ffa0098090b014df35f7da9b1003
Author: denis-vedenin <denved98@mail.ru>
Date:   Fri Aug 4 19:40:38 2023 +0300

    Task 5 done'Add Hello, DevOps in README.md'

commit 374212650769097a7e16cfb1fde01cb47d1feeff
Author: denis-vedenin <denved98@mail.ru>
Date:   Fri Aug 4 19:36:41 2023 +0300

    Task 4 done'touch README.md'
```

# 7. Удалить последние 3 коммита с помощью git reset.

```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git reset --hard HEAD~3
HEAD is now at 3742126 Task 4 done'touch README.md'

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git log
commit 374212650769097a7e16cfb1fde01cb47d1feeff (HEAD -> main)
Author: denis-vedenin <denved98@mail.ru>
Date:   Fri Aug 4 19:36:41 2023 +0300

    Task 4 done'touch README.md'

commit 5e2741e03bcf9041786690ded408dfb0dd0e48d0
Author: denis-vedenin <denved98@mail.ru>
Date:   Fri Aug 4 19:32:48 2023 +0300

    Task 3 done'git lo -3'

commit 37e6aff02a69253a253baab0b1f19c7926bda320
Author: denis-vedenin <denved98@mail.ru>
Date:   Fri Aug 4 19:30:50 2023 +0300

    Task 2 done
```