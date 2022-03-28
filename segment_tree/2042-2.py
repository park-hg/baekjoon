import sys
import math
sys.stdin = open('input.txt', 'r')
N, M, K = map(int, sys.stdin.readline().split())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
h = math.ceil(math.log2(N))
tree = [-1]*(2**(h+1))

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

init(1, 0, N-1)

def sum(node, start, end, left, right):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return sum(node*2, start, mid, left, right) + sum(node*2+1, mid+1, end, left, right)

def update(node, start, end, index, val):
    if index < start or index > end:
        return tree[node]
    if start == end:
        tree[node] = val
        return tree[node]
    mid = (start+end)//2
    tree[node] = update(node*2, start, mid, index, val) + update(node*2+1, mid+1, end, index, val)
    return tree[node]

for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    elif a == 2:
        print(sum(1, 0, N-1, b-1, c-1))