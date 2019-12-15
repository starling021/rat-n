#blue start 
	BS="\033[1;34m"
#color end
	CE="\033[0m"
#red start
	RS="\033[1;31m"
#green start
	GNS="-e \033[1;32m"
#white start
  WHS="\033[0;97m"

if [[ "$2" = "downloads" ]]
then
{
cd ~/mouse
rm -rf downloads
mkdir downloads
} &> /dev/null
sleep 1
echo -e ""$BS"[*]"$WHS" Cleaning up..."$CE""
sleep 10
exit

elif [[ "$2" = "payloads" ]]
then
{
cd ~/mouse
rm -rf payloads
mkdir payloads
} &> /dev/null
sleep 1
echo -e ""$BS"[*]"$WHS" Cleaning up..."$CE""
sleep 10
exit
fi
