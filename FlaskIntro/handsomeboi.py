from flask import Flask, render_template

app = Flask(__name__)

class Handsomeboi:
    def __init__(self, n, a, tu):
        self.name = n
        self.age = a
        self.thumbnail_url = tu

h1 = Handsomeboi("Tom Hiddleston",
"37",
"https://pbs.twimg.com/profile_images/872735699488866304/3X7wPXrK_400x400.jpg")

h2 = Handsomeboi("Tom Holland", 
"22",
"https://i.pinimg.com/originals/95/1f/eb/951feb1543d4bc23f36e1a960aa93495.jpg")

h3 = Handsomeboi ("Chris Hemsworth",
"34",
"https://i.pinimg.com/736x/04/7b/9c/047b9c4d51d50662d6742e1c013ec575--chris-hemsworth-smile-men-smiling.jpg")

handsomeboi_list = [h1, h2, h3]

@app.route("/handsomeboi")
def handsomeboi(): 
    return render_template("handsomeboi.html", handsomebois= handsomeboi_list)

if __name__ == "__main__":
    app.run(debug=True)