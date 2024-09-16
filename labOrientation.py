#Jared Allen Wenceslao

#Part 1
'''def printName(n):
    name = "Jared Allen Wenceslao"
    for i in range(n):
        print(name)

printName(5)
printName(2)
printName(0)'''

#Part 2
'''def printName(n):
    name = "Jared Allen Wenceslao"
    for i in range(n):
        print(name)

def main():
    while True:
        userInput = int(input("Enter the number: ")) #input function for the user to enter the number
        if userInput < 1:
            print("Error: You have entered a number that is less than 1, please enter again")
        else:
            printName(userInput)
            break

#Run
main()'''

#Part 3
from sys import argv

def printName(n):
   name = "Jared Allen Wenceslao"
   for i in range(n):
      print(name)

#Main

if len(argv) == 1:        #Program produces a response in the absence of a command-line input
   exit("Error: No number being entered, please enter a number.")
number = int(argv[1])     
if number < 1:            #Program produces a response if the user entered a number that is less than 1
   print("Error: You have entered a number that is less than 1, please enter again")        
else:
   printName(number)