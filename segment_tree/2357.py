import sys
import math
sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

h = math.ceil(math.log2(N))
max_tree = [0]*(2**(h+1))
min_tree = [0]*(2**(h+1))

def max_init(node, start, end):
    if start == end:
        max_tree[node] = nums[start]
        return max_tree[node]
    mid = (start+end)//2
    max_tree[node] = max(max_init(node*2, start, mid), max_init(node*2+1, mid+1, end))
    return max_tree[node]

def min_init(node, start, end):
    if start == end:
        min_tree[node] = nums[start]
        return min_tree[node]
    mid = (start+end)//2
    min_tree[node] = min(min_init(node*2, start, mid), min_init(node*2+1, mid+1, end))
    return min_tree[node]

max_init(1, 0, N-1)
min_init(1, 0, N-1)

def get_max(node, start, end, left, right):
    if end < left or start > right:
        return -1
    if left <= start and end <= right:
        return max_tree[node]
    mid = (start+end)//2
    return max(get_max(node*2, start, mid, left, right), get_max(node*2+1, mid+1, end, left, right))

def get_min(node, start, end, left, right):
    if end < left or start > right:
        return 10**9+1
    if left <= start and end <= right:
        return min_tree[node]
    mid = (start+end)//2
    return min(get_min(node*2, start, mid, left, right), get_min(node*2+1, mid+1, end, left, right))

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(get_min(1, 0, N-1, a-1, b-1), get_max(1, 0, N-1, a-1, b-1))
