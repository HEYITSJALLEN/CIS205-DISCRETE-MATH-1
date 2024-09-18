#Jared Allen Wenceslao

from sys import argv

"""
#Argv ---> The input value of the terminal
print(argv[0]) # ---> Arguemnt 0 is a python file
print(argv[1])"""

# Loop through each line of the file
if len(argv) == 1:        
    exit("Error: Please input the right file name.")


# Open the file provided as the first argument (argv[1]) in read mode
filePath = open(argv[1])
contentFiles = filePath.readlines() 
totalOfEight = 0 # Initialize a counter for the total number of '8' digits found in the file
totalValues = 0 # Initialize a sum for the total value of all digits in the file

for line in contentFiles: 
    line = line.rstrip()
    i = line.count("8")  #Count the occurrences of the digit '8' in the current line
    totalOfEight += i    # Add the count of '8's in this line to the total count


    for char in line:
        if char.isdigit():
            totalValues += int(char)

# Print the total number of '8's found in the file           
print("There are total of: ",totalOfEight," eights in this file.")  

# Print the total sum of all the digits found in the file
print("Total of all digits is",totalValues)

# Print the last line read (after the loop ends, 'line' will contain the last line)
print(line)
