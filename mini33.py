from pytube import YouTube
import json 
import os

class Media:
    def __init__(self, name, director, imdb_score, url, duration, casts):
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts if casts else []

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Director: {self.director}")
        print(f"IMDB Score: {self.imdb_score}/10")
        print(f"Duration: {self.duration} minutes")
        print(f"Casts: {', '.join(self.casts) if self.casts else 'N/A'}")
        print(f"URL: {self.url}")
         
    def download(self):
        try:
            print(f"Attempting to download {self.name}...")
            yt = YouTube(self.url)
            stream = yt.streams.get_highest_resolution()
            if not os.path.exists("downloads"):
                os.makedirs("downloads")
            stream.download(output_path="downloads")
            print(f"Successfully download {self.name} to 'downloads' folder!")
        except Exception as e:
            print(f"Error downloading {self.name}: {e}")

    def to_dict(self):
        return {
            "name": self.name,
            "director": self.director,
            "imdb_score": self.imdb_score,
            "url": self.url,
            "casts": self.casts
        }
    

class Film(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, genre):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.genre = genre

    def show_info(self):
        super().show_info()
        print(f"Genre: {self.genre}")

class Clip(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, length_type):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.length_type = length_type

    def show_info(self):
        super().show_info()
        print(f"Length type: {self.length_type}")

class Series(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, seasons, length_type):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.seasons = seasons
        self.length_type = length_type

    def show_info(self):
        super().show_info()
        print(f"Number of Seasons: {self.seasons}")
        print(f"Lerngth Type: {self.length_type}")
        
        
class Documentary(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, topic):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.topic = topic

    def show_info(self):
        super().show_info()
        print(f"Topic: {self.topic}")

class Antique(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, release_year, condition):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.release_year = release_year
        self.condition = condition

    def show_info(self):
        super().show_info()
        print(f"Release Year: {self.release_year}")
        print(f"Condition: {self.condition}")

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            "release_year": self.release_year,
            "condition": self.condition
        })
        return base_dict
    

class Actor:
    def __init__(self, name, property, birth_year):
        self.name = name
        self.property = property
        self.birth_year = birth_year

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Property: {self.property}")
        print(f"Birth Year: {self.birth_year}")

class MediaManager:
    def __init__(self):
        self.media_list = []
        self.load_from_file()

    def add_media(self, media):
        self.media_list.append(media)
        self.save_to_file()
        print(f"Added {media.name} to the media list!")

    def remove_media(self, name):
        self.media_list = [m for m in self.media_list if m.name != name]
        self.save_to_file()
        print(f"Remove {name} from the media list!")

    def show_all(self):
        if not self.media_list:
            print("No media items available!")
            return
        for media in self.media_list:
            media.show_info()

    def save_to_file(self):
        if os.path.exists("media_data.json"):
            with open("media_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:

                    media = Media(item["name"], item["director"], item["imdb_score"],
                                  item["url"], item["duration"], item["casts"])
                    self.media_list.append(media)

    def load_from_file(self):
        if os.path.exists("media_data.json"):
            with open("media_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:

                    media = Media(item["name"], item["director"], item["imdb_score"],
                                  item["url"], item["duration"], item["casts"])
                    self.media_list.append(media)

if __name__ == "__main__":

    manager = MediaManager()


    film = Film("Inception", "Christopher Nolan", 8.8, "https://www.youtube.com/watch?v=YoHD9XEInc0", 148,
                ["Leonardo DiCaprio", "Ellen Page"], "Sci-Fi")
    series = Series("Breaking Bad", "Vince Gilligan", 9.5, "https://www.youtube.com/watch?v=HhesaQXLuRY", 60,
                    ["Bryan Cranston", "Aaron Paul"], 5, "long")
    doc = Documentary("Planet Earth", "Alastair Fothergill", 9.4, "https://www.youtube.com/watch?v=XuKdX7ndrA8", 50,
                     ["David Attenborough"], "Nature")
    clip = Clip("Car Chase", "John Doe", 7.2, "https://www.youtube.com/watch?v=dQw4w9WgXcQ", 5,
                ["Tom Cruise"], "Short")
    
    
    manager.add_media(film)
    manager.add_media(series)
    manager.add_media(doc)
    manager.add_media(clip)
    manager.add_media(Antique)


    print("/nAll Media Items:")
    manager.show_all()



    film.download()


    actor = Actor("Leonardo DiCaprio", "Lead Actor", 1974)
    actor.show_info()


    manager.remove_media("Inception")
