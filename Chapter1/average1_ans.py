#!/usr/bin/env python3

numbers = []
total = 0
count = 0

while True:
    number = input("enter a number or Enter to finish: ")
    if number:
        try:
            num = int(number)
        except ValueError as err:
            continue
        numbers.append(num)
        total += num
        count += 1
    else:
        break

#print(numbers)
print(f"count= {count}, sum = {total}, lowest = {min(numbers)}, highest = {max(numbers)}, mean = {total/count}")
