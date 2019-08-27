#-*- coding: utf-8 -*-


def check_chaining_from(start, rel, cnt_remaining, n_ppl, included):
  # print(start)
  # print(rel)
  if cnt_remaining == 0:
    # print(included)
    return True

  ret = False
  for j in rel[start]:
    if j not in included:
        included.append(j)
        ret |= check_chaining_from(j, rel, cnt_remaining - 1, n_ppl, included)
        if ret:
          return ret
        included.pop()
  return ret


def check_chaining_friends(rel, cnt_remaining, n_ppl):
  included = []
  for i in range(n_ppl):
    included.append(i)
    if check_chaining_from(i, rel, cnt_remaining, n_ppl, included):
      return 1
    included.pop()
  return 0


N, M = (map(int, input().split()))

rel = [[] for i in range(N)]


for i in range(M):
  a, b = (map(int, input().split()))
  rel[a].append(b)
  rel[b].append(a)

print(check_chaining_friends(rel, 4, N))
