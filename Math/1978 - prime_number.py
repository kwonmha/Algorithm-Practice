#-*- coding: utf-8 -*-

import math


def is_prime(num):
  if num == 1:
    return False

  root = int(math.sqrt(num))

  for div in range(2, root + 1):
    if num % div == 0:
      return False

  return True


input()
nums = list(map(int, input().split()))

count = 0
for num in nums:
  if is_prime(num):
    count += 1
print(count)
