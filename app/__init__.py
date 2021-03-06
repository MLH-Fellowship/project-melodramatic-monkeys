import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


isKayla = True

@app.route('/')
def mario_index():
    return render_template('mario_index.html', url=os.getenv("URL"))

@app.route('/mario_about')
def mario_about():
    return render_template('mario_about.html', url=os.getenv("URL"))

@app.route('/mario_experience')
def mario_experience():
    return render_template('mario_experience.html', url=os.getenv("URL"))

@app.route('/mario_education')
def mario_education():
    return render_template('mario_education.html', url=os.getenv("URL"))

@app.route('/mario_hobbies')
def mario_hobbies():
    return render_template('mario_hobbies.html', url=os.getenv("URL"))

@app.route('/mario_places')
def mario_places():
    return render_template('mario_places.html', url=os.getenv("URL"))



@app.route('/kayla')
def kayla_index():
    return render_template('kayla_index.html', url=os.getenv("URL"))

@app.route('/kayla_about')
def kayla_about():
    return render_template('kayla_about.html', url=os.getenv("URL"))

@app.route('/kayla_experience')
def kayla_experience():
    return render_template('kayla_experience.html', url=os.getenv("URL"))

@app.route('/kayla_education')
def kayla_education():
    return render_template('kayla_education.html', url=os.getenv("URL"))

@app.route('/kayla_hobbies')
def kayla_hobbies():
    return render_template('kayla_hobbies.html', url=os.getenv("URL"))

@app.route('/kayla_places')
def kayla_places():
    return render_template('kayla_places.html', url=os.getenv("URL"))

