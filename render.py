from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
from flask import render_template, flash, Markup

from github import Github
import pprint
import os
import sys
import traceback
from exercises import exercise_2_link

class GithubOAuthVarsNotDefined(Exception):
    '''raise this if the necessary env variables are not defined '''

if os.getenv('GITHUB_CLIENT_ID') == None or \
        os.getenv('GITHUB_CLIENT_SECRET') == None or \
        os.getenv('APP_SECRET_KEY') == None or \
        os.getenv('GITHUB_ORG') == None:
    raise GithubOAuthVarsNotDefined('''
      Please define environment variables:
         GITHUB_CLIENT_ID
         GITHUB_CLIENT_SECRET
         GITHUB_ORG
         APP_SECRET_KEY
      ''')



from collections import defaultdict
import itertools

def constant_factory(value):
    return itertools.repeat(value).next


app = Flask(__name__)

app.debug = True

app.secret_key = os.environ['APP_SECRET_KEY']
oauth = OAuth(app)

# This code originally from https://github.com/lepture/flask-oauthlib/blob/master/example/github.py
# Edited by P. Conrad for SPIS 2016 to add getting Client Id and Secret from
# environment variables, so that this will work on Heroku.


github = oauth.remote_app(
    'github',
    consumer_key=os.environ['GITHUB_CLIENT_ID'],
    consumer_secret=os.environ['GITHUB_CLIENT_SECRET'],
    request_token_params={'scope': 'read:org'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)


@app.context_processor
def inject_logged_in():
    return dict(logged_in=('github_token' in session))

@app.context_processor
def inject_github_org():
    return dict(github_org=os.getenv('GITHUB_ORG'))

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/login')
def login():
    print 'we got to login'
    return github.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.clear()
    flash('You were logged out')
    return redirect(url_for('home'))


#@app.route('/logout')
#def logout():
#    session.pop('github_token', None)
#    return redirect(url_for('index'))


@app.route('/login/authorized')
def authorized():
    print 'we got to authorized'
    resp = github.authorized_response()

    if resp is None:
        session.clear()
        login_error_message = 'Access denied: reason=%s error=%s full=%s' % (
            request.args['error'],
            request.args['error_description'],
            pprint.pformat(request.args)
        )        
        flash(login_error_message, 'error')
        return redirect(url_for('home'))    

    try:
        session['github_token'] = (resp['access_token'], '')
        session['user_data']=github.get('user').data
        github_userid = session['user_data']['login']
        org_name = os.getenv('GITHUB_ORG')
    except Exception as e:
        session.clear()
        message = 'Unable to login: ' + str(type(e)) + str(e)
        flash(message,'error')
        return redirect(url_for('home'))
    
    try:
        g = Github(resp['access_token'])
        org = g.get_organization(org_name)
        named_user = g.get_user(github_userid)
        isMember = org.has_in_members(named_user)
    except Exception as e:
        message = 'Unable to connect to Github with accessToken: ' + resp['access_token'] + " exception info: " + str(type(e)) + str(e)
        session.clear()
        flash(message,'error')
        return redirect(url_for('home'))
    
    if not isMember:
        session.clear() # Must clear session before adding flash message
        message = 'Unable to login: ' + github_userid + ' is not a member of ' + org_name + \
          '</p><p><a href="https://github.com/logout" target="_blank">Logout of github as user:  ' + github_userid + \
          '</a></p>' 
        flash(Markup(message),'error')

    else:
        flash('You were successfully logged in')

    return redirect(url_for('home'))    

@app.route('/generator')
def render_generator():
    return render_template('generator.html')
    
@app.route('/muscle-group-checklist')
def render_muscle_group_checklist():
    return render_template('muscle-group-checklist.html')



import random
#lists of each exercise for each muscle group 
biceps = ["barbell curls", "alternating dumbbell curls", "hammer curls", "zottman curls", "spider curls"]
triceps= ["tricep dips", "skullcrushers", "overhead dumbbell extensions", "tricep pushdowns"]
shoulders = ["barbell overhead press", "dumbbell overhead press", "dumbbell front/side raises", "barbell shoulder rows", "dumbbell shoulder rows"]
chest = ["barbell bench press", "dumbbell fly", "decline push-ups", "cable chest crossover"]
back = ["pull-ups", "bent-over barbell row", "lat pulldowns", "one arm dumbbell row", "t-bar row", "back extension"]
core = ["planks", "russian twists", "bicycles", "windshield wipers", "v-ups", "side v-ups", "medicine ball throws", "mountain climbers"]
quadriceps = ["barbell squat", "lunges", "wall-sits", "goblet squat", "box jumps"]
hamstrings = ["barbell deadlift", "lying leg curls", "single-leg deadlift", "step-ups", "floor glute-ham raise"]

#chooses a random exercise from a certain list
def randomExercise(list):
    return random.choice(list)

#checks True/False if user chose a muscle group & adds appropriate exercises into the new list your_workout
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


#dropdown menu links/webpages for each muscle group
@app.route('/exercises') 
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
    
@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')
    
if __name__=="__main__":
    app.run(debug=True, port=54322)
