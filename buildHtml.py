#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

def getCategoryById(CategoryId):
    connector = sqlite3.connect('db.db')
    cursor = connector.cursor()
    CategoriesArray = None
    cursor.execute("SELECT * FROM Categories WHERE CategoryID = " +  CategoryId)
    CategoriesArray = cursor.fetchone()
    connector.commit()
    connector.close()

    return CategoriesArray

def getChilds(CategoryId):
    connector = sqlite3.connect('db.db')
    cursor = connector.cursor()
    CategoriesArray = None
    cursor.execute("SELECT * FROM Categories WHERE CategoryParentID = " +  str(CategoryId))
    CategoriesArray = cursor.fetchall()
    connector.commit()
    connector.close()

    return CategoriesArray

def RenderList(f, categoryRow):
    # class='list-group'
    # class='list-group-item'
    ulheader = "<ul>"
    f.write(ulheader)

    categoryName = categoryRow[1]
    li = "<li><span><i class='icon-minus-sign'></i> " + categoryName.encode('utf-8') + "</span>"
    f.write(li)

    CategoryID = categoryRow[0]
    childRecords = getChilds(CategoryID)
    if len(childRecords)>0:
        for child in childRecords:
            RenderList(f,child)
    li += "</li>"
    ulfooter = "</ul>"
    f.write(ulfooter)
