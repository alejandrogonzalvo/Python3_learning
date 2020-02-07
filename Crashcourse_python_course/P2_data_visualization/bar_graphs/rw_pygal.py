import pygal as p

from random_walk import RandomWalk


while True:

    rw = RandomWalk(500)
    rw.walk()

    hist_x = p.Bar()
    hist_y = p.Bar()


    hist_x._title = "Probabilities of X positioning in a random walk"
    
    freq = []
    rw.x_val.sort()
    for x in rw.x_val:
        x_freq = rw.x_val.count(x)
        freq.append(x_freq)

    x_labels = []
    x_set = set(rw.x_val)
    for x in x_set:
        x_labels.append(x)
    x_labels.sort()
    hist_x.x_labels = x_labels
    hist_x.x_title = "Values of x" 
    hist_x.y_title = "Frequency of value"
    hist_x.add('X values', freq)
    hist_x.render_to_file('X_values_visual.svg')



    hist_y._title = "Probabilities of Y positioning in a random walk"

    freq = []
    rw.y_val.sort()
    for y in rw.y_val:
        y_freq = rw.y_val.count(y)
        freq.append(y_freq)

    x_labels = []
    y_set = set(rw.y_val)
    for y in y_set:
        x_labels.append(y)
    x_labels.sort()
    hist_y.x_labels = x_labels
    hist_y.x_title = "Values of y" 
    hist_y.y_title = "Frequency of value"
    hist_y.add('X values', freq)
    hist_y.render_to_file('Y_values_visual.svg')

    i = input("Make another walk? (y/n): ")
    if i == 'n':
        break
