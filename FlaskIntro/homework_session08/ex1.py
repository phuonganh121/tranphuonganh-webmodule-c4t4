from flask import Flask, redirect

app = Flask(__name__)


@app.route("/") 
def index(): 
    return "helo"

@app.route("/about-me") 
def about_me():
    return '''my name is phương anh''' 

@app.route("/school")
def school(): 
    return redirect ("http://techkids.vn")

if __name__ == "__main__":
    app.run(debug=True)

