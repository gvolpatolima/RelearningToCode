import random
import string


def generate_password(length=18):
    # Define character pools
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits  # 0-9
    special_chars = string.punctuation  # !, @, #, etc.

    # Ensure password contains at least one character from each pool
    all_chars = letters + digits + special_chars
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password with random characters
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle to ensure randomness
    random.shuffle(password)

    # Join list into a string
    return ''.join(password)


# Test the generator
if __name__ == "__main__":
    print("Generated Password:", generate_password())
