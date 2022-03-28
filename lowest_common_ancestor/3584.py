import sys
sys.stdin = open('input.txt', 'r')

def anc(u, parent):
    parents = [u]
    while u != 0:
        parents.append(parent[u])
        u = parent[u]
    return parents[::-1]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    graph = [[i] for i in range(N+1)]
    parent = [0]*(N+1)
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        parent[b] = a
    u, v = map(int, sys.stdin.readline().split())
    
    u_par, v_par = anc(u, parent), anc(v, parent)
    print(parent)
    print(u_par, v_par)
    i = 0
    while i < min(len(u_par), len(v_par)) and u_par[i] == v_par[i]:
        i += 1

    print(u_par[i-1])

