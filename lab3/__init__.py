from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='template')

from lab3 import routes