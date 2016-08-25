import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home.html')

@app.route('/generator')
def render_generator():
    return render_template('generator.html')

@app.route('/exercises') #This one will be a dropdown, need to fix
def render_exercises():
    return render_template('exercises.html')

@app.route('/search')
def render_search():
    return render_template('search.html')
    
@app.route('/muscle-group-checklist') #fix this
def render_muscle_group_checklist():
    return render_template('muscle-group-checklist.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
