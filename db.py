#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import os


def BuildDatabase():
    RED="\033[31m"
    GREEN="\033[32m"
    YELLOW="\033[33m"
    NC='\033[0m'
    print YELLOW + "Building database..." + NC
    try:
        os.remove("db.db")
    except Exception as e:
        pass

    connector = sqlite3.connect('db.db')
    cursor = connector.cursor()
    cursor.execute('''CREATE TABLE Categories
                 (CategoryID integer primary key, CategoryName text, CategoryLevel integer, BestOfferEnabled integer,
                  CategoryParentID integer)''')

    connector.commit()
    connector.close()
    print GREEN + "Successfull..." + NC
