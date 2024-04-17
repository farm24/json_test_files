import requests
import json

jsonx = requests.get("https://raw.githubusercontent.com/farm24/json_test_files/main/test.json")

t = json.loads(jsonx.text)

print(t["test"])
print(t["testb"])