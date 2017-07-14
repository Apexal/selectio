from selectio import app, db_session
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")