# 1. Распределить основные сетевые протоколы (перечислены ниже) по уровням модели TCP/IP
```
UDP - Транспротный 
TCP - Транспротный 
FTP - Прикладной 
RTP - Прикладной 
DNS - Прикладной 
ICMP - Сетевой
HTTP - Прикладной 
NTP - Сетевой
SSH - Сетевой
```

# 2. Узнать pid процесса и длительность подключения ssh с помощью утилиты ss

```
denis@denis-VirtualBox:~$ sudo ss -atop | grep ssh
[sudo] password for denis:
LISTEN 0      128           0.0.0.0:ssh         0.0.0.0:*     users:(("sshd",pid=3826,fd=3))                         
ESTAB  0      0      192.168.56.106:ssh    192.168.56.1:51404 users:(("sshd",pid=4238,fd=4),("sshd",pid=4201,fd=4)) timer:(keepalive,109min,0)
LISTEN 0      128              [::]:ssh            [::]:*     users:(("sshd",pid=3826,fd=4))  
```

# 3. Закрыть все порты для входящих подключений, кроме ssh
```
denis@denis-VirtualBox:~$ sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
denis@denis-VirtualBox:~$ sudo iptables -L
Chain INPUT (policy DROP)
target     prot opt source               destination         
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination 
```

# 4. Установить telnetd на ВМ, зайти на другой ВМ с помощью telnet и отловить введенный пароль и введенные команды при входе c помощью tcpdump
```
denis@denis-VirtualBox:~$ sudo apt-get install telnetd

login as: denis
denis@192.168.56.106's password:
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.19.0-50-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

Expanded Security Maintenance for Applications is not enabled.

34 updates can be applied immediately.
5 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

7 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm

Last login: Sat Aug  5 17:01:32 2023 from 192.168.56.1

```