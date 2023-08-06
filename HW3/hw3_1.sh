#!/bin/bash
#Пишем скрипт о нагрузке ЦП и Памяти и о нахождение IP адресса
cpuUsage=$(top -bn1 | awk '/Cpu/ { print $2}')
memUsage=$(free -h | awk '/Mem/{print $3}' | sed 's/Gi/Гб/g')
ipUsage=$(ip -4 a | grep /24 | sed 's/inet/ /g')
# Вывод о нагрузках ЦП и Памяти и IP адресс
echo "Нагрузка ЦП: $cpuUsage%"
echo "Нагрузка Памяти: $memUsage"
echo "IP Адрес:  $ipUsage"
