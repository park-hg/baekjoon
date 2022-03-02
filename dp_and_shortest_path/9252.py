import sys
sys.stdin = open('input.txt', 'r')

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

dp = [[0]*len(B) for _ in range(len(A))]

for i in range(len(A)):
    if A[i] == B[0]:
        break
for ii in range(i, len(A)):
    dp[ii][0] = 1

for i in range(len(B)):
    if A[0] == B[i]:
        break
for ii in range(i, len(B)):
    dp[0][ii] = 1

print(dp)
for i in range(len(A)-1):
    for j in range(len(B)-1):
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j]+(A[i+1] == B[j+1]))

lcs = []
row, col = len(A)-1, len(B)-1
length = dp[row][col]
while row >= 0 and col >= 0:
    if A[row] == B[col]:
        lcs.append(A[row])
        length -= 1
        row -= 1
        col -= 1
    elif length == dp[row][col-1]:
        col -= 1
    else:
        row -= 1

print(len(lcs))
if len(lcs) > 0:
    print(''.join(lcs[::-1]))
