# 1. Вывести в консоль список всех пользователей системы.
```
denis@denis-VirtualBox:~$ awk -F: '{ print $1}' /etc/passwd
root
daemon
bin
sys
sync
games
man
lp
mail
news
uucp
proxy
www-data
backup
list
irc
gnats
nobody
systemd-network
systemd-resolve
messagebus
systemd-timesync
syslog
_apt
tss
uuidd
systemd-oom
tcpdump
avahi-autoipd
usbmux
dnsmasq
kernoops
avahi
cups-pk-helper
rtkit
whoopsie
sssd
speech-dispatcher
fwupd-refresh
nm-openvpn
saned
colord
geoclue
pulse
gnome-initial-setup
hplip
gdm
denis
vboxadd
user_test
sshd
telnetd
```

# 2. Найти и вывести в консоль домашние каталоги для текущего пользователя и root.
```
denis@denis-VirtualBox:~$ pwd
/home/denis

denis@denis-VirtualBox:/$ echo ~root
/root
```

# 3. Создать Bash скрипт get-date.sh, выводящий текущую дату.
```
denis@denis-VirtualBox:~$ bash get-date.sh
Пят 11 жні 2023 18:30:57 +03
```
![bashpng](/HW8/screen/bash.PNG)

# 4. Запустить скрипт через ./get-date.sh и bash get-date.sh. Какой вариант не работает? Сделать так, чтобы оба варианта работали.
```
denis@denis-VirtualBox:~$ bash get-date.sh
Пят 11 жні 2023 18:30:57 +03
denis@denis-VirtualBox:~$ ./get-date.sh
Пят 11 жні 2023 18:32:59 +03
```

# 5. Создать пользователей alice и bob с домашними директориями и установить /bin/bash в качестве командной оболочки по умолчанию.
```
Создание первого поьзователя bob:

denis@denis-VirtualBox:~$ sudo useradd -m bob
[sudo] password for denis: 
denis@denis-VirtualBox:~$ sudo passwd bob
New password: 
BAD PASSWORD: The password is a palindrome
Retype new password: 
passwd: password updated successfully
```
```
Создание второго поьзователя alice:

denis@denis-VirtualBox:~$ sudo useradd -m alice
denis@denis-VirtualBox:~$ sudo passwd alice
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: password updated successfully
```
```
denis@denis-VirtualBox:~$ grep -E "alice|bob" /etc/passwd
bob:x:1002:1002::/home/bob:/bin/sh
alice:x:1003:1003::/home/alice:/bin/sh

Установить /bin/bash в качестве командной оболочки по умолчанию

denis@denis-VirtualBox:~$ sudo usermod -s /bin/bash bob
denis@denis-VirtualBox:~$ sudo usermod -s /bin/bash alice
denis@denis-VirtualBox:~$ grep -E "alice|bob" /etc/passwd
bob:x:1002:1002::/home/bob:/bin/bash
alice:x:1003:1003::/home/alice:/bin/bash
```

# 6. Запустить интерактивную сессию от пользователя alice. Создать файл secret.txt с каким-нибудь секретом в домашней директории при помощи текстового редактора nano.
```
denis@denis-VirtualBox:~$ su alice
Password:
alice@denis-VirtualBox:~$ pwd
/home/alice

alice@denis-VirtualBox:~$ nano secret.txt
alice@denis-VirtualBox:~$ ls
secret.txt
```

# 7. Вывести права доступа к файлу secret.txt.
```
alice@denis-VirtualBox:~$ ls -l
total 4
-rw-rw-r-- 1 alice alice 31 жні 11 20:36 secret.txt
```

# 8. Выйти из сессии от alice и открыть сессию от bob. Вывести содержимое файла /home/alice/secret.txt созданного ранее не прибегая к команде sudo. В случае, если это не работает, объяснить.
```
alice@denis-VirtualBox:~$ su bob
Password: 
bob@denis-VirtualBox:~$ pwd
/home/bob
```
```
bob@denis-VirtualBox:~$ cat /home/alice/secret.txt
cat: /home/alice/secret.txt: Permission denied

Как я понимаю у bob не хватает прав. Так как alice владелец.
```
# 9. Создать файл secret.txt с каким-нибудь секретом в каталоге /tmp при помощи текстового редактора nano.
```
bob@denis-VirtualBox:~$ nano /tmp/secret.txt
bob@denis-VirtualBox:~$ cat /tmp/secret.txt
Я не знаю CI/CD
```
# 10. Вывести права доступа к файлу secret.txt. Поменять права таким образом, чтобы этот файл могли читать только владелец и члены группы, привязанной к файлу.
```
bob@denis-VirtualBox:~$ chmod 440 /tmp/secret.txt 
bob@denis-VirtualBox:~$ ls -l /tmp/secret.txt
-r--r----- 1 bob bob 23 жні 11 21:34 /tmp/secret.txt
bob@denis-VirtualBox:~$ cat /tmp/secret.txt
Я не знаю CI/CD
```

# 11. Выйти из сессии от bob и открыть сессию от alice. Вывести содержимое файла /tmp/secret.txt созданного ранее не прибегая к команде sudo. В случае, если это не работает, объяснить.
```
bob@denis-VirtualBox:~$ su alice
Password: 
alice@denis-VirtualBox:/home/bob$ cd ~
alice@denis-VirtualBox:~$ pwd
/home/alice
alice@denis-VirtualBox:~$ cat /tmp/secret.txt 
cat: /tmp/secret.txt: Permission denied

Так как владелец и группа bob:bob то у alice не хватает прав на чтение .
```

