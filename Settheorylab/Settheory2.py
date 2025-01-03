from sys import argv 

def main():
    filePath = open(argv[1])
    contents = filePath.readlines()
    line1 = contents[0].rstrip()
    line2 = contents[1].rstrip()
    splitA = line1.split(" ")
    splitB = line2.split(" ")
    setA = set(splitA)
    setB = set(splitB)

    # Prints sets A and B
    print("A = {" + ', '.join(setA) + "}")
    print("B = {" + ', '.join(setB) + "}")

    # Prints the intersection
    print("A intersect B = {" + ', '.join(intersection(setA, setB)) + "}")

    # Prints union
    print("A union B = {" + ', '.join(union(setA, setB)) + "}")
    
    # Prints Aminus and Bminus
    print("A - B = {" + ', '.join(Aminus(setA, setB)) + "}")
    print("B - A = {" + ', '.join(Bminus(setA, setB)) + "}")

    # Print cartesian product
    print("A x B = {"+ ', '.join(cartesian(setA, setB)) + "}")
    print("B x A = {" + ', '.join(cartesian(setB, setA)) + "}")

def intersection(setA, setB):
    return setA & setB

def union(setA, setB):
    return setA | setB

def Aminus(setA, setB):
    return setA - setB

def Bminus(setA, setB):
    return setB - setA

def cartesian(setA, setB):
    cartesianResult = [f'({a},{b})' for a in setA for b in setB]
    return cartesianResult

# Main
# This program creates a response in the absence of a command-line input
if len(argv) == 1:        
    exit("Error: Please input file name.")
main()