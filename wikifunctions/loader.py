# wikifunctions/loader.py

import requests
import json

class WikiFunctionLoader:
    def __init__(self, function_id):
        self.function_id = function_id
        self.impl = None
        self.desc = None
        self._fetch_function()

    def _fetch_function(self):
        url = f"https://www.wikifunctions.org/w/api.php?action=wikilambda_fetch&format=json&zids={self.function_id}&formatversion=2"
        response = requests.get(url)
        func = response.json()
        self.impl = json.loads(func[self.function_id]["wikilambda_fetch"])["Z2K2"]["Z14K3"]["Z16K2"]
        self.desc = json.loads(func[self.function_id]["wikilambda_fetch"])["Z2K2"]["Z14K1"]

    def execute_function(self, *args, **kwargs):
        exec(self.impl)
        return Z12526(*args, **kwargs)

    def fetch_description(self):
        url = f"https://www.wikifunctions.org/w/api.php?action=wikilambda_fetch&format=json&zids={self.desc}&formatversion=2"
        response = requests.get(url)
        func = response.json()
        return json.loads(func[self.desc]["wikilambda_fetch"])["Z2K2"]["Z8K1"][1]["Z17K3"]["Z12K1"][1]["Z11K2"]

