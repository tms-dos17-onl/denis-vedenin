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

# 4. Запустить скрипт через ./get-date.sh и bash get-date.sh. Какой вариант не работает? Сделать так, чтобы оба варианта работали.
```
denis@denis-VirtualBox:~$ bash get-date.sh
Пят 11 жні 2023 18:30:57 +03
denis@denis-VirtualBox:~$ ./get-date.sh
Пят 11 жні 2023 18:32:59 +03
```

