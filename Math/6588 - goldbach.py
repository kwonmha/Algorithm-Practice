#-*- coding: utf-8 -*-

import math


def prime_numbers_smaller_than(num):
  numbers = list(range(num))
  numbers[1] = 0
  root = int(math.sqrt(num))

  for div in range(2, root + 1):
    if numbers[div] == 0:
      continue
    for idx in range(div * 2, num, div):
      numbers[idx] = 0

  return numbers


prime_numbers_check = prime_numbers_smaller_than(1000000)

while True:
  num = int(input())
  if num == 0:
    break
  i = 0

  while i <= num / 2:
    if prime_numbers_check[i] != 0 and prime_numbers_check[num - i] != 0:
      print("{} = {} + {}".format(num, i, num - i))
      break
    i += 1
  else:
    print("Goldbach's conjecture is wrong.")

