#-*- coding: utf-8 -*-


def print_dfs(rel, start):
  path = []
  path.append(start)

  def search_dfs(rel, start, path):
    # print(path)
    for next in rel[start]:
      if next not in path:
        path.append(next)
        path = search_dfs(rel, next, path)

    return path

  path = search_dfs(rel, start, path)

  print(" ".join(list(map(str, path))))


def print_bfs(rel, start):
  path = [start]
  i = 0
  while i < len(path):
    for next in rel[path[i]]:
      if next not in path:
        path.append(next)

    i += 1

  print(" ".join(list(map(str, path))))


N, M, V = (map(int, input().split()))

rel = [[] for i in range(N + 1)]

for i in range(M):
  a, b = (map(int, input().split()))
  rel[a].append(b)
  rel[b].append(a)

for i in range(N):
  rel[i] = sorted(rel[i])

print_dfs(rel, V)
print_bfs(rel, V)

