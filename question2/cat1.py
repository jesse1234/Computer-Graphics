import pandas as pd
import json

# german
with open(
    r"C:\Users\user\Documents\1.University\Computer_Graphics\de-DE.jsonl", "r"
) as json_file:
    json_german = list(json_file)

from sklearn.model_selection import train_test_split

german_train, test1 = train_test_split(json_german, test_size=0.3)
german_dev, german_test = train_test_split(test1, test_size=0.5)

# german test jsonl
with open("german-test.jsonl", "w") as f:
    for item in german_test:
        f.write(json.dumps(item) + "\n")

# german train jsonl
with open("german-train.jsonl", "w") as f:
    for item in german_train:
        f.write(json.dumps(item) + "\n")

# german dev jsonl
with open("german-dev.jsonl", "w") as f:
    for item in german_dev:
        f.write(json.dumps(item) + "\n")


# english
with open(
    r"C:\Users\user\Documents\1.University\Computer_Graphics\en-US.jsonl", "r"
) as json_file:
    json_english = list(json_file)

from sklearn.model_selection import train_test_split

english_train, test2 = train_test_split(json_english, test_size=0.3)
english_dev, english_test = train_test_split(test2, test_size=0.5)

# english test jsonl
with open("english-test.jsonl", "w") as f:
    for item in english_test:
        f.write(json.dumps(item) + "\n")

# english train jsonl
with open("english-train.jsonl", "w") as f:
    for item in english_train:
        f.write(json.dumps(item) + "\n")

# english dev jsonl
with open("english-dev.jsonl", "w") as f:
    for item in english_dev:
        f.write(json.dumps(item) + "\n")


# swahili
with open(
    r"C:\Users\user\Documents\1.University\Computer_Graphics\sw-KE.jsonl", "r"
) as json_file:
    json_swahili = list(json_file)

from sklearn.model_selection import train_test_split

swahili_train, test3 = train_test_split(json_swahili, test_size=0.3)
swahili_dev, swahili_test = train_test_split(test3, test_size=0.5)

# swahili test jsonl
with open("swahili-test.jsonl", "w") as f:
    for item in swahili_test:
        f.write(json.dumps(item) + "\n")

# swahili train jsonl
with open("swahili-train.jsonl", "w") as f:
    for item in swahili_train:
        f.write(json.dumps(item) + "\n")

# swahili dev jsonl
with open("swahili-dev.jsonl", "w") as f:
    for item in swahili_dev:
        f.write(json.dumps(item) + "\n")
