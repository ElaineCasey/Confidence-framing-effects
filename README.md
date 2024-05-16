# Confidence-framing-effects

This is a replication of experiment from Sakamoto & Miyoshi (2024) examining confidence framing effects using a 2AFC dot-number discrimination task.

## Experiment

### Stimuli

Stimuli are white dots with a size of 0.15 degrees of visual angle. The dots appear within a white rimmed circle with size 6 degrees of visual angle. There are two circles filled with dots presented on screen.
The number of dots in one stimulus is set on three levels (50, 100, 150). The number of dots in the second stimulus varies on 20 levels from this baseline in steps of 2% increase or decrease.
The dots are positioned randomly within the circle frame.

Each dot number level is presnted four times.

To generate the stimuli please call generate_dot_arrays.py
The images generated and saved by this script will be used for the experiment.

### Proceudre

There is first a practice session with 10 trials.
The main experiment consists of 6 blocks with 40 trials.

At the beginning of each trial, a fixation cross is presented, with a size of 1 degree of visual angle, for 500ms. The stimuli are presneted for 600ms. Participants are asked to respond using the left and right arrow keys. A likert scale with 4 options is then presented for participants to indicate their confidence on this trial. There is 500ms between each trial.

#### Framing condition

Participants are randomly assigned to either a 'more' or 'less' condition. In the 'more' condition, they are asked to respond to the stimulus with a greater number of dots. In the 'less' condition, they are asked to respond to the stimulus with a fewer number of dots.
Confidence is reported for each condition. Frame is a between-subjects factor.

## Reference

Sakamoto, Y., & Miyoshi, K. (2024). A confidence framing effect: Flexible use of evidence in metacognitive monitoring. Consciousness and Cognition, 118, 103636.
