from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to our flask app"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}"
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    # return "The marks you got is " + str(score)
    result = ""
    if (score >= 50):
        result = "PASS"
    else :
        result = "FAIL"
    return render_template('result.html', result = result)
        
@app.route('/successfor/<int:score>')
def successfor(score):
    result = ""
    if (score >= 50):
        result = "PASS"
    else :
        result = "FAIL"

    exp = {'score' : score, 'result' : result}
    return render_template('result1.html', result = exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result2.html', result = score)

if __name__ == "__main__":
    app.run(debug = True)