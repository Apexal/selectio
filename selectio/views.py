from selectio import app, db_session
from selectio.models import *
from flask import render_template, request, redirect, url_for, flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/persons')
@app.route('/persons/<id>')
def persons(id=None):
    if id is None:
        persons = Person.query.all()
        print(persons)
        return render_template('persons/persons.html', persons=persons)
    else:
        person = Person.query.get(id)
        print(person)
        return render_template('persons/person.html', person=person, QualityEnum=QualityEnum)

@app.route('/persons/add', methods=['POST', 'GET'])
def add_person():
    if request.method == 'POST':
        # Get all values from form
        first_name = request.form['firstName'].strip()
        last_name = request.form['lastName'].strip()
        nickname = first_name

        if 'nickname' in request.form:
            nickname = request.form['nickname'].strip()

        relation = request.form['relation'].strip().lower()
        gender = request.form['gender'].strip().lower()
        description = request.form['description'].strip()

        # Create new person
        new_person = Person(first_name, last_name, nickname, relation, gender, description)
        db_session.add(new_person)
        db_session.commit()

        return redirect(url_for('persons'))
    else:
        relations = ['self', 'partner', 'sibling', 'parent', 'family', 'friend', 'classmate', 'teacher', 'boss', 'co-worker']
        return render_template('persons/add_person.html', relations=relations)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
