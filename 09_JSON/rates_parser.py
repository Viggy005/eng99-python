import json

class RatesParser:
    def __init__(self,file_path):
        file_path = file_path
        exchange_dic = self.open_json_file(file_path)
        self.Base = exchange_dic.get("base")
        self.date = exchange_dic.get("date")
        self.GBP = exchange_dic["rates"]["GBP"]
        self.USD = exchange_dic["rates"]["USD"]
        self.AUD = exchange_dic["rates"]["AUD"]
        self.rates = exchange_dic["rates"]
    def open_json_file(self,file_path) -> dict:
        with open(file_path) as exchange_file:
            return json.load(exchange_file)

    def convert(self,currency_wanted,value_in_euro):
        if currency_wanted in list(self.rates):
            return f"you will get {self.rates[currency_wanted] * value_in_euro} in {currency_wanted}"
        else:
            return f"we don't have the currency({currency_wanted}) you are looking for"




obj1 = RatesParser("exchange_rates.json")
print(obj1.Base)
print(obj1.GBP)
print(obj1.USD)
print(obj1.AUD)
print(obj1.rates)
print(type(obj1.rates))
print(obj1.convert("ZAR",20))
print(obj1.convert("TAR",20))

#on initialisation, read in a provided filepath
# Base,date, BGP, USD, AUD rates
# eg self.gbp = <0.8937>
#method called convert
#takes in a string corresponding to a currency
# takes in a value (euro)
#retun value in other curency
#think about how to handel currency not in json file
