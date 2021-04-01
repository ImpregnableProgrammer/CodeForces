# Following problem: https://codeforces.com/contest/294/problem/A
n = int(input())
wires = [*map(int, input().split(" "))]
m = int(input())
for i in range(m):
    x, y = map(int, input().split(" "))
    if x > 1:
        wires[x-2] += y - 1
    if x < n:
        wires[x] += wires[x-1] - y
    wires[x-1] = 0
    
for n in wires:
    print(n)
    
