#!/bin/bash

# Set the paths to your input JSONL files and output Excel file
INPUT_JSONL_DIR="1.1/data"
OUTPUT_EXCEL_FOLDER="output_excel_files"

# Set the Python script file name
PYTHON_SCRIPT="main3.py"

# Run the Python script with the appropriate flags and parameters
python $PYTHON_SCRIPT --input-folder $INPUT_JSONL_DIR --output-folder $OUTPUT_EXCEL_FOLDER

# Optionally, you can add more commands or post-processing steps here if needed

