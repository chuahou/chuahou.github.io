# chuahou.github.io

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A [website](https://chuahou.dev) with no content.
Made using Flask, and Frozen-Flask to statically generate HTML for GitHub pages.

## Dependencies

- Python 3 with pip
- GNU make
- [UglifyCSS](https://www.npmjs.com/package/uglifycss)

## Installation

After cloning the repository, enter the flask/ directory and build:

	cd flask
	make

To display on `0.0.0.0:8000` using Python's HTTP server, run

	make run

## Structure

This is written as a barebones Flask app in the flask/ folder. The Makefile uses
Frozen-Flask to generate the site to the root of the repository, which is then
uploaded for use by GitHub Pages. UglifyCSS is used to minimize CSS which is
then inlined by Jinja.

Any files that should live in the root of the repository **must** be documented
in flask/precious.txt to avoid getting cleaned during building.
