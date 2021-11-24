dic1 = {"Title": "Iron_man",
  "Lead_actor": "Robert",
  "Budget": "120_million",
  "Box_office": "600 million",
  "rating": {"IMDB": 7, "rotten": 5},
  "rating1": 3,
  "perfect": True,
  "flaws": None
}

dic2 = dic1["rating"]
print(list(dic2.values()))
var1 = "rating1"
print(dic1[var1])