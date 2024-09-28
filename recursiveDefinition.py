#Example: Simple Recursive Sequence S(n) = S(n-1) + 5

def simple_sequence(n):
    if n == 0:
        return 0
    else:
        return simple_sequence(n - 1) + 5

# Example usage:
print(simple_sequence(4))  # Output: 20

#Example: Fibonacci Sequence

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
print(fibonacci_recursive(5))  # Output: 5

# [] ----> Represents Empty list
# Generating the First n Fibonacci Numbers

def generate_fibonacci_recursive(n):
    sequence = []
    for i in range(n):
        sequence.append(fibonacci_recursive(i))
    return sequence

# Example usage:
print(generate_fibonacci_recursive(6))  # Output: [0, 1, 1, 2, 3, 5]

#Recursive vs. Iterative Approach

def fibonacci_iterative(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a
        a = b
        b = temp + b
    return a

# Example usage:
print(fibonacci_iterative(5))  # Output: 5




