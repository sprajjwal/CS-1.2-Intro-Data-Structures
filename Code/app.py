from flask import Flask, render_template, redirect, url_for, request
from word_sampling import word_sampler
from histogram import histogram
import sys
from datetime import datetime
import requests
import random
import tweeter
import os

app = Flask(__name__)

def get_gif(query):
    """ get's a random gif from Tenor"""
    params = {  # parameters for API request
                "q": query,
                "key": os.environ['TENOR_KEY']
            }
    while True:
        response = requests.get("https://api.tenor.com/v1/search", params=params).json()
        gif = response["results"][random.randint(0, len(response["results"])-1)]
        if gif: # API request      
            gif = gif['media'][0]['tinygif']
            return gif


class Renders:
    def __init__(self, *args, **kwargs):
        self.message = ""
        self.count = 10
    
    def about(self):
        return render_template('about.html')
    
    def tweet_page(self):
        """Renders the index route"""
        file = "bro_code.txt"
        with open(file, 'r') as f:
            words = f.read().split()
            hist = histogram(words)
        self.count = int(request.args.get('words'))
        for ind in range(self.count):
            self.message += word_sampler(hist)
            if ind < self.count - 1:
                self.message += " "
        self.message = self.message.capitalize()
        self.message += "."
        gif = get_gif("barney stinson")
        h = gif['dims'][1] * 2.5
        w = gif['dims'][0] * 2.5
        source = gif['url']
        return render_template('tweet.html', tweet=self.message, time=datetime.now(), gif=source, h=h, w=w)

    def send_tweet(self):
        message = self.message
        tweeter.tweet(message)
        return redirect(url_for('foo'))

    def index(self):
        return render_template('index.html')

ren = Renders()

@app.route('/')
def index():
    ren.message = ""
    return ren.index()

@app.route('/tweet')
def tweet():
    ren.count = 7 #default
    return ren.tweet_page()

@app.route('/send_tweet', methods=['POST'])
def foo1():
    return ren.send_tweet()

@app.route('/about')
def about():
    return ren.about()
    

