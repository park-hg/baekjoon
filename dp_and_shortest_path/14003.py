import sys
import bisect
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

arr = []
ind = [0]*N

for i in range(N):
    if not arr or A[i] > arr[-1]:
        arr.append(A[i])
        ind[i] = len(arr)-1
    else:
        left = bisect.bisect_left(arr, A[i])
        arr[left] = A[i]
        ind[i] = left

index = len(arr)-1
lis = []
for i in range(N-1, -1, -1):
    if ind[i] == index:
        lis.append(A[i])
        index -= 1

print(len(arr))
print(*lis[::-1])
