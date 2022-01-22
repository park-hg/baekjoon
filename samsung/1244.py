import sys
sys.stdin = open('input.txt', 'r')
t = int(sys.stdin.readline())

def backtrack(c, num):
    global ans
    if c == 0:
        ans = max(ans, int(''.join(num)))
        return
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            new_num = num[:]
            new_num[i], new_num[j] = num[j], num[i]
            backtrack(c-1, new_num)
    


for i in range(t):
    num, c = sys.stdin.readline().split()
    num = list(num)
    c = int(c)
    ans = 0
    backtrack(c, num)
    print('#'+str(i+1), ans)
