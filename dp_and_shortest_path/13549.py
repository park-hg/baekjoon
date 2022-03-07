import sys
import heapq
sys.stdin = open('input.txt', 'r')
N, K = map(int, sys.stdin.readline().split())

visited = [0]*100001
visited[N] = True
heap = [(0, N)]
while heap:
    dist, x = heapq.heappop(heap)
    if x == K:
        print(dist)
        break
    if 0 <= 2*x < 100001 and not visited[2*x]:
        heapq.heappush(heap, (dist, 2*x))
        visited[2*x] = True
    if 0 <= x-1 < 100001 and not visited[x-1]:
        heapq.heappush(heap, (dist+1, x-1))
        visited[x-1] = True
    if 0 <= x+1 < 100001 and not visited[x+1]:
        heapq.heappush(heap, (dist+1, x+1))
        visited[x+1] = True
