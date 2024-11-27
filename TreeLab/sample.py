inputString = "6 6 * 2 7 * - 2 /"
# print the input string (1.)

# Create a method (2.)
# Use split method to convert the input string to a split
inputList = inputString.split()
# print(inputList)


myStack = []
# Loop through (and print) each item in the inputList (3.1)
for item in inputList:
    # print(item)
    # if the next item is a number, push it onto the stack.
    if item.isnumeric() == True: # ----> .isnumeric is a method or property
        myStack.append(int(item))
    else:
        # If the item is an operator, pop the last two items from the stack
        num2 = myStack.pop() # Second popped value (right operand)
        num1 = myStack.pop() # First popped value (left operand)
        
    # If the next item is an operator, pop the last two items
    # Perform the operation based on the operator
    # From the stack and store them as num1 and num2
        if item == "+":
            result = num1 + num2
        elif item == "-":
            result = num1 - num2
        elif item == "*":
            result = num1 * num2
        elif item == "/":
            result = num1 / num2  

            # Can't multiply sequence by non-integer of type 'str'
            # Push the result back onto the stack
        myStack.append(result)
    

# Step 5: Pop and print the final result from the stack
finalResult = myStack.pop()
print("Final Result:", finalResult)