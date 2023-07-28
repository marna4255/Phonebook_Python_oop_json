import json

class Contact:
    name = ""
    phone = 0

    def __init__(self, name = "", phone = 0):
        self.name = name
        self.phone = phone

    """converts a Python object into JSON and returns a string"""
    def __str__(self):
        return json.dumps({"name":self.name, "phone":self.phone})
    


