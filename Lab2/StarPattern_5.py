#Print Rhombus using star patterns 

num = int(input("Enter value: ")) #taking input from the user
 

for i in range(1, num+1):
    
    for j in range(num-i):
        print(" "  , end="")

    for j in range(num):
        print("*", end="")

    print()

