import pandas as pd
import json
import os

output_folder_path = "output_excel_files"

'''Define a function to create Excel files'''
def create_excel_file(language, data):
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