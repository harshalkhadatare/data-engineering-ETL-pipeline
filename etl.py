# Printing 'H' pattern in python
for row in range (7):
    for col in range (4):
        if (
            (col == 0) or
            (col == 3) or 
            (row == 3)
        ):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
    
# ----------------------------------------------------
