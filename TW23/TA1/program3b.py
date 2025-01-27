i = 1
while i <= 7:
    if i == 2 or i == 4:
        i += 1
        continue  #Skip number 2 and 4
    #Print the number repeatedly based on its number
    k = 1
    while k <= i:
        print(i, end="")
        k += 1
    #Move to the next line
    print()
    i += 1