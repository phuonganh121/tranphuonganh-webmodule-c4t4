from flask import Flask, render_template
import mlab
from ex1_b import Hobby

app = Flask (__name__)
mlab.connect()

@app.route("/")
def index(): 
    hobby_list = Hobby.objects()
    return render_template("index.html", hobbies= hobby_list)

if __name__ == "__main__":
    app.run(debug=True)