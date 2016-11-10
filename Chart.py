import matplotlib.pyplot as plt
import numpy as np

class Chart(object):

    def __init__(self, dataPoints, chartType, xLabel, yLabel, topic):
        xData = list(dataPoints.keys())
        yData = list(dataPoints.values())
        if chartType == 1:
            plt.plot(xData, yData)
            plt.title('Line chart for "' + topic + '"')
            plt.xticks(xData, xData)
        if chartType == 2:
            ind = np.arange(len(xData))
            width = 0.35
            plt.bar(ind, yData, width, color='r')
            plt.title('Bar chart for "' + topic + '"')
            plt.xticks(ind + width/2., xData)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.show()
