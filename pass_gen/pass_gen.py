# Import the random module
import random

# Define a function to generate a random password
def generate_password(length, complexity):
    """
    Generate a random password with a given length and complexity.

    Parameters:
    length (int): The length of the password.
    complexity (int): The complexity of the password. It can be one of the following values:
    - 1: Use lowercase letters, numbers, and symbols.
    - 2: Use lowercase and uppercase letters, numbers, and symbols, with at least one of each type.
    - 3: Use lowercase, uppercase, numbers, and symbols, with at least two of each type.

    Returns:
    str: The generated password.
    """
    # Define the character sets for each complexity level
    low_chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    medium_chars = low_chars + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    high_chars = medium_chars
    very_high_chars = high_chars

    # Choose the character set based on the complexity
    if complexity == 1:
        chars = low_chars
    elif complexity == 2:
        chars = medium_chars
    elif complexity == 3:
        chars = very_high_chars
    else:
        # If the complexity is invalid, raise an exception
        raise ValueError("Invalid complexity. Please enter 1, 2, or 3.")

    # Initialize an empty string for the password
    password = ""
    # Loop for the length of the password
    for i in range(length):
        # Choose a random character from the character set
        char = random.choice(chars)
        # Append the character to the password
        password += char

    # If the complexity is 2 or 3, check if the password meets the requirements
    if complexity in [2, 3]:
        # Define the minimum number of each type of character
        if complexity == 2:
            min_count = 1
        else:
            min_count = 2
        # Count the number of each type of character in the password
        lower_count = sum(char.islower() for char in password)
        upper_count = sum(char.isupper() for char in password)
        digit_count = sum(char.isdigit() for char in password)
        symbol_count = sum(char in "!@#$%^&*()" for char in password)
        # If any type of character is less than the minimum, replace some characters with that type
        if lower_count < min_count:
            password = replace_chars(password, min_count - lower_count, "abcdefghijklmnopqrstuvwxyz")
        if upper_count < min_count:
            password = replace_chars(password, min_count - upper_count, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if digit_count < min_count:
            password = replace_chars(password, min_count - digit_count, "0123456789")
        if symbol_count < min_count:
            password = replace_chars(password, min_count - symbol_count, "!@#$%^&*()")

    # Return the password
    return password

# Define a helper function to replace some characters in a string with a given character set
def replace_chars(string, count, chars):
    """
    Replace some characters in a string with a given character set.

    Parameters:
    string (str): The original string.
    count (int): The number of characters to replace.
    chars (str): The character set to use for replacement.

    Returns:
    str: The modified string.
    """
    # Convert the string to a list of characters
    string_list = list(string)
    # Loop for the number of characters to replace
    for i in range(count):
        # Choose a random index in the string list
        index = random.randrange(len(string_list))
        # Choose a random character from the character set
        char = random.choice(chars)
        # Replace the character at the index with the new character
        string_list[index] = char
    # Convert the string list back to a string
    string = "".join(string_list)
    # Return the modified string
    return string

# Define the main function
def main():
    """
    The main function of the program.
    """
    # Print a welcome message
    print("Welcome to Shecktar Password Generator, a Python application that generates strong and random passwords for you.")
    print("")
    # Ask the user for the length of the password
    length = int(input("Please Enter the Desired length of the password: "))
    # If the length is zero, raise an exception
    if length == 0:
        raise ValueError("Invalid length. The length of the password cannot be zero.")
    # If the length is between 1 and 5, warn the user about the risks
    if 1 <= length <= 5:
        print("Warning: The length of the password is too short. It may be easy to guess or leak. Please consider using a longer password for better security.")
        # Ask the user if they still wish to continue with the short password
        choice = input("Do you still wish to continue with the short password? (y/n): ")
        # If the user chooses no, ask them to enter a new length
        if choice.lower() == "n":
            length = int(input("Enter a new length of the password: "))
    print("")
    # Ask the user for the complexity of the password
    complexity = int(input("Enter the complexity of the password (1 for low, 2 for high, or 3 for very high): "))
    # Generate the password
    password = generate_password(length, complexity)
    # Print the password
    print("Your password is:", password)
    print("")
    print("Copy and save your password somewhere safe. Do not share your password with anyone or use it for multiple accounts. You can also generate a new password if you are not satisfied with the current one")

# Call the main function
if __name__ == "__main__":
    main()