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

![bash]()
```

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
