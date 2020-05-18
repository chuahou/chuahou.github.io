from abc import ABC, abstractmethod
from flask import render_template
import yaml

# Index page
def index(links_path):
    links = []
    with open(links_path) as links_file:
        lines = links_file.read().splitlines()
        for line in lines:
            split = line.split()
            links.append((split[0], split[1]))
    return lambda: render_template(
            "main.html",
            center_content=True,
            links=links)

# Quicklinks page
def quicklinks(qlinks_path):
    with open(qlinks_path) as yaml_file:
        categories = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return lambda: render_template(
            "quicklinks.html",
            center_content=True,
            categories=categories,
            link_to_top=True)

# Generic text page
def text(title, text_file, center_content=True):
    text = open(text_file).read()
    return lambda: render_template(
            "text.html",
            center_content=center_content,
            title=title,
            text=text,
            link_to_top=True)
