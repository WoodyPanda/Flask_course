from lab2 import app, render_template

def render_hello_world():
    return render_template('hello_world.html')

if __name__ == '__main__':
    app.run()