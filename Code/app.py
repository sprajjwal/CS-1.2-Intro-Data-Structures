from flask import Flask, render_template
from word_sampling import word_sampler
from histogram import histogram
import sys

app = Flask(__name__)
@app.route('/')
def tweet_page():
    """Renders the index route"""

    file = "bro_code.txt"
    with open(file, 'r') as f:
        words = f.read().split()
        hist = histogram(words)
    count = 7 #request.form.get('num_words')
    str = ""
    for _ in range(count):
        str += word_sampler(hist)
        str += " "
    print(str)
    return render_template('base.html', string=str)