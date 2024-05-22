# setup packages
from expyriment import design, control, stimuli, misc
import random
import numpy as np
import os
import sys

# setup variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LEFT_PRESS = 'f'
RIGHT_PRESS = 'j'
N_TRIALS = 60
FRAME_CONDITION = sys.argv[1]

# load pre-generated image stimuli
dir_path = r'/Users/elainecasey/Documents/ConfidenceFramingEffects/stimuli'
STIM_FILES = []
for path in os.listdir(dir_path):
    STIM_FILES.append(path)

# file is uploaded from Mac onto github also, cannot get rid of using .gitignore
STIM_FILES.remove('.DS_Store')
# Generate fixation cross
fixation = stimuli.FixCross(size=(40, 40),
                            colour=WHITE,
                            line_width=6)


def display_scale():
    scale_text = """How confident are you in your choice? 

    1 - Not confident at all  2 - Somewhat confident  3 - Quite confident  4 - Very confident"""
    scale = stimuli.TextScreen(
        '', scale_text, position=(0, -250), text_colour=WHITE)

    scale.preload()
    scale.present()


# Initialise experiment
exp = design.Experiment(name="Confidence-framing",
                        text_size=30,
                        background_colour=BLACK)
# control.set_develop_mode(on=True)
control.initialize(exp)

# Generate canvas to overlay stimuli & fixation on
canvas = stimuli.Canvas(size=exp.screen.size, colour=BLACK)
blankscreen = stimuli.BlankScreen(colour=BLACK)
fixation.plot(canvas)

# Run experiment
control.start(skip_ready_screen=True)

resp_screen = stimuli.TextScreen('', f"""Are there {FRAME_CONDITION.upper()} dots on the LEFT or the RIGHT ? 
                                 
    Press 'F' for LEFT 
                                 
    Press 'J' for RIGHT""", position=(0, -250), text_colour=WHITE)

# present instructions at beginning of experiment
stimuli.TextScreen("Instructions",
                   f"""Keep your eyes fixated on the central cross.

    A cue will appear followed by two circles of dots on the left and right hand sides of the screen.
    Use the arrow keys to indicate which circle contains {FRAME_CONDITION.upper()} dots.
    Press'{LEFT_PRESS.upper()}' to choose the left circle.
    Press '{RIGHT_PRESS.upper()}' to choose the right circle.

    After your choice, you will be asked to report your confidence that you made the correct choice.
    You will choose a value on a scale from 1-4. 1 indicates you are not confident and 4 indicates you are very confident in your response.

    Press any key to continue.
    """, text_colour=WHITE).present()

exp.keyboard.wait()
blankscreen.present()
exp.clock.wait(1000)

for trial in range(N_TRIALS):
    fixation.present()
    exp.clock.wait(500)

    # Choose two images to present on every trial
    trial_stim = random.sample(STIM_FILES, 2)
    img1 = stimuli.Picture(("stimuli/" + trial_stim[0]), position=(-550, 100))
    img2 = stimuli.Picture(("stimuli/" + trial_stim[1]), position=(550, 100))
    img1.plot(canvas)
    img2.plot(canvas)
    canvas.present()
    exp.clock.wait(600)

    resp_screen.present()
    key, rt = exp.keyboard.wait_char([LEFT_PRESS, RIGHT_PRESS])

    display_scale()
    conf_key, conf_rt = exp.keyboard.wait(keys=[misc.constants.K_1, misc.constants.K_2,
                                                misc.constants.K_3, misc.constants.K_4])
    confidence_rating = int(conf_key)-48  # Convert ASCII value to integer

    exp.data.add([key, rt, conf_key, confidence_rating, trial_stim])

    # ISI
    blankscreen.present()
    exp.clock.wait(500)


control.end()
