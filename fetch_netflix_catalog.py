import requests
import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")


genre_url = "https://api.themoviedb.org/3/genre/movie/list"
genre_response = requests.get(genre_url, params={"api_key": API_KEY})
genre_data = genre_response.json()


genre_map = {}
for genre in genre_data["genres"]:
    genre_map[genre["id"]] = genre["name"]

print("Genre map sample:", genre_map)


url = "https://api.themoviedb.org/3/discover/movie"
all_movies = []   # this empty list will hold every movie we collect

for page in range(1, 228):   # 227 pages total, based on what TMDB told us
    params = {
        "api_key": API_KEY,
        "with_watch_providers": 8,
        "watch_region": "IN",
        "sort_by": "popularity.desc",
        "page": page
    }

    response = requests.get(url, params=params)
    data = response.json()

    for movie in data["results"]:
        genre_names = [genre_map.get(g, "") for g in movie["genre_ids"]]

        all_movies.append({
            "title": movie["title"],
            "genres": ", ".join(genre_names),
            "release_date": movie.get("release_date"),
            "rating": movie.get("vote_average"),
            "popularity": movie.get("popularity"),
        })

    print(f"Finished page {page}")
    time.sleep(0.3)   # small pause so we don't hammer the API too fast

print("Total movies collected:", len(all_movies))
print("Sample movie:", all_movies[0])

df = pd.DataFrame(all_movies)
df.to_csv("netflix_movies.csv", index=False)
print("saved to netflix_movies.csv")

tv_genre_url = "https://api.themoviedb.org/3/genre/tv/list"
tv_genre_response = requests.get(tv_genre_url, params={"api_key": API_KEY})
tv_genre_data = tv_genre_response.json()

tv_genre_map ={}
for genre in tv_genre_data["genres"]:
    tv_genre_map[genre["id"]] = genre["name"]

tv_url = "https://api.themoviedb.org/3/discover/tv"
all_tv_shows = []

for page in range(1, 228):
    params = {
        "api_key": API_KEY,
        "with_watch_providers": 8,
        "watch_region": "IN",
        "sort_by": "popularity.desc",
        "page": page
    }

    response = requests.get(tv_url, params=params)
    data = response.json()

    if data.get("results") is None:
        break
    for show in data["results"]:
        genre_names = [tv_genre_map.get(g, "") for g in show["genre_ids"]]

        all_tv_shows.append({
            "title": show["name"],
            "genres":", ".join(genre_names),
            "release_date":show.get("first_air_date"),
            "rating": show.get("vote_average"),
            "popularity": show.get("popularity"),
        })

    print(f"Finished TV page {page}")
    time.sleep(0.3)

print("Total TV shows collected", len(all_tv_shows))

df_tv = pd.DataFrame(all_tv_shows)
df_tv.to_csv("netflix_tv_shows.csv", index=False)
print("saved to netflix_tv_shows.csv")


df_movies = pd.read_csv("netflix_movies.csv")
df_tv = pd.read_csv("netflix_tv_shows.csv")

df_movies["type"] = "Movie"
df_tv["type"] = "TV Shows"

df_combined = pd.concat([df_movies, df_tv], ignore_index=True)

df_combined.to_csv("netflix_full_catalog.csv", index=False)
print("combined dataset saved:", df_combined.shape)