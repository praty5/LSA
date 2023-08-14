nums = [] #empty list
sum=0     #sum of the numbers
prod=1    #product of the numbers
n=0       #counter
max = 0   #largest number
while n < 3:                               #loop to get 3 numbers
    inp = int(input("Enter a number: "))   #get input from user
    nums.append(inp)                       #add input to list
    n+=1                                   #increment counter

for i in range(3):                         #loop to find largest number, sum and product
    if nums[i]>max:                        #if the number is greater than the current max, set it as the new max
        max = nums[i]                      #set new max
    sum = sum+nums[i]                      #add the number to the sum
    prod = prod*nums[i]                    #multiply the number to the product
    
print("The largest number is: ",max)          #print the results
print("The sum of the numbers is: ",sum)
print("The product of the numbers is: ",prod)
