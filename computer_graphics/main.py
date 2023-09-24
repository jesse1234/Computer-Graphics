import pandas as pd
import jsonlines
import random
from datetime import datetime
from functions import remove_special_characters, generate_email
from constraints import count_gender, get_students_with_special_chars

# Load the Excel file with the 'openpyxl' engine
file_path = "Test Files.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# Apply the function to create a new 'Email Address' column
df["Email Address"] = df.apply(generate_email, axis=1)

# Number of Male and Female Students
male_count, female_count = count_gender(df)

print('Number of Male Students:', male_count)
print('Number of Female Students:', female_count)

# Filter DataFrame to get students with special characters in their name
students_special_char = get_students_with_special_chars(df)

# List names with special characters
special_char_names = students_special_char['Student Name'].tolist()

# Print names
print('Names with special characters:')
for name in special_char_names:
    print(name)

# Save the updated DataFrame as an Excel file
xlsx_output_file = "student_file.xlsx"
df.to_excel(xlsx_output_file, index=False)

print("Email addresses generated and saved as Excel:", xlsx_output_file)

# Loading all the individual documents and combine them into one DataFrame
data_files = ['student_file.xlsx', 'Test Files.xlsx']

dfs = []

for file_path in data_files:
    df = pd.read_excel(file_path, engine='openpyxl')
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

# Shuffle the DataFrame randomly
shuffled_df = merged_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Convert Timestamp columns to string format
shuffled_df['DoB'] = shuffled_df['DoB'].dt.strftime('%Y-%m-%d')  # Change 'DoB' to your date column name

# Shuffle DataFrame as a JSON file
json_output_file = 'shuffled_data.json'
shuffled_df.to_json(json_output_file, orient='records', lines=False)

# Saving another file in JSONL format
jsonl_output_file = 'shuffled_data.jsonl'
with jsonlines.open(jsonl_output_file, mode='w') as writer:
    for _, row in shuffled_df.iterrows():
        writer.write(row.to_dict())

print("Data shuffled and saved as JSON:", json_output_file)
print("Data shuffled and saved as JSONL:", jsonl_output_file)
