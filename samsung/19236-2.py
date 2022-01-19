import sys
sys.stdin = open('input.txt', 'r')

graph = []
for _ in range(4):
    a0, b0, a1, b1, a2, b2, a3, b3 = map(int, sys.stdin.readline().split())
    graph.append([[a0, b0-1], [a1, b1-1], [a2, b2-1], [a3, b3-1]])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
