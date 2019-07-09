#-*- coding: utf-8 -*-

a, b = map(int, input().split())

big = max(a, b)
small = min(a, b)

while small != 0:
  remainder = big % small
  big = small
  small = remainder
print(big)
print(a // big * b)





