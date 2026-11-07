#printing inverted triangle 

num = int(input("Enter value: ")) #taking input from the user 

for i in range(num+1):  # here running for loop from i = 0 to i= num+1 

    for j in range(i):      #inner loop to print spaces 
        print(" ", end= "")
    for j in range(num-i):  #inner loop to print stars
        print("* ", end="")
    print()                 #to move on next line 