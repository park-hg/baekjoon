import sys
sys.stdin = open('input.txt', 'r')

line = list(sys.stdin.readline().split())
type = line[0]
for var in line[1:]:
    for i in range(len(var)):
        if var[i] in ['&', '[', '*']:
            break
    name = var[:i]
    add = var[i:-1][::-1]

    if '][' in add:
        add = add.replace('][', '[]')

    print(type+add, name+';')
