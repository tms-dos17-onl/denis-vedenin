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

# 8. Вернуть коммит, где создается пустой файл README.md. Для этого нужно найти ID коммита в git reflog, а затем сделать cherry-pick.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git reflog
c24d232 (HEAD -> main) HEAD@{0}: commit: Task 7 done 'git reset --hard HEAD~3'
3742126 HEAD@{1}: reset: moving to HEAD~3
21d5854 HEAD@{2}: commit: Task 6 done 'Revert Task 5'
626a58b HEAD@{3}: revert: Revert "Task 5 done'Add Hello, DevOps in README.md'"
80fc5d3 HEAD@{4}: commit: Task 5 done'Add Hello, DevOps in README.md'
3742126 HEAD@{5}: commit: Task 4 done'touch README.md'
5e2741e HEAD@{6}: commit: Task 3 done'git lo -3'
37e6aff HEAD@{7}: commit: Task 2 done
8156faf HEAD@{8}: commit: Task 1 done 'remote repositories'
516b422 (origin/main, origin/HEAD) HEAD@{9}: pull: Fast-forward
544b7a8 HEAD@{10}: checkout: moving from bf2224bb6e47fa878b8fe88559ca21ba948f9abc to main
bf2224b HEAD@{11}: reset: moving to bf2224bb
49288cd HEAD@{12}: checkout: moving from main to 49288cd
544b7a8 HEAD@{13}: checkout: moving from bf2224bb6e47fa878b8fe88559ca21ba948f9abc to main
bf2224b HEAD@{14}: reset: moving to bf2224bb6e47fa878b8fe88559ca21ba948f9abc
49288cd HEAD@{15}: checkout: moving from main to 49288cd06d51de6479b9e3a3f21a5044368ec81f
544b7a8 HEAD@{16}: pull --tags origin main: Fast-forward
bf2224b HEAD@{17}: reset: moving to bf2224bb
544b7a8 HEAD@{18}: checkout: moving from bf2224bb6e47fa878b8fe88559ca21ba948f9abc to main
bf2224b HEAD@{19}: reset: moving to bf2224bb
49288cd HEAD@{20}: checkout: moving from main to 49288cd06d51de6479b9e3a3f21a5044368ec81f
544b7a8 HEAD@{21}: checkout: moving from 1fb3f5968af5dee26e7e0a47f01710d17f20ba41 to main
1fb3f59 HEAD@{22}: checkout: moving from 544b7a8059fb7b7356e82c75fe6ee663cb3a788a to 1fb3f5968af5dee26e7e0a47f01710d17f20ba41
544b7a8 HEAD@{23}: checkout: moving from b68ea90831d4aa5952b3e9bdbab0ec4cc8363d7f to 544b7a8059fb7b7356e82c75fe6ee663cb3a788a
b68ea90 HEAD@{24}: checkout: moving from main to b68ea90831d4aa5952b3e9bdbab0ec4cc8363d7f
544b7a8 HEAD@{25}: checkout: moving from bf2224bb6e47fa878b8fe88559ca21ba948f9abc to main
bf2224b HEAD@{26}: checkout: moving from main to bf2224bb

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git cherry-pick 3742126
Auto-merging HW7/HW7.md
CONFLICT (content): Merge conflict in HW7/HW7.md
error: could not apply 3742126... Task 4 done'touch README.md'
hint: After resolving the conflicts, mark them with
hint: "git add/rm <pathspec>", then run
hint: "git cherry-pick --continue".
hint: You can instead skip this commit with "git cherry-pick --skip".
hint: To abort and get back to the state before "git cherry-pick",
hint: run "git cherry-pick --abort".

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main|CHERRY-PICKING)
$ git cherry-pick --continue
error: Committing is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
U       HW7/HW7.md

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main|CHERRY-PICKING)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

You are currently cherry-picking commit 3742126.
  (fix conflicts and run "git cherry-pick --continue")
  (use "git cherry-pick --skip" to skip this patch)
  (use "git cherry-pick --abort" to cancel the cherry-pick operation)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   HW7.md

no changes added to commit (use "git add" and/or "git commit -a")

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main|CHERRY-PICKING)
$ git add .

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main|CHERRY-PICKING)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

You are currently cherry-picking commit 3742126.
  (all conflicts fixed: run "git cherry-pick --continue")
  (use "git cherry-pick --skip" to skip this patch)
  (use "git cherry-pick --abort" to cancel the cherry-pick operation)

Changes to be committed:
        modified:   HW7.md


Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main|CHERRY-PICKING)
$ git cherry-pick --continue
[main 0838600] Task 4 done'touch README.md'
 Date: Fri Aug 4 19:36:41 2023 +0300
 1 file changed, 6 insertions(+)
```

# 9. Удалить последний коммит с помощью git reset.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git reset --hard HEAD~
HEAD is now at 0838600 Task 4 done'touch README.md'
```

# 10. Переключиться на ветку mainили master. Если ветка называетсяmaster, то переименовать её в main.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin/HW7 (main)
$ git checkout main
Already on 'main'
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)
```

# 11. Скопировать файл https://github.com/tms-dos17-onl/_sandbox/blob/main/.github/workflows/validate-shell.yaml , положить его по такому же относительному пути в репозиторий. Создать коммит и запушить его в удаленный репозиторий.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git add .

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .github/workflows/validate-shell.yaml

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git commit -m "Task 11 done '.github/workflows/validate-shell.yaml'"
[main 4ea8911] Task 11 done '.github/workflows/validate-shell.yaml'
 1 file changed, 24 insertions(+)
 create mode 100644 .github/workflows/validate-shell.yaml
```

