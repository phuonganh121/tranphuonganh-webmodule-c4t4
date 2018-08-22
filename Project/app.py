from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("pagecon3.html")

if __name__ == "__main__":
    app.run (debug=True)
