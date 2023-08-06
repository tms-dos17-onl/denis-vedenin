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

Запускаю tcpdump на первой ВМ для отлова пакетов
denis@denis-VirtualBox:~$ sudo tcpdump -i enp0s8 > tcpdump 
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on enp0s8, link-type EN10MB (Ethernet), snapshot length 262144 bytes
128 packets captured
128 packets received by filter
0 packets dropped by kernel

Запускаю telnet на второй ВМ
denis@denis-VirtualBox:~$ telnet 192.168.56.106 23
Trying 192.168.56.106...
Connected to 192.168.56.106.
Escape character is '^]'.
Ubuntu 22.04.2 LTS
denis-VirtualBox login: denis
Password: 
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.19.0-50-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

Expanded Security Maintenance for Applications is not enabled.
50 updates can be applied immediately.
5 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable
7 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm
Last login: Sun Aug  6 14:52:43 +03 2023 from denis-VirtualBox on pts/3

Вывод пакетов вывел в файл tcpdump.md
```

#
```
denis@denis-VirtualBox:~$ sudo iptables -A INPUT -p tcp --dport 222 -j ACCEPT
denis@denis-VirtualBox:~$ sudo iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:222

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination   

Дальше попробовал прослушать порт запустил на первой ВМ 
denis@denis-VirtualBox:~$ sudo nc -lpv 222
Listening on 0.0.0.0 222
Connection received on 192.168.56.1 56083
google
Hello world !
И на второй ВМ и получил чат
denis@denis-VBox:~$ sudo nc 192.168.56.106 222
google
Hello world !

denis@denis-VirtualBox:~$ nmap -PN 222 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2023-08-06 15:58 +03
Nmap scan report for 222 (0.0.0.222)
Host is up (0.016s latency).
All 1000 scanned ports on 222 (0.0.0.222) are filtered

Nmap scan report for localhost (127.0.0.1)
Host is up (0.00049s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
23/tcp  open  telnet
631/tcp open  ipp

Nmap done: 2 IP addresses (2 hosts up) scanned in 0.37 seconds
```