import requests

url = "https://twitter-api45.p.rapidapi.com/timeline.php"

querystring = {"screenname":"polisiidol"}

headers = {
	"X-RapidAPI-Key": "5d6dc34b2dmsh972584ee74c36dbp116949jsn1a45ba4a8b30",
	"X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())