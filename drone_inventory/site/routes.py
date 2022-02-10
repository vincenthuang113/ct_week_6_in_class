from re import template
from flask import Blueprint, render_template
from flask_login import login_required

site = Blueprint('site', __name__, template_folder='site_templates')

"""
first arugement 'site' is the Blueprint's name
second arguement, __name__ is the Blueprint's import name which is to find the source
"""

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')