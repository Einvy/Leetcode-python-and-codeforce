n = int(input())
a = list(map(int,input().split()))
b = a.count(1)
if b >= 1:
    print("HARD")
else:
    print("EASY")
# Can also just do if 1 in a: instead 
