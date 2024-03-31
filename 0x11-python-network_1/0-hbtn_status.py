#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) = response:
    body = response.read().decode('utf-8')

print("- Body response:")
print("\t- type_", type(body))
print("\t- content:", body)
