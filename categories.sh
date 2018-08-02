#!/bin/sh
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
NC='\033[0m'

if [ $# -eq 0 ]
  then
    echo "${RED}Unrecognized action"
    echo "--rebuild to create database and fill data"
    echo "or --render [CategoryId] to render data in a .html file${NC}"
else
	if [ $1 = "--rebuild" ];
	 then exec python mainDB.py
	elif [ $1 = "--render" ];
		then exec python mainHtml.py $2
  else
    echo "${RED}Unrecognized action"
    echo "--rebuild to create database and fill data"
    echo "or --render [CategoryId] to render data in a .html file${NC}"
	fi
fi
