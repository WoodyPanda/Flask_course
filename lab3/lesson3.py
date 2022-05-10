from lab3 import app, render_template

def redirect_page():
    return render_template('user.html')

def show_user_profile(username):
    return 'Hello, %s' % username

if __name__ == '__main__':
    app.run()
