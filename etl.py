for row in range(5):
    for col in range(4):
        if (
            row == 1 or
            (row == 2 and col == 1) or
            row == 3 or
            (row == 4 and col == 3)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
