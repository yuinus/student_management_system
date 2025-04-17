from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user
from models.user_model import User
from app import db, bcrypt

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user_data = db.users.find_one({"username": username})

        if user_data and bcrypt.check_password_hash(user_data['password'], password):
            user = User(user_data)
            login_user(user)

            if user.role == "admin":
                return redirect(url_for('dashboard_admin'))
            elif user.role == "teacher":
                return redirect(url_for('dashboard_teacher'))
            else:
                return redirect(url_for('dashboard_student'))

        flash("Invalid username or password", "danger")

    return render_template("login.html")
