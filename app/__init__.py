import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('about.html', url=os.getenv("URL"))

@app.route('/experience')
def experience():
    return render_template('experience.html', url=os.getenv("URL"))

@app.route('/education')
def education():
    return render_template('education.html', url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', url=os.getenv("URL"))

