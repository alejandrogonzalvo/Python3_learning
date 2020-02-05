from dice import Dice

import pygal as p


dice_1 = Dice()
dice_2 = Dice()
dice_3 = Dice(3)


results = []
for rolls in range(1000000):
    result = dice_1.roll() + dice_2.roll() + dice_3.roll()
    results.append(result)

# Count how many has occured each possibility
frequencies = []
max_result = dice_1.sides + dice_2.sides + dice_3.sides
for value in range(1, max_result):
    side_freq = results.count(value)
    frequencies.append(side_freq)


hist = p.Bar()

hist._title = "Probabilities of possible results in a dice roll "

x_labels = []
for side in range(1, max_result + 1):
    x_labels.append(side)
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('Dice/s', frequencies)
hist.render_to_file('dice_visual.svg')



