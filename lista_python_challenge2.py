# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:13:38 2020

@author: lucas
"""
import re
import urllib.request
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

comments = re.findall("<!--(.*?)-->", html, re.DOTALL)

data = comments[-1]

count = {}
for a in data:
    count[a] = count.get(a, 0) + 1
count

print (count)