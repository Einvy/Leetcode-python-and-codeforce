n = input()

if n.isupper(): # If all capital
    new = n.lower() #Sets to all lower
elif len(n) == 1 or n[1:].isupper(): # Checks if only 1 letter or if after first letter all letters are capitalized.
    new = n.lower() # If either case sets to lower
    new = new[0].upper() + new[1:] # sets first letter capital and rest to lower.
else: # No changes are needed
    new = n
print(new)
