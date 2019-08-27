#-*- coding: utf-8 -*-
import queue

MAX_POS = 100000


def min_time(N, K):
	q = queue.Queue(MAX_POS)
	visited = [987654321] * (MAX_POS + 1)

	# q.put(N)
	# visited[N] = 0
	#
	# while not q.empty():
	# 	cur_pos = q.get()
	# 	print(cur_pos)
	#
	# 	if cur_pos == K:
	# 		return visited[cur_pos]
	#
	# 	if cur_pos + 1 < MAX_POS and visited[cur_pos + 1] > (visited[cur_pos] + 1):
	# 		visited[cur_pos + 1] = visited[cur_pos] + 1
	# 		q.put(cur_pos + 1)
	#
	# 	if cur_pos - 1 >= 0 and visited[cur_pos - 1] > (visited[cur_pos] + 1):
	# 		visited[cur_pos - 1] = visited[cur_pos] + 1
	# 		q.put(cur_pos - 1)
	#
	# 	if cur_pos * 2 <= MAX_POS and visited[cur_pos * 2] > visited[cur_pos]:
	# 		visited[cur_pos * 2] = visited[cur_pos]
	# 		q.put(cur_pos * 2)

	q.put((N, 0))

	while not q.empty():
		cur_pos, cur_time = q.get()

		if cur_pos == K:
			return cur_time

		if cur_pos < 0 or cur_pos > 100000:
			continue

		if cur_time >= visited[cur_pos]:
			continue

		visited[cur_pos] = cur_time

		q.put((cur_pos * 2, cur_time))
		q.put((cur_pos - 1, cur_time + 1))
		q.put((cur_pos + 1, cur_time + 1))


N, K = (map(int, input().split()))

print(min_time(N, K))
