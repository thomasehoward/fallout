#!/bin/bash

WORDFILE="/usr/share/dict/words"
WORDLEN=$1
NUMWORDS=$2

#Number of lines in $WORDFILE
tL=`awk 'NF!=0 {++c} END {print c}' $WORDFILE`

for i in `seq $NUMWORDS`
do

rnum=$((RANDOM%$tL+1))
WORDLIST=$(sed -n "$rnum p" $WORDFILE)

# create specific wordlist files by difficulty

for WORD in $WORDLIST
  do
  if [ ${#WORD} = $WORDLEN ]; then
    echo $WORD
  fi
  done
done


