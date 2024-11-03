# This creates an empty set
empty_set = set()

""" # This creates an empty dictionary
empty_set = {}

# empty_set = {}
empty_set.add("orange")
print(empty_set)  # Output: {'orange'}

# This creates a set with values
fruits = {"apple", "banana"} # ----> Concatenation
print(fruits)  # Output: {'apple', 'banana'} """

# A set is immutable. It cannot be changed

# MUTATE - change
# STRING IS IMMUTABLE
# IMPUTABLE - cannot change

fruits = {"apple", "banana"}
fruits.add("orange")
fruits.update(["cherry", "kiwi"])

fruits.remove("kiwi")
fruits.discard("kiwi")


#Sample of pop and push ---> old technique
fruit_list = ["guava" ,"pineapple"]
result = fruit_list.pop() #Removes pineapple
print(result) # Output: pineapple
result = fruit_list.pop #removes guava
print(result) #pritns guava

fruits[0] #doesnt mean anything for a set
fruit_list[0] #first item in the list

