n = int(input())
amount = 0
newa = 0
newb = 0
value = 0
for _ in range(n):
    a,b = map(int,input().split())
    newa += a
    newb += b
    amount = newb - newa
    value = max(value,amount) 
print(value)

# Have to check if the capacity needs to be increased based off the amount of people that are on.
# Ex: As the ride goes on people will be going in and out of the tram so it might go beyond that capacity meaning the capacity needs to be increased.
