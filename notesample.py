courses = set()  # Create an empty set to store collection of courses
prerequisites = set()  # Stores a set of prerequisites (A,B)

def add_course(course):  # Fixed parameter name
    courses.add(course)

def remove_course(course):
    courses.discard(course)

def add_prerequisite(prereq, course):
    if prereq in courses and course in courses:
        prerequisites.add((prereq, course))

def remove_prerequisite(prereq, course):
    prerequisites.discard((prereq, course))

def get_prerequisites(course): 
    result = set()
    for prereq, c in prerequisites:
        if c == course:
            result.add(prereq)
    return result 

def get_dependents(course):
    result = set()
    for prereq, c in prerequisites:
        if prereq == course:
            result.add(c)
    return result

course_list = ["CS 101", "CS 202", "CS 205", "CS 206", "CS 201", 
               "CS 250", "CS 300", "CS 301", "CS 311", "CS 320", 
               "CS 401", "CS 411"]

# Adding courses
for item in course_list:
    add_course(item)

# Adding prerequisites correctly
add_prerequisite("CS 101", "CS 205")
add_prerequisite("CS 202", "CS 206")
add_prerequisite("CS 205", "CS 301")
add_prerequisite("CS 201", "CS 250")
add_prerequisite("CS 300", "CS 301")
add_prerequisite("CS 311", "CS 401")

# Test basic course prerequisites
print("Prerequisites for CS 301: ", get_prerequisites("CS 301"))
print("Dependents for CS 205: ", get_dependents("CS 205"))
