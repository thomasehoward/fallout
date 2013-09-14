#!/bin/bash

ATTEMPTS=0
#PASSWORD=

function terminalOutput {
for i in {1..12}
do
echo " 0xF$(LC_CTYPE=C tr -dc A-F0-9 < /dev/urandom | head -c 3) $(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c 12) 0xF$(LC_CTYPE=C tr -dc A-F0-9 < /dev/urandom | head -c 3) $(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c 12) "
done
}

clear
#for i in 1 2 3 4 5 6; do setterm -background black -foreground green -store > /dev/tty$i; done
echo "ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM"
sleep 1s
echo "COPYRIGHT 2075-2077 ROBCO INDUSTRIES"
sleep 1s
echo "ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL"
sleep 3s
clear
echo "WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK"
echo ""
sleep 1s
echo ">SET TERMINAL/INQUIRE" | pv -qL 10
sleep 1s
echo ""
echo "RIT-V300"
echo ""
sleep 1s
echo ">SET FILE/PROTECTION=OWNER:RWED ACCOUNTS.F" | pv -qL 10
echo ">SET HALT RESTART/MAINT" | pv -qL 10
echo ""
sleep 2s
echo "Initialising Robco Industries(TM) MF Boot Agent v2.3.0"
sleep 1s
echo "RETROS BIOS"
sleep 1s
echo "RBIOS-4.02.08.00 52EE5.E7.E8"
sleep 1s
echo "Copyright 2201-2203 Robco Ind."
sleep 1s
echo "Uppermem: 64 KB"
sleep 1s
echo "Root (5A8)"
sleep 1s
echo "Maintenance Mode"
sleep 1s
echo ""
echo ">RUN DEBUG/ACCOUNTS.F" | pv -qL 10
sleep 3s
clear
echo "ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL"
sleep 1s
echo "ENTER PASSWORD NOW"
sleep 2s
echo ""
echo "4 ATTEMPT(S) LEFT: * * * *"
echo ""
terminalOutput
echo ""
read -p " > " passwd

