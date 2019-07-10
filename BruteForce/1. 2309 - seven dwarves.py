#-*- coding: utf-8 -*-

heights = [0] * 9

for i in range(9):
  heights[i] = int(input())

heights.sort()
heights_sum = sum(heights)

for d1 in range(9):
  for d2 in range(d1 + 1, 9):
    r1 = heights[d1]
    r2 = heights[d2]
    if heights_sum - (r1 + r2) == 100:
      heights.remove(r1)
      heights.remove(r2)

      for i in range(7):
        print(heights[i])
      exit()