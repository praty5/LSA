import re
regex = r"[0-9]+"

i=0
# Open log file
with open("info.log", "r") as f:
    # Read the lines
    lines = f.readlines()

num = int((re.findall(regex, lines[0]))[0])
#num= int(num[0])
odd = re.findall(regex, lines[1])
odd= int(odd[0])
even = re.findall(regex, lines[2])
even= int(even[0])

print(f'Total numbers: {num}')
print(f'Number of odd numbers: {odd}')
print(f'Number of even numbers: {even}')
# Get the number of odd and even numbers using regex
lower = min(odd, even)
summ = []*lower
# get the numbers from even and odd .dat file row by row and print the sum of them
while i < lower:
    with open("odd.dat", "r") as f:
        # Read the lines
        lines = f.readlines()
        odd = re.findall(regex, lines[i])
        odd= int(odd[0])
    with open("even.dat", "r") as f:
        # Read the lines
        lines = f.readlines()
        even = re.findall(regex, lines[i])
        even= int(even[0])
    summ.append(odd+even)
    i += 1
    
print(summ)
with open("Summation.dat", "w") as f:
    for item in summ:
        f.write(f"{item}")
        f.write("\n")