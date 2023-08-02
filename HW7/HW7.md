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

# 12. Создать из ветки main ветку develop. Переключиться на неё и создать README.md в корне репозитория. Написать в этом файле какие инструменты DevOps вам знакомы и с какими вы бы хотели познакомиться больше всего (2-3 пункта).

```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git branch 
  develop
* main

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git checkout develop
Switched to branch 'develop'

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop)
$ nano README.md

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop)
$ cat README.md 
Хочу стать DevOps с полного нуля 
............................
Хочу знать
CI/CD
Ansible
AWS
Apache
Docker
Kubernetes
............................

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop)
$ git commit -m "Add file README.md and new branch develop"
[develop a87b176] Add file README.md and new branch develop
 2 files changed, 39 insertions(+)

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop)
$ git push origin develop
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 20 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1011 bytes | 1011.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/tms-dos17-onl/denis-vedenin.git
   1534688..a87b176  develop -> develop
```
# 13. Создайте из ветки mainветку supportи создайте там файл LICENSEс содержимым https://www.apache.org/licenses/LICENSE-2.0.txt . Создать коммит. Вывести последние 3 коммита.

```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git branch support

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git checkout support
Switched to branch 'support'
M       HW7/HW7.md

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (support)
$ touch LICENSE.md

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (support)
$ curl -O https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt > LICENSE.md
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed    
100  6656  100  6656    0     0  14788      0 --:--:-- --:--:-- --:--:-- 14857

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (support)
$ git add .

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (support)
$ git commit -m "Add file LICENSE.md and new branch support"

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (support)
$ git log -3
commit 6bc21a2769d7ad6571b46c7103db2bc5fad7830d (HEAD -> support)
Author: denis-vedenin <denved98@mail.ru>
Date:   Tue Aug 1 22:42:13 2023 +0300

    Add file LICENSE.md and new branch support

commit 15346889336178c521de89f6c2ebb695a4baf5e8 (origin/main, origin/HEAD, main) 
Author: denis-vedenin <denved98@mail.ru>
Date:   Mon Jul 31 23:15:04 2023 +0300

    Add validate-shell.yaml

commit 0aa5b782be5df717789ad771a0dbe1537d63d9fb
Author: denis-vedenin <denved98@mail.ru>
Date:   Mon Jul 31 17:32:26 2023 +0300
<<<<<<< HEAD
```

# 14. Переключиться обратно на ветку mainи там создать файл LICENSEс содержимым https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt . Создать коммит. Вывести последние 3 коммита.

```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (support)
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ touch LICENSE

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ touch LICENSE.txt

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ curl -O https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt > LICENSE.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current                                 Dload  Upload   Total   Spent    Left  Speed
100  6656  100  6656    0     0  15313      0 --:--:-- --:--:-- --:--:-- 15371 

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git add .

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   HW7.md
        renamed:    LICENSE -> LICENSE.txt
        modified:   MIT-LICENSE.txt


Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git commit -m "Change 14 task"
[main dca26ec] Change 14 task
 3 files changed, 19 insertions(+), 1 deletion(-)
 rename HW7/{LICENSE => LICENSE.txt} (100%)

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git log -3
commit a8109811b8d094948bc601ba7b2b26ccef4210ab (HEAD -> main, origin/main, origin/HEAD)
Author: denis-vedenin <denved98@mail.ru>
Date:   Tue Aug 1 23:27:05 2023 +0300

    Add file LICENSE.md in branch main

commit 15346889336178c521de89f6c2ebb695a4baf5e8
Author: denis-vedenin <denved98@mail.ru>
Date:   Mon Jul 31 23:15:04 2023 +0300

    Add validate-shell.yaml

commit 0aa5b782be5df717789ad771a0dbe1537d63d9fb
Author: denis-vedenin <denved98@mail.ru>
Date:   Mon Jul 31 17:32:26 2023 +0300
```
# 15. Сделать слияние ветки supportв ветку mainи решить конфликты выбора пути выбора только одной лицензии.

```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git merge support
Auto-merging HW7/HW7.md
CONFLICT (content): Merge conflict in HW7/HW7.md
Automatic merge failed; fix conflicts and then commit the result.

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main|MERGING)
$ git mergetool

This message is displayed because 'merge.tool' is not configured.
See 'git mergetool --tool-help' or 'git help config' for more details.
'git mergetool' will now attempt to use one of the following tools:
opendiff kdiff3 tkdiff xxdiff meld tortoisemerge gvimdiff diffuse diffmerge ecmerge p4merge araxis bc codecompare smerge emerge vimdiff nvimdiff
Merging:
HW7/HW7.md

Normal merge conflict for 'HW7/HW7.md':
  {local}: modified file
  {remote}: modified file
Hit return to start merge resolution tool (vimdiff):
4 files to edit

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main|MERGING)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   HW7.md
        new file:   LICENSE-2.0.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        HW7.md.orig


Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main|MERGING)
$ git add .

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main|MERGING)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   HW7.md
        new file:   HW7.md.orig
        new file:   LICENSE-2.0.txt


Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main|MERGING)
$ git commit -m "merge branch support in main"
[main 7954728] merge branch support in main

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
=======
>>>>>>> support
```

