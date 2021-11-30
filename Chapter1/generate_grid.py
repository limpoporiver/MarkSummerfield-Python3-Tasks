#!/usr/bin/env python3


import random


def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)

print("Let's generate table of test numbers")
rows = get_int("How many rows do you need?: ", 1, None)
columns = get_int("How many columns: ", 1, None)
minimum = get_int("minimal number (or Enter for 0): ", -1000000, 0)

default = 1000
if default <= minimum:
    default = 2 * minimum
# maximum = get_int("maximum (or Enter for " + str(default) + "): ", minimum, default)
maximum = get_int(f"maximum (or Enter for {default}): ", minimum, default)

row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        max_wide_num = len(str(maximum)) + 1
        while len(s) < max_wide_num:
            s = " " + s
#       дополняем строку пробелами чтобы каждое число было из 10 символов
        line += s
        column += 1
    print(line)
    row += 1
