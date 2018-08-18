from flask import *
import mlab
from models.movie import Movie

app = Flask(__name__)
app.config['SECRET_KEY'] = "xp{v~8Zp8jcxj2wd`;5"
mlab.connect()

@app.route("/")
def index():
  if "username" in session:
    movie_list = Movie.objects()
    return render_template("index.html", movies=movie_list)
  else: 
    return redirect('/login')

@app.route("/login", methods = ['GET', 'POST'])
def login():
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST": 
    form = request.form 
    username = form ['username']
    password = form ['password']
    if username == "admin" and password == "123456": 
      # valid credential 
      session ['username'] = username
      return redirect('/')
    else:  
      # login fails
      flash("Login failed")
      flash ("Try again")
      return render_template("login.html")
    
if __name__ == "__main__":
  app.run(debug=True)