#writing a program to check if the number is armstrong or not 
#ARMSTRONG number is the number which equals to the sum of its own digits each raised to the power of the number of digits

num = input("Enter a number to check for Armstrong : ")  #taking input from the user 
num_len = len(num) #finding the length of the number 

#print(num_len)  prints the length 

result = 0  #using this for storing the result 

for i in num:  #for loop fto iterate over the input value 
    i = int(i)  # explicitly converting i into integer to perform arithmetic operation **
    result += i**num_len   #calculating 

num = int(num) #Our result is an integer so converting num also to integer after that will compare so no logical error comes

#now check for if result and the original num is equal or not 
if(result== num):
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")
