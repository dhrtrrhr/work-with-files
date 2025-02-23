import json
with open ("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    print(loaded_data)
