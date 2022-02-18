from dis import dis
import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())

path_len = 10**6
path = []
def dfs(i, discovered = [N]):
    global path_len, path
    if i == 1:
        if len(discovered) < path_len:
            path_len = len(discovered)
            path = discovered[:]
            return
    if len(discovered) > path_len:
        return
    if i < 1:
        return
    if i%3 == 0:
        dfs(i//3, discovered+[i//3])
    if i%2 == 0:
        dfs(i//2, discovered+[i//2])

    dfs(i-1, discovered+[i-1])

dfs(N)

print(path_len-1)
print(*path)