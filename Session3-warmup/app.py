from flask import Flask

app = Flask(__name__) 

@app.route("/hello/<name>")
def hello(name):
    return "Hello, " + name 

@app.route("/add/<a>/<b>")
def add (a, b): 
    # return "{}".format(a+b)
    return str(int(a) + int(b))


if __name__ == "__main__":
    app.run(debug=True)

