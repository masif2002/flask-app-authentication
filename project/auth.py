from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == "POST":
        # Extracting details
        email = request.form.get('email')   
        name = request.form.get('name')
        password = request.form.get('password')

        # Hashing Password
        password = generate_password_hash(password, method='sha256')

        # Checking if user already exists
        user = User.query.filter_by(email=email).first()
        
        if (user):
            flash('User already exists')

        else:
            # Creating a new user
            new_user = User(email=email, name=name, password=password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('auth.login'))

    return render_template('signup.html')

@auth.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get('checkbox') else False

        user = User.query.filter_by(email=email).first()

        if (not user):
            flash("User not found")
        elif not check_password_hash(user.password, password):
            flash("Login credentials incorrect")    
        else:
            login_user(user, remember=remember)
            return redirect(url_for('view.profile'))

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('view.home'))