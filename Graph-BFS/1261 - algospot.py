#-*- coding: utf-8 -*-
import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def min_wall_to_remove(X, Y, map):
  visited = [[987654321] * (X+1) for _ in range(Y+1)]
  h = []
  heapq.heappush(h, (0, (1, 1)))
  visited[1][1] = 0

  while len(h) > 0:
    wall, coord = heapq.heappop(h)
    x, y = coord

    if x == X and y == Y:
      return wall

    for i in range(4):
      newx = x + dx[i]
      newy = y + dy[i]

      if not (0 < newx <= X) or not (0 < newy <= Y):
        # print("drop", newy, newx)
        continue

      if map[newy][newx] == 1:
        newwall = wall + 1
      else:
        newwall = wall

      if visited[newy][newx] <= newwall:
        # print("long", newy, newx, visited[newy][newx])
        continue

      visited[newy][newx] = newwall
      heapq.heappush(h, (newwall, (newx, newy)))

    # print(h)


M, N = (map(int, input().split()))

map = [[-1] * (M+1) for _ in range(N+1)]

for n in range(1, N+1):
  line = input()
  for m in range(1, M+1):
    map[n][m] = int(line[m-1])

print(min_wall_to_remove(M, N, map))
