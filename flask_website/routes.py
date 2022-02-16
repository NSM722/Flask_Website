#from flask import Flask, app
from flask_website import app
from flask import Flask, render_template, url_for,request,json
from requests.sessions import session
from werkzeug.utils import redirect
from werkzeug.wrappers import response
import random
lucky_number = 13
random_number = random.randint(1, 20)

import requests, json

@app.route("/")
@app.route("/home")
def home():
    jumbotron = {
        "title": "Welcome to our coffee shop",
        "body": "Your coffee will be gently roasted in by our master Baristas before it is delivered fresh to you.."
    }
    return render_template('home.html', title='Home', content=jumbotron)

@app.route("/about")
def about():
    jumbotron = {
        "title": "Our Story",
        "body": "We intend to nurture a sense of marvel with your experience and also communication with just what we do.We set new standards for fair coffee trade. No distance is too far for the best coffees in the world. We maintain direct relationships with our partners, paying them high prices for their unique coffees."
    }
    return render_template('about.html', title='About Us', content=jumbotron)

@app.route("/menu")
def menu():
    jumbotron = {
        "title": "We are proud of our Coffee",
        "body" : "We want to share our world of coffee with you.There is nothing to write here, it is just needed to tasted..."
    }
    url = "https://opensheet.vercel.app/1Xt48Tfm0Nf6ITDM-PaQx6PyVRNyJUPjRcy5UoqdKtsQ/Menu"
    response = requests.get(url)
    data = response.json()
    return render_template('menu.html', title='Menu', items=data, content=jumbotron)

@app.route("/team")
def team():
    jumbotron = {
        "title": "Meet our team - We make the world's best coffee",
        "body" : "While we do everything in our power to roast and serve the happiest coffee feasible, coffee itself isn't really actually the core of our firm. It's our guests."
    }
    return render_template('team.html', title='Our Team', content=jumbotron)

@app.route("/contact") #@app.route("/contact", methods=['POST', 'GET'])
def contact():
    jumbotron = {
        "title": "Stay in touch! We love to hear from you",
        "body" : "Follow us for updates on the below social media pages and feel free to leave behind your comments."
    }
    """if request.method == 'POST':
        user = request.form['firstname']
        return redirect(url_for('user_name', user=user))
    else:
        return render_template('contact.html', title='Contact Us', content=jumbotron)"""
    return render_template('contact.html', title='Contact', content=jumbotron)

"""@app.route("/users")
def randomusers():
    jumbotron = {
        "title": "Coffee Bonanza - You Snooze You Lose!",
        "body" : "Try your luck in the fun game below to win free coffee and join our weekly winners list!"
    }
    url = "https://randomuser.me/api/?results=12"
    response = requests.request("GET", url)
    # print(response.status_code)
    # print(response.json())
    data = response.json()
    return render_template('users.html', users=data['results'], content=jumbotron)

@app.route("/test", methods=['POST', 'GET'])
def test_page():
    jumbotron = {
        "title": "Test",
        "body": "dummy page"
    }
    if request.method == 'POST':
        user = request.form['firstname']
        return redirect(url_for('user_name', user=user))
    else:
        return render_template('test.html', title='Test', content=jumbotron)

@app.route("/<user>")
def user_name(user):
    return f'<h1>Thank you for your comments {user}, we will get back to you soon 🎃</h1>'"""