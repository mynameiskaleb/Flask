from app import app
from flask import render_template, flash, url_for
from app.forms import LoginForm, SignupForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logging in...')
        return redirect(url_for('home')) #redirects to user's home page
    return render_template('login.html', form=form)

@app.route('/signup')
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Creating account...')
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)
