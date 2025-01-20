from pprint import pprint

import requests
from threading import Thread
import queue
all_songs = []

# www.example.com/search?q=some_query&type=music&genre=classic

ACCESS_TOKEN = '221D0eyK7BV5RwDXXCQglRlwVMULwYyNbOtDhN4TuoMAQWmhvfxfkiu4RgUA34BK'
RANDOM_GENERE_API_URL = 'https://binaryjazz.us/wp-json/generator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

class GetGenre(Thread):

    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        genre = requests.get(RANDOM_GENERE_API_URL).json()
        self.queue.put(genre)

class Genius(Thread):

    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        genre = self.queue.get()
        data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
        data = data.json()
        try:
            song_id = data['response']['hits'][0]['result']['api_path']
            all_songs.append(f'{GENIUS_URL}{song_id}/apple_music_player')
        except IndexError as ie:
            self.run()

queue = queue.Queue()

genre_list = []
genius_list = []

for _ in range(5):
    t = GetGenre(queue)
    t.start()
    genre_list.append(t)

for _ in range(5):
    t = Genius(queue)
    t.start()
    genius_list.append(t)

for t in genius_list:
    t.join()

print(all_songs)
print(len(all_songs))