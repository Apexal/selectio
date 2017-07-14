from selectio import app, db_session
from selectio.models import *
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/persons')
@app.route('/persons/<id>')
def persons(id=None):
    #new_person = Person("Frank", "Matranga", "Mr.", "self", "Male", 17)
    #db_session.add(new_person)
    #db_session.commit()
    
    persons = Person.query.all()
    print(persons)
    return render_template("persons.html", persons=persons)