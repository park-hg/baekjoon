import sys
from collections import Counter
sys.stdin = open('input.txt', 'r')
r, c, k = map(int, sys.stdin.readline().split())
r, c = r-1, c-1
A = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

def r_op(array):
    new_array = []
    max_len = 0
    for row in array:
        row = [x for x in row if x != 0]
        new_row = []
        for num, cnt in sorted(Counter(row).most_common(), key=lambda x: (x[1], x[0])):
            new_row.append(num)
            if len(new_row) > 100:
                break
            new_row.append(cnt)
            if len(new_row) > 100:
                break
        max_len = max(max_len, len(new_row))
        new_array.append(new_row)

    for row in new_array:
        row += [0]*(max_len - len(row))
    
    return new_array

def c_op(array):
    array_t = [[0]*len(array) for _ in range(len(array[0]))]
    for i in range(len(array)):
        for j in range(len(array[0])):
            array_t[j][i] = array[i][j]

    new_array_t = r_op(array_t)
    new_array = [[0]*len(new_array_t) for _ in range(len(new_array_t[0]))]
    for i in range(len(new_array_t)):
        for j in range(len(new_array_t[0])):
            new_array[j][i] = new_array_t[i][j]

    return new_array

ans = -1
for i in range(101):
    if 0 <= r < len(A) and 0 <= c < len(A[0]) and A[r][c] == k:
        ans = i
        break
    if len(A) >= len(A[0]):
        A = r_op(A)
    else:
        A = c_op(A)
print(ans)
