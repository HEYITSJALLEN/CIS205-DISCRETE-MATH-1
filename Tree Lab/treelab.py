from sys import argv

if len(argv) == 1:        #Program produces a response in the absence of a command-line input
    exit("Error: Please input file name.")

else:
    #opening the file
    filename = argv[1]
    expression = open(filename)
    lines = expression.readlines()
    stack = []
    formulas = []

    for line in lines:
        #removing whitespaces and splitting the line
        line = line.rstrip()
        line = line.split()
        formulas.append(line)
        
        #evaluate RPN expression
        for num in line:
            if num == "+":
                b = stack.pop()
                a = stack.pop()
                result = float(a) + float(b)
                stack.append(float(result))
            elif num == "-":
                b = stack.pop()
                a = stack.pop()
                result = float(a) - float(b)
                stack.append(float(result))
            elif num == "*":
                b = stack.pop()
                a = stack.pop()
                result = float(a) * float(b)
                stack.append(float(result))
            elif num == "/":
                b = stack.pop()
                a = stack.pop()
                result = float(a) / float(b)
                stack.append(float(result))
            else:
                stack.append(float(i))

    #Printing original RPN expressions and their results
    for i in range(len(formulas)):
        print(' '.join(formulas[i]))
        print(stack[i])



    