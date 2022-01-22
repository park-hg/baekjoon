import sys
sys.stdin = open('input.txt', 'r')

for test in range(1, 11):
    _ = sys.stdin.readline()
    l = [int(num) for num in sys.stdin.readline().split()]

    ans = 0
    for i in range(2, len(l)-2):
        n = min(l[i]-l[i-2], l[i]-l[i-1], l[i]-l[i+1], l[i]-l[i+2])
        n = max(n, 0)
        ans += n

    print('#'+str(test), ans)