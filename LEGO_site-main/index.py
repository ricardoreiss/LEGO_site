from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/index.html")
def index():
	return render_template("index.html")

@app.route("/objetivo.html")
def objetivo():
	return render_template("objetivo.html")

@app.route("/more.html")
def more():
	return render_template("more.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)