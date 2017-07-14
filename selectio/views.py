from selectio import app, db_session
from selectio.models import *
from flask import render_template, request, redirect, url_for, flash

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
        # Get all values from form
        first_name = request.form['firstName'].strip()
        last_name = request.form['lastName'].strip()
        nickname = first_name

        if 'nickname' in request.form:
            nickname = request.form['nickname'].strip()

        title = request.form['title'].strip()
        relation = request.form['relation'].strip().lower()
        gender = request.form['gender'].strip().lower()
        description = request.form['description'].strip()

        # Create new person
        new_person = Person(first_name, last_name, nickname, title, relation, gender, description)
        db_session.add(new_person)
        db_session.commit()

        return redirect(url_for('persons'))
    else:
        titles = ['Mr.', 'Mrs.', 'Ms.', 'Fr.', 'Dr.']
        relations = ['self', 'brother', 'sister', 'mother', 'father', 'friend', 'classmate']
        return render_template('persons/add_person.html', titles=titles, relations=relations)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
