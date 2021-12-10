from app import app
from flask import render_template, flash, url_for
from app.forms import LoginForm, SignupForm

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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logging in...')
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

#new user email verification
@app.route('/emailverification')
def email_verification():
    #placeholder for email email_verification
    return redirect(url_for('home'))
