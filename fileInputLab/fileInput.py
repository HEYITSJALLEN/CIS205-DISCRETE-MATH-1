from sys import argv

if len(argv) == 1:        
    exit("Error: Please input the right file name.")

filePath = open(argv[1])
contentFiles = filePath.readlines()
totalOfEight = 0
totalValues = 0

for line in contentFiles: 
    line = line.rstrip()
    i = line.count("8") 
    totalOfEight += i    

    for char in line:
        if char.isdigit():
            totalValues += int(char)
            
print("There are total of: ",totalOfEight," eights in this file.")      
print("Total of all digits is",totalValues)
print(line)
