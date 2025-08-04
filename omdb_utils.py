import requests

def get_movie_details(title, api_key):
    url = f"http://www.omdbapi.com/?t={title}&plot=full&apikey={api_key}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises an error for bad status codes
        data = response.json()

        if data.get("Response") == "True":
            plot = data.get("Plot", "N/A")
            poster = data.get("Poster", "N/A")
            return plot, poster
        else:
            return "N/A", "N/A"
    except Exception:
        return "N/A", "N/A"