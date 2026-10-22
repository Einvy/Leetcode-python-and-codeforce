s = list(map(int,input().split()))
print(4 - len(set(s)))
# Set only accepts new values so that means that we get the length of the colors that are not the same and subtract it from the required amount that we have.
