from flask import Blueprint, render_template
from flask_login import login_required, current_user

view = Blueprint("view", __name__)

@view.route('/')
def home():
    return render_template('home.html', user=current_user)

@view.route('/profile')
@login_required
def profile():
    print(current_user.id)
    return render_template('profile.html', name=current_user.name)