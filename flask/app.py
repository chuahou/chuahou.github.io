from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html", center_content=True)

if __name__ == "__main__":
    freezer = Freezer(app)
    freezer.freeze()
