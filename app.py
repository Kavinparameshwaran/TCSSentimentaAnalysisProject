from flask import Flask, render_template, request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def Sentiment():
    if request.method == "POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        if score["neg"] != 0:
            return render_template('home.html', message="NotHappy😞😞")
        else:
            return render_template('home.html', message='Happy😄😄')
    return render_template('home.html')
if __name__ == "__main__":
    app.run()

