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