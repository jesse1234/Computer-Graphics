import os
import pandas as pd
import json
import requests
from zipfile import ZipFile


'''Define a function to create Excel files'''
def create_excel_file(language, data, output_folder_path):
    '''Create a DataFrame from the data'''
    df = pd.DataFrame(data)

    '''Output Excel file path'''
    output_file_path = os.path.join(output_folder_path, f"en-{language}.xlsx")

    '''Create an Excel writer'''
    excel_writer = pd.ExcelWriter(output_file_path, engine="openpyxl")

    '''Write DataFrame to the Excel file'''
    df.to_excel(excel_writer, index=False)

    '''Save the Excel file'''
    excel_writer._save()


''' This function reads from the en-US file and extracts id, utt, annot_utt'''
def load_en_us_data(en_us_file_path):
    en_us_data = {}
    with open(en_us_file_path, "r", encoding="utf-8") as en_us_file:
        for line in en_us_file:
            data = json.loads(line)
            en_us_data[data["id"]] = {
                "utt_en-US": data["utt"],
                "annot_utt_en-US": data["annot_utt"]
            }
    return en_us_data


'''Iterates through all the files in the input folder and extracts data, defining the language using locale'''
def extract_data_from_jsonl(file_path, en_us_data):
    data_by_language = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data = json.loads(line)
            language = data["locale"].split("-")[-1]
            if language not in data_by_language:
                data_by_language[language] = []
            id_value = data["id"]
            simplified_data = {
                "id": id_value,
                f"utt_{language}": data["utt"],
                f"annot_utt_{language}": data["annot_utt"],
            }
            if id_value in en_us_data:
                simplified_data.update(en_us_data[id_value])
            data_by_language[language].append(simplified_data)

    return data_by_language

def zip_excel_files(input_excel_path, output_zip_path, zip_file_name):
    zip_file_path = os.path.join(output_zip_path, zip_file_name)

    ''' Get a list of all the Excel files in the input folder '''
    excel_files = [os.path.join(input_excel_path, file) for file in os.listdir(input_excel_path) if file.endswith(".xlsx")]

    ''' Create a ZipFile object and add the Excel files to it '''
    with ZipFile(zip_file_path, "w") as zip_object:
        for file in excel_files:
            zip_object.write(file, os.path.basename(file))

    ''' Check if the zip file was created '''
    if os.path.exists(zip_file_path):
        print("ZIP file created")
    else:
        print("ZIP file not created")

def google_drive_upload(access_token, upload_file_path, output_file_name):
    headers = {"Authorization": f"Bearer {access_token}"}
    url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"

    files = {"data": ("metadata", json.dumps({"name": output_file_name}), "application/json; charset=UTF-8"),
             "file": ("application/zip", open(upload_file_path, "rb"))}

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        print("File uploaded successfully!")
    else:
        print("Error uploading file.")        

      