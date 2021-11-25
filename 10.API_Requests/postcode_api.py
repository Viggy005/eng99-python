import requests
from pprint import pprint #pprint is prettyprint
import json
# # GET METHOD
# postcode_req = requests.get(
#     "https://api.postcodes.io/postcodes/nr22nq"
# )
# print(postcode_req)
# if postcode_req.status_code == 200:
#     print(postcode_req.headers)
#     pprint(postcode_req.json(),sort_dicts = False)
#     print(type(postcode_req.json()))
#     print(postcode_req.content)
#     print(type(postcode_req.content))
#     postcode = postcode_req.json()["result"]
#
#
# #print the eastings and northings of the requested post code
#     print(postcode["eastings"])
#     print(postcode["northings"])
#
# #POST METHOD
#
#
# #HTTP Request
#
# #verb - URL - Version
#
# # Header - key-value pairs(meta data)
# #Body - text / json
#
# #http Response
#
# # Response code(eg 200/404)
# #HTTP VERSION
# #Headers
# #BODY

# POST Method

postcode_headers = {"Content-Type": "application/json"}
json_data = {
    "postcodes": ["nr22nq", "m456gn", "ex165bl"]
}
multi_req = requests.post(
    "https://api.postcodes.io/postcodes",
    headers=postcode_headers,
    #data=json.dumps(json_data)
    json=json_data
)
print(multi_req)
postcodes = multi_req.json()
print(postcodes)
print(type(postcodes))

#for postcode in list(postcodes):
#    print(f"<{postcode['result']['result']['postcode']}> - Latitude : {postcode['result']['result']['latitude']} - Longitude : {postcode['result']['result']['longitude']} ")
for res in postcodes["result"]:
    print(f"<{res['result']['postcode']}> - Latitude : {res['result']['latitude']} - Longitude : {res['result']['longitude']} ")


# Create a postcode class
# that can hold data lat and long and easting/ northings
# for a single postcode
#metod that is called in the __init__, which takes a postcode string and makes the API call
