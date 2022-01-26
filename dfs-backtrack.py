graph = {
    1:[2, 3, 4],
    2:[5],
    3:[5],
    4:[],
    5:[6, 7],
    6:[],
    7:[3]
}
max_len = 0
ans = []
def dfs_backtrack(v, visited=[]):
    global ans, max_len
    visited.append(v)
    if len(visited) > max_len:
        ans = visited[:]
        max_len = len(visited)
    for w in graph[v]:
        if w not in visited:
            dfs_backtrack(w, visited)
            visited.remove(w)
    return visited

dfs_backtrack(1)
print(ans)
