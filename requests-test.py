import requests

url = "https://imdb8.p.rapidapi.com/title/auto-complete"

querystring = {"q":"Game of Thrones"}

headers = {
    'x-rapidapi-key': "3f0f3a3ce3msh5ce0b6c8481deddp11fc79jsn59039ff3114a",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())