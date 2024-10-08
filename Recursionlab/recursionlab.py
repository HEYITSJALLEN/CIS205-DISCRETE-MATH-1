from sys import argv


if len(argv) == 1:        
    exit("Error: Please input file name.")

filePath = open(argv[1])
contents = filePath.readlines()
A = [int(line.strip()) for line in contents] #Converts the list into integers

def sortSelection(p, r):
    if p < r:
        q = divide(p, r)
        #Recursively sort the sublists before and after the partition.
        sortSelection(p, q - 1)
        sortSelection(q + 1, r)

def divide(p, r):
    x = A[r]
    i = p - 1
    #Iterate through the elements in the range [p, r-1].
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            # Swap elements at positions 'i' and 'j'.
            (A[i], A[j]) = (A[j], A[i])
    # Swap the pivot element with the element at position 'i+1'.
    (A[i + 1], A[r]) = (A[r], A[i + 1])
    return (i + 1)


#MAIN calling of functions
sortSelection(0, len(A) - 1)
print(A)

