import os
import pandas as pd
import json
import argparse
from functions import create_excel_file

def main():
    parser = argparse.ArgumentParser(description='Convert JSONL files to Excel files by language')
    parser.add_argument('--input-folder', required=True, help='Path to the folder containing JSONL files')
    parser.add_argument('--output-folder', required=True, help='Path to the folder where Excel files will be saved')
    args = parser.parse_args()
    
    ''' These are the input and output folder paths'''
    input_folder_path = args.input_folder
    output_folder_path = args.output_folder
    os.makedirs(output_folder_path, exist_ok=True)

    ''' Initialize an empty dictionary to store data by language'''
    data_by_language = {}

    ''' Load en-US data for reference'''
    en_us_data = {}
    en_us_file_path = os.path.join(input_folder_path, "en-US.jsonl")
    with open(en_us_file_path, "r", encoding="utf-8") as en_us_file:
        for line in en_us_file:
            data = json.loads(line)
            en_us_data[data["id"]] = {
                "utt_en-US": data["utt"],
                "annot_utt_en-US": data["annot_utt"]
            }

    ''' Iterate through all JSONL files in the folder'''
    for filename in os.listdir(input_folder_path):
        if filename.endswith(".jsonl") and filename != "en-US.jsonl":
            file_path = os.path.join(input_folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    data = json.loads(line)
                    language = data["locale"].split("-")[-1]  
                    if language not in data_by_language:
                        data_by_language[language] = []
                    id_value = data["id"]
                    ''' Extract and keep only the columns that are needed'''
                    simplified_data = {
                        "id": id_value,
                        f"utt_{language}": data["utt"],
                        f"annot_utt_{language}": data["annot_utt"],
                    }
                    if id_value in en_us_data:
                        simplified_data.update(en_us_data[id_value])
                    data_by_language[language].append(simplified_data)


    ''' Create Excel files for each language'''
    for language, data in data_by_language.items():
        create_excel_file(language, data)

if __name__ == '__main__':
    main()
