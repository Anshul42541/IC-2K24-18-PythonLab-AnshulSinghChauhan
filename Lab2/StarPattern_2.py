#Print pyramid triangle pattern
n = int(input("Enter value: ")) #taking input from the user 

for i in range(1, n + 1): # here running for loop from i = 1 to i= n+1 
    for j in range(n - i):  #inner loop to print spaces 
        print(" ", end="")

    for j in range(i):      #second inner loop to print stars 
        print("* ", end="")

    print()    #using for next line 
     