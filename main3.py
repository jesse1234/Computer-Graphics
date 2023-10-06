import os
import argparse
import json
from functions import create_excel_file, load_en_us_data, extract_data_from_jsonl, zip_excel_files, google_drive_upload

def main():
    parser = argparse.ArgumentParser(description='Convert JSONL files to Excel files by language')
    parser.add_argument('--input-folder', required=True, help='Path to the folder containing JSONL files')
    parser.add_argument('--output-folder', required=True, help='Path to the folder where Excel files will be saved')
    args = parser.parse_args()

    '''These are the input and output folder paths'''
    input_folder_path = args.input_folder
    output_folder_path = args.output_folder
    input_excel_path = args.input_folder
    output_zip_path = args.output_folder
    os.makedirs(output_folder_path, exist_ok=True)
    os.makedirs(output_zip_path, exist_ok=True)

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

                input_excel_path = "output_excel_files"
    zip_file_name = "output.zip"

    zip_excel_files(input_excel_path, output_zip_path, zip_file_name)

    ''' Post the zip file to Google Drive '''
    access_token = "ya29.a0AfB_byBKVEKCr0LYnhK9dg9Av0ZsTKgYaGWsaTQ7MSdiI4v9FpdciAODAD-emsAqq_yFlWnHgu7tMdLrXXRT_5j5YYMXP6C92WpaNU9Sage2DpvG3UsEw7CRNsKMllwyVW3fZaEofazE9c1guHAlPKO8ABiwU7j2ir6AaCgYKAWcSARISFQGOcNnCI68Urgw2tjP5KF71p7Ah4w0171"
    upload_file_path = "output_excel_files/output.zip"
    output_file_name = "files.zip"
    
    file_id = google_drive_upload(access_token, upload_file_path, output_file_name)
    
    if file_id:
        print("Zip file uploaded to Google Drive")
    else:
        print("Zip file not uploaded to Google Drive")  

if __name__ == '__main__':
    main()
