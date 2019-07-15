PORT="$( cd && cat .lport )"
IP="$( cd && cat .lhost )"

echo -e "           *** Connected to ["$BS""$TIP""$CE"] ***              " 
echo -e "               *** From ["$O""$IP""$CE"] ***                  "
echo -e "                  *** On port ["$O""$PORT""$CE] ***                     "
cd 
cd mouse
trap '2'
