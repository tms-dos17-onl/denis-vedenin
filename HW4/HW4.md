# HW_4
# 1. Отобразить все процессы в системе
```
Вывод команды без фоновых процессов
denis@denis-VirtualBox:~$ ps -a
    PID TTY          TIME CMD
   1341 tty2     00:00:00 gnome-session-b
   3545 pts/0    00:00:00 ps
Вывод команды с фоновыми процессами
denis@denis-VirtualBox:~$ ps -A | head -10
    PID TTY          TIME CMD
      1 ?        00:00:03 systemd
      2 ?        00:00:00 kthreadd
      3 ?        00:00:00 rcu_gp
      4 ?        00:00:00 rcu_par_gp
      5 ?        00:00:00 slub_flushwq
      6 ?        00:00:00 netns
      8 ?        00:00:00 kworker/0:0H-kblockd
      9 ?        00:00:02 kworker/u16:0-flush-8:0
     10 ?        00:00:00 mm_percpu_wq
```
# 2. Запустить бесконечный процесс в фоновом режиме
```
denis@denis-VirtualBox:~$ ping 8.8.8.8 > ping_google &
[1] 3703
denis@denis-VirtualBox:~$ jobs
[1]+  Running                 ping 8.8.8.8 > ping_google &
```

# 3. Убедиться, что процесс продолжил работу после завершения сессии
```
denis@denis-VirtualBox:~$ ps aux
denis       3250  0.0  0.0  21288  3872 pts/0    S    22:00   0:00 /bin/bash ./ping.sh
denis       3251  0.0  0.0  21504  1288 pts/0    S    22:00   0:00 ping 8.8.8.8
```

# 4. Убить процесс, запущенный в фоновом режиме
```
denis@denis-VirtualBox:~$ kill 3250
denis@denis-VirtualBox:~$ jobs -l
[1]+  3250 Terminated              ./ping.sh
```

# 5. Написать свой сервис под управлением systemd, добавить его в автозагрузку (можно использовать процесс из п.2)
```
denis@denis-VirtualBox:~$ sudo nano /etc/systemd/system/hw4_5_1.service
[sudo] password for denis: 
[Unit]
Description=ping google

[Service]
Type=simple
ExecStart=/home/denis/ping.sh
Restart=always

[Install]
WantedBy=multi-user.target


denis@denis-VirtualBox:~$ sudo systemctl start hw4_5_1

denis@denis-VirtualBox:~$ sudo systemctl status hw4_5_1
● hw4_5_1.service - ping google
     Loaded: loaded (/etc/systemd/system/hw4_5_1.service; disabled; vendor preset: enabled)
     Active: active (running) since Fri 2023-08-04 12:49:50 +03; 1s ago

   Main PID: 3661 (ping.sh)
      Tasks: 2 (limit: 4598)
     Memory: 656.0K
        CPU: 8ms
     CGroup: /system.slice/hw4_5_1.service
             ├─3661 /bin/bash /home/denis/ping.sh
             └─3662 ping 8.8.8.8
```



# 6. Посмотреть логи своего сервиса.
```
denis@denis-VirtualBox:~$ journalctl | grep hw4_5_1
жні 04 12:46:33 denis-VirtualBox sudo[3611]:    denis : TTY=pts/0 ; PWD=/home/denis ; USER=root ; COMMAND=/usr/bin/nano /etc/systemd/system/hw4_5_1.service
жні 04 12:49:20 denis-VirtualBox sudo[3622]:    denis : TTY=pts/0 ; PWD=/home/denis ; USER=root ; COMMAND=/usr/bin/systemctl status hw4_5_1
жні 04 12:49:40 denis-VirtualBox sudo[3653]:    denis : TTY=pts/0 ; PWD=/home/denis ; USER=root ; COMMAND=/usr/bin/systemctl status hw4_5_1
жні 04 12:49:50 denis-VirtualBox sudo[3657]:    denis : TTY=pts/0 ; PWD=/home/denis ; USER=root ; COMMAND=/usr/bin/systemctl start hw4_5_1
жні 04 12:49:51 denis-VirtualBox sudo[3663]:    denis : TTY=pts/0 ; PWD=/home/denis ; USER=root ; COMMAND=/usr/bin/systemctl status hw4_5_1
```
