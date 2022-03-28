import sys
sys.stdin = open('input.txt', 'r')
N, K = map(int, sys.stdin.readline().split())
K -= 5
words = []
for _ in range(N):
    word = set(sys.stdin.readline().rstrip())-set('antic')
    temp = 0
    for c in word:
        temp |= 1 << (ord(c) - ord('a'))

    words.append(temp)

def check(bit):
    cnt = 0
    sz = 0
    for i in range(N):
        if bit & (1 << i):
            sz += 
    return cnt

ans = 0
if K < 0 :
    print(ans)
else:
    for bit in range(1 << N):
        ans = max(ans, check(bit))
    print(ans)