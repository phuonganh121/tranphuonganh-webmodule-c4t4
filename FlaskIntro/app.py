# 1 Create Flask App
from flask import Flask, render_template

app = Flask(__name__)

class Movie:
    def __init__(self, t, c, tu):
        self.title = t
        self.casts = c
        self.thumbnail_url = tu

m = Movie("Ant Man 2",
"Paul Rudd, ...",
"https://4.bp.blogspot.com/-InIo1OIRQvs/WxDNk-Zr8hI/AAAAAAAAaKA/t3urTLKYJaoW36s2EtckrY6FzGjFTtw3gCLcBGAs/s4000/DekILl0UEAAPVQU.jpg%2Borig.jpg")

m2 = Movie ("Home alone",
"abc",
"https://www.imdb.com/title/tt0099785/")

movie_list = [m, m2]
@app.route("/") #trangchu
def index(): #chayham
    return render_template("index.html", name= "Hoa",
    image_url="https://4.bp.blogspot.com/-InIo1OIRQvs/WxDNk-Zr8hI/AAAAAAAAaKA/t3urTLKYJaoW36s2EtckrY6FzGjFTtw3gCLcBGAs/s4000/DekILl0UEAAPVQU.jpg%2Borig.jpg")

@app.route("/about-me") 
def about_me():
    return "abc"

@app.route("/hello/<name>")
def hello(name):
    return name + ", abc"

@app.route("/movie")
def movie():
    return render_template("movie.html", movies= movie_list)

@app.route("/casts")
def casts():
    return render_template("casts.html", casts=["xuab bac", "tu long"])
    

# Run App  
if __name__ == "__main__":
    app.run(debug=True)