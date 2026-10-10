# BMI Calculator - Beginner Tier
# Oasis Infobyte - Python Programming Track - Task 2

def get_valid_float(prompt):
    """
    Keeps asking the user until they enter a valid positive number.
    This handles the "Input validation" requirement:
    - rejects non-numeric input
    - rejects negative/zero values
    """
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value <= 0:
                print("❌ Error: Please enter a positive number greater than 0.\n")
                continue
            return value
        except ValueError:
            print("❌ Error: That is not a valid number. Please enter digits only (e.g., 65.5).\n")


def classify_bmi(bmi):
    """Returns the health category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 40)
    print("      WELCOME TO BMI CALCULATOR")
    print("=" * 40)

    weight = get_valid_float("Enter your weight in kg: ")
    height = get_valid_float("Enter your height in meters (e.g., 1.65): ")

    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)  # round to 2 decimal places

    category = classify_bmi(bmi)

    print("\n------ RESULT ------")
    print(f"Your BMI is: {bmi}")
    print(f"Category: {category}")
    print("---------------------")


# This makes sure main() runs only when this file is run directly
if __name__ == "__main__":
    main()