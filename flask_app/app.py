from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

# Function for sentiment analysis
def analyze_sentiment(text):
    # Create a TextBlob object and get the sentiment polarity
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    # Classify based on polarity: positive polarity is happy, negative is sad
    if polarity > 0:
        return "happy"
    else:
        return "sad"

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None

    # If the form is submitted, get the text and analyze sentiment
    if request.method == "POST":
        text = request.form["text"]
        sentiment = analyze_sentiment(text)

    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
