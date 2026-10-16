t = int(input())
for _ in range(t):
    a,b,c = map(int, input())
    ab = (a + b) / 2
    if ab > c:
        print("YES")
    else:
        print("NO")
