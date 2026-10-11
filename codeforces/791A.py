a,b = map(int,input().split())
count = 0 

while a <= b:
    a *= 3
    b *= 2
    count += 1

if a == 1 and b == 1:
    count = 1
print(count)






