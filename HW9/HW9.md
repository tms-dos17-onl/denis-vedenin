# 1. Добавить новый диск к виртуальной машине и проверить, что система видит его.
```
denis@denis-VirtualBox:~$ lsblk

NAME                MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0                 7:0    0  63,4M  1 loop /snap/core20/1974
loop1                 7:1    0     4K  1 loop /snap/bare/5
loop2                 7:2    0  73,9M  1 loop /snap/core22/858
loop3                 7:3    0 237,2M  1 loop /snap/firefox/2987
loop4                 7:4    0 349,7M  1 loop /snap/gnome-3-38-2004/143
loop5                 7:5    0 485,5M  1 loop /snap/gnome-42-2204/120
loop6                 7:6    0  91,7M  1 loop /snap/gtk-common-themes/1535
loop7                 7:7    0  12,3M  1 loop /snap/snap-store/959
loop8                 7:8    0  53,3M  1 loop /snap/snapd/19457
loop9                 7:9    0   452K  1 loop /snap/snapd-desktop-integration/83
loop10                7:10   0  63,5M  1 loop /snap/core20/2015
loop11                7:11   0 485,5M  1 loop /snap/gnome-42-2204/126
sda                   8:0    0    25G  0 disk 
├─sda1                8:1    0     1M  0 part 
├─sda2                8:2    0   513M  0 part /boot/efi
└─sda3                8:3    0  24,5G  0 part 
  ├─vgubuntu-root   253:0    0  22,6G  0 lvm  /var/snap/firefox/common/host-hunspell
  │                                           /
  └─vgubuntu-swap_1 253:1    0   1,9G  0 lvm  [SWAP]
sdb                   8:16   0    10G  0 disk 
└─sdb1                8:17   0    10G  0 part /mnt/disksdb1
```

# 2. Вывести в консоль информацию по текущему размеру файловой системы.
```
denis@denis-VirtualBox:~$ df -h

Файл.система              Размер Использовано  Дост Использовано% Cмонтировано в
tmpfs                       391M         1,5M  390M            1% /run
/dev/mapper/vgubuntu-root    23G         9,4G   12G           45% /
tmpfs                       2,0G            0  2,0G            0% /dev/shm
tmpfs                       5,0M         4,0K  5,0M            1% /run/lock
/dev/sda2                   512M         6,1M  506M            2% /boot/efi
tmpfs                       391M         112K  391M            1% /run/user/1000
/dev/sdb1                   9,8G          24K  9,3G            1% /mnt/disksdb1
```
# 3. Расширить корневую файловую систему за счёт добавленного диска.
```
В задание №1 я добавил диск отворматировал и создал раздел
denis@denis-VirtualBox:~$ lsblk

sda               8:0    0    25G  0 disk 
├─sda1            8:1    0     1M  0 part 
├─sda2            8:2    0   513M  0 part /boot/efi
└─sda3            8:3    0  24,5G  0 part 
  ├─vgubuntu-root
  │             253:0    0  22,6G  0 lvm  /var/snap/firefox/common/host-hunspell
  │                                       /
  └─vgubuntu-swap_1

                253:1    0   1,9G  0 lvm  [SWAP]
sdb               8:16   0    10G  0 disk 
└─sdb1            8:17   0    10G  0 part 
```
## но дальше я немог увеличить диск так как в нем уже был раздел, я его удалил и далее уже по инструкции https://www.cyberciti.biz/faq/howto-add-disk-to-lvm-volume-on-linux-to-increase-size-of-pool/ прошёл все шаги и у мея всё получилась. Возможно было сделать как то по другому , но лично мне помог этот способ.
```
denis@denis-VirtualBox:~$ sudo pvcreate /dev/sdb

WARNING: dos signature detected on /dev/sdb at offset 510. Wipe it? [y/n]: y
  Wiping dos signature on /dev/sdb.
  Physical volume "/dev/sdb" successfully created.

denis@denis-VirtualBox:~$  sudo lvmdiskscan -l
  WARNING: only considering LVM devices
  /dev/sda3   [     <24,50 GiB] LVM physical volume
  /dev/sdb    [      10,00 GiB] LVM physical volume
  1 LVM physical volume whole disk
  1 LVM physical volume

denis@denis-VirtualBox:~$ sudo vgextend vgubuntu /dev/sdb
  Volume group "vgubuntu" successfully extended

denis@denis-VirtualBox:~$ sudo lvm lvextend -l +100%FREE /dev/vgubuntu/root

  Size of logical volume vgubuntu/root changed from 22,58 GiB (5781 extents) to <32,58 GiB (8340 extents).
  Logical volume vgubuntu/root successfully resized.

denis@denis-VirtualBox:~$ lsblk

sda               8:0    0    25G  0 disk 
├─sda1            8:1    0     1M  0 part 
├─sda2            8:2    0   513M  0 part /boot/efi
└─sda3            8:3    0  24,5G  0 part 
  ├─vgubuntu-root
  │             253:0    0  32,6G  0 lvm  /var/snap/firefox/common/host-hunspell
  │                                       /
  └─vgubuntu-swap_1
                253:1    0   1,9G  0 lvm  [SWAP]

sdb               8:16   0    10G  0 disk 
└─vgubuntu-root 253:0    0  32,6G  0 lvm  /var/snap/firefox/common/host-hunspell
```
# 4. Вывести информацию по новому размеру файловой системы.
```
denis@denis-VirtualBox:~$ df -Th

Файл.система              Тип   Размер Использовано  Дост Использовано% Cмонтировано в
tmpfs                     tmpfs   391M         1,5M  390M            1% /run
/dev/mapper/vgubuntu-root ext4     23G         9,4G   12G           45% /
tmpfs                     tmpfs   2,0G            0  2,0G            0% /dev/shm
tmpfs                     tmpfs   5,0M         4,0K  5,0M            1% /run/lock
/dev/sda2                 vfat    512M         6,1M  506M            2% /boot/efi
tmpfs                     tmpfs   391M         108K  391M            1% /run/user/1000
```

