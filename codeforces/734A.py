n = int(input())
s = input()
if len(s) == n:
    if s.count("A") > s.count("D"):
        print("Anton")
    elif s.count("D") > s.count("A"):
        print("Danik")
    else:
        print("Friendship")
