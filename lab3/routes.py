from lab3 import app
from lab3.lesson3 import *

@app.route('/')
@app.route('/index')

@app.route('/users/<username>/url')
def redirect_user():
    return redirect_page()

@app.route('/users/<username>')
def user(username='user'):
    return show_user_profile(username)
