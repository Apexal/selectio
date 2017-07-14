from selectio import app, db_session
from selectio.models import *
from flask import render_template, request, flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/persons')
@app.route('/persons/<id>')
def persons(id=None):
    #new_person = Person("Frank", "Matranga", "Mr.", "self", "Male", 17)
    #db_session.add(new_person)
    #db_session.commit()

    if id is None:
        persons = Person.query.all()
        print(persons)
        return render_template('persons/persons.html', persons=persons)
    else:
        person = Person.query.get(id)
        print(person)
        return render_template('persons/person.html', person=person)

@app.route('/persons/add', methods=['POST', 'GET'])
def add_person():
    if request.method == 'POST':
        flash('Succes')
        return redirect(url_for('persons'))
    else:
        titles = ['Mr.', 'Mrs.', 'Ms.', 'Fr.', 'Dr.']
        relations = ['self', 'brother', 'sister', 'mother', 'father', 'friend', 'classmate']
        return render_template('persons/add_person.html', titles=titles, relations=relations)
