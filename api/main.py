# Import and Setup
from flask import Flask, render_template
app=Flask(__name__)
from bs4 import BeautifulSoup
import requests
import random
import urllib.request
import shutil


# Scrape WebPage
page = requests.get('https://www.azquotes.com/top_quotes.html')
htmlParse = BeautifulSoup(page.text, "html.parser")
quotes = htmlParse.findAll("a", attrs={"class": "title"})
authors = htmlParse.findAll("div", attrs={"class": "author"})
authorpic = htmlParse.findAll("img")



# Flask Server
@app.route('/')
def home():
  randomQuote = random.randint(0, len(quotes)-1)
  return render_template('index.html', authortext=authors[randomQuote].text, quotetext=quotes[randomQuote].text, authorpic=authorpic[randomQuote])



# Running It
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)