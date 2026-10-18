y = int(input())
# can use a set because sets only take unique values meaning no duplicates.

while True:
    y += 1
    val = str(y)
    if len(set(val)) == len(val): #len(set(val)) gets the unique values and makes sure it is same length as the original number.
        print(val)
        break
