import json
data = {

    "ім'я": "Влад",
    "Вік": "15",
    "Улюблені предмети": [
        "фізика",
        "хімія"

    ]

}

with open ("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file,ensure_ascii=False, indent=4)
