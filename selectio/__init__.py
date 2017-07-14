import os
from flask import Flask
app = Flask(__name__)

from selectio.database import db_session, init_db
from selectio.models import *

init_db()

import selectio.views

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))