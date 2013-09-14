#!/bin/bash

WORDFILE="/usr/share/dict/words"

WORDLEN=$1
#NUMWORDS=235886

#Number of lines in $WORDFILE
#tL=`awk 'NF!=0 {++c} END {print c}' $WORDFILE`

#for i in `seq $NUMWORDS`

#do

#rnum=$((RANDOM%$tL+1))

#rnum=$(jot -r 1 1 $tL)

#echo $rnum

WORDLIST=$(cat $WORDFILE)

#sed -n $WORDFILE

# create specific wordlist files by difficulty

for WORD in $WORDLIST
do
  if [ ${#WORD} = $WORDLEN ]; then
    echo $WORD | tr '[:lower:]' '[:upper:]'
  else
    :
  fi
done

#done


