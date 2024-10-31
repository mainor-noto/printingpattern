# TODO: ask the user for how mny rows
# and store it in variable called rows
rows = int(input("Enter the number of rows "))

for row in range(1, rows + 1):
    for star in range(1, row + 1):
        print("* ", end="")
    print()

    #add end=""
