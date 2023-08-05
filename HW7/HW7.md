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
<<<<<<< HEAD

# 9. Удалить последний коммит с помощью git reset.
```
Денис DevOps@denis-vedenin MINGW64 ~/denis-vedenin (main)
$ git reset --hard HEAD~
HEAD is now at 0838600 Task 4 done'touch README.md'
```
=======
>>>>>>> fe53632a880b6f97f8f0b05e4e8ddb651972f306
