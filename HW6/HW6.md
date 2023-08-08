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