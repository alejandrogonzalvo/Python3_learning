import json

mydict = {
    "key 1": "Value 1",
    "key 2": "Value 2",
    "decimal": 100,
    "boolean": False,
    "list": [1, 2, 3],
    "dict": {
        "child key 1": "value 1",
        "child key 2": "value 2"
    }
}

with open("prueba.json", "w") as f_obj:
    json.dump(mydict,f_obj, indent=4)
print(json.dumps(mydict, indent=4))