import streamlit as st

import requests


API_URL = "https://movie-backend-cbzb.onrender.com"


st.title("🎥🍿 Movie Explorer")
st.write("Welcome to the Movie Explorer!")    



# -----------------------------
# Sidebar Menu
# -----------------------------


menu = st.sidebar.selectbox(
    "Select Option",
    [

        "Choose an Option",
        "View All Movies",
        "Search or Filter Movies",
        "Add New Movie",
        "Update Movie",
        "Delete Movie"
    ]
)


if menu == "Choose an Option":
    st.info("Please select an option from the sidebar.")

# -----------------------------
# View All Movies
# -----------------------------

elif menu == "View All Movies":
    st.header("All Movies")
    response = requests.get(f"{API_URL}/movies")
    Movies = response.json()
    

    if Movies:
        st.success(f"Successfully loaded {len(Movies)} movies!")
        st.write("---")
        for movie in Movies:
            with st.container():
                col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                
                
                with col1:
                    st.markdown(f"### 🎥 {movie.get('movie_name', 'N/A')}")

                with col2:
                    st.markdown(f"**Genre:**\n{movie.get('genre', 'N/A')}")

                with col3:
                    st.markdown(f"**Language:**\n{movie.get('language', 'N/A')}")

                with col4:
                    st.markdown(f"**Rating:**\n⭐ {movie.get('rating', 'N/A')}")

                st.write("---")

    else:
        st.info("The database is currently empty. No movies found!")



# -----------------------------
# Search or Filter Movies
# -----------------------------

elif menu == "Search or Filter Movies":
    st.header("Search or Filter Movies")

    with st.form(key="search_filter_form"):
        Genre = st.selectbox("Genre", ["Action", "Crime", "Comedy", "Drama", "Horror", "Sci-Fi"])
        Language = st.selectbox("Language", ["English", "Hindi", "Telugu", "Korean"])
        rating = st.slider("Rating", min_value=1, max_value=10)

        submit_button = st.form_submit_button(label="Search Movies")

    if submit_button:
        search_criteria = {
            "genre": Genre,
            "language": Language,
            "rating": rating
        }


        response = requests.post(
            f"{API_URL}/searchmovies/filter",
            json=search_criteria
            )

        if response.status_code == 200:
            data = response.json()
            
            if "filtered_movies" in data:
                movies = data["filtered_movies"]
                st.success("Movies found successfully!")
                
                for movie in movies:
                    with st.container():
                        col1, col2, col3, col4 = st.columns([2,1,1,1])
                        
                        with col1:
                            st.markdown(f"### 🎥 {movie.get('movie_name')}")

                        with col2:
                            st.markdown(f"**Genre:** {movie.get('genre')}")

                        with col3:
                            st.markdown(f"**Language:** {movie.get('language')}")

                        with col4:
                            st.markdown(f"⭐ {movie.get('rating')}")

                        st.write("---")

            else:
                st.error("Movie Not Found")

# -----------------------------
# adding a movie
# -----------------------------



elif menu == "Add New Movie":
    st.header("Add a New Movie")
    with st.form(key="add_movie_form"):
        Movie_id = st.number_input("Movie ID", min_value=1, step=1)
        Movie_name = st.text_input("Movie_name")
        genre = st.selectbox("Genre", ["Action", "Crime", "Comedy", "Drama", "Horror", "Sci-Fi"])
        language = st.selectbox("Language", ["English", "Hindi", "Telugu", "Korean"])
        rating = st.slider("Rating", min_value=1, max_value=10)

        submit_button = st.form_submit_button(label="Add Movie")

    if submit_button:
        new_movie = {
            "id": Movie_id,
            "movie_name": Movie_name,
            "genre": genre,
            "language": language,
            "rating": rating
        }


        response = requests.post(
            f"{API_URL}/addmovie",
            json=new_movie
        )

        data = response.json()
        
        if data["success"]:
            st.success(f"Movie '{Movie_name}' added successfully!")
        
        else:
            st.error(data["message"])


# -----------------------------
# updating a movie
# -----------------------------

elif menu == "Update Movie":
    st.header("Update a Movie")
    with st.form(key="update_movie_form"):
        Movie_id = st.number_input("Movie ID", min_value=1, step=1)
        Movie_name = st.text_input("Movie_name")
        genre = st.selectbox("Genre", ["Action", "Crime", "Comedy", "Drama", "Horror", "Sci-Fi"])
        language = st.selectbox("Language", ["English", "Hindi", "Telugu", "Korean"])
        rating = st.slider("Rating", min_value=1, max_value=10)

        submit_button = st.form_submit_button(label="Update Movie")

    if submit_button:
        update_movie = {
            "movie_name": Movie_name,
            "genre": genre,
            "language": language,
            "rating": rating
        }
        


        response = requests.put(
            f"{API_URL}/updatemovie/{Movie_id}",
            json=update_movie
            )

        data = response.json()
        
        if data["success"]:
            st.success(f"Movie '{Movie_name}' updated successfully!")

        else:
            st.error(data["message"])


# -----------------------------
# delete a movie
# -----------------------------

elif menu == "Delete Movie":
    st.header("Delete a Movie")

    with st.form(key="delete_movie_form"):
        Movie_id = st.number_input("Movie ID", min_value=1, step=1)

        submit_button = st.form_submit_button(label="Delete Movie")

    if submit_button:
        response = requests.delete(
            f"{API_URL}/deletemovie/{Movie_id}"
            )
        
        data = response.json()
        
        if data["success"]:
            st.success(f"Movie id '{Movie_id}' deleted successfully!")

        else:
            st.error(data["message"])


