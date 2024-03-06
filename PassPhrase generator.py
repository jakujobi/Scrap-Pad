# Create a password generator that makes passphrases
# from a given list of words.

# Import the random module
import random

# Define the list of words
words = ["hello", "world", "python", "code"]

# Define a function to generate a password
def generate_password():
    # Create an empty list to store the words
    password = []
    
    # Iterate over the range of the length of the password
    for _ in range(4):
        # Choose a random word from the list
        word = random.choice(words)
        
        # Append the word to the password list
        password.append(word)
    
    # Join the words in the password list with a space
    return " ".join(password)

# Call the function to generate a password
password = generate_password()