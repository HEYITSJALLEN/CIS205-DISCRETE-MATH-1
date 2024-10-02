#Jared Allen Wenceslao
from sys import argv

# A function called isStatement() to contain all of the condition statements
# Based as a criteria on reading a sentence each line.
def isStatement(line):
    line = line.strip()

    if line.endswith("?"):
        return False
    
    if len(line.split()) == 1:
        return False
    
    questionWords = ["what", "where", "how", "why", "when", "who"]
    pronouns = ["he", "she", "it", "they", "our","you", "I", "we", "us", "them"]

    for word in line.lower().split():
        if word in questionWords:
            return False
              
    for word in line.lower().split():
        if word in pronouns:
            return False
        
    return True

# Function to contain the main function.
def main():
    filePath = open(argv[1])
    contents = filePath.readlines()
        
    for line in contents:
        if isStatement(line):
            print(line.strip(), ': STATEMENT')
        else:
            print(line.strip(), ': NOT A STATEMENT')

# Main
if len(argv) == 1:        #Program produces a response in the absence of a command-line input
        exit("Error: Please input the right file name.")
main()