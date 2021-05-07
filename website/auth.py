from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .db_connection import connect

auth = Blueprint('auth', __name__)
connect, cursor = connect()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return render_template("landing.html")

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        cursor.execute(
            "SELECT * FROM users WHERE email = %s", email)
        user = cursor.fetchone()
        print(user)
        if user:
            if password == user['password']:
                cursor.execute('select count(rating) as ratings_count from users join ratings on users.user_id = ratings.user_id where users.user_id = %s',user['user_id'])
                ratings_provided = cursor.fetchone()
                session['logged_in'] = True
                session['id'] = user['user_id']
                session['username'] = email
                session['ratings_provided'] = ratings_provided['ratings_count']
                flash('You have logged in!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again.', category='error')
        else:
            flash('Email does not exist, please try again.', category='error')
    return render_template("login.html")

@auth.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('ratings_provided', None)
    flash('You have logged out!', category='success')
    return redirect(url_for('auth.login'))


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if 'username' in session:
        return render_template("landing.html")

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        name = first_name + ' ' + last_name
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        age = request.form.get('age')
        gender = request.form.get('gender')
        cursor.execute(
            "SELECT * FROM users WHERE email = %s", email)
        user = cursor.fetchone()
        if user:
            flash('It appears your email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) == 0:
            flash('Please do not leave first name blank.', category='error')
        elif len(last_name) == 0:
            flash('Please do not leave last name blank.', category='error')
        elif gender is None:
            flash('Please do not leave the gender blank.', category='error')
        elif password1 != password2:
            flash('Passwords does not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            cursor.execute("SELECT MAX(user_id) as max FROM users")
            new_id = cursor.fetchone()['max'] + 1
            cursor.execute("INSERT INTO users (user_id, name, email, password, age, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                           (new_id, name, email, password1, age, gender))
            connect.commit()
            flash('Account created!', category='success')
            return redirect(url_for('auth.login')) 
    return render_template("sign_up.html")
