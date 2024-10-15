from sys import argv

def main():
    filePath = open(argv[1])
    contents = filePath.readlines()
    # PARING THE LINE CONTENTS
    line1 = contents[0].rstrip()
    line2 = contents[1].rstrip()
    splitA = line1.split(" ")
    splitB = line2.split(" ")
    setA = ", ".join(splitA)
    setB = ", ".join(splitB)
    print("A = {" + setA + "}")
    print("B = {" + setB + "}")

#MAIN
if len(argv) == 1:        
    #Program produces a response in the absence of a command-line input
    exit("Error: Please input file name.")
main()