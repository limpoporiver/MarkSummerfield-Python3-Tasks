#!/usr/bin/env python3


import sys


Zero  = [" *** ", 
         "*   *", 
         "*   *", 
         "*   *",
         "*   *",
         "*   *",
         " *** "]
One   = [" * ",
         "** ",
         " * ",
         " * ",
         " * ",
         " * ",
         "***"]
Two   = [" *** ",
         "*   *",
         "*  * ",
         "  *  ",
         " *   ",
         "*    ",
         "*****"]
Three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]
Four  = ["    * ",
         "   ** ",
         "  * * ",
         " *  * ",
         "******",
         "    * ",
         "    * "]
Five  = ["*****",
         "*    ",
         "*    ",
         " *** ",
         "    *",
         "*   *",
         " *** "]
Six   = [" *** ",
         "*   *",
         "*    ",
         "**** ",
         "*   *",
         "*   *",
         " *** "]
Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
Eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
Nine  = [" ****",
         "*   *",
         "*   *",
         " ****",
         "    *",
         "    *",
         " *** "]


Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

 
try:
#   digits = sys.argv[1] #"Usage: bigdigits.py <numbers>"
    digits = input("Введите целое число: ")
    row = 0
    print(" ")
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
#           line += digit[row].replace('*', digits[column]) + " "
            line += digit[row] + "   "
            column += 1
        print(line)
        row += 1
    print(" ")
except IndexError:
    print("Usage: bigdigits.py <numbers>")
except ValueError as err:
    print(err, "in", digits)
    print("на вход нужны только целые числа")
