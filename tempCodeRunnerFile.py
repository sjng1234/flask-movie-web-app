@app.route("/search",methods=["POST","GET"])
def search():
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    headers = {
        'x-rapidapi-key': "3f0f3a3ce3msh5ce0b6c8481deddp11fc79jsn59039ff3114a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    video_title = request.form["search_query"]
    querystring = {"q":video_title}
    response = requests.request("GET", url, headers=headers, params=querystring)

    datas = response.json()
    
    try:
        return render_template("search-result.html",data = datas)
    except:
        return render_template("error404.html")