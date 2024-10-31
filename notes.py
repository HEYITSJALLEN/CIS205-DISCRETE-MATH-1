# courses = set()

courses = set() #Create an empty set to store collection of courses
# binary relations
prerequisites = set() #Stores a set of prerequisites (A,B) meaning A is a prerequisite for B {("CS 101", "CS205"), ("CS 205", "CS206")}

# SET {}
#TUPLE() ---> ORDERED

def add_course(crouse): #(crouse) ---> parameter
    courses.add(crouse)

# add_course("CS 101")
# add_course("CS 205")

def remove_course(course):
    courses.discard(course)

def add_prerequisite(prereq, course): # Tuple ---> Ordered pair
    # Check to see of prereq and course are both in the list of courses

    if prereq in courses and course in courses:
        prerequisites.add((prereq, course))

def remove_prerequisite(prereq, course):
        prerequisites.remove((prereq, course))

def get_prerequisites(course): 
    result = set()
    for prereq, c in prerequisites:
        if c == course:
            result.add(prereq)
    return result 

prerequisites = {("CS101", "CS205"), ("CS101", "CS205")}
get_prerequisites = ("CS205")

# (prereq, course)
# (course, depent)

def get_dependents(course):
    result = set()
    for prereq, c in prerequisites:
        if prereq == course:
            result.add(c)
    return result

course_list = ["CS 101","CS 202" ,"CS 205","CS 206","CS 201","CS 250", "CS 300","CS 301","CS 311","CS 320","CS 401","CS 415","CS 420","CS 490"]

for item in course_list:
        add_course(item)

add_prerequisite("CS 101")
add_prerequisite("CS 202")
add_prerequisite("CS 205")
add_prerequisite("CS 206")
add_prerequisite("CS 201")
add_prerequisite("CS 250")
add_prerequisite("CS 300")
add_prerequisite("CS 301")
add_prerequisite("CS 311")
add_prerequisite("CS 320")
add_prerequisite("CS 401")
add_prerequisite("CS 411")

# add_course("CS 101")
# add_course("CS 202")
# add_course("CS 205")
# add_course("CS 206")
# add_course("CS 201")
# add_course("CS 250")


# Test basic course prerequisites
print("Prerequisites for CS 301: ", get_dependents("CS 301"))
print("Dependents for CS 205: ", get_dependents("CS 205"))
