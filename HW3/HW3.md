# 1. Создать bash-скрипт собирающий данные о количестве свободной памяти, текущей загрузке процессора, ip-адрес, вывести в формате «Ключ: значение», причем все ключи заменить на русские названия, например чтобы вместо «Mem: 1024Mb» получалось «Память: 1024Мб», для приведения к нужному формату использовать grep, sed и awk.
```
Для начал создаем файл hw3_1.sh
denis@denis-VirtualBox:~/Desktop$ touch hw3_1.sh
denis@denis-VirtualBox:~/Desktop$ nano hw3_1.sh
Далее в файл записываю в файл
#!/bin/bash
#Пишем скрипт о нагрузке ЦП и Памяти и о нахождение IP адресса
cpuUsage=$(top -bn1 | awk '/Cpu/ { print $2}')
memUsage=$(free -h | awk '/Mem/{print $3}' | sed 's/Gi/Гб/g')
ipUsage=$(ip -4 a | grep /24 | sed 's/inet/ /g')
# Вывод о нагрузках ЦП и Памяти и IP адресс
echo "Нагрузка ЦП: $cpuUsage%"
echo "Нагрузка Памяти: $memUsage"
echo "IP Адрес:  $ipUsage"
```

# 2. Написать bash-скрипт который создает пользователя (принимает имя в качестве первого аргумента) и создает в его домашней директории файл с информацией о системе: Ядро, CPU, RAM, Дисковая подсистема (lscpu, lsblk, uname, etc). Вывод каждой команды должен быть отделен сепаратором (например ====)
```
Создаю файл hw3_2.sh
#!/bin/bash
#Создание пользователя

sudo useradd -m $1
sudo passwd $1
echo "=====" >>/home/$1/sys_info
uname -a >>/home/$1/sys_info
echo "=====" >>/home/$1/sys_info
lscpu >>/home/$1/sys_info
echo "=====" >>/home/$1/sys_info
lsblk >>/home/$1/sys_info
echo "=====" >>/home/$1/sys_info
vmstat -s >>/home/$1/sys_info
Даю пра на исполнение файла
denis@denis-VirtualBox:~/Desktop$ chmod +x hw3_2.sh 
Выполняю команду с параметром  user_test
denis@denis-VirtualBox:~/Desktop$ sudo ./hw3_2.sh user_test
[sudo] password for denis: 
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: password updated successfully
Далее сменил пользователя для проверки 
denis@denis-VirtualBox:~$ su user_test
Password:
$pwd
/home/user_test
```
# 3. Cоздать файл immortalfile, запретить удаление файла даже пользователем root и попытаться его удалить из под root, результатом должно быть “Operation not permitted”. Подсказка: CHATTR(1)
```
denis@denis-VirtualBox:~$ touch /tmp/immortalfile 
denis@denis-VirtualBox:~$ sudo chattr +i /tmp/immortalfile 
denis@denis-VirtualBox:~$ sudo rm /tmp/immortalfile
rm: cannot remove '/tmp/immortalfile': Operation not permitted
```

# 4. выполнить команду, разобраться что она делает и что сохраняется в file.log
```
env -i bash -x -l -c 'echo hello_there!' > file.log 2>&1
env -i выполняет указанную команду с пустым окружением, bash -x -l -c выполняет команду 'echo hello_there!' в качестве кода на языке bash, при этом:
ключ -x выводит команду и их аргументы по мере их выполнения (запускает в режиме отладки, где перед каждой командой ставится +)
ключ -l вызывает этот командный интерпретатор.
ключ -с считывает команду из строки (непостредственно выводит "hello_there!")
">file.log" - перенаправляет поток вывода в файл file.log. Если файл не существует, он будет создан, если существует — перезаписан сверху.
2 > &1 - перенаправить стандартный поток ошибок в файл (ошибка будет направлена ​​в тот же поток, что поток и вывод потока - в файл file.log)
```