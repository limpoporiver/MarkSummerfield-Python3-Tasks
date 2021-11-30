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

sorted_numbers = []
while numbers:
  minimum = numbers[0]
  for x in numbers:
    if x < minimum:
      minimum = x
  sorted_numbers.append(minimum)
  numbers.remove(minimum)

# print(sorted_numbers)

if sorted_numbers:
  if len(sorted_numbers)%2 == 0:
    med_index1 = int(len(sorted_numbers)/2)
    median = (sorted_numbers[med_index1 - 1] + sorted_numbers[med_index1]) / 2
  else:
    med_index = int((len(sorted_numbers) + 1) / 2 - 1) 
    median = sorted_numbers[med_index]
  
  lowest = min(sorted_numbers)
  highest = max(sorted_numbers)
  mean = total/count
  
  print(f"count= {count}, sum = {total}, lowest = {lowest}, highest = {highest}, mean = {mean}, median = {median}")
