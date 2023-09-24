import re
import pandas as pd

# Function to remove special characters from a string
def remove_special_characters(input_string):
    # Replace special characters with an empty string
    return re.sub(r'[^a-zA-Z0-9]+', '', input_string)

# Function to generate email addresses
def generate_email(row):
    name_parts = row["Student Name"].split()
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = name_parts[-1]
        email = f"{first_name[0].lower()}{remove_special_characters(last_name.lower())}@gmail.com"  # Fix email format
        return email
    else:
        return ""

# Add other functions here as needed
