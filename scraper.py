import re
import sys

import requests

url = sys.argv[1]

response = requests.get(url)
match = re.search(r'[a-zA-Z0-9_.+-]+@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}', response.text)
print(match.group(0))