# 16. Переключиться на ветку developи сделать перебазирование относительно ветки main.

```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git checkout develop
Switched to branch 'develop'
Your branch is up to date with 'origin/develop'.

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop)
$ git rebase main
Auto-merging HW7/HW7.md
CONFLICT (content): Merge conflict in HW7/HW7.md
error: could not apply a87b176... Add file README.md and new branch develop
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".    
Could not apply a87b176... Add file README.md and new branch develop

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 1/2)
$ git status
interactive rebase in progress; onto 11a34f1
Last command done (1 command done):
   pick a87b176 Add file README.md and new branch develop
Next command to do (1 remaining command):
   pick 374b793 Update HW7
  (use "git rebase --edit-todo" to view and edit)
You are currently rebasing branch 'develop' on '11a34f1'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        both modified:   HW7.md


Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 1/2)
$ git add .

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 1/2)
$ git status
interactive rebase in progress; onto 11a34f1
Last command done (1 command done):
   pick a87b176 Add file README.md and new branch develop
Next command to do (1 remaining command):
   pick 374b793 Update HW7
  (use "git rebase --edit-todo" to view and edit)
You are currently rebasing branch 'develop' on '11a34f1'.
  (all conflicts fixed: run "git rebase --continue")

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   HW7.md
        modified:   README.md


Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 1/2)
$ git commit
[detached HEAD ae4d938] Add file README.md and new branch develop
 2 files changed, 13 insertions(+)

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 1/2)
$ git status
interactive rebase in progress; onto 11a34f1
Last command done (1 command done):
   pick a87b176 Add file README.md and new branch develop
Next command to do (1 remaining command):
   pick 374b793 Update HW7
  (use "git rebase --edit-todo" to view and edit)
You are currently editing a commit while rebasing branch 'develop' on '11a34f1'.
  (use "git commit --amend" to amend the current commit)
  (use "git rebase --continue" once you are satisfied with your changes)

nothing to commit, working tree clean

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 1/2)
$ git rebase --continue
Auto-merging HW7/HW7.md
CONFLICT (content): Merge conflict in HW7/HW7.md
error: could not apply 374b793... Update HW7
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".    
Could not apply 374b793... Update HW7

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 2/2)
$ git status
interactive rebase in progress; onto 11a34f1
Last commands done (2 commands done):
   pick a87b176 Add file README.md and new branch develop
   pick 374b793 Update HW7
No commands remaining.
You are currently rebasing branch 'develop' on '11a34f1'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        both modified:   HW7.md

no changes added to commit (use "git add" and/or "git commit -a")

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 2/2)
$ git add .

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 2/2)
$ git commit -m "rebase 2/2"
[detached HEAD d2c1445] rebase 2/2
 1 file changed, 6 insertions(+)

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 2/2)
$ git status
interactive rebase in progress; onto 11a34f1
Last commands done (2 commands done):
   pick a87b176 Add file README.md and new branch develop
   pick 374b793 Update HW7
No commands remaining.
You are currently editing a commit while rebasing branch 'develop' on '11a34f1'.
  (use "git commit --amend" to amend the current commit)
  (use "git rebase --continue" once you are satisfied with your changes)

nothing to commit, working tree clean

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (develop|REBASE 2/2)
$ git rebase --continue
Successfully rebased and updated refs/heads/develop.
```

# 17. Вывести историю последних 10 коммитов в виде графа с помощью команды git log -10 --oneline --graph.

```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git log -10 --oneline --graph
* 7da0fd6 (HEAD -> main, origin/main, origin/HEAD) 16 task done
* 11a34f1 Add HW7_16
*   7954728 merge branch support in main
|\
| * 4716de9 (origin/support, support) Update LICENSE-2.0.txt
| * 20f7d2c Add file LICENSE.md and new branch support v2
| * 6bc21a2 Add file LICENSE.md and new branch support
* | 57355c8 Add HW7_15
* |   4486248 Merge branch 'main' of https://github.com/tms-dos17-onl/denis-vedenin        
|\ \  
| * | d0b488b Update LICENSE.txt
* | | 9b54720 Change 14 task v2
|/ /
```