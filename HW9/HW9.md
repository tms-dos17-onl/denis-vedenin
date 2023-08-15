# 1. Добавить новый диск к виртуальной машине и проверить, что система видит его.
```
Без добавленого диска
denis@denis-VBox:~$ lsblk -b | grep sd

sda      8:0    0 32212254720  0 disk 
├─sda1   8:1    0     1048576  0 part 
├─sda2   8:2    0   537919488  0 part /boot/efi
└─sda3   8:3    0 31671189504  0 part /var/snap/firefox/common/host-hunspell
```
```
Диск 2 добавлен
denis@denis-VBox:~$ lsblk | grep sd

sda      8:0    0    30G  0 disk 
├─sda1   8:1    0     1M  0 part 
├─sda2   8:2    0   513M  0 part /boot/efi
└─sda3   8:3    0  29,5G  0 part /var/snap/firefox/common/host-hunspell

sdb      8:16   0     5G  0 disk 

Второй способ 
denis@denis-VBox:~$ sudo fdisk -l | grep sd

Disk /dev/sda: 30 GiB, 32212254720 bytes, 62914560 sectors
/dev/sda1     2048     4095     2048    1M BIOS boot
/dev/sda2     4096  1054719  1050624  513M EFI System
/dev/sda3  1054720 62912511 61857792 29,5G Linux filesystem

Disk /dev/sdb: 5 GiB, 5368709120 bytes, 10485760 sectors
```
![](/HW9/screenHW9/disk.PNG)

# 2. Вывести в консоль информацию по текущему размеру файловой системы.
```
denis@denis-VBox:~$ lsblk -f | grep sd
sda                                                                             
├─sda1                                                                          
├─sda2 vfat     FAT32       E7C0-0791                             505,9M     1% /boot/efi
└─sda3 ext4     1.0         45a4be74-420e-4d85-afea-fe830c241928   15,5G    41% /var/snap/firefox/common/host-hunspell

sdb                                                             
└─sdb1 ext4     1.0         a1129056-bd24-4570-b71a-2dcb7356c44d    4,6G     0% /media/denis/a1129056-bd24-4570-b71a-2dcb7356c44d
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