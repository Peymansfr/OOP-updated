class Song:
    def __init__(self, name, author, director, writer, genre, year):
        self.name = name
        self.author = author
        self.director = director
        self.writer = writer
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"{self.author}: {self.name} {self.year} \n The genre of the song {self.name} is {self.genre}"