# 12. Создать из ветки main ветку develop. Переключиться на нее и создать README.md в корневом репозитории. Напишите в этом файле, какие инструменты DevOps вам знакомы и с чем вы хотели бы познакомиться с большими скоростями (2-3 балла).
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git checkout -b develop
Switched to a new branch 'develop'

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git checkout -b develop
Switched to a new branch 'develop'

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (develop)
$ cat README.md 
Я знаю:
- Git,Github
- Linux
- VirtualBox

Я хочу узнать:
- CI/CD
- AWS
- Kubernetes
- Docker
- Jenkins
```

# 13. Настройте из ветки mainветку supportи там файл LICENSEв корневой репозитории с содержимым https://www.apache.org/licenses/LICENSE-2.0.txt . Создать коммит. Вывести последние 3 коммита.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git checkout -b support
Switched to a new branch 'support'

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (support)
$ curl -O https://www.apache.org/licenses/LICENSE-2.0.txt > LICENSE
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 11358  100 11358    0     0  47027      0 --:--:-- --:--:-- --:--:-- 47722

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (support)
$ git log -3
commit 87835f1cbcc8df2555df6446d38c01c93580f358 (HEAD -> support)
Author: denis-vedenin <denved98@mail.ru>
Date:   Sat Aug 5 13:53:06 2023 +0300

    Task 12 done 'new branch support and add file LICENSE'

commit 4ea8911729e3d0c2c8655db7d516a2bae9016d6c (main)
Author: denis-vedenin <denved98@mail.ru>
Date:   Sat Aug 5 13:23:10 2023 +0300

    Task 11 done '.github/workflows/validate-shell.yaml'

commit a20bdecf3eb51a5636058b75bb014632a841dedb
Author: denis-vedenin <denved98@mail.ru>
Date:   Sat Aug 5 12:58:14 2023 +0300

    Task 10 done 'git checkout main'
```

# 14. Переключиться обратно на ветку mainи создать там файл LICENSEв корневой репозитории с содержимым https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt . Создать коммит. Вывести последние 3 коммита.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ curl.exe https://raw.githubusercontent.com/git/git-scm.com/main/MIT-LICENSE.txt > LICENSE
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1072  100  1072    0     0   3727      0 --:--:-- --:--:-- --:--:--  3761

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git add .
warning: in the working copy of 'LICENSE', LF will be replaced by CRLF the next time Git touches it

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   LICENSE


Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git commit -m "Task 14 done 'add file LICENSE'"
```

# 15. Сделать слияние ветки supportв ветку mainи решить конфликты выбора пути выбора только одной лицензии.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git merge support
Auto-merging LICENSE
CONFLICT (add/add): Merge conflict in LICENSE
Automatic merge failed; fix conflicts and then commit the result.

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main|MERGING)
$ nano LICENSE

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main|MERGING)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
        new file:   LICENSE-2.0.txt

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both added:      LICENSE

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   HW7/HW7.md


Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main|MERGING)
$ git add .

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main|MERGING)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   HW7/HW7.md
        modified:   LICENSE
        new file:   LICENSE-2.0.txt
```

# 16. Переключиться на ветку develop и сделать rebase относительно ветки main.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git checkout develop
Switched to branch 'develop'

Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (develop)
$ git rebase main
Successfully rebased and updated refs/heads/develop.
```

# 17. Вывести историю последних 10 коммитов в виде графа с помощью команды git log -10 --oneline --graph. 
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (develop)
$ git log -10 --oneline --graph
* bd304ae (HEAD -> develop) Task 12 done 'new branch develop'
*   dc19dec (main) Change conflict LICENSE
|\
| * d973439 (support) Update LICENSE
| * 87835f1 Task 12 done 'new branch support and add file LICENSE'
* | 480fa17 Task 14 done 'add file LICENSE'
|/
* 4ea8911 Task 11 done '.github/workflows/validate-shell.yaml'
* a20bdec Task 10 done 'git checkout main'
*   38938dc Conflict
|\  
| * fe53632 (origin/main, origin/HEAD) Task 8 done 'git reglog and git cherry pick'     
* | cf3505f Task 9 done 'git reset --hard HEAD~'
|/
```

# 18. Запушить ветку develop. В истории коммитов должен быть мерж support -> main.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (develop)
$ git push origin develop -f
Enumerating objects: 42, done.
Counting objects: 100% (41/41), done.
Delta compression using up to 20 threads
Compressing objects: 100% (32/32), done.
Writing objects: 100% (34/34), 9.70 KiB | 1.39 MiB/s, done.
Total 34 (delta 15), reused 3 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (15/15), completed with 1 local object.
remote: 
remote: Create a pull request for 'develop' on GitHub by visiting:
remote:      https://github.com/tms-dos17-onl/denis-vedenin/pull/new/develop
remote:
To https://github.com/tms-dos17-onl/denis-vedenin.git
 * [new branch]      develop -> develop
```