# Random Password Generator - Beginner Tier
# Oasis Infobyte - Python Programming Track - Task 3

import random
import string


def get_valid_length():
    """Keeps asking until the user enters a valid length (minimum 8)."""
    while True:
        user_input = input("Enter desired password length (minimum 8): ")
        try:
            length = int(user_input)
            if length < 8:
                print("❌ Error: Password length must be at least 8 characters.\n")
                continue
            return length
        except ValueError:
            print("❌ Error: Please enter a valid whole number (e.g., 12).\n")


def get_character_types():
    """
    Asks the user which character types to include.
    Keeps asking until at least 2 types are selected.
    """
    while True:
        print("\nWhich character types do you want to include?")
        print("(Enter y or n for each)")
        use_upper = input("Include UPPERCASE letters? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols (!@#$...)? (y/n): ").strip().lower() == 'y'

        selected_count = sum([use_upper, use_lower, use_digits, use_symbols])

        if selected_count < 2:
            print("❌ Error: Please select at least 2 character types.\n")
            continue

        return use_upper, use_lower, use_digits, use_symbols


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generates a password that includes at least one character from each selected type."""
    character_pool = ""
    required_chars = []

    if use_upper:
        character_pool += string.ascii_uppercase
        required_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        character_pool += string.ascii_lowercase
        required_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        character_pool += string.digits
        required_chars.append(random.choice(string.digits))
    if use_symbols:
        character_pool += "!@#$%^&*()-_=+"
        required_chars.append(random.choice("!@#$%^&*()-_=+"))

    # Fill the remaining length with random characters from the pool
    remaining_length = length - len(required_chars)
    random_chars = [random.choice(character_pool) for _ in range(remaining_length)]

    # Combine and shuffle so required characters aren't always at the start
    password_chars = required_chars + random_chars
    random.shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("=" * 45)
    print("      WELCOME TO PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        length = get_valid_length()
        use_upper, use_lower, use_digits, use_symbols = get_character_types()

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

        print("\n------ GENERATED PASSWORD ------")
        print(f"Your password is: {password}")
        print("---------------------------------")

        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for using Password Generator. Goodbye!")
            break


if __name__ == "__main__":
    main()