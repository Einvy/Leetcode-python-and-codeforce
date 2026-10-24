n = int(input())
p = list(map(int,input().split()))
x = list(map(int,input().split()))
test = set() # Set makes it to where it is only unique values
test.update(p[1:]) # Do not need first value as it just tells how many items there are
test.update(x[1:]) # again do not need first value
count = 0
for vals in range(1, n + 1): 
    if vals in test:
        count += 1
if n == count:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
