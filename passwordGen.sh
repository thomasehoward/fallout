#!/bin/bash

WORDFILE="/usr/share/dict/words"
DIFFICULTY=$1
MAXCOUNT=12
COUNT=1

case $DIFFICULTY in
  veryeasy)
    WORDLEN=6
    ;;
  easy)
    WORDLEN=7
    ;;
  moderate)
    WORDLEN=8
    ;;
  hard)
    WORDLEN=9
    ;;
  veryhard)
    WORDLEN=10
    ;;
  *)
    echo "Please specify a difficulty: veryeasy | easy | moderate | hard | veryhard"
    exit 1
esac

# number of lines in WORDFILE
wL=`awk 'NF!=0 {++c} END {print c}' $WORDFILE`

# declares empty array PASSWDLIST
#declare -a PASSWDLIST=()

while [[ "$COUNT" -le $MAXCOUNT ]]
do
rnum=$(jot -r 1 1 $wL)
WORDLIST=$(sed -n "$rnum p" $WORDFILE)
  for WORD in $WORDLIST
  do
    if [ ${#WORD} = $WORDLEN ]; then
      echo $WORD | tr '[:lower:]' '[:upper:]'
      let "COUNT += 1"
    else
      :
    fi
  done
done

#echo $PASSWDLIST

