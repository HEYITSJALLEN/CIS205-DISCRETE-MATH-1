from sys import argv

if len(argv) == 1:        # Program produces a response in the absence of a command-line input
    exit("Error: Please input file name.")

else:
    # Opening the file
    filename = argv[1]
    expression = open(filename)
    lines = expression.readlines()
    stack = []
    
    for line in lines:
        # Removing whitespaces and splitting the line
        line = line.rstrip()
        operators = line.split()  # Split the line into a list of operators
        
        # Evaluate RPN expression
        for operator in operators:
            if operator == "+":
                b = stack.pop()
                a = stack.pop()
                result = a + b
                stack.append(result)
            elif operator == "-":
                b = stack.pop()
                a = stack.pop()
                result = a - b
                stack.append(result)
            elif operator == "*":
                b = stack.pop()
                a = stack.pop()
                result = a * b
                stack.append(result)
            elif operator == "/":
                b = stack.pop()
                a = stack.pop()
                result = a / b
                stack.append(result)
            else:
                stack.append(float(operator))  # Convert operator to float and push to stack

    # Printing original RPN expressions and their results
    for line in lines:
        operators = line.rstrip().split()  # Split the line into a list of operators
        print(' '.join(operators))  # Print the original expression
        print(stack.pop())           # Print the result of the RPN expression
