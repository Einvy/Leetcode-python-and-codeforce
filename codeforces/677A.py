n,h = map(int,input().split())
height = list(map(int, input().split()))

w = 0

for he in height:
    if he > h:
        w += 2
    else:
        w += 1
print(w)






