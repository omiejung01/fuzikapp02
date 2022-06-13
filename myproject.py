from flask import Flask
from app1 import file


app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! General Kenobi</h1>"

@app.route("/app1")
def app1():
	return file.hello()


if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')

