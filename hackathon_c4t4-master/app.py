from flask import *
import mlab
from models.food import *
app = Flask(__name__)
mlab.connect()
app.config['SECRET_KEY'] = "xp{v~8Zp8jcxj2wd`;5"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pagecon")
def pagecon():
    list_food = Food.objects()
    return render_template("pagecon.html", items = list_food)

@app.route("/test")
def test():
    return render_template("index.html")

@app.route("/login" , methods = [ 'GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST": 
        form = request.form 
        print(form)
        email = form ['Email']
        password = form ['password']
        if email == "abc@gmail.com" and password == "123456": 
        # valid credential 
            session ['Email'] = email
            return redirect('/userprofile')
        else:  
        # login fails
            flash ("Login failed")
            flash ("Try again")
            return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route("/userprofile")
def userprofile():
    return render_template("userprofile.html")


if __name__ == "__main__":
    app.run(debug=True)