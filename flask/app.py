import datetime

from flask import Flask, render_template
from flask_frozen import Freezer
import yaml

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

@app.route("/quicklinks/index.html")
def quicklinks():
    categories = []
    with open("data/quicklinks.yml") as yaml_file:
        categories = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return render_template("quicklinks.html", center_content=True,
            categories=categories, link_to_top=True)

@app.route("/sitemap.xml")
def sitemap():
    locations = []
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    return render_template("sitemap.xml", date=date, locations=locations)

if __name__ == "__main__":
    freezer = Freezer(app)
    freezer.freeze()
