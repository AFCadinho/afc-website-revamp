from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AFC Adinho V2!\nHello World"