# 1. Определить все IP-адреса, маски подсетей и временные MAC-адреса Linux VM. Определите класс и адрес подсети, в которых находится ВМ.
```
denis@denis-VirtualBox:~$ ifconfig

enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::2f4f:ed63:e916:c770  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:64:82:de  txqueuelen 1000  (Ethernet)
        RX packets 6714  bytes 9661552 (9.6 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2176  bytes 180472 (180.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

enp0s8: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.56.106  netmask 255.255.255.0  broadcast 192.168.56.255
        inet6 fe80::3c17:ac14:3783:f692  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:e7:b1:5d  txqueuelen 1000  (Ethernet)
        RX packets 2  bytes 650 (650.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 60  bytes 7764 (7.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 316  bytes 32656 (32.6 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 316  bytes 32656 (32.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
```
ip adress - enp0s3:inet 10.0.2.15;enp0s8:inet 192.168.56.106
маски подсетей - enp0s3:enp0s8:netmask 255.255.255.0 
MAC-адреса - enp0s3: 08:00:27:64:82:de enp0s8: 08:00:27:e7:b1:5d
Класс сети - enp0s3: А enp0s8: C
Адрес сети - enp0s8:11000000.10101000.00111000.00000000 enp0s3:00001010.00000000.00000010.00000000
```

# 2. Определить публичный IP-адрес хоста и Linux VM? Чем они названы?
```
Linux
denis@denis-VirtualBox:~$ curl ifconfig.me
46.216.25.119denis@denis-VirtualBox:~$ 
Windows
C:\Windows\system32>curl.exe ifconfig.me
46.216.25.119
Как я понимаю ВМ автоматически берет сеть хоста(роутера) для выхода в интернет.
```

# 3.Вывести ARP-таблицу на хосте и найти там запись, соответствующую MAC-адресу с большим количеством заданий. Если её нет, то объясни почему.
```
Интерфейс: 192.168.31.197 --- 0x8
  адрес в Интернете      Физический адрес      Тип
  192.168.31.1          3c-cd-57-6f-9a-cd     динамический
  192.168.31.255        ff-ff-ff-ff-ff-ff     статический
  224.0.0.22            01-00-5e-00-00-16     статический
  224.0.0.251           01-00-5e-00-00-fb     статический
  224.0.0.252           01-00-5e-00-00-fc     статический
  239.192.152.143       01-00-5e-40-98-8f     статический
  239.255.102.18        01-00-5e-7f-66-12     статический
  239.255.255.250       01-00-5e-7f-ff-fa     статический
  255.255.255.255       ff-ff-ff-ff-ff-ff     статический

Интерфейс: 192.168.56.1 --- 0xa
  адрес в Интернете      Физический адрес      Тип
  192.168.56.106        08-00-27-e7-b1-5d     динамический
  192.168.56.255        ff-ff-ff-ff-ff-ff     статический
  224.0.0.22            01-00-5e-00-00-16     статический
  224.0.0.251           01-00-5e-00-00-fb     статический
  239.255.255.250       01-00-5e-7f-ff-fa     статический

Интерфейс: 192.168.56.1 --- 0xa есть соответствующий MAC адрес.
```

# 4. Выполнить разбиение сети 172.20.0.0/16 на подсети с маской /24 и ответить на следующие вопросы:
- Сколько всего подсетей будет в сети? 
```
256 (Пример:172.20.1.0\24;172.20.2.0\24;172.20.3.0\24 ...)
```
- Сколько узлов будет в каждой подсети? 
```
(24 бит	255.255.255.0	8 бит	28 – 2)	254 узлов будет 
```
- Каким будет сетевой адрес первой и второй подсети?
```
172.20.0.0\24; 172.20.1.0\24;
```
- Каким будут адреса первого и последнего хостов в первой и второй подсетях?
```
172.20.0.1\24; 172.20.0.254\24;
```
- Каким будет широковещательный адрес в последней подсети?
```
172.20.255.255
```

# 5. Найдите IP-адрес, соответствующий доменному имени ya.ru. Выполните HTTP-запрос на указанный IP-адрес, чтобы скачать страницу с помощью утилиты curl. В результате должна появиться HTML страничка в консоли. Подсказка: https://stackoverflow.com/questions/46563730/can-i-access-to-website-using-ip-address
```
1 способ 
denis@denis-VirtualBox:~$ ping ya.ru -c 3
PING ya.ru (5.255.255.242) 56(84) bytes of data.
64 bytes from ya.ru (5.255.255.242): icmp_seq=1 ttl=51 time=16.7 ms
64 bytes from ya.ru (5.255.255.242): icmp_seq=2 ttl=51 time=16.2 ms
64 bytes from ya.ru (5.255.255.242): icmp_seq=3 ttl=51 time=16.6 ms
--- ya.ru ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2002ms
rtt min/avg/max/mdev = 16.190/16.494/16.661/0.215 ms
```
```
denis@denis-VirtualBox:~$ nslookup
> ya.ru

;; communications error to 127.0.0.53#53: timed out
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	ya.ru
Address: 77.88.55.242
Name:	ya.ru
Address: 5.255.255.242
Name:	ya.ru
Address: 2a02:6b8::2:242
```
```
denis@denis-VirtualBox:~$ curl -k -L -H "Host:ya.ru" http://77.88.55.242 > ya.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 12876  100 12876    0     0  75770      0 --:--:-- --:--:-- --:--:-- 75770

html сайта находится в файле ya.html
```