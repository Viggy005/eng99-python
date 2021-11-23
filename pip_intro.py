#PIP
#pip
#Installs
#Packages

import requests

request_bbc = requests.get("https://www.bbc.co.uk") # get command for API

print(request_bbc, type(request_bbc), repr(request_bbc))
print(request_bbc.status_code)
print(request_bbc.headers)
print(request_bbc.content)

