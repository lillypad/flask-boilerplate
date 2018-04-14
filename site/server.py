#!/usr/bin/env python

from flask import Flask
from flask import render_template
from pages.index.views import page_index


app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
)

app.register_blueprint(page_index)

if __name__ == '__main__':
    app.run(debug=True)
