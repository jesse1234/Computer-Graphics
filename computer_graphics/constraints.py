import pandas as pd
import re

# Number of Male and Female Students
def count_gender(df):
    male_students = df[df['Gender'] == 'M']
    female_students = df[df['Gender'] == 'F']
    return len(male_students), len(female_students)

# Using a regex pattern to match certain characters
def has_special_characters(name):
    special_char_pattern = re.compile(f'[^a-zA-Z\s\d,]+')
    return bool(special_char_pattern.search(name))

# Filter DataFrame to get students with special characters in their name
def get_students_with_special_chars(df):
    return df[df['Student Name'].apply(has_special_characters)]

# Add other constraints here as needed
