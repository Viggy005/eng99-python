# d = {
#     "course": "engineering 99",
#     "stream": "Devops",
#     "number of trainers": 11
#      }
# print(d, type(d))
# print(d["stream"])
# print(d.get("number of trainers"))
# d.update({"stream":"date eng"})
# print(d)
# d["new"]= 5
# print(d)

# create a dictionary for your fav film

Iron_Man = {
    "Title": "Iron Man",
    "Lead_actor":"Robert",
    "budget":"140 Million USD",
    "IMDB":7.9,
    "director":"Jon Favreau"
    }
print(Iron_Man)
Iron_Man["Box Office"]= "585 Million USD"
print(Iron_Man)
Iron_Man.update({"Production House":"Marvel"})
print(Iron_Man)
print(Iron_Man.get("budget"))
print(Iron_Man.get("Budget"))
print(Iron_Man["Lead_actor"])
Iron_Man["main_cast"] = ["robert","pepper","jarwiz"]
print(Iron_Man.get("main cast"))
print(Iron_Man.pop("budget"))
print(Iron_Man["main"
               "qcast"])
