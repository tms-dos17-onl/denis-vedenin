# 1. Вывести список всех удаленных репозиториев для локального.
```
PS C:\Users\Ирка Pipirka\denis-vedenin> git remote -v
origin  https://github.com/tms-dos17-onl/denis-vedenin.git (fetch)
origin  https://github.com/tms-dos17-onl/denis-vedenin.git (push) 
```

# 2. Вывести список всех веток.
```
PS C:\Users\Ирка Pipirka\denis-vedenin> git branch -a
* main
remotes/origin/HEAD -> origin/main
sremotes/origin/main
```
# 3. Вывести последниe 3 коммитa с помощью git log.
```
PS C:\Users\Ирка Pipirka\denis-vedenin> git log -3    
commit d986eb1d5b016919988ee70057195d3cfd5004dd (HEAD -> main)
Author: Denis Vedenin <denved98@mail.ru>
Date:   Wed Jul 26 21:47:04 2023 +0300

    Вывод списка всех веток репозитория

commit bf2224bb6e47fa878b8fe88559ca21ba948f9abc (origin/main, origin/HEAD)
Author: Denis Vedenin <denved98@mail.ru>
Date:   Wed Jul 26 21:38:14 2023 +0300

    Выолнение 1 задания ДЗ

:
```

# 4. Создать пустой файл README.md и сделать коммит.
```
PS C:\Users\Ирка Pipirka\denis-vedenin\HW7> echo >  README.md

Командлет Write-Output в конвейере команд в позиции 1
Укажите значения для следующих параметров:
InputObject[0]:


    Каталог: C:\Users\Ирка Pipirka\denis-vedenin\HW7


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        26.07.2023     21:57           1093 HW7.md
-a----        26.07.2023     22:10              0 README.md
```
# 5. Добавить фразу "Hello, DevOps" в README.md файл и сделать коммит.
```
PS C:\Users\Ирка Pipirka\denis-vedenin\HW7> echo "Hello,DevOps" > .\README.md
Каталог: C:\Users\Ирка Pipirka\denis-vedenin\HW7> ls


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        26.07.2023     22:12           1748 HW7.md
-a----        26.07.2023     22:15             30 README.md


PS C:\Users\Ирка Pipirka\denis-vedenin\HW7> cat .\README.md
Hello,DevOps
PS C:\Users\Ирка Pipirka\denis-vedenin\HW7>
```
# 6. Сделать реверт последнего коммита. Вывести последниe 3 коммитa с помощью git log.
```
PS C:\Users\Ирка Pipirka\denis-vedenin\HW7> git revert 6e77063a51f53e6544d8cbdef17b4ee3b34fc606
[main fd7f450] Revert "Добавление фразы 'Hello,DEvOps'в README.md файл"
 2 files changed, 16 deletions(-)
```
## Вывод последних 3 коммитов
```
PS C:\Users\Ирка Pipirka\denis-vedenin\HW7> git log -3
commit fd7f4501a93504f61dc9bebf00f7cdd34daa68a8 (HEAD -> main)
Author: Denis Vedenin <denved98@mail.ru>
Date:   Wed Jul 26 23:24:10 2023 +0300

    Revert "Добавление фразы 'Hello,DEvOps'в README.md файл"

    This reverts commit 6e77063a51f53e6544d8cbdef17b4ee3b34fc606.

commit 6e77063a51f53e6544d8cbdef17b4ee3b34fc606 (origin/main, origin/HEAD)
Author: Denis Vedenin <denved98@mail.ru>
Date:   Wed Jul 26 22:21:05 2023 +0300

    Добавление фразы 'Hello,DEvOps'в README.md файл

commit 2d8b72667f031a0d000a069eae3aa6e7e0cf151e
Author: Denis Vedenin <denved98@mail.ru>
Date:   Wed Jul 26 22:14:09 2023 +0300

    Создание пустого файла README.md
```

# 7. Удалить последние 3 коммита с помощью git reset.
```
PS C:\Users\Денис DevOps\denis-vedenin\HW7> git reset --hard HEAD~3
HEAD is now at fd7f450 Revert "Добавление фразы 'Hello,DEvOps'в README.md файл"q
```

# 8. Вернуть коммит, где создается пустой файл README.md. Для этого нужно найти ID коммита в git reflog, а затем сделать cherry-pick.
```
PS C:\Users\Денис DevOps\denis-vedenin\HW7> git reflog
166233f (HEAD -> main, origin/main, origin/HEAD) HEAD@{0}: commit: git reset --hard HEAD~3
6308227 HEAD@{1}: pull: Fast-forward
fd7f450 HEAD@{2}: reset: moving to HEAD~3
6308227 HEAD@{3}: clone: from https://github.com/tms-dos17-onl/denis-vedenin.git
```

```
PS C:\Users\Денис DevOps\denis-vedenin\HW7> git cherry-pick 2d8b726
error: your local changes would be overwritten by cherry-pick.
hint: commit your changes or stash them to proceed.
fatal: cherry-pick failed

PS C:\Users\Денис DevOps\denis-vedenin\HW7> git cherry-pick --continue
[main 6fd3e0b] Создание пустого файла README.md
 Author: Denis Vedenin <denved98@mail.ru>
 Date: Wed Jul 26 22:14:09 2023 +0300
 1 file changed, 7 insertions(+)

PS C:\Users\Денис DevOps\denis-vedenin\HW7> git log
commit 6fd3e0b64735931ac7b46d71336d9bc9f0fff7f3 (HEAD -> main)
Author: Denis Vedenin <denved98@mail.ru>
Date:   Wed Jul 26 22:14:09 2023 +0300

    Создание пустого файла README.md
<<<<<<< HEAD
```

# 9. Удалить последний коммит с помощью git reset.
```
PS C:\Users\Денис DevOps\denis-vedenin\HW7> git reset HEAD~1       
Unstaged changes after reset:
M       HW7/HW7.md
PS C:\Users\Денис DevOps\denis-vedenin\HW7> git log
commit 6308227231bc492b0af9324bed0935a1e1c479bd (HEAD -> main)
Author: Denis Vedenin <denved98@mail.ru>
Date:   Wed Jul 26 23:45:01 2023 +0300

    Revert "Изменение текста в файле"

    This reverts commit 42fb47d25e50f13b3f9aeefc56a86386d594ee18.

```

#  10. Переключиться на ветку mainили master. Если ветка называетсяmaster, то переименовать её в main.

```
PS C:\Users\Денис DevOps\denis-vedenin\HW7> git checkout main
Already on 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\Денис DevOps\denis-vedenin\HW7> git branch       
* main
```

# 11. Скопировать файл https://github.com/tms-dos17-onl/_sandbox/blob/main/.github/workflows/validate-shell.yaml , положить его по таким же относительному пути в репозиторий. Создать коммит и запушить его в удаленный репозиторий.

```
PS C:\Users\Денис DevOps\denis-vedenin\HW7> mkdir .github

PS C:\Users\Денис DevOps\denis-vedenin\HW7> mkdir ./.github/workflows


    Каталог: C:\Users\Денис DevOps\denis-vedenin\HW7\.github

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        31.07.2023     23:11                workflows
```