# 12. Добавить пользователя alice в группу, привязанную к файлу /tmp/secret.txt.
```
denis@denis-VirtualBox:~$ sudo usermod -a -G bob alice

denis@denis-VirtualBox:~$ su alice 
Password: 

alice@denis-VirtualBox:/home/denis$ cd ~
alice@denis-VirtualBox:~$ cat /tmp/secret.txt 
Я не знаю CI/CD

alice@denis-VirtualBox:~$ ls -l /tmp/secret.txt 
-r--r----- 1 bob bob 23 жні 11 21:34 /tmp/secret.txt

alice@denis-VirtualBox:~$ tail -3 /etc/passwd
telnetd:x:130:138::/nonexistent:/usr/sbin/nologin
bob:x:1002:1002::/home/bob:/bin/bash
alice:x:1003:1002::/home/alice:/bin/bash
alice@denis-VirtualBox:~$ 
```

# 13. Вывести содержимое файла /tmp/secret.txt.
```
alice@denis-VirtualBox:~$ cat /tmp/secret.txt 
Я не знаю CI/CD
```

# 14. Скопировать домашнюю директорию пользователя alice в директорию /tmp/alice с помощью rsync.
```
alice@denis-VirtualBox:~$ rsync --archive --verbose --progress /home/alice/ /tmp/alice
sending incremental file list
created directory /tmp/alice
./
.bash_logout
            220 100%    0,00kB/s    0:00:00 (xfr#1, to-chk=6/8)
.bashrc
          3.771 100%    3,60MB/s    0:00:00 (xfr#2, to-chk=5/8)
.profile
            807 100%  788,09kB/s    0:00:00 (xfr#3, to-chk=4/8)
secret.txt
             31 100%   30,27kB/s    0:00:00 (xfr#4, to-chk=3/8)
.local/
.local/share/
.local/share/nano/

sent 5.238 bytes  received 144 bytes  10.764,00 bytes/sec
total size is 4.829  speedup is 0,90

alice@denis-VirtualBox:~$ ls /tmp/alice/
secret.txt

Используя опцию --archive, мы рекурсивно (включая вложенные директории) копируем содержимое /source/ в директорию /destination/ вместе с симлинками. Копируются права доступа, атрибуты времени, информация о владельце и группе. Опция --progress включает отображение прогресса во время копирования, --verbose – увеличивает детализацию сообщений программы.
```

# 15. Скопировать домашнюю директорию пользователя alice в директорию /tmp/alice на другую VM по SSH с помощью rsync. Как альтернатива, можно скопировать любую папку с хоста на VM по SSH.
```
Первая ВМ 
denis@denis-VirtualBox:~$ sudo rsync -avz /home/alice denis@192.168.31.184:/tmp
denis@192.168.31.184's password: 
sending incremental file list
alice/
alice/.bash_history
alice/.bash_logout
alice/.bashrc
alice/.profile
alice/secret.txt
alice/.local/
alice/.local/share/
alice/.local/share/nano/
sent 2.943 bytes  received 131 bytes  472,92 bytes/sec
total size is 5.191  speedup is 1,69
```
![](/HW8/screen/VM_1.PNG)
```
Вторая ВМ
denis@denis-VBox:~$ ls /tmp
alice
snap-private-tmp
systemd-private-ae7d01ed582544498c496ef68529e1af-chrony.service-8lPJP1
systemd-private-ae7d01ed582544498c496ef68529e1af-colord.service-LCajbV
systemd-private-ae7d01ed582544498c496ef68529e1af-fwupd.service-rA9nk3
systemd-private-ae7d01ed582544498c496ef68529e1af-ModemManager.service-UhpNoD
systemd-private-ae7d01ed582544498c496ef68529e1af-power-profiles-daemon.service-LSrUpd
systemd-private-ae7d01ed582544498c496ef68529e1af-switcheroo-control.service-WwxkKs
systemd-private-ae7d01ed582544498c496ef68529e1af-systemd-logind.service-BDp4ri
systemd-private-ae7d01ed582544498c496ef68529e1af-systemd-oomd.service-1xsgAM
systemd-private-ae7d01ed582544498c496ef68529e1af-systemd-resolved.service-KzBrUA
systemd-private-ae7d01ed582544498c496ef68529e1af-upower.service-BjbViA
tracker-extract-3-files.1000
denis@denis-VBox:~$ cd /tmp
denis@denis-VBox:/tmp$ ls alice/
secret.txt
```
![](/HW8/screen/VM_2.PNG)

# 16. Удалить пользователей alice и bob вместе с домашними директориями.
```
denis@denis-VirtualBox:~$ sudo userdel --remove bob
[sudo] password for denis: 
denis@denis-VirtualBox:~$ sudo userdel --remove --force alice
denis@denis-VirtualBox:~$ ls /home/
denis  user_test
```

# 17.С помощью утилиты htop определить, какой процесс потребляет больше всего ресурсов в системе
```
denis@denis-VirtualBox:~$ htop
```
![](/HW8/screen/htop.PNG)