#!/bin/bash
   
printf '\033]2;install.sh\a'

G="\033[1;34m[*] \033[0m"
S="\033[1;32m[+] \033[0m"
E="\033[1;31m[-] \033[0m"

if [[ $(id -u) != 0 ]]
then
   echo -e ""$E"Permission denied!"
   exit
fi

{
ASESR="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
} &> /dev/null
if [[ "$ASESR" != 0 ]]
then
   echo -e ""$E"No Internet connection!"
   exit
fi

sleep 0.5
clear
sleep 0.5
echo
cat banner/banner.txt
echo

sleep 1
echo -e ""$G"Installing dependencies..."
sleep 1

{
pkg update
pkg -y install git
pkg -y install python
pkg -y install openssl
apt-get update
apt-get -y install git
apt-get -y install python3
apt-get -y install openssl
apk update
apk add git
apk add python3
apk add openssl
pacman -Sy
pacman -S --noconfirm git
pacman -S --noconfirm python3
pacman -S --noconfirm openssl
zypper refresh
zypper install -y git
zypper install -y python3
zypper install -y openssl
yum -y install git
yum -y install python3
yum -y install openssl
dnf -y install git
dnf -y install python3
dnf -y install openssl
eopkg update-repo
eopkg -y install git
eopkg -y install python3
eopkg -y install openssl
xbps-install -S
xbps-install -y git
xbps-install -y python3
xbps-install -y openssl
} &> /dev/null

if [[ -d ~/mouse ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/mouse.git
} &> /dev/null
fi

if [[ -d ~/mouse ]]
then
cd ~/mouse
else
echo -e ""$E"Installation failed!"
exit
fi

{
cd bin
cp mouse /usr/local/bin
chmod +x /usr/local/bin/mouse
cp mouse /bin
chmod +x /bin/mouse
cp mouse /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/mouse
} &> /dev/null

sleep 1
echo -e ""$S"Successfully installed!"
sleep 1
