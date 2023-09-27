import pandas as pd
import json

with open(
    r"C:\Users\user\Documents\1.University\Computer_Graphics\de-DE.jsonl", "r"
) as file:
    train = json.load(file)

from sklearn.model_selection import train_test_split

with open("file_name") as f:
    lines = f.readlines()

train, test = train_test_split(lines, test_size=0.3)
val, test = train_test_split(test, test_size=0.5)
