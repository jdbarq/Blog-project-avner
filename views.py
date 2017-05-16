from flask import render_template, request

from app import app

@app.route('/')
def homepage():
    name = request.args.get('name')
    number = request.args.get('number')
    return render_template('page.html', name=name, number=number)