```
denis@denis-VirtualBox:~$ lsblk

NAME                MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS

sda                   8:0    0    25G  0 disk 
├─sda1                8:1    0     1M  0 part 
├─sda2                8:2    0   513M  0 part /boot/efi
└─sda3                8:3    0  24,5G  0 part 
  ├─vgubuntu-root   253:0    0  32,6G  0 lvm  /var/snap/firefox/common/host-hunspell
  │                                           /
  └─vgubuntu-swap_1 253:1    0   1,9G  0 lvm  [SWAP]

sdb                   8:16   0    10G  0 disk 
└─vgubuntu-root     253:0    0  32,6G  0 lvm  /var/snap/firefox/common/host-hunspell
```
# 5. Вывести в консоль текущую рабочую директорию.
```
denis@denis-VirtualBox:~$ pwd
/home/denis
```
# 6. Вывести в консоль все файлы из домашней директории.
```
denis@denis-VirtualBox:~$ ls -la ~
итого 88
drwxr-x--- 14 denis denis 4096 жні 19 16:25  .
drwxr-xr-x  3 root  root  4096 жні 18 17:52  ..
-rw-------  1 denis denis 1048 жні 19 16:23  .bash_history
-rw-r--r--  1 denis denis  220 жні 18 17:52  .bash_logout
-rw-r--r--  1 denis denis 3771 жні 18 17:52  .bashrc
drwx------ 10 denis denis 4096 жні 18 18:12  .cache
drwx------ 11 denis denis 4096 жні 18 18:32  .config
drwx------  3 denis denis 4096 жні 18 18:10  .local
-rw-r--r--  1 denis denis  807 жні 18 17:52  .profile
drwx------  3 denis denis 4096 жні 18 18:12  snap
-rw-r--r--  1 denis denis    0 жні 18 18:31  .sudo_as_admin_successful
-rw-r-----  1 denis denis    5 жні 19 16:25  .vboxclient-clipboard.pid
-rw-r-----  1 denis denis    5 жні 19 16:25  .vboxclient-draganddrop.pid
-rw-r-----  1 denis denis    5 жні 19 16:25  .vboxclient-seamless.pid
-rw-r-----  1 denis denis    5 жні 19 16:25  .vboxclient-vmsvga-session-tty2.pid
drwxr-xr-x  2 denis denis 4096 жні 18 18:10  Видео
drwxr-xr-x  2 denis denis 4096 жні 18 18:10  Документы
drwxr-xr-x  2 denis denis 4096 жні 18 18:10  Загрузки
drwxr-xr-x  2 denis denis 4096 жні 18 18:10  Изображения
drwxr-xr-x  2 denis denis 4096 жні 18 18:10  Музыка
drwxr-xr-x  2 denis denis 4096 жні 18 18:10  Общедоступные
drwxr-xr-x  2 denis denis 4096 жні 18 18:10 'Рабочий стол'
drwxr-xr-x  2 denis denis 4096 жні 18 18:10  Шаблоны
```
# 7. Построить маршрут до google.com при помощи утилиты traceroute.
```
denis@denis-VirtualBox:~$ sudo traceroute google.com

traceroute to google.com (216.58.206.46), 30 hops max, 60 byte packets
1  _gateway (10.0.2.2)  0.221 ms  0.159 ms  0.111 ms
2  * * *
3  * * *
4  * * *
5  * * *
6  * * *
7  * * *
8  * * *
9  * * *
10  * * *
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *
```
## Как я понял команда traceroute отправляет UDP пакеты и то что я увидел * * * значит что шлюзы либо не высылают нам ICMP с сообщением «time exceeded», либо у их сообщений слишком маленький TTL и оно нас не достигает. Поэтому я дабил опцию -I.
```
denis@denis-VirtualBox:~$ sudo traceroute -I google.com

traceroute to google.com (216.58.206.46), 30 hops max, 60 byte packets
1  _gateway (10.0.2.2)  0.996 ms  0.946 ms  0.926 ms
2  XiaoQiang (192.168.31.1)  2.744 ms  3.072 ms  2.642 ms
3  46.216.0.1 (46.216.0.1)  3.060 ms  3.438 ms  3.413 ms
4  195.50.15.55 (195.50.15.55)  3.915 ms  4.127 ms  4.921 ms
5  195.50.15.54 (195.50.15.54)  5.594 ms  5.971 ms  5.951 ms
6  185.11.76.65 (185.11.76.65)  4.002 ms  3.954 ms  3.920 ms
7  185.11.76.28 (185.11.76.28)  3.900 ms  3.218 ms  4.203 ms
8  72.14.210.226 (72.14.210.226)  27.819 ms  27.804 ms  27.784 ms
9  108.170.236.193 (108.170.236.193)  27.767 ms  28.048 ms  28.030 ms
10  192.178.74.165 (192.178.74.165)  26.462 ms  27.691 ms  28.359 ms
11  lcfraa-aa-in-f14.1e100.net (216.58.206.46)  29.088 ms  29.070 ms  27.515 ms
```
# 8. Установить Sonatype Nexus OSS по следующей инструкции, а именно:
- установку произвести в директорию /opt/nexus.
```
Сначала обновляем системные пакеты до последней версии
denis@denis-VirtualBox:~$ sudo apt-get update -y

Далее установил java 8 версии, так как nexus основан на java
sudo apt-get install openjdk-8-jdk -y

Создаю отдельного пользователя для запуска Nexus
sudo useradd -M -d /opt/nexus -s /bin/bash -r nexus

Создаю пользовотеля nexus
denis@denis-VirtualBox:~$ sudo useradd -M -d /opt/nexus -s /bin/bash -r nexus

Проверяю создался ли пользователь 
denis@denis-VirtualBox:~$ cat /etc/passwd
nexus:x:998:997::/opt/nexus:/bin/bash

Далее выполняю действия
denis@denis-VirtualBox:~$ sudo mkdir /opt/nexus
denis@denis-VirtualBox:~$ ls /opt
nexus  VBoxGuestAdditions-7.0.6

denis@denis-VirtualBox:~$ wget https://sonatype-download.global.ssl.fastly.net/repository/downloads-prod-group/3/nexus-3.29.2-02-unix.tar.gz

Заменил ../sonatype-work на ./sonatype-work: в файле nexus_vmoption.md
denis@denis-VirtualBox:~$ sudo nano /opt/nexus/bin/nexus.vmoptions
Раскомментируйте и отредактируйте следующую строку с пользователем nexus: в файле nexus_rc.md
denis@denis-VirtualBox:~$ sudo nano /opt/nexus/bin/nexus.rc
```
- запустить приложение от отдельного пользователя nexus.
```
denis@denis-VirtualBox:~$ sudo -u nexus /opt/nexus/bin/nexus start
Starting nexus

denis@denis-VirtualBox:~$ sudo tail -f /opt/nexus/sonatype-work/nexus3/log/nexus.log > nexuslog.txt

denis@denis-VirtualBox:~$ sudo /opt/nexus/bin/nexus stop
Shutting down nexus
Stopped.
```
- реализовать systemd оболочку для запуска приложения как сервис.
```
Скрипт сервиса находится в файле nexus_service.md
denis@denis-VirtualBox:~$ sudo nano /etc/systemd/system/nexus.service

denis@denis-VirtualBox:~$ sudo systemctl start nexus

denis@denis-VirtualBox:~$ sudo systemctl status nexus
● nexus.service - nexus service
     Loaded: loaded (/etc/systemd/system/nexus.service; disabled; vendor preset: enabled)
     Active: active (running) since Sat 2023-08-19 19:54:02 +03; 10s ago
    Process: 7020 ExecStart=/opt/nexus/bin/nexus start (code=exited, status=0/SUCCESS)

   Main PID: 7192 (java)
      Tasks: 46 (limit: 4585)
     Memory: 375.2M
        CPU: 27.206s
     CGroup: /system.slice/nexus.service
             └─7192 /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -server -Dinstall4j.jvmDir=/usr/lib/>
жні 19 19:54:02 denis-VirtualBox systemd[1]: Starting nexus service...
жні 19 19:54:02 denis-VirtualBox nexus[7020]: Starting nexus
жні 19 19:54:02 denis-VirtualBox systemd[1]: Started nexus service.
```
![](/HW9/screenHW9/nexus.PNG)
# 9. Создать в Nexus proxy репозиторий для пакетов ОС и разрешить анонимный доступ.
![](/HW9/screenHW9/pakeg.PNG)
![](/HW9/screenHW9/pakeg2.PNG)
# 10. Поменять для текущей VM основной репозиторий пакетов на созданный ранее proxy в Nexus.
```
denis@denis-VirtualBox:~$ sudo cat /etc/apt/sources.list | grep 8081
# deb http://127.0.0.1:8081/repository/my_oc_packages/ focal main restricted
# deb http://127.0.0.1:8081/repository/my_oc_packages/ focal-updates main restricted
# deb http://127.0.0.1:8081/repository/my_oc_packages/ focal universe
# deb http://127.0.0.1:8081/repository/my_oc_packages/ focal-updates universe
# deb http://127.0.0.1:8081/repository/my_oc_packages/ focal multiverse  
# deb http://127.0.0.1:8081/repository/my_oc_packages/ focal-updates multiverse 
deb http://127.0.0.1:8081/repository/ubuntu/ focal main restricted
deb http://127.0.0.1:8081/repository/ubuntu/ focal-updates main restricted
deb http://127.0.0.1:8081/repository/ubuntu/ focal universe
deb http://127.0.0.1:8081/repository/ubuntu/ focal-updates universe
```
# 11. Выполнить установку пакета snap и убедиться, что на proxy репозитории в Nexus появились пакеты.
```
denis@denis-VirtualBox:~$ sudo apt install snap
Чтение списков пакетов… Готово
Построение дерева зависимостей… Готово
Чтение информации о состоянии… Готово         
Следующие НОВЫЕ пакеты будут установлены:
  snap
Обновлено 0 пакетов, установлено 1 новых пакетов, для удаления отмечено 0 пакетов, и 5 пакетов не обновлено.
Необходимо скачать 376 kB архивов.
После данной операции объём занятого дискового пространства возрастёт на 2.714 kB.
Пол:1 http://127.0.0.1:8081/repository/ubuntu focal/universe amd64 snap amd64 2013-11-29-9 [376 kB]
Получено 376 kB за 1с (336 kB/s)          
Выбор ранее не выбранного пакета snap.
(Чтение базы данных … на данный момент установлено 168372 файла и каталога.)
Подготовка к распаковке …/snap_2013-11-29-9_amd64.deb …
Распаковывается snap (2013-11-29-9) …
Настраивается пакет snap (2013-11-29-9) …
Обрабатываются триггеры для man-db (2.10.2-1) …
```
![](/HW9/screenHW9/snap.PNG)
# 12. (**) На основании шагов из предыдущих пунктов создать DEB/RPM пакет для установки Nexus и загрузить его в Nexus.
```
не делал
```