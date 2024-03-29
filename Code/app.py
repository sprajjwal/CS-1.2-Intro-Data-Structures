from flask import Flask, render_template, redirect, url_for, request
from word_sampling import word_sampler
from histogram import histogram
import sys
from datetime import datetime
import requests
import random
import tweeter
import os
from markov import Markogram

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
    def __init__(self):
        self.message = ""
        self.count = 10
    
    def about(self):
        return render_template('about.html')
    
    def tweet_page(self):
        """Renders the index route"""
        file = "trump.txt"
        with open(file, 'r') as f:
            words = f.read().split()
        #     hist = histogram(words)
        self.count = int(request.args.get('words'))
        # for ind in range(self.count):
        #     self.message += word_sampler(hist)
        #     if ind < self.count - 1:
        #         self.message += " "
        # self.message = self.message.capitalize()
        # self.message += "."
        m = Markogram(words,3)
        message = m.get_string(self.count)
        self.message = message
        message = tweeter.str_to_html(message)
        
        gif = get_gif("Donald Trump")
        h = gif['dims'][1] * 2.5
        w = gif['dims'][0] * 2.5
        source = gif['url']
        return render_template('tweet.html', tweet=message, time=datetime.now(), gif=source, h=h, w=w)

    def send_tweet(self):
        message = self.message
        tweeter.tweet(message)
        return redirect(url_for('index'))

    def index(self):
        return render_template('index.html')

# flask 
ren = Renders()

@app.route('/')
def index():
    return ren.index()

@app.route('/tweet')
def tweet():
    ren.message = ""
    ren.count = 7 #default
    return ren.tweet_page()

@app.route('/send_tweet', methods=['POST'])
def send_tweet():
    return ren.send_tweet()

@app.route('/about')
def about():
    return ren.about()
    
