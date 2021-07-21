import functools
from logging import error
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import flask
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELET id FROM user WHERE username = ?', (username, )
        ).fetchone() is not None:
            error = f'The username {username}, is already in use'

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)', (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        
        flash(error)
    
    return render_template('auth/register.html')
    

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username, )
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(['password'], password):
            error = 'Incorrect password'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)
    
    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id, )
        ).fetchone()



