# -*- coding:utf-8 -*-
import random

num = random.randint(0, 100)

while True:
    try:
        guess = int(raw_input("Please Enter a num 1~100:"))
    except ValueError as e:
        print "please input a num"
        continue
    if guess > num:
        print "guess Bigger", guess
    elif guess < num:
        print "guess Smaller", guess
    else:
        print "guess right ,game over"
        break

    print "\n"



