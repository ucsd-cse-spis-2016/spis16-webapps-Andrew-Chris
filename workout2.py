
from collections import defaultdict
import itertools

def constant_factory(value):
    return itertools.repeat(value).next

#Creates the dictionary of exercises that the user will get. 
#Each exercise is also created to have a clickable link to a video or picture on how to do it
exercise_2_link = defaultdict(constant_factory('#'))
#Biceps
exercise_2_link['barbell curls'] = 'http://www.drdarden.com/forum_images/407723.1131124795296.barbell_curl.gif'
exercise_2_link['alternating dumbbell curls'] = 'http://2.bp.blogspot.com/-ErA2Xwvs0qc/Vf-W7rQhCOI/AAAAAAAAAJI/EFgT0mmqqm8/s1600/women%2527s%2Bhealth%2B-%2BALTERNATING%2BDUMBBELL%2BSUPINATED%2BCURL%2B00047.jpeg'
exercise_2_link['hammer curls'] = 'http://bodybuilding-wizard.com/wp-content/uploads/2015/08/standing-hammer-curls-2-9.jpg'
exercise_2_link['zottman curls'] = 'https://www.youtube.com/watch?v=H5Wr4lNYfn8'
exercise_2_link['spider curls'] = 'http://assets.menshealth.co.uk/main/thumbs/33059/prone-dumbbell-spider-curl__landscape.jpg'

#Triceps
exercise_2_link['tricep dips'] = 'http://hiitacademy.com/wp-content/uploads/2015/02/tricep_dips_feet_ext-1024x495.jpg'
exercise_2_link['skullcrushers'] = 'https://www.youtube.com/watch?v=gXbSA9EKUtA'
exercise_2_link['overhead dumbbell extensions'] = 'http://www.musclemag.com/content/content/9797/dumbbel-overhead-triceps-extension.jpg'
exercise_2_link['tricep pushdowns'] = 'http://truthofbuildingmuscle.com/wp-content/uploads/2015/01/tricep_pushdown_rope.jpg'

#Shoulders
exercise_2_link['barbell overhead press'] = 'http://fitfinity.net/wp-content/uploads/2010/09/barbell-push-press_470x360.jpg'
exercise_2_link['dumbbell overhead press'] = 'http://cdn-mf1.heartyhosting.com/sites/mensfitness.com/files/styles/photo_gallery_full/public/20.-neutral-grip-overhead-press-30-best-shoulder-exercises-of-all-time-shoulders.jpg?itok=K3phJliJ'
exercise_2_link['dumbbell front/side raises'] = 'http://10in30.com/wp-content/uploads/2011/04/front-sideraise.jpg'
exercise_2_link['barbell shoulder rows'] = 'http://assets.menshealth.co.uk/main/thumbs/15479/barbelluprightrowwide__landscape.jpg'
exercise_2_link['dumbbell shoulder rows'] = 'http://gym-inspiration.com/uploads/images/wideAppeal2.jpg'

#Chest
exercise_2_link['barbell bench press'] = 'http://stronglifts.com/wp-content/uploads/bench-press.jpg'
exercise_2_link['dumbbell fly'] = 'http://www.building-muscle101.com/images/xdumbbell-flyes-main.jpg.pagespeed.ic.MVYe92s52y.jpg'
exercise_2_link['decline push-ups'] = 'http://www.building-muscle101.com/images/xdumbbell-flyes-main.jpg.pagespeed.ic.MVYe92s52y.jpg'
exercise_2_link['cable chest crossover'] = 'https://www.youtube.com/watch?v=taI4XduLpTk'

#Back
exercise_2_link['pull-ups'] = 'https://qph.ec.quoracdn.net/main-qimg-4436150aea610f6bb632a22d62526242?convert_to_webp=true'
exercise_2_link['bent-over barbell row'] = 'http://stronglifts.com/wp-content/uploads/barbell-row.jpg'
exercise_2_link['lat pulldowns'] = 'http://cdn-mf1.heartyhosting.com/sites/mensfitness.com/files/styles/photo_gallery_full/public/lat_pulldown_main.jpg?itok=KAmPm2k2'
exercise_2_link['one arm dumbbell row'] = 'http://bodybuilding-wizard.com/wp-content/uploads/2014/04/one-arm-dumbbell-row-exercise-guide-01.jpg'
exercise_2_link['t-bar row'] = 'http://workoutlabs.com/wp-content/uploads/watermarked/Bent_Over_Two-Arm_Long_Bar_Row_M_WorkoutLabs.png'
exercise_2_link['back extension'] = 'https://s-media-cache-ak0.pinimg.com/564x/8e/67/52/8e6752133217a3f8e7796894e3337dc5.jpg'

#Core
exercise_2_link['planks'] = 'https://15128-presscdn-0-60-pagely.netdna-ssl.com/wp-content/uploads/2012/09/2012-9-12-Plank-1.jpeg'
exercise_2_link['russian twists'] = 'http://maltapersonaltraining.com/wp-content/uploads/2014/06/russian-twist-.jpg'
exercise_2_link['bicycles'] = 'http://hiitacademy.com/wp-content/uploads/2015/02/bicycle_abs.jpg'
exercise_2_link['windshield wipers'] = 'https://www.youtube.com/watch?v=Fuccu9GFO6g'
exercise_2_link['v-ups'] = 'http://3hh6gt2tuded1bgtz92lingb-wpengine.netdna-ssl.com/wp-content/uploads/2016/02/V-Ups.jpg'
exercise_2_link['side v-ups'] = 'http://www.womenshealthmag.com/sites/womenshealthmag.com/files/images/0912-oblique-v-up.jpg'
exercise_2_link['medicine ball throws'] = 'https://www.youtube.com/watch?v=5lDV_R-k9js'
exercise_2_link['mountain climbers'] = 'http://hiitacademy.com/wp-content/uploads/2015/02/mountain_climbers.jpg'

#Quadriceps
exercise_2_link['barbell squat'] = 'http://fitover40challenge.com/wp-content/uploads/2015/04/14294333074669-Squat.jpg'
exercise_2_link['lunges'] = 'http://assets2.tribesports.com/system/guide_photos/images/000/001/811/large/20130423155649-reverse-dumbbell-lunge.jpg?1366729007'
exercise_2_link['wall-sits'] = 'http://workoutlabs.com/wp-content/uploads/watermarked/Wall_Sit_squat_M_WorkoutLabs.png'
exercise_2_link['goblet squat'] = 'http://www.directlyfitness.com/store/wp-content/uploads/2012/09/goblet-squat.jpg'
exercise_2_link['box jumps'] = 'http://www.outsideonline.com/sites/default/files/styles/three-quarter-page-scaled-1x/public/migrated-images/December2011_BoxJumps_11142011_Featured.jpg?itok=miihcTWH'

#Hamstrings
exercise_2_link['barbell deadlift'] = 'https://www.youtube.com/watch?v=RovZFcTK_Gg'
exercise_2_link['lying leg curls'] = 'https://www.youtube.com/watch?v=dBo-Pw2a2h8'
exercise_2_link['single-leg deadlift'] = 'http://www.sweatlikeapig.com/wp-content/uploads/2013/04/single-leg-barbell-straight-leg-deadlift.jpg'
exercise_2_link['step-ups'] = 'http://cdn.builtlean.com/wp-content/uploads/2011/10/step-ups-leg-superset-cardio-workout-1.jpg'
exercise_2_link['floor glute-ham raise'] = 'https://www.youtube.com/watch?v=od6refujbEY'





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

