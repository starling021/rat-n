if [[ -d /data/data/com.termux ]]
then
if [[ -f /data/data/com.termux/files/usr/bin/mouse ]]
then
UPD="true"
else
UPD="false"
fi
else
if [[ -f /usr/local/bin/mouse ]]
then
UPD="true"
else
UPD="false"
fi
fi
{
ASESR="$( curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//' )"
} &> /dev/null
if [[ "$ASESR" = "" ]]
then 
sleep 1
echo -e ""$RS"[-] "$WHS"Download failed!"$CE""
sleep 1
exit
fi
if [[ $EUID -ne 0 ]]
then
sleep 1
echo -e ""$RS"[-] "$WHS"Permission denied!"$CE""
sleep 1
exit
fi
sleep 1
echo -e ""$BS"[*] "$WHS"Installing update..."$CE""
{
mkdir ~/.mouse
cp -r ~/mouse/downloads ~/.mouse
cp -r ~/mouse/payloads ~/.mouse
rm -rf ~/mouse
rm /bin/mouse
rm /usr/local/bin/mouse
rm /data/data/com.termux/files/usr/bin/mouse
cd ~
git clone https://github.com/entynetproject/mouse.git
if [[ "$UPD" != "true" ]]
then
sleep 0
else
cd ~/mouse
chmod +x install.sh
./install.sh
fi
cp -r ~/.mouse/downloads ~/mouse
cp -r ~/.mouse/payloads ~/mouse
rm -rf ~/.mouse
} &> /dev/null
echo ""$GNS"[+] "$WHS"Successfully updated!"$CE""
sleep 1
exit
