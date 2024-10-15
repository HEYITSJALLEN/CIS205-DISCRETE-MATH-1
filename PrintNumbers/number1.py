for i in range(1, 8):
    for j in range(1, 6):
        if j == 4 - i or j == 3 or i == 7:
            print("+", end="")
        else:
            print(" ", end="")
    print()