# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:52:11 2020

@author: lucas
"""

import string
test_list = []

print ( test_list)

test_list = list(string.ascii_lowercase) 

print ( test_list)

trad = []
for i in range (2,26):
    trad.append(test_list[i])

print(trad)
for i in range (0,2):
    trad.append(test_list[i])

print(trad)

def traducao (a):
    new = "Mensagem é:" 
    for i in a:
        if i == " ":
            new += " "
        elif i == ",":
            new +=","
        elif i == ".":
            new += "."
        elif i == "(":
            new +="("
        elif i == "'":
            new +="'"
        elif i == ")":
            new +=")"
        else:
            var = test_list.index(i)
    
            new += trad[var]
    return  print( new)

mensagem = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
traducao(mensagem)
"""
intab = "abcdefghijklmnopqrstuvwxyz"
outtab="cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(intab, outtab)

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
str = "http://www.pythonchallenge.com/pc/def/map.html"
print (str.translate(trantab))
"""
