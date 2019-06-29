#! /bin/bash

RSA="\033[1;31m"
YSA="\033[1;93m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
sleep 1
echo -e "$RSA"run it as"$CE" "$YSA"root"$CE"
sleep 1
echo -e "$RSA"or use"$CE" "$YSA"sudo"$CE"
sleep 1
exit
fi

if [[ -d ~/mouse ]]
then
cd  ~/mouse
{
cp bin/mouse /usr/local/bin
chmod +x /usr/local/bin/mouse
cp bin/mouse /bin
chmod +x /bin/mouse
} &> /dev/null
else
cd ~
{
git clone https://github.com/entynetproject/mouse.git
cd  ~/mouse
cp bin/mouse /usr/local/bin
chmod +x /usr/local/bin/mouse
cp bin/mouse /bin
chmod +x /bin/mouse
} &> /dev/null
fi

if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
uicache -r
fi
