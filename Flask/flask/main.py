from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/index")
def index():
    return "This is index page with changes to see the difference using debug"

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug = True)