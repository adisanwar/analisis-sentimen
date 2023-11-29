import requests
from textblob import TextBlob
import matplotlib.pyplot as plt

# Endpoint URL for Twitter API in RapidAPI
url = "https://twitter-api45.p.rapidapi.com/timeline.php" # Replace with the actual endpoint

# Example query parameters
querystring = {"screenname": "polisiidol", "count": "10"}  # Modify according to your needs

# Headers containing your RapidAPI key
headers = {
    "X-RapidAPI-Key": "5d6dc34b2dmsh972584ee74c36dbp116949jsn1a45ba4a8b30",
    "X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Process the response
if response.status_code == 200:
    tweets = response.json()  # Extract tweets data from the response

    # Variables to store sentiment counts
    sentiment_counts = {
        'Tweet Positif': 0,
        'Tweet negatif': 0,
        'Tweet Neutral': 0
    }

    # Analyze sentiment for each tweet using TextBlob
    for tweet in tweets['timeline']:  # Tweets data is under 'timeline' key
        text = tweet.get('text')
        if text:
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity

            # Determine sentiment based on polarity score
            if polarity > 0:
                sentiment = 'Tweet Positif'
            elif polarity < 0:
                sentiment = 'Tweet negatif'
            else:
                sentiment = 'Tweet Neutral'

            # Update sentiment counts
            sentiment_counts[sentiment] += 1

            # Print tweet text and its sentiment
            print(f"Tweet: {text}")
            print(f"Sentiment: {sentiment}")
            print("-------------")

    # Prepare data for visualization
    labels = sentiment_counts.keys()
    values = sentiment_counts.values()

    # Create a bar chart using Matplotlib
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=['green', 'red', 'blue'])
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Analysis of Tweets')
    plt.show()

else:
    print("Failed to fetch tweets. Status code:", response.status_code)
