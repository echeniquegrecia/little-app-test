from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello Renny, soy yo, Grecia, desde mi API!<h1>"

if __name__ == '__main__':
    app.run()
