import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
   
    characters = ""
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not characters:
        return "Error: No character types selected!"
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
   
    print("=== PASSWORD GENERATOR ===")
    print()
    
    # Get password length
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("Password length must be at least 4 characters!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    print("\nSelect character types to include:")
    
    # Get complexity preferences
    use_lowercase = input("Include lowercase letters? (y/n): ").lower().startswith('y')
    use_uppercase = input("Include uppercase letters? (y/n): ").lower().startswith('y')
    use_digits = input("Include digits? (y/n): ").lower().startswith('y')
    use_symbols = input("Include symbols? (y/n): ").lower().startswith('y')
    
    # Ensure at least one character type is selected
    if not any([use_lowercase, use_uppercase, use_digits, use_symbols]):
        print("At least one character type must be selected! Using all types.")
        use_lowercase = use_uppercase = use_digits = use_symbols = True
    
    return length, use_uppercase, use_lowercase, use_digits, use_symbols

def display_password_strength(password):
    """Display password strength analysis."""
    strength_score = 0
    feedback = []
    
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Use at least 8 characters")
    
    if len(password) >= 12:
        strength_score += 1
    
    if any(c.islower() for c in password):
        strength_score += 1
    else:
        feedback.append("Add lowercase letters")
    
    if any(c.isupper() for c in password):
        strength_score += 1
    else:
        feedback.append("Add uppercase letters")
    
    if any(c.isdigit() for c in password):
        strength_score += 1
    else:
        feedback.append("Add numbers")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        strength_score += 1
    else:
        feedback.append("Add symbols")
    
    # Determine strength level
    if strength_score >= 5:
        strength = "Very Strong"
    elif strength_score >= 4:
        strength = "Strong"
    elif strength_score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:", ", ".join(feedback))

def main():
    """Main function to run the password generator."""
    while True:
        # Get user input
        length, use_uppercase, use_lowercase, use_digits, use_symbols = get_user_input()
        
        # Generate password
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        
        # Display results
        print("\n" + "="*50)
        print("GENERATED PASSWORD:")
        print("="*50)
        print(f"Password: {password}")
        print(f"Length: {len(password)} characters")
        
        # Show password strength
        display_password_strength(password)
        
        # Ask if user wants to generate another password
        print("\n" + "="*50)
        again = input("Generate another password? (y/n): ").lower()
        if not again.startswith('y'):
            print("Thank you for using Password Generator!")
            break
        print()

if __name__ == "__main__":
    main()