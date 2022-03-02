import sys
import bisect
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
arr = [0]

for i in range(N):
    if A[i] > arr[-1]:
        arr.append(A[i])
    else:
        left = bisect.bisect_left(arr, A[i])
        arr[left] = A[i]

print(len(arr)-1)