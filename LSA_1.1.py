#Program to randomly generate N (user input) numbers and output the largest number and the sum, product of the numbers
import random                     #importing random module for using the random function

sum=0                             #sum of the numbers
prod=1                            #product of the numbers
max=0                             #largest numbers

inp = int(input("Enter the amount of numbers to be generated: "))  #input for the amount of numbers to be generated
nums = [random.randint(1,100) for i in range(inp)]   #generating random numbers and storing them in a list using list comprehension
print("The random numbers generated are :",nums)    #printing the list of random numbers

for i in range(inp):            #loop for calculating the sum, product and largest number
    sum += nums[i]              #adding the numbers to sum
    prod *= nums[i]             #multiplying the numbers to prod
    if nums[i]>max:             #checking if the number is greater than max
        max = nums[i]           #if yes, then assigning the number to max

print("The largest number is: ",max)            #print the results
print("The sum of the numbers is: ",sum)
print("The product of the numbers is: ",prod)