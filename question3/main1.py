# this code was run in google collab
#!pip install jsonlines"
import jsonlines
import json
from google.colab import files

# Upload the three JSONL files: en_data.jsonl, sw_data.jsonl, de_data.jsonl
uploaded = files.upload()

# Initialize a dictionary to store translations
translations = {}

# Process English data
if 'english-train.jsonl' in uploaded:
    with jsonlines.Reader(uploaded['english-train.jsonl']) as reader:
        english_data = list(reader)

    for entry in english_data:
        id = entry['id']
        utt = entry['utt']
        translations[id] = {'en': utt, 'translations': {}}

# Process Swahili data
if 'swahili-train.jsonl' in uploaded:
    with jsonlines.Reader(uploaded['swahili-train.jsonl']) as reader:
        swahili_data = list(reader)

    for entry in swahili_data:
        id = entry['id']
        utt = entry['utt']
        if id in translations:
            translations[id]['translations']['sw'] = utt

# Process German data
if 'german-train.jsonl' in uploaded:
    with jsonlines.Reader(uploaded['german-train.jsonl']) as reader:
        german_data = list(reader)

    for entry in german_data:
        id = entry['id']
        utt = entry['utt']
        if id in translations:
            translations[id]['translations']['ge'] = utt

# Save the combined translations to a single JSON file
with open('combined_translations.json', 'w', encoding='utf-8') as json_file:
    json.dump(translations, json_file, ensure_ascii=False, indent=4)
