import json

class Film:

    def __init__(self,filepath):
        filepath = filepath
        film_info = self.open_json_file(filepath)
        self.title = film_info.get("Title")
        self.year = film_info.get("Lead_actor")
        self.ratings = film_info.get("rating")

    def open_json_file(self,filepath : str) -> dict:
        with open(filepath) as film_file:
            return json.load(film_file)

    def get_avergae_rating(self)-> float:
        #return (self.ratings["IMDB"]+self.ratings["rotten"]) /2
        temp_list = list(self.ratings.values())
        avg = 0
        for no in range(len(temp_list)):
            avg += temp_list[no]
        return avg/len(temp_list)



shrek = Film("shrek.json")

print(shrek.title)
print(shrek.year)

print(shrek.get_avergae_rating())
