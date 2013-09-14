#!/bin/bash

WORDFILE="/usr/share/dict/words"
WORDLEN=$1
#NUMWORDS=$2
MAXCOUNT=$2
COUNT=1

# number of lines in $WORDFILE

tL=`awk 'NF!=0 {++c} END {print c}' $WORDFILE`

#for i in `seq $NUMWORDS`

while [ "$COUNT" -le $MAXCOUNT ]

do
rnum=$(jot -r 1 1 $tL)
WORDLIST=$(sed -n "$rnum p" $WORDFILE)

# create specific wordlist files by difficulty

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
