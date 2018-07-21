# 1 Create Flask App
from flask import Flask #Flask: class

app = Flask(__name__)

@app.route("/") #trangchu
def index(): #chayham
    return "Hello, this is the homepage"

@app.route("/about-me") 
def about_me():
    return "Let's go to CHRONO!!!!!"

@app.route("/hello/<name>")
def hello(name):
    return name + ", let's go and meet Hai Sam"

# Run App  
if __name__ == "__main__":
    app.run(debug=True)