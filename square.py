def makeSquare():
    size = 5
    print("H"*size)
    print("H   H")
    print("H   H")
    print("H   H")
    print("H"*size)
makeSquare()

def makeSquare():
    size = 8
    print("H"*size)
    for i in range(0,size-2):
        print("H"+" "*(size-2)+"H")
    print("H"*size)
makeSquare()

def makeSquare():
    size = 8
    print("H"*size)
    for i in range (0,size):
        if i==0 or i == size-1:
            print("H"*size)
        else:
            print("H"+" "*(size -2)+ "H")
makeSquare()

from sys import argv
def makeSquare(char,size):

    for i in range (0,size):
        if i==0 or i == size-1:
            print(char*size)
        else:
            print(char+" "*(size -2)+ char)

#makeSquare("J", 5 )
print(argv)

from sys import argv 

#argv = argument vector

def makeSquare(char,size):

    for i in range (0,size):
        if i==0 or i == size-1:
            print(char*size)
        else:
            print(char+" "*(size -2)+ char)

if argv < 3:
    print("Usage: pratice.py char size")
    exit()
makeSquare(argv[1], int(argv[2]) )
