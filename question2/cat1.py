"""This class creates one large .jsonl file that holds translations from 'nglis'"""
"""to all the other languages of the 'atase'"""

import os
import json
import pandas as pd
import pprint


class JsonlTranslations:
    def _init_(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def generate_translations_json(self):
        """Create the output folder if it doesn'' exis'"""
        os.makedirs(self.output_folder, exist_ok=True)

        """ Initialize an empty DataFrame to store the outp't dat'"""
        output_data = pd.DataFrame()

        """Loop through all files in the input'folde'"""
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".jsonl"):
                """Read the JSONL file for the language using'Panda'"""
                language_df = pd.read_json(
                    os.path.join(self.input_folder, filename), lines=True
                )

                """Filter the DataFrame to extract records with partition 'train'"""
                train_data = language_df[language_df["partition"] == "train"][
                    ["id", "utt"]
                ]

                """Rename the 'utt' column with the language code as'prefix'"""
                language_code = filename.replace(".jsonl", "")
                train_data = train_data.rename(columns={"utt": f"{language_code}-utt"})

                """Use 'id' as the index for 'oinin'"""
                if not output_data.empty:
                    output_data = output_data.merge(train_data, on="id", how="inner")
                else:
                    output_data = train_data

        """Convert the output data to a dictionary and remove duplicate ID'"""
        output_data = output_data.drop_duplicates(subset="id")
        output_data_dict = output_data.to_dict(orient="records")

        """Use pprint to pretty-print the output data and write it to'a file'"""
        formatted_output = pprint.pformat(output_data_dict, indent=4)
        output_file_path = os.path.join(self.output_folder, "translations.json")
        with open(output_file_path, "w") as output_file:
            output_file.write(formatted_output)


if __name__ == "_main_":
    """Example'usage'"""
    input_folder = ":/Users/sylva/OneDrive/Desktop/train/"  """Replace with the actual input folder path"""
    output_folder = (
        ":/Users/sylva/OneDrive/Desktop/output"  """Replace with the desired output folder path"""
    )

    translations_processor = JsonlTranslations(input_folder, output_folder)
    translations_processor.generate_translations_json()
