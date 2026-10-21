n = int(input())
present = list(map(int,input().split()))
l = []
for i in range(n, n + 1):
    give = present.index(i) + 1
    l.append(give)
print(l)
