#!/usr/bin/python3

try:
    from scribus import *
except ImportErr:
    pass

"""Resize a textframe with 'main' attribute with value 'True' to page margins"""
for p in range(1, pageCount() + 1):
    gotoPage(p)
    typ = getPageType(p)
    W, H = getPageSize()
    mm = getPageMargins()
    ii=getPageItems()
    if len(ii) == 0:
        continue
    for i in ii:
        # just text frame  4
        if i[1]!=4:
            continue
        aa = getObjectAttributes(i[0])
        if len(aa) == 0:
            continue
        found = None
        for a in aa:
            if a["Name"] == "main" and a["Value"] == "True":
                found = i
        if found == None:
            continue
        #resize
        w = W - (mm[2]+mm[1])
        h = H - (mm[3]+mm[0])
        sizeObject(w, h, found[0])
        #position on margins
        if typ == 2:
            moveObjectAbs(mm[1], mm[0], found[0])
        elif typ == 0:
            moveObjectAbs(mm[2], mm[0], found[0])
        
