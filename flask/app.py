from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)

@app.route("/")
def index():
    dict_links = []
    with open("data/main_links.txt") as links_file:
        links = links_file.read().splitlines()
        for link in links:
            split = link.split()
            dict_links.append((split[0], split[1]))
    return render_template("main.html", center_content=True, links=dict_links)

if __name__ == "__main__":
    freezer = Freezer(app)
    freezer.freeze()
