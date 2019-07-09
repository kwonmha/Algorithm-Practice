#-*- coding: utf-8 -*-

num_test = int(input())

for i in range(num_test):
  a, b = map(int, input().split())

  big = max(a, b)
  small = min(a, b)

  while small != 0:
    remainder = big % small
    big = small
    small = remainder
  print(a // big * b)

