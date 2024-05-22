# Confidence-framing-effects

This is a replication of experiment from Sakamoto & Miyoshi (2024) examining confidence framing effects using a 2AFC dot-number discrimination task.

## Experiment

### Stimuli

Stimuli are white dots that are positioned within a white rimmed circle. There are two circles filled with dots presented on the left and right sides of the screen. In the centre a fixation cross is presented.
The number of dots in a stimulus varies on 20 levels from three baseline levels (50, 100, 150) in steps of 2% increase or decrease.
The dots are positioned randomly within the circle frame with no overlap.

<img src="https://github.com/ElaineCasey/Confidence-framing-effects/blob/main/stimuli/random_dots_46.png" width="150" height="150">

To generate the [stimuli](https://github.com/ElaineCasey/Confidence-framing-effects/tree/main/stimuli) run this [script](https://github.com/ElaineCasey/Confidence-framing-effects/blob/main/confidence_framing_experiment.py) prior to beginning the experiment.
The images generated and saved by this script will be used by the [experiment script](https://github.com/ElaineCasey/Confidence-framing-effects/blob/main/confidence_framing_experiment.py).

### Proceudre

At the beginning of each trial, a fixation cross is presented for 500ms. The stimuli are presneted for 600ms. Participants are asked to respond using the left and right arrow keys. Participants are then asked to indicate their confidence on this trial on a scale from 1 to 4 using the number keys. There is a 500ms break between each trial.

#### Framing condition

Participants are assigned to either a 'more' or 'less' condition. In the 'more' condition, they are asked to respond to the stimulus with a greater number of dots. In the 'less' condition, they are asked to respond to the stimulus with a fewer number of dots.
Confidence is reported for each condition. Frame is a between-subjects factor.

When calling confidence_framing_experiment.py input the frame condition as an argument.
For example, `python confidecne_framing_experiment.py MORE`

## Reference

Sakamoto, Y., & Miyoshi, K. (2024). A confidence framing effect: Flexible use of evidence in metacognitive monitoring. Consciousness and Cognition, 118, 103636.
