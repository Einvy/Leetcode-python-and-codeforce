n = int(input()) 
steps = 0

while n != 0:
    if n >= 5:
        n -= 5
        steps += 1
    elif n >= 4:
        n -= 4
        steps += 1
    elif n >= 3:
        n -= 3
        steps += 1
    elif n >= 2:
        n -= 2
        steps += 1
    else:
        steps += 1
        n -= 1
print(steps)

# EASIER way of doing this
# x = int(input())
# steps = x // 5 gives the total steps that 5 is able to do.
# if x % 5 != 0: this gices the remainder which will be 1 2 3 or 4 so we just need to add 1 more step
#     steps += 1
# print(steps)
#




