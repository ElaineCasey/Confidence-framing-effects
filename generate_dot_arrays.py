import matplotlib.pyplot as plt
import numpy as np


def generate_numbers(baseline, percent_increases):
    dotnums_list = []
    for i in baseline:
        for pchange in percent_increases:
            adjusted_num = int(i * (1 + pchange))
            dotnums_list.append(adjusted_num)
    return dotnums_list


def generate_random_dots(num_dots, dot_rad, array_rad):
    dots = []
    while len(dots) < num_dots:
        # for a random 'angle' with a specific 'distance' from the centre, calculate the 'x' and 'y' coordinates of the dot for plotting
        angle = np.random.uniform(0, 2*np.pi)
        distance = np.random.uniform(0, array_rad - dot_rad)
        x = distance * np.cos(angle)
        y = distance * np.sin(angle)
        new_dot = (x, y, dot_rad)
        if not any(overlap(dot, new_dot) for dot in dots):
            dots.append(new_dot)
    return dots


def overlap(dotA, dotB):  # check if dot positions overlap
    x1, y1, r1 = dotA
    x2, y2, r2 = dotB
    # get squared distance between centres of each dot
    distance_squared = (x1 - x2)**2 + (y1 - y2)**2
    return distance_squared < (r1 + r2)**2


def plot_random_dots(dots, array_rad, imgsize=(10, 10)):
    fig, ax = plt.subplots(facecolor='black', figsize=imgsize)
    ax.add_patch(plt.Circle((0, 0), array_rad,
                 color='white', fill=False))

    for dot in dots:
        x, y, radius = dot
        ax.add_patch(plt.Circle((x, y), radius, color='white'))

    # make images square
    ax.set_aspect('equal', adjustable='box')
    ax.autoscale_view()
    plt.axis('off')


BASELINE_LEVELS = [50, 100, 150]
PERCENT_INCREASES = np.linspace(-0.20, 0.20, 21)
dotnumberspertrial = generate_numbers(BASELINE_LEVELS, PERCENT_INCREASES)

DOT_RADIUS = 0.3  # Specify radius of dots
ARRAY_RADIUS = 20  # Specify radius of the area where the dots are presented

# Generate random circles and save images for each number of circles
for num_dots in dotnumberspertrial:
    dots = generate_random_dots(num_dots, DOT_RADIUS, ARRAY_RADIUS)
    plot_random_dots(dots, ARRAY_RADIUS)

    save_path = f"/Users/elainecasey/Documents/ConfidenceFramingEffects/stimuli/random_dots_{num_dots}.png"
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()
