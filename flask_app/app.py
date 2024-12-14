from flask import Flask, render_template, request
import pickle

# Load the vectorizer and model
with open("/Users/vinaymittal/Monash/Emotion-mlops/models/vectorizer.pkl", "rb") as file:
    vect = pickle.load(file)

with open("/Users/vinaymittal/Monash/Emotion-mlops/models/model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Retrieve text input from the form
        user_input = request.form["text_input"]
        print(user_input)
        
        # Transform the user input using the vectorizer (make sure it's in a list)
        feature = vect.transform([user_input])
        
        
        # Make prediction using the model
        result = model.predict(feature)
        print(result)
        
        # Analyze sentiment (this can be based on the model's output)
        sentiment = "happy" if result == 1 else "sad"  # Example: Assuming 1 = happy, 0 = sad

        # Return the page with original, transformed text, and the analysis result
        return render_template('index.html', original=user_input, result=sentiment)
    
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
