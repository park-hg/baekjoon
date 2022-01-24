import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1-x2)**2 + (y1-y2)**2

ans = 1e12
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        ans = min(ans, distance(points[i], points[j]))

print(ans)