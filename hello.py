from flask import Flask, render_template



app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
def home():

    return render_template("home.html")



# http://127.0.0.1:5000/notme
@app.route("/notme")
def hello_not_you():
    return "<p>please remove '/notme' from the url!</p>"


if __name__ == "__main__":
    app.run(debug = True)