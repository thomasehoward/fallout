#!/bin/bash

# remainder fun! time to figure out how to print something inside garbage chars

WORD=DERPP

REM=$(expr $(expr 12 - ${#WORD}) / 2 )

echo " 0xF$(LC_CTYPE=C tr -dc A-F0-9 < /dev/urandom | head -c 3) $(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c ${REM})${WORD}$(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c ${REM})"
