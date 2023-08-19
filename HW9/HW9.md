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
# 4. Вывести информацию по новому размеру файловой системы.
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