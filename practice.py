#Jared Allen Wenceslao

from sys import argv

#P A R T 1
if len(argv) == 1:        #Program produces a response in the absence of a command-line input
    exit("Error: Please input file name.")

filePath = open(argv[1])
contents = filePath.readlines()
totalOfEight = 0
totalValues = 0

#This part for each line, it is removing any trailing 
#whitespace using the rstrip() method. Then, it is counting 
#the number of occurrences of the character "8" in the line
#and adding that number to the totalOfEight variable.

for line in contents: 
    line = line.rstrip()
    i = line.count("8") 
    totalOfEight += i    

#P A R T 2 in which a for loop added that reads every character in a line
#and if the character is digit, it will be added to the totalValues variable

    for char in line:
        if char.isdigit():
            totalValues += int(char)
            
print("There are a total of",totalOfEight, "eights in this file.")      
print("Total of all digits is",totalValues)
print(line)
