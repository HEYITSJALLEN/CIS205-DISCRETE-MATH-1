#Make all test pass
#Return the fibonacci value at n
#Formula: Fn = Fn-1 + Fn2
#Example: 0,1,1,2,3,5,8,13,21
def fibonacci(n: int):
    if n ==0:
        return 0
    # Make this into recurive
    if n ==1:
        return 1
    else:return fibonacci(n-1) + fibonacci(n-2)


fib8 = [
    fibonacci(0),
    fibonacci(1),
    fibonacci(2),
    fibonacci(3),
    fibonacci(4),
    fibonacci(5),
    fibonacci(6),
    fibonacci(7),
    fibonacci(8),
]

print(fib8)
print(fib8 == [0,1,1,2,3,5,8,13,21])


""" # Correctly comparing fib8 to the expected Fibonacci sequence
expected_fib8 = [0, 1, 1, 2, 3, 5, 8, 13, 21]
print(fib8 == expected_fib8)  # This will return True if the values match """