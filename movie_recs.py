import requests

API_KEY = "42c6c7b7"
URL = "https://www.omdbapi.com/"

'''Getting details of movies using API KEY'''
def movie_details(title):
    params = {
        'apikey': API_KEY,
        'title': title
    }
    response = requests.get(URL, params=params)
    data = response.json() #assigning response from api request to variable
    return data

'''Getting movies based on keywords (genre, etc.)'''
def get_recs(keyword):
    params = {
        'apikey': API_KEY,
        'key': keyword
    }
    response = requests.get(URL, params=params)
    data = response.json()
    return data.get("Search", [])

'''Formatting movie details'''
def movie_info(data):
    if data.get("Response") == "FALSE" or not data:
        print("\n Movie was not found")
        return False
    
    print(f"\n Title: {data['Title']} ({data['Year']})")
    print(f"\n IMDb Rating: {data['imdbRating']}")
    print(f"\n Genre: {data['Genre']}")
    
    
def main():
    print("Welcome to Movie Recs!")
    title = input("Enter a movie title: ").strip()
    
    movie_data = movie_details(title)
    #Debug step for API Response
    print("DEBUG = movie_data = ", movie_data)
    
    found = movie_info(movie_data)
    
    if not found:
        return 
    
    #Pick genre for recs
    genre = movie_data["Genre"].split(",")[0]
    recs = get_recs(genre) #list of genre titles
    
    if not recs:
        print("No recs found :(")
        
    print("Recommended Movies: ")
    for movie in recs[:3]:
        print(f"* {movie['Title']} ({movie['Year']})")
        

if __name__ == "__main__":
    main()
    


