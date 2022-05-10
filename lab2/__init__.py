from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

from lab2 import routes