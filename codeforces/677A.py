n,h = map(int,input().split())
height = list(map(int, input().split()))
w = 0
for he in height:
    if he > h:
        w += 2
    else:
        w += 1
print(w)

# If not taller it means that you walk normally and take a unit of width
# If taller you bend down and take 2 units of width.
# n is the people h is the height of the wall, the next height is each persons height. 

