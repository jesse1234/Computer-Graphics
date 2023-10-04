import os
import argparse
from functions import create_excel_file, load_en_us_data, extract_data_from_jsonl

def main():
    parser = argparse.ArgumentParser(description='Convert JSONL files to Excel files by language')
    parser.add_argument('--input-folder', required=True, help='Path to the folder containing JSONL files')
    parser.add_argument('--output-folder', required=True, help='Path to the folder where Excel files will be saved')
    args = parser.parse_args()

    '''These are the input and output folder paths'''
    input_folder_path = args.input_folder
    output_folder_path = args.output_folder
    os.makedirs(output_folder_path, exist_ok=True)

    '''Load en-US data for reference'''
    en_us_file_path = os.path.join(input_folder_path, "en-US.jsonl")
    en_us_data = load_en_us_data(en_us_file_path)

    '''Iterate through all JSONL files in the input folder'''
    for filename in os.listdir(input_folder_path):
        if filename.endswith(".jsonl") and filename != "en-US.jsonl":
            file_path = os.path.join(input_folder_path, filename)
            data_by_language = extract_data_from_jsonl(file_path, en_us_data)

            '''Create Excel files for each language'''
            for language, data in data_by_language.items():
                create_excel_file(language, data, output_folder_path)

if __name__ == '__main__':
    main()
