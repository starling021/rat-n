PORT="$( cd && cat .lport )"
IP="$( cd && cat .lhost )"
TIP="$( cd && cat .rhost )"

	BS="\033[1;34m"
	CE="\033[0m"
	O="\033[0;33m"

echo -e "           *** Connected to ["$BS""$TIP""$CE"] ***              " 
echo -e "               *** From ["$O""$IP""$CE"] ***                  "
echo -e "                  *** On port ["$O""$PORT""$CE"] ***                     "
cd 
cd mouse
trap '2'
