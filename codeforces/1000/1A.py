n,m,a = map(int,input().split())
# flagstone is a * a
# shape = n * m
# // this removes the fraction so 6 / 4 would normally be 1.5 but with // it becomes just 1
newm = m // a
newn = n // a
if m % a != 0:
    newm += 1
if n % a != 0:
    newn += 1
print(newm * newn)
