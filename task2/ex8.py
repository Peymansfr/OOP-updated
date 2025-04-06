def movies_of_genre(movies: list, genre: str):
    return [movie for movie in movies if movie['genre'] == genre]

print("Movies in the action genre:")
john_woo = movie("A Better Tomorrow", "John Woo", "action", 1986)

movies_of_genre(movies, "action")
for movie in movies_of_genre(movies, "action"):
    print(f"{movie['director']}: {movie['name']}")