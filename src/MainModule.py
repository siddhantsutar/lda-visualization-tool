##########################################################################################
# File: MainModule.py                                                                    # 
# Description: Generate topic-specific visualizations using Latent Dirichlet Allocation. #
##########################################################################################

import logging
from Dataset import *
from Chart import *

class MainModule(object):
    def __init__(self): #Initialize
        self.dataset = None
        self.nTopics = 5
        self.nTopWords = 6
        self.type = ""
        self.topicList = []
        self.topic = None
        self.headerWidth = 50
        self.printHeader("Welcome to Topic Modeling Visualization Tool!")

    def printHeader(self, title, newLine=False): #Fancy title
        if newLine:
            print ""
        print "-" * self.headerWidth
        print title.center(self.headerWidth, ' ')
        print "-" * self.headerWidth
        
    def setDataset(self):
        try:
            self.dataset = Dataset(raw_input("Enter the name of the dataset to import: "))
        except:
            print "Error loading dataset. Try again!"
            self.setDataset()

    def setNTopics(self):
        self.nTopics = int(raw_input("Enter the number of topics to generate (default: 5): "))

    def setNTopWords(self):
        self.nTopWords = int(raw_input("Enter the number of words per topic (default: 5): ")) + 1

    def setType(self):
        self.type = raw_input("Enter specific type (e.g. enhancement, minor): ")
        if self.type.lower() not in self.dataset.uniqueTypes:
            print "Type does not exist in the database. Try again!"
            self.setType()
            return
        self.dataset.updateByType(self.type)

    def getTopics(self, fit = True):
        if fit:
            self.topicList = self.dataset.fitLDA(self.nTopics, self.nTopWords)
        self.printHeader("Topic list", True)
        for each in range(0, len(self.topicList)):
            print "Topic " + str(each) + ": " + ' '.join(self.topicList[each])

    def setTopic(self):
        readTopic = raw_input("Choose topic or enter topic name: ")
        try:
            readTopic = int(readTopic)
            if readTopic >= len(self.topicList):
                print "No topic associated with the entered number. Try again!"
                self.setTopic()
                return
        except:
            pass
        if isinstance(readTopic, int):
            self.topic = self.topicList[readTopic]
        elif isinstance(readTopic, basestring):
            self.topic = readTopic.split(' ')
        self.graphSelection()

    def graphSelection(self):
        self.printHeader("Graph selection", True)
        if int(raw_input("Show time vs. frequency chart for " + self.type + " type? Enter 1 for 'yes': ")) == 1:
            graphData = self.dataset.getDataPoints(self.topic, 1)
            Chart(graphData, 1, "Years", "Frequency", ' '.join(self.topic))
        if int(raw_input("Show type vs. frequency chart? Enter 1 for 'yes': ")) == 1:
            graphData = self.dataset.getDataPoints(self.topic, 2)
            Chart(graphData, 2, "Type", "Frequency", ' '.join(self.topic))
        if int(raw_input("Show time and type vs. frequency chart? Enter 1 for 'yes': ")) == 1:
            graphData = self.dataset.getDataPoints(self.topic, 3)
            Chart(graphData, 3, "Years-Type", "Frequency", ' '.join(self.topic))

    def getNext(self):
        print ""
        if int(raw_input("Continue (1) or exit (0): ")) == 1:
            self.getTopics(False)
            self.setTopic()
            self.getNext()
        else:
            exit

#Driver
def main():
    mm = MainModule()
    mm.setDataset()
    mm.setNTopics()
    mm.setNTopWords()
    mm.setType()
    mm.getTopics()
    mm.setTopic()
    mm.getNext()

main()
