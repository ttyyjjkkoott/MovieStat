import requests

def get_movie_data(movie_title):
    # Define the base URL of the OMDb API
    base_url = "http://www.omdbapi.com/"

    # Define the API key
    api_key = "secret"

    # Define the parameters for the API request
    params = {
        "apikey": api_key,
        "t": movie_title
    }

    # Send a GET request to the OMDb API
    response = requests.get(base_url, params=params)

    # Convert the response to JSON
    data = response.json()

    return data

def get_movie_review(movie_data):
    # Extract the IMDb rating from the movie data
    imdb_rating = movie_data.get("imdbRating")

    # Generate a review based on the IMDb rating
    if imdb_rating is None:
        return "No reviews found for this movie."
    elif float(imdb_rating) > 7.5:
        return "This movie is highly recommended."
    elif float(imdb_rating) > 5.0:
        return "This movie is somewhat recommended."
    else:
        return "This movie is not recommended."

if __name__ == "__main__":
    # Get the movie title from the user
    movie_title = input("Please enter a movie title: ")

    # Get the movie data from the OMDb API
    movie_data = get_movie_data(movie_title)

    # Generate a review based on the movie data
    review = get_movie_review(movie_data)

    # Define the keys of the data you're interested in
    keys = ["Title", "Year", "Rated", "Released", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot", "Language", "Country", "Awards", "Metascore", "imdbRating", "BoxOffice", "Production"]

    # Print the movie data and the review
    print(f"Movie Data for '{movie_title}':\n")
    for key in keys:
        print(f"{key}: {movie_data.get(key, 'N/A')}")
    print(f"\nReview: {review}")
