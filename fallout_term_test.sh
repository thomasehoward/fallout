#!/bin/bash

# variables config section
ATTEMPTS=0
#PASSWORD=
DIFFICULTY=$1
MAXCOUNT=12
COUNT=1

function passwordGen {

WORDFILE="/usr/share/dict/words"

case $DIFFICULTY in
  veryeasy)
    WORDLEN=5
    ;;
  easy)
    WORDLEN=6
    ;;
  moderate)
    WORDLEN=7
    ;;
  hard)
    WORDLEN=8
    ;;
  veryhard)
    WORDLEN=9
    ;;
  *)
    echo "Please specify a difficulty: veryeasy | easy | moderate | hard | veryhard"
    exit 1
esac

# number of lines in WORDFILE
wL=`awk 'NF!=0 {++c} END {print c}' $WORDFILE`

# declares empty array PASSWDLIST
declare -a PASSWDLIST

while [ "$COUNT" -le $MAXCOUNT ]
do
rnum=$(jot -r 1 1 $wL)
WORDLIST=$(sed -n "$rnum p" $WORDFILE | tr '[:lower:]' '[:upper:]')
  for WORD in $WORDLIST
  do
    if [ ${#WORD} = $WORDLEN ]; then
      declare -a PASSWD=("${PASSWDLIST[@]}" "${WORD}")
#      for i in "${!PASSWD[@]}"
#      do
        echo " 0xF$(LC_CTYPE=C tr -dc A-F0-9 < /dev/urandom | head -c 3) $(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c 3)${PASSWD[@]}$(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c 3) 0xF$(LC_CTYPE=C tr -dc A-F0-9 < /dev/urandom | head -c 3) $(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c 12)"
#      done
      let "COUNT += 1"
    else
      :
    fi
  done
done
}

#function terminalOutput {
#for i in {1..17}
#do
#echo " 0xF$(LC_CTYPE=C tr -dc A-F0-9 < /dev/urandom | head -c 3) $(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c 12) 0xF$(LC_CTYPE=C tr -dc A-F0-9 < /dev/urandom | head -c 3) $(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c 12) "
#done
#}

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
sleep 1s
echo ""
echo "4 ATTEMPT(S) LEFT: * * * *" 
echo ""
passwordGen
#terminalOutput
echo ""
read -p " > " derp

