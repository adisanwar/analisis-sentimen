import requests

url = "https://twitter-api45.p.rapidapi.com/timeline.php"

querystring = {"screenname":"polisiidol"}

headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": ""
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
