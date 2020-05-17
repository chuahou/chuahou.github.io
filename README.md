# chuahou.github.io

A [website](https://chuahou.dev) with no content.
Made using Flask, and Frozen-Flask to statically generate HTML for GitHub pages.

## Dependencies

- Python 3 with pip
- GNU make

## Installation

After cloning the repository, enter the flask/ directory and install
dependencies:

	cd flask
	make

Then, to statically generate the site, run

	make install

To display on `0.0.0.0:8000` using Python's HTTP server, run

	make run

## Structure

This is written as a barebones Flask app in the flask/ folder. The Makefile uses
Frozen-Flask to generate the site to the root of the repository, which is then
uploaded for use by GitHub Pages.

Any files that should live in the root of the repository **must** be documented
in flask/precious.txt to avoid getting cleaned during building.
