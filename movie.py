# FREEZE CODE BEGIN
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"
# FREEZE CODE END


def main():
    title = input()
    director = input()
    year = input()

    movie = Movie(title, director, year)
    print(movie)


# FREEZE CODE BEGIN
if __name__ == "__main__":
    # --- Main Program ---
    main()
# FREEZE CODE END