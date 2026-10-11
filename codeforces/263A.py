moves = 0
for row in range(5):
    val = list(map(int,input().split()))
    for column in range(5):
        if val[column] == 1:
            moves = abs(row - 2) + abs(column - 2)
print(moves)
