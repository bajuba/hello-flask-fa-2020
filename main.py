from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "Hello World"

@app.route("/banana")
def banana():
    return "banana"

@app.route("/apple")
def apple():
    return "apple"

app.run()