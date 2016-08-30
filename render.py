import os
from flask import Flask, url_for, render_template, request, session

from collections import defaultdict
import itertools

def constant_factory(value):
    return itertools.repeat(value).next

exercise_2_link = defaultdict(constant_factory('#'))
exercise_2_link['spider curls'] = 'http://assets.menshealth.co.uk/main/thumbs/33059/prone-dumbbell-spider-curl__landscape.jpg'


app = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('home.html')

@app.route('/generator')
def render_generator():
    return render_template('generator.html')
    
@app.route('/muscle-group-checklist')
def render_muscle_group_checklist():
    return render_template('muscle-group-checklist.html')

import random

biceps = ["barbell curls", "alternating dumbbell curls", "hammer curls", "zottman curls", "spider curls"]
triceps= ["tricep dips", "skullcrushers", "overhead dumbbell extensions", "tricep pushdowns"]
shoulders = ["barbell overhead press", "dumbbell overhead press", "dumbbell front/side raises", "barbell shoulder rows", "dumbbell shoulder rows"]
chest = ["barbell bench press", "dumbbell fly", "decline push-ups", "cable chest crossover"]
back = ["pull-ups", "bent-over barbell row", "lat pulldowns", "one arm dumbbell row", "t-bar row", "back extension"]
core = ["planks", "russian twists", "bicycles", "windshield wipers", "v-ups", "side v-ups", "medicine ball throws", "mountain climbers"]
quadriceps = ["barbell squat", "lunges", "wall-sits", "goblet squat", "box jumps"]
hamstrings = ["barbell deadlift", "lying leg curls", "single-leg deadlift", "step-ups", "floor glute-ham raise"]


def randomExercise(list):
    return random.choice(list)


def workout(bis_result, tris_result, delts_result, pecs_result, lats_result, core_result, quads_result, hammies_result):
    your_workout = []
    if bis_result == True:
        your_workout.append(randomExercise(biceps))
    if tris_result == True:
        your_workout.append(randomExercise(triceps))
    if delts_result == True:
        your_workout.append(randomExercise(shoulders))
    if pecs_result == True:
        your_workout.append(randomExercise(chest))
    if lats_result == True:
        your_workout.append(randomExercise(back))
    if core_result == True:
        your_workout.append(randomExercise(core))
    if quads_result == True:
        your_workout.append(randomExercise(quadriceps))
    if hammies_result == True:
        your_workout.append(randomExercise(hamstrings))
    return your_workout

@app.route('/your-workout')
def your_workout():
    try:
        bis_result = 'bis' in request.args #checks dictionary if 'bis' exists; sets true or false
        tris_result = 'tris' in request.args
        delts_result = 'delts' in request.args
        pecs_result = 'pecs' in request.args
        lats_result = 'lats' in request.args
        core_result = 'core' in request.args
        quads_result = 'quads' in request.args
        hammies_result = 'hammies' in request.args
        workout_result =  workout(bis_result, tris_result, delts_result, pecs_result, lats_result, core_result, quads_result, hammies_result)
        return render_template('your-workout.html', Workout_list=workout_result, exercise_2_link=exercise_2_link)
    except ValueError:
        return "Sorry: something went wrong."



@app.route('/exercises') #This one will be a dropdown, need to fix
def render_exercises():
    return render_template('exercises.html')
    
@app.route('/exercises/bis')
def render_bis():
    return render_template('exercises/bis.html')

@app.route('/exercises/tris')
def render_tris():
    return render_template('exercises/tris.html')
    
@app.route('/exercises/delts')
def render_delts():
    return render_template('exercises/delts.html')
    
@app.route('/exercises/pecs')
def render_pecs():
    return render_template('exercises/pecs.html')
    
@app.route('/exercises/lats')
def render_lats():
    return render_template('exercises/lats.html')
    
@app.route('/exercises/core')
def render_core():
    return render_template('exercises/core.html')
    
@app.route('/exercises/quads')
def render_quads():
    return render_template('exercises/quads.html')
    
@app.route('/exercises/hammies')
def render_hammies():
    return render_template('exercises/hammies.html')



@app.route('/search')
def render_search():
    return render_template('search.html')
    

    
if __name__=="__main__":
    app.run(debug=False, port=54322)
