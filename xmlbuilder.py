#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import requests
import xml.etree.ElementTree as ET

def SetCategories():
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    NC = '\033[0m'

    print YELLOW + "Extracting data from eBay..." + NC
    XMLHeaders = {
        'X-EBAY-API-CALL-NAME': 'GetCategories',
        'X-EBAY-API-APP-NAME': 'EchoBay62-5538-466c-b43b-662768d6841',
        'X-EBAY-API-CERT-NAME': '00dd08ab-2082-4e3c-9518-5f4298f296db',
        'X-EBAY-API-DEV-NAME': '16a26b1b-26cf-442d-906d-597b60c41c19',
        'X-EBAY-API-SITEID': "0",
        'X-EBAY-API-COMPATIBILITY-LEVEL': "861"
    }
    XMLData = '''<?xml version="1.0" encoding="utf-8"?>
                <GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
                  <CategorySiteID>0</CategorySiteID>
                  <ViewAllNodes>True</ViewAllNodes>
                  <DetailLevel>ReturnAll</DetailLevel>
                  <RequesterCredentials>
                    <eBayAuthToken>AgAAAA**AQAAAA**aAAAAA**PlLuWA**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GlDpaDpAudj6x9nY+seQ**LyoEAA**AAMAAA**wSd/jBCbxJHbYuIfP4ESyC0mHG2Tn4O3v6rO2zmnoVSF614aVDFfLSCkJ5b9wg9nD7rkDzQayiqvwdWeoJkqEpNQx6wjbVQ1pjiIaWdrYRq+dXxxGHlyVd+LqL1oPp/T9PxgaVAuxFXlVMh6wSyoAMRySI6QUzalepa82jSQ/qDaurz40/EIhu6+sizj0mCgjcdamKhp1Jk3Hqmv8FXFnXouQ9Vr0Qt+D1POIFbfEg9ykH1/I2CYkZBMIG+k6Pf00/UujbQdne6HUAu6CSj9wGsqQSAEPIXXvEnVmtU+6U991ZUhPuA/DMFEfVlibvNLBA7Shslp2oTy2T0wlpJN+f/Jle3gurHLIPc6EkEmckEpmSpFEyuBKz+ix4Cf4wYbcUk/Gr3kGdSi20XQGu/ZnJ7Clz4vVak9iJjN99j8lwA2zKW+CBRuHBjZdaUiDctSaADHwfz/x+09bIU9icgpzuOuKooMM5STbt+yJlJZdE3SRZHwilC4dToTQeVhAXA4tFZcDrZFzBmJsoRsJYrCdkJBPeGBub+fqomQYyKt1J0LAQ5Y0FQxLHBIp0cRZTPAuL/MNxQ/UXcxQTXjoCSdZd7B55f0UapU3EsqetEFvIMPxCPJ63YahVprODDva9Kz/Htm3piKyWzuCXfeu3siJvHuOVyx7Q4wyHrIyiJDNz5b9ABAKKauxDP32uqD7jqDzsVLH11/imKLLdl0U5PN+FP30XAQGBAFkHf+pAvOFLrdDTSjT3oQhFRzRPzLWkFg</eBayAuthToken>
                  </RequesterCredentials>
                </GetCategoriesRequest>'''

    r =requests.post('https://api.sandbox.ebay.com/ws/api.dll', headers=XMLHeaders, data=XMLData)


    root = ET.fromstring(r.text.encode('utf-8'))
    categories = root.find('{urn:ebay:apis:eBLBaseComponents}CategoryArray')
    connector = sqlite3.connect('db.db')
    cursor = connector.cursor()
    categoryArray = []
    print GREEN + "Completed..." + NC
    print YELLOW + "Filling database..." + NC
    for child in categories:
        id = int(child.find('{urn:ebay:apis:eBLBaseComponents}CategoryID').text)
        categoryName = child.find('{urn:ebay:apis:eBLBaseComponents}CategoryName').text
        categoryLevel = int(child.find('{urn:ebay:apis:eBLBaseComponents}CategoryLevel').text)

        bestOfferEnabled = 0
        try:
            if child.find('{urn:ebay:apis:eBLBaseComponents}BestOfferEnabled').text == 'true':
                bestOfferEnabled = 1
        except Exception as e:
            pass

        categoryParentID = int(child.find('{urn:ebay:apis:eBLBaseComponents}CategoryParentID').text)
        if categoryParentID == id:
            categoryParentID = -1

        # print categoryName, categoryParentID


        category = (id, categoryName, categoryLevel, bestOfferEnabled, categoryParentID)
        categoryArray.append(category)

    cursor.executemany('INSERT INTO Categories(CategoryID, CategoryName, CategoryLevel, BestOfferEnabled, CategoryParentID) VALUES (?,?,?,?,?)', categoryArray)

    connector.commit()
    connector.close()
    print GREEN + "Filling completed..." + NC
