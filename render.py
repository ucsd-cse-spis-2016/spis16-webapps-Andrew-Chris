import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home.html')



@app.route('/generator')
def render_generator():
    return render_template('generator.html')
    
@app.route('/muscle-group-checklist') #fix this
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

@app.route('/your-workout') #fix this
def your_workout():
    try:
        bis_result = request.args['bis']
        tris_result = request.args['tris']
        delts_result = request.args['delts']
        pecs_result = request.args['pecs']
        lats_result = request.args['lats']
        core_result = request.args['core']
        quads_result = request.args['quads']
        hammies_result = request.args['hammies']
        workout_result =  workout(bis_result, tris_result, delts_result, pecs_result, lats_result, core_result, quads_result, hammies_result)
        return render_template('your-workout.html', workout=workout_result)
    except ValueError:
        return "Sorry: something went wrong."



@app.route('/exercises') #This one will be a dropdown, need to fix
def render_exercises():
    return render_template('exercises.html')



@app.route('/search')
def render_search():
    return render_template('search.html')
    

    
if __name__=="__main__":
    app.run(debug=False, port=54321)
