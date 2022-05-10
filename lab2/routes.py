from lab2.lesson2 import *

@app.route('/')
@app.route('/index')
def index():
    return render_hello_world()

