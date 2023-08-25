import random
odd= []
even= []
x = int(input("Enter the amount of numbers you want to create: "))
numbers = [random.randint(1, 100) for i in range(x)]

odd = [i for i in numbers if i % 2 != 0]
even = [i for i in numbers if i % 2 == 0]

print("The list of numbers is: ", numbers,end="\n")
print()
print("The list of odd numbers is: ", odd,end="\n")
print()
print("The list of even numbers is: ", even,end="\n")
print()

#Creating a log file to store the information
f = open("info.log", "w")
f.write("Total numbers are: "+str(len(numbers)))
f.write("\n")
f.write("Total odd numbers are: "+str(len(odd)))
f.write("\n")
f.write("Total even numbers are: "+str(len(even)))
f.close()

#Creating a .dat file to store odd and even numbers
f = open("odd.dat", "w")
for i in odd:
    f.write(str(i)+"\n")
f.close()

f = open("even.dat", "w")
for i in even:
    f.write(str(i)+"\n")
f.close()

