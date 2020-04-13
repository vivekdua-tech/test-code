import numpy as np
import matplotlib.pyplot as plt


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


def plotFromList(plotData):
    """
        plotData is in form of tuple list:
        [('temp1', 2), ('temp2', 3)]
        plot using the data provided. 
    """
    #men_means, men_std = (20, 35, 30, 35, 27), (2, 3, 4, 1, 2)
    #women_means, women_std = (25, 32, 34, 20, 25), (3, 5, 2, 3, 3)

    ind = np.arange(len(plotData))  # the x locations for the groups
    width = 0.35  # the width of the bars
    yax_list = [x[1] for x in plotData]
    xax_list = [x[0] for x in plotData]
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, yax_list, width,
                color='SkyBlue', label='Cyclomatic-Complexity')
    #rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
    #           color='IndianRed', label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('CCN')
    ax.set_title('CCN across modules')
    ax.set_xticks(ind)
    ax.set_xticklabels(xax_list)
    ax.legend('CCN comparison')
    autolabel(rects1, "left")
    autolabel(rects2, "right")
    return plt
