#-*- coding: utf-8 -*-

def calc_gcd(a, b):
  big = max(a, b)
  small = min(a, b)

  while small != 0:
    remainder = big % small
    big = small
    small = remainder

  return big


num_test = int(input())

for i in range(num_test):
  numbers = list(map(int, input().split()))[1:]

  gcd_sum = 0
  for i1 in range(len(numbers) - 1):
    for i2 in range(i1 + 1, len(numbers)):
      gcd = calc_gcd(numbers[i1], numbers[i2])
      gcd_sum += gcd

  print(gcd_sum)
