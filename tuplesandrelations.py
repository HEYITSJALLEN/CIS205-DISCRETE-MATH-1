# Define people as tuples (ID, Name)
person1 = (1, "Alice")
person2 = (2, "Bob")
person3 = (3, "Charlie")
person4 = (4, "Diana")

# Create a list of all people
people = [person1, person2, person3, person4]

# Define relationships as tuples of IDs (Person A, Person B)
friendship1 = (1, 2)  # Alice and Bob are friends
friendship2 = (2, 3)  # Bob and Charlie are friends
friendship3 = (3, 4)  # Charlie and Diana are friends
friendship4 = (1, 4)  # Alice and Diana are friends

# Create a list of all friendships
friendships = [friendship1, friendship2, friendship3, friendship4]

# Function to get the name of a person by ID
def get_name(person_id):
    for person in people:
        if person[0] == person_id:
            return person[1]
    return None

# Display all friendships
print("Friendships:")
for friendship in friendships:
    person_a = get_name(friendship[0])
    person_b = get_name(friendship[1])
    print(f"{person_a} is friends with {person_b}")


""" Explanation:
Tuples person1, person2, etc., store each person's ID and name.
Relationships (friendships) are represented as tuples of IDs, where each tuple indicates a friendship between two people.
The get_name() function looks up a person's name by their ID.
The loop at the end prints out each friendship. """

"""
[] List - Ordered (Allows duplicates, mutable)
{} Set - Unordered (No duplicate, mutable)
() Tuple - Ordered (Immutable, No changes)

Dictionary

"""