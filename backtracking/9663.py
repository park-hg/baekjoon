import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())

cnt = 0
board = [0]*N
def backtrack(n):
    global cnt
    if n == N:
        cnt += 1
        return
    
    for i in range(N):
        flag = True
        for j in range(n):
            if i == board[j] or abs(i-board[j]) == abs(n-j):
                flag = False
                break
        if flag:
            board[n] = i
            backtrack(n+1)
            board[n] = 0

backtrack(0)
print(cnt)