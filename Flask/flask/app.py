from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to flask framework"

@app.route("/index")
def index():
    return "This is index page with changes to see the difference using debug"

if __name__ == "__main__":
    app.run(debug = True)