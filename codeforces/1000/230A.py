s,n = map(int,input().split())
hold = []
for _ in range(n): # Does this for each dragon that is given. giving it a set strength and bonus
    x,y = map(int,input().split())
    hold.append((x,y)) # This appends it as a pair
hold.sort() # So now lowest dragon will appear first
for x, y in hold: # Takes values from hold and gives it x and y
    if s <= x: # If our strength is lower than dragons strength we lose.
        print("NO")
        break
    s += y # This happens if we win because we take the bonus strength from the dragon
else:
    print("YES")
