import re


def check_password_strength(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 12
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|`~]', password))

    # Calculate score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Provide feedback
    if score == 5:
        feedback = "Strong Password :)"
    elif score == 4:
        feedback = "Good Password, but could be stronger with additional complexity."
    elif score == 3:
        feedback = "Moderate Password. Consider increasing length and adding more complexity."
    elif score == 2:
        feedback = "Weak Password. Try to use a mix of uppercase, lowercase, numbers, and special characters."
    else:
        feedback = "Very Weak Password. Consider using a longer password with diverse characters."

    # Return results
    return {
        "length": length_criteria,
        "uppercase": uppercase_criteria,
        "lowercase": lowercase_criteria,
        "digit": digit_criteria,
        "special_char": special_char_criteria,
        "score": score,
        "feedback": feedback
    }


def main():
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)

    # Display results
    print("\nPassword Strength Analysis:")
    print(f"Length (>= 12 characters): {'YES' if result['length'] else 'NO'}")
    print(f"Uppercase Letters: {'YES' if result['uppercase'] else 'NO'}")
    print(f"Lowercase Letters: {'YES' if result['lowercase'] else 'NO'}")
    print(f"Digits: {'YES' if result['digit'] else 'NO'}")
    print(f"Special Characters: {'YES' if result['special_char'] else 'NO'}")
    print(f"\nOverall Score: {result['score']}/5")
    print(f"Feedback: {result['feedback']}")


if __name__ == "__main__":
    main()
