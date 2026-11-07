#printing square pattern using stars 

num = int(input("Enter value: ")) #taking input from the user

for i in range(1,num+1):
    for j in range(1, num+1):
        if(i==1 or i ==num or j ==1 or j==num):  #condition that star should be print at only borders 
            print("* ", end="")
        else:
            print("  ", end="") 
    print()