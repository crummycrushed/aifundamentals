import json

data = {
"employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]
}

with open("data.json", "w", newline="\n") as f:
    json.dump(data, f)


# dump this dict data into the open file f as json 


with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)