# -*_ coding:utf-8 -*-
import re

print re.search(r"\d+", "my age is 23 and my height is 175cm", re.I).group()

for item in re.findall(r"\d+", "my baby is 4 years old and my dad is 47 "):
    print item

str1 = "my baby is 4 years old and my dad is 47 "

print re.sub(r"\d+", "secret", str1)

for item in re.split(r" ", str1):
    print item
