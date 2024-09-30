import re

# Function to check if a line is a statement
def is_statement(line):
    # Remove leading and trailing whitespace
    line = line.strip()

    # Check if the line ends with a question mark
    if line.endswith('?'):
        return False

    # Check if the line is just a single word
    if len(line.split()) == 1:
        return False

    # Check if the line begins with a question word
    question_words = ['what', 'where', 'how', 'why', 'who', 'when']
    if any(line.lower().startswith(word) for word in question_words):
        return False

    # Check if the line contains any pronouns
    pronouns = ['he', 'she', 'it', 'they']
    if any(re.search(r'\b{}\b'.format(pronoun), line.lower()) for pronoun in pronouns):
        return False

    # If none of the above conditions are met, it's a statement
    return True

# Read the text file and process each line
file_path = 'input1.txt'  # Replace with the path to your input file
try:
    with open(file_path, 'r') as file:
        for line in file:
            if is_statement(line):
                print(f'{line.strip()}: STATEMENT')
            else:
                print(f'{line.strip()}: NOT A STATEMENT')
except FileNotFoundError:
    print(f'File not found: {file_path}')
except Exception as e:
    print(f'An error occurred: {str(e)}')