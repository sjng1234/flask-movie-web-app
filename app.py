import flask
import requests

print("Import success!")
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
# def homepage():
#     return "Hello World"
def render_landing_page():
    try:
        return render_template("landing-page.html",user_account = "sjng1234", account_type = "Premium")
    except:
        return "An error occured"

@app.route("/login")
def login():
    return "Welcome to our login page"

@app.route("/fakesearch")
def fakesearch():
    try:
        return render_template("fake-search.html")
    except:
        return render_template("error404.html")

# # Static routing
# @app.route("/search",methods=["POST","GET"])
# def search():
#     url = "https://imdb8.p.rapidapi.com/title/auto-complete"
#     headers = {
#         'x-rapidapi-key': "3f0f3a3ce3msh5ce0b6c8481deddp11fc79jsn59039ff3114a",
#         'x-rapidapi-host': "imdb8.p.rapidapi.com"
#     }
#     video_title = request.form["search_query"]
#     querystring = {"q":video_title}
#     response = requests.request("GET", url, headers=headers, params=querystring)

#     datas = response.json()
    
#     try:
#         return render_template("search-result.html",data = datas)
#     except:
#         return render_template("error404.html")

# Dynamic routing
@app.route("/search",methods=["POST"])
def search():
    video_id = request.form["search_query"]
    return redirect(url_for('.search_result', video = video_id))

@app.route("/search/<video>",methods=["GET"])
def search_result(video):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    headers = {
        'x-rapidapi-key': "3f0f3a3ce3msh5ce0b6c8481deddp11fc79jsn59039ff3114a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    querystring = {"q":video}
    response = requests.request("GET", url, headers=headers, params=querystring)

    datas = response.json()
    
    try:
        return render_template("search-result.html",data = datas)
        
    except:
        return render_template("error404.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1",port="5000")

