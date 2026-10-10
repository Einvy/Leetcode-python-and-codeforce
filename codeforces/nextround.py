n, k = map(int,input().split())
a = list(map(int, input().split()))
count = 0
# for things in k:
    # a = int(input())
for vals in a:
    if vals >= a[k-1] and vals > 0:
        count += 1
print(count)
