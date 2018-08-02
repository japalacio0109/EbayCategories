#!/usr/bin/python
# -*- coding: utf-8 -*-

import db
import xmlbuilder

def main():
    db.BuildDatabase()
    xmlbuilder.SetCategories()

try:
    main()
except Exception as e:
    RED="\033[31m"
    GREEN="\033[32m"
    YELLOW="\033[33m"
    NC='\033[0m'
    print (RED + "Oops! can't proccess the request... " + str(e) + NC)
