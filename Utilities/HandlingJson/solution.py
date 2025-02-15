import json

# Convert json to object

json_string = """
{
    "items" : [
        {
            "id": "ALPHA"
        },
        {
            "id": "BRAVO"
        }
    ]
}
"""

data_from_json = json.loads(json_string)
print(data_from_json)

# Convert object to json

class Data(object):

    def __init__(self):
        self.items = [{"id": "ALPHA"}, {"id": "BRAVO"}]

data = Data()

json_from_data = json.dumps(data.__dict__)
print(json_from_data)