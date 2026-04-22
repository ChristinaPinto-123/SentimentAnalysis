from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    
    if polarity > 0:
        classification = "Positive"
    elif polarity < 0:
        classification = "Negative"
    else:
        classification = "Neutral"
        
    return classification, round(polarity, 2), round(subjectivity, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_text = request.form['text_input']
        if user_text:
            classification, score, sub_score = analyze_sentiment(user_text)
            result = {
                'text': user_text,
                'sentiment': classification,
                'polarity': score,
                'subjectivity': sub_score
            }
            
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)