#!/usr/bin/env python

from flask import Blueprint
from flask import render_template

page_index = Blueprint('page_index', __name__)


@page_index.route('/', methods=['GET'])
def index():
    try:
        return render_template(
            'index.html',
            title="Your Home Page"
        )
    except Exception as e:
        return str(e)
