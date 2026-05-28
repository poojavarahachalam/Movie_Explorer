from fastapi import FastAPI, Body



app = FastAPI()

# -----------------------------
# Dummy Database
# -----------------------------

Movies = [
    {
    "id": 1,
    "movie_name": "Inception",
    "genre": "Sci-Fi",
    "language": "English",
    "rating": 9
},
    {
    "id": 2,
    "movie_name": "The Godfather",
    "genre": "Crime",
    "language": "English",
    "rating": 8.5
},

    {
    "id": 3,
    "movie_name": "Parasite",
    "genre": "Drama",
    "language": "Korean",
    "rating": 8.6
},
    {
    "id": 4,
    "movie_name": "3 Idiots",
    "genre": "Comedy",
    "language": "Hindi",
    "rating": 9.5
},
    {
    "id": 5,
    "movie_name": "Avengers: Endgame",
    "genre": "Action",
    "language": "English",
    "rating": 8.4

},

   {
    "id": 6,
    "movie_name": "The Dark Knight",
    "genre": "Action",
    "language": "English",
    "rating": 9.0
},

    {
    "id": 7,  
    "movie_name": "Interstellar",
    "genre": "Sci-Fi",
    "language": "English",
    "rating": 8.6
},

    {
    "id": 8,
    "movie_name": "The Shawshank Redemption",
    "genre": "Drama",
    "language": "English",
    "rating": 9.3

},

   {
    "id": 9,
    "movie_name": "Pulp Fiction",
    "genre": "Crime",
    "language": "English",
    "rating": 8.9
},

    {
    "id": 10,
    "movie_name": "The Matrix",
    "genre": "Sci-Fi",
    "language": "English",
    "rating": 8.7
}]

# -----------------------------
# Home Route
# -----------------------------


@app.get("/")
def home():


    return {
        "message": "Welcome to Movie Database API!"
    }

# -----------------------------
# Get All Movies
# -----------------------------

@app.get("/movies")

def get_movies():
    return Movies


# -----------------------------
# Get single movie by id
# -----------------------------

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):


    for movie in Movies:


        if movie["id"] == movie_id:


            return {
                "movie": movie
            }


    return {
        "message": "Movie Not Found"
    }

# -----------------------------
# filter movies 
# -----------------------------



@app.post("/searchmovies/filter")

def search_movies(filters: dict = Body()):

    genre = filters.get("genre")
    language = filters.get("language")
    rating = filters.get("rating")

    filtered_movies = Movies


    if genre:
        filtered_movies = [movie for movie in filtered_movies if genre.lower() in movie["genre"].lower()]

    if language:
        filtered_movies = [movie for movie in filtered_movies if language.lower() in movie["language"].lower()]

    if rating:
        filtered_movies = [movie for movie in filtered_movies if float(movie["rating"]) >= float(rating)]

    if not filtered_movies:
        return {
            "message": "Movie Not Found"
        }

    return {
        "filtered_movies": filtered_movies
    }



# -----------------------------
# Add Movie 
# -----------------------------


@app.post("/addmovie")
def add_movie(movie: dict = Body()):


    Movies.append(movie)


    return {
        "message": "Movie Added Successfully",
        "movie": movie
    }


# -----------------------------
# update Movie 
# -----------------------------

@app.put("/updatemovie/{movie_id}")
def update_movie(movie_id: int, updated_data: dict = Body()):


    for movie in Movies:


        if movie["id"] == movie_id:


            movie.update(updated_data)


            return {
                "success": True,
                "message": "Movie Updated Successfully",
                "updated_movie": movie
            }


    return {
        "success": False,
        "message": "Movie Not Found"
    }


# -----------------------------
# delete Movie 
# -----------------------------

@app.delete("/deletemovie/{movie_id}")
def delete_movie(movie_id: int):
    for i in range(len(Movies)):
        if Movies[i]["id"] == movie_id:
            deleted_movie = Movies.pop(i)
            return {
                "success": True,
                "message": "Movie Deleted Successfully",
                "deleted_movie": deleted_movie
            }

    return {
        "success": False,
        "message": "Movie Not Found"
    }








