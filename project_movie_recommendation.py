#Python has a built-in module that you can use to make random numbers.
import random

# Dictionary of movies categorized by genres
movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "The Dark Knight", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Hangover", "Dumb and Dumber", "21 Jump Street"],
    "Sci-Fi": ["Inception", "The Matrix", "Interstellar", "Blade Runner 2049", "Arrival"],
    "Horror": ["The Conjuring", "A Nightmare on Elm Street", "It", "The Exorcist", "Hereditary"],
    "Drama":  ["Forrest Gump", "The Shawshank Redemption", "Fight Club", "The Godfather", "Good Will Hunting"],
    "Romance":["The Notebook", "Titanic", "Pride and Prejudice", "La La Land", "Crazy Rich Asians"]
}

def suggest_movie():
    print("\n Welcome to the Movie Suggestion Bot!")
    
    while True:
        # Display available genres
        # The join() method takes all items in an iterable and joins them into one string.
        print("\nAvailable genres: " + ", ".join(movies))
        
        # Get user choice
        genre = input("\nEnter a genre to get a movie recommendation (or type 'exit' to quit): ").strip().title()
        
        if genre.lower() == 'exit':
            print("\n Thank you for using the Movie Suggestion Bot! Enjoy your movie! ")
            break  # Exit the loop
        
        #  Check if genre exists
        if genre in movies:
            #   Pick a random movie from the selected genre using choice function
            #   The choice() method returns a randomly selected element from the specified sequence.
            #   The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
            movie = random.choice(movies[genre])
            print(f"\n Recommended Movie for {genre}: **{movie}** ")
        else:
            print(" Invalid genre! Please choose from the available genres.")

#  Run the movie suggestion bot
suggest_movie()
