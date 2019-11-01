from flask import Flask, render_template, redirect, url_for
from word_sampling import word_sampler
from histogram import histogram
import sys
from datetime import datetime
import requests
import random
import tweeter

app = Flask(__name__)

def get_gif(query):
    """ get's a random gif from Tenor"""
    params = {  # parameters for API request
                "q": query,
                "key": "RPQS73MCKCBE"
            }
    response = requests.get("https://api.tenor.com/v1/search", params=params).json() # API request
    gif = response["results"][random.randint(0, len(response["results"]))]
    return gif['media'][0]['tinygif']
class Renders:
    def __init__(self, *args, **kwargs):
        self.message = ""
    
    
    def tweet_page(self):
        """Renders the index route"""
        file = "bro_code.txt"
        with open(file, 'r') as f:
            words = f.read().split()
            hist = histogram(words)
        count = 7 #request.form.get('num_words')
        for ind in range(count):
            self.message += word_sampler(hist)
            if ind < count - 1:
                self.message += " "
        self.message = self.message.capitalize()
        self.message += "."
        gif = get_gif("barney stinson")
        h = gif['dims'][1] * 2.5
        w = gif['dims'][0] * 2.5
        source = gif['url']
        return render_template('base.html', tweet=self.message, time=datetime.now(), gif=source, h=h, w=w)

    def send_tweet(self):
        message = self.message
        tweeter.tweet(message)
        return redirect(url_for('foo'))

ren = Renders()

@app.route('/')
def foo():
    return ren.tweet_page()

@app.route('/tweet', methods=['POST'])
def foo1():
    return ren.send_tweet()

