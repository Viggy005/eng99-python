import json

with open("demo.json") as jsonfile:
    read_file = jsonfile.read() # gives us a string not very usefull
    print(read_file, type(read_file))
    # demo =json.load(jsonfile)
    # print(demo)
    # print(type(demo))
    # print(demo["objects"]["key"])
    demo = json.loads(read_file) # loads convert json string document into a python dictionary
    print(demo)
    print(type(demo))
    print(demo["objects"]["key"])

#create a python dict
# with information about
#your favourite film / TV series
film = {
    "Title":"Iron_man",
    "Lead_actor":"Robert",
    "Budget":"120_million",
    "Box_office":"600 million",
    "rating": {
        "IMDB": 7,
        "rotten": 0.87
    },
    "perfect": True,
    "flaws": None
}
# film_json_string = json.dumps(film)
# print(film_json_string)
# print(type(film_json_string))
#
# with open("shrek.json","w") as shrekfile:
#     shrekfile.write(film_json_string)
# print(film)
# film["Title"] ="Iron_man_2"
# print(film)
# film["Iron_man_2"]= "title"
# print(film)
# film.pop("Iron_man_2")
# print(film)
# film.pop("Title")
# print(film)

with open("shrek2.json","w") as shrekfile:
    json.dump(film,shrekfile)

