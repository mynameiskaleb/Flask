from app import app
from flask import render_template, flash, url_for
from app.forms import LoginForm, SignupForm
from flask_login import current_user, login_user, logout_user
from app.models import User

#web app homepage
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#user's home page
@app.route('/home')
def home():
    # get user's subscribed stocks
    # get user's buy/sell history
    return render_template('home.html')

#login user
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


#signup user
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Creating account...')
        return redirect(url_for('email_verification'))
    return render_template('signup.html', form=form)

@app.route('logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

#new user email verification
@app.route('/emailverification')
def email_verification():
    #placeholder for email email_verification
    return redirect(url_for('home'))
