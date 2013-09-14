### Notes
# The actual output on the terminal display screen takes the following form:
# 0xF+(3 random digits from ABCDEF1-0)\s+(12 random characters from !#$%^*()_-\|:;"',.<>?/{}[] characters)
#
# random garbage command: LC_CTYPE=C tr -dc !#$%^*\(\)_-:;\"\',.<>?/{}[] < /dev/urandom | head -c 12
#
###

#!/bin/bash

clear

for i in {1..20}
do
echo " 0xF$(LC_CTYPE=C tr -dc A-F0-9 < /dev/urandom | head -c 3) $(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c 12) 0xF$(LC_CTYPE=C tr -dc A-F0-9 < /dev/urandom | head -c 3) $(LC_CTYPE=C tr -dc \!#\$%^*\(\)_-:\;\"\',.\<\>?/{}[] < /dev/urandom | head -c 12) "
done

