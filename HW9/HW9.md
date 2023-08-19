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
![](/HW9/screenHW9/disk.PNG)

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
# 6. Вывести в консоль все файлы из домашней директории.
# 7. Построить маршрут до google.com при помощи утилиты traceroute.
# 8. Установить Sonatype Nexus OSS по следующей инструкции, а именно:
- установку произвести в директорию /opt/nexus.
- запустить приложение от отдельного пользователя nexus.
- реализовать systemd оболочку для запуска приложения как сервис.
# 9. Создать в Nexus proxy репозиторий для пакетов ОС и разрешить анонимный доступ.
# 10. Поменять для текущей VM основной репозиторий пакетов на созданный ранее proxy в Nexus.
# 11. Выполнить установку пакета snap и убедиться, что на proxy репозитории в Nexus появились пакеты.
# 12. (**) На основании шагов из предыдущих пунктов создать DEB/RPM пакет для установки Nexus и загрузить его в Nexus.