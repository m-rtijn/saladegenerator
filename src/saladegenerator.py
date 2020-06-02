#!/usr/bin/python3
"""
    saladegenerator.py

    Copyright (c) 2020 Martijn

    This file is part of saladegenerator.

    saladegenerator is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    saladegenerator is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with saladegenerator.  If not, see <https://www.gnu.org/licenses/>.
"""

import csv
from random import choice
from random import randint

from flask import Flask
from flask import render_template



app = Flask(__name__)

CSV_DATA_FILE_NAME = "static/database.csv"

leaf_list = []
carb_list = []
protein_list = []
herb_list = []
extra_list = []
dressing_list = []

ingredients = [
        leaf_list,
        carb_list,
        protein_list,
        herb_list,
        extra_list,
        dressing_list
    ]

with open(CSV_DATA_FILE_NAME) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    i = 0
    for row in csvreader:
        ingredients[i].extend(row)
        i = i + 1


@app.route("/")
def index_html():
    """Choose random ingredients and render the page."""
    leaf = choice(leaf_list)
    carb = choice(carb_list)
    protein = choice(protein_list)

    herb_count = randint(1, 2)
    extra_count = randint(1, 5)
    dressing_count = randint(0, 1)

    herbs = set()
    extra = set()
    dressing = set()

    while len(herbs) < herb_count:
        herbs.add(choice(herb_list))

    while len(extra) < extra_count:
        extra.add(choice(extra_list))

    while len(dressing) < dressing_count:
        dressing.add(choice(dressing_list))

    return render_template(
            "index.html",
            leaf=leaf,
            carb=carb,
            protein=protein,
            herbs=herbs,
            extra=extra,
            dressing=dressing)


@app.errorhandler(404)
def page_not_found():
    """Redirect to index page for all pages that can't be found."""
    return index_html(), 301


if __name__ == "__main__":
    app.run(host="0.0.0.0")
