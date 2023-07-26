#1. Вывести список всех удаленных репозиториев для локального.
```
PS C:\Users\Ирка Pipirka\denis-vedenin> git remote -v
origin  https://github.com/tms-dos17-onl/denis-vedenin.git (fetch)
origin  https://github.com/tms-dos17-onl/denis-vedenin.git (push) 
```

#2. Вывести список всех веток.
``
PS C:\Users\Ирка Pipirka\denis-vedenin> git branch -a
* main
remotes/origin/HEAD -> origin/main
sremotes/origin/main
``
#3. Вывести последниe 3 коммитa с помощью git log.
``
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
``