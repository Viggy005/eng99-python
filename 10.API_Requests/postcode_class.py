# Create a postcode class
# that can hold data lat and long and easting/ northings
# for a single postcode
#metod that is called in the __init__, which takes a postcode string and makes the API call
import requests
import json
class Postcode:
    def __init__(self,postcode):
        self.postcode_headers = {"Content-Type": "application/json"}
        self.json_data = {
            "postcodes": [postcode]
        }
        self.multi_req = requests.post(
            "https://api.postcodes.io/postcodes",
            headers=self.postcode_headers,
            # data=json.dumps(json_data)
            json=self.json_data
        )


        # self.multi_req = self.multi_req.json()

        if self.multi_req.status_code == 200:
            post_codes = self.multi_req.json()
            for res in post_codes["result"]:
                self.latitude = res['result']['latitude']
                self.longitude = res['result']['longitude']
                self.eastings = res['result']['eastings']
                self.northings = res['result']['northings']
                self.post_code = res['result']['postcode']
        else:
            print("not entered a valid postcode")


norwich = Postcode("nr22nq")
#print(norwich.northings)
#print(norwich.post_codes)
print(norwich.post_code)
print(norwich.latitude)
print(norwich.longitude)
print(norwich.eastings)
print(norwich.northings)

