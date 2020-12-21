#!/usr/bin/python3

try:
    from scribus import *
except ImportErr:
    pass

"""Resize a textframe with 'main' attribute with value 'True' to page margins"""
attr = [{"Name": "main", "Type":"boolean", "Value":"True", "Parameter":"", "Relationship": "None", "RelationshipTo":"", "AutoAddTo":""}]
for p in range(1, pageCount() + 1):
    gotoPage(p)
    ii=getPageItems()
    if len(ii) == 0:
        continue
    for i in ii:
        # just text frame  4
        if i[1]!=4:
            continue
        setObjectAttributes(attr, i[0])
