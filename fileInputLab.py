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