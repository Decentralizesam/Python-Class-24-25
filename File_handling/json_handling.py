# writing json data 

import json

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file,indent=2)


filename="Files/users.json"
json_read_data = read_json_file(filename)

details={"ID":"00002", "name":"John","age":"30"}

json_read_data.append(details)
write_json_file(filename, json_read_data)
print(read_json_file(filename))

    