#!/bin/bash - 
#===============================================================================
#
#          FILE: robco.sh
# 
#         USAGE: ./robco.sh 
# 
#   DESCRIPTION: Pointless RobCo Terminal Scroll from Fallout
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Micheal Quinn
#  ORGANIZATION: 
#       CREATED: 08/08/2012 08:35:24 AM CDT
#      REVISION: 0.3
#===============================================================================

set -o nounset                              # Treat unset variables as an error

#-------------------------------------------------------------------------------
#  Make the Files
#-------------------------------------------------------------------------------
hostname > .hn
echo "		ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM" > .robco1
echo "		  COPYRIGHT 2075-2077 ROBCO INDUSTRIES" > .robco2
echo "		      Server" > .robco3

#-------------------------------------------------------------------------------
#  Clear screen and engage scroll effect
#-------------------------------------------------------------------------------
clear
while IFS= read -r -n1 char
do
	echo  -ne "$char"
	sleep 0.05
done < .robco1
echo  ""
sleep 0.3
while IFS= read -r -n1 char
do
        echo -ne "$char"
        sleep 0.05
done < .robco2
echo  ""
sleep 0.3
while IFS= read -r -n1 char
do
        echo -ne "$char"
        sleep 0.05
done < .robco3
echo -ne " "
while IFS= read -r -n1 char
do
        echo -ne "$char"
        sleep 0.05
done < .hn
echo ""
