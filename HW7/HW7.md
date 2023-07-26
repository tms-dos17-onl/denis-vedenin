##1. Вывести список всех удаленных репозиториев для локального.
```
PS C:\Users\Ирка Pipirka\denis-vedenin> git remote -v
origin  https://github.com/tms-dos17-onl/denis-vedenin.git (fetch)
origin  https://github.com/tms-dos17-onl/denis-vedenin.git (push) 
```

##2. Вывести список всех веток.
```
PS C:\Users\Ирка Pipirka\denis-vedenin> git branch -a
* main
remotes/origin/HEAD -> origin/main
sremotes/origin/main
```
##3. Вывести последниe 3 коммитa с помощью git log.
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

##4. Создать пустой файл README.md и сделать коммит.
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
##5. Добавить фразу "Hello, DevOps" в README.md файл и сделать коммит.
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
##6. Сделать реверт последнего коммита. Вывести последниe 3 коммитa с помощью git log.
```
PS C:\Users\Ирка Pipirka\denis-vedenin\HW7> git revert 6e77063a51f53e6544d8cbdef17b4ee3b34fc606
[main fd7f450] Revert "Добавление фразы 'Hello,DEvOps'в README.md файл"
 2 files changed, 16 deletions(-)
```
# Вывод последних 3 коммитов
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