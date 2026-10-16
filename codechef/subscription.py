# cook your dish here
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    c = n // 6
    if n % 6 != 0:
        c += 1
    print(c * x)
