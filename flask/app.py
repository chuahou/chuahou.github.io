import datetime

from flask import Flask, render_template
from flask_frozen import Freezer
import yaml

import pages

app = Flask(__name__)

# list of pages and their rendering functions
page_list = [
        ("/", pages.index("data/main_links.txt")),
        ("/quicklinks/", pages.quicklinks("data/quicklinks.yml"))
        ]

# add each page to app
for rule, (endpoint, view_func) in page_list:
    if rule[-1] == '/': # add "index.html" if necessary for freezing purposes
        rule += "index.html"
    app.add_url_rule(rule, endpoint, view_func)

# generate sitemap from page_list
@app.route("/sitemap.xml")
def sitemap():
    locations = [rule for rule, _ in page_list]
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    return render_template("sitemap.xml", date=date, locations=locations)

# freeze app to build/
if __name__ == "__main__":
    freezer = Freezer(app)
    freezer.freeze()
