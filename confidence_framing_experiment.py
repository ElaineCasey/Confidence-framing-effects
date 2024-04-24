# from expyriment.stimuli.extras import DotCloud
from expyriment import design, control, stimuli, misc
import random
import numpy as np

# setup variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LEFT_PRESS = 'f'
RIGHT_PRESS = 'j'

N_TRAILS_PER_TARGET = 2  # CHANGE
DOT_NUMBER = 10
CLOUD_RADIUS = 10


def generate_numbers(baseline, percent_increases):
    dotnums_list = []
    for i in baseline:
        for pchange in percent_increases:
            adjusted_num = int(i * (1 + pchange))
            if adjusted_num != i:
                dotnums_list.append(adjusted_num)
    return dotnums_list


baseline_levels = [50, 100, 150]
percent_increases = np.linspace(-0.20, 0.20, 21)
dotnumberspertrial = generate_numbers(baseline_levels, percent_increases)


def display_scale():  # change to present as image
    scale_text = "How confident are you? 1 - Not confident at all  2 - Somewhat confident  3 - Quite confident  4 - Very confident"
    scale = stimuli.TextLine(scale_text, position=(0, 0))
    scale.preload()
    scale.present()


# change so that conditions are pre-specified per block
if random.random() > 0.5:
    FRAME_CONDITION = 'MORE'
else:
    FRAME_CONDITION = 'LESS'

# initialise experiment
exp = design.Experiment(name="Confidence-framing",
                        text_size=30,
                        background_colour=BLACK)
# control.set_develop_mode(on=True)

control.initialize(exp)

# generate stimuli
fixation = stimuli.FixCross(size=(40, 40),
                            colour=WHITE,
                            line_width=6)

# dot_cloud = DotCloud(CLOUD_RADIUS, (-300, 0), dot_colour=WHITE)

left_circle = stimuli.Circle(
    radius=300, colour=WHITE, position=(-300, 0), line_width=5)
right_circle = stimuli.Circle(
    radius=300, colour=WHITE, position=(300, 0), line_width=5)

canvas = stimuli.Canvas(size=exp.screen.size, colour=BLACK)

left_circle.plot(canvas)
right_circle.plot(canvas)
fixation.plot(canvas)

# Run experiment
blankscreen = stimuli.BlankScreen(colour=BLACK)

control.start(skip_ready_screen=True)

stimuli.TextScreen("Instructions",
                   f"""Keep your eyes fixated on the central cross.

    A cue will appear followed by two circles of dots on the left and right hand sides of the screen.
    Use the arrow keys to indicate which circle contains {FRAME_CONDITION.upper()} dots.
    Press'{LEFT_PRESS.upper()}' to choose the left circle.
    Press '{RIGHT_PRESS.upper()}' to choose the right circle.

    After your choice, you will be asked to report your confidence that you made the correct choice.
    You will choose a value on a scale from 1-4. 1 indicates you are not confident and 4 indicates you are very confident in your response.

    Press any key to continue.
    """).present()

exp.keyboard.wait()
blankscreen.present()
exp.clock.wait(1000)

for trial in range(N_TRAILS_PER_TARGET):
    fixation.present()
    exp.clock.wait(2000)

    canvas.present()
    key, rt = exp.keyboard.wait_char([LEFT_PRESS, RIGHT_PRESS])

    display_scale()
    exp.keyboard.wait()

    conf_key, conf_rt = exp.keyboard.wait(keys=[misc.constants.K_1, misc.constants.K_2,
                                                misc.constants.K_3, misc.constants.K_4])
    confidence_rating = int(conf_key)-48  # Convert ASCII value to integer
    exp.data.add([confidence_rating])
    # exp.data.add([key, rt, conf_key])
control.end()
