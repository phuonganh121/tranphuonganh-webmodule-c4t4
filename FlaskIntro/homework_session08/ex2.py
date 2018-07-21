from flask import Flask, redirect

app = Flask(__name__)

Users = {
        'huy' : {
                'name' : 'Nguyen Quang Huy',
                'age' : 29
        },
        'don' : {
                "name" : 'Don zoombie',
                'age' : 23
        },
}

def user_info(user,Users):
    if user in Users:
        for categories, info in Users[user]:
            return (categories, ':', info)
    else: return None
 
@app.route("/user/<username>")
def info(username):
    if user_info(username,Users) != None: 
        return user_info(username,Users)
    else: return "User not found"

if __name__ == "__main__":
    app.run(debug=True) 






