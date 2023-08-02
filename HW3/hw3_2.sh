sudo useradd -m $1
sudo passwd $1
echo "=====" >> /home/$1/sys_info
uname -a >> /home/$1/sys_info
echo "=====" >> /home/$1/sys_info
lscpu >> /home/$1/sys_info
echo "=====" >> /home/$1/sys_info
lsblk >> /home/$1/sys_info
echo "=====" >> /home/$1/sys_info
vmstat -s >> /home/$1/sys_info
