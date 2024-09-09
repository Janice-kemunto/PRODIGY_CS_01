import re

def check_password_strength(password):
    # Initialize strength score and feedback list
    strength_score = 0
    feedback = []
    
    # Check for length
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for numbers
    if re.search(r'\d', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Determine password strength
    if strength_score == 5:
        feedback.append("Your password is strong!")
        strength = "Strong"
    elif 3 <= strength_score < 5:
        feedback.append("Your password is moderate.")
        strength = "Moderate"
    else:
        feedback.append("Your password is weak.")
        strength = "Weak"
    
    return {
        'strength': strength,
        'feedback': feedback
    }

# Example usage:
password = input("Enter a password to check its strength: ")
result = check_password_strength(password)

print(f"Password strength: {result['strength']}")
for comment in result['feedback']:
    print(comment)
