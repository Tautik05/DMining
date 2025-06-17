import re

def is_valid_email(email):
    # Regular expression for validating email addresses
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

# Prompt user for email input
email = input("Enter an email address: ")

# Check if the email is valid
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
