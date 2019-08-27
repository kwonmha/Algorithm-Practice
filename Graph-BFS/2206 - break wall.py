#-*- coding: utf-8 -*-
import queue

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def min_move(X, Y, map):
  visited = [[[987654321] * (X + 1) for _ in range(Y + 1)] for __ in range(2)]
  q = queue.Queue(100000)

  q.put(((1, 1), 1, True))

  while not q.empty():
    coord, dist, can_break = q.get()
    x, y = coord

    if x == X and y == Y:
      return min(visited[0][y][x], visited[1][y][x])

    for i in range(4):
      newx = x + dx[i]
      newy = y + dy[i]

      if not (0 < newx <= X) or not (0 < newy <= Y):
        continue

      if can_break and map[newy][newx] == 1:
        if visited[1][newy][newx] <= dist + 1:
          # print("1 continue")
          continue
        new_can_break = False
        visited[1][newy][newx] = dist + 1
        q.put(((newx, newy), dist + 1, new_can_break))
      elif not can_break and map[newy][newx] == 1:
        continue
      # map == 0
      else:
        if visited[0][newy][newx] <= dist + 1:
          # print("0 continue")
          continue
        visited[0][newy][newx] = dist + 1
        new_can_break = can_break
        q.put(((newx, newy), dist + 1, new_can_break))

      # print(newy, newx, new_can_break)

  return -1

N, M = (map(int, input().split()))

map = [[-1] * (M+1) for _ in range(N+1)]

for n in range(1, N+1):
  line = input()
  for m in range(1, M+1):
    map[n][m] = int(line[m-1])

print(min_move(M, N, map))