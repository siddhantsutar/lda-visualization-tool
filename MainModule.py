import logging
from Dataset import *
from Chart import *

class MainModule(object):
    def __init__(self):
        self.dataset = None
        self.nTopics = 5
        self.nTopWords = 6
        self.type = ""
        self.topicList = []
        self.topicID = -1
        self.headerWidth = 50
        self.printHeader("Welcome to Topic Modeling Visualization Tool!")

    def printHeader(self, title, newLine=False):
        if newLine:
            print ""
        print "-" * self.headerWidth
        print title.center(self.headerWidth, ' ')
        print "-" * self.headerWidth
        
    def setDataset(self):
        self.dataset = Dataset(raw_input("Enter the name of the dataset to import: "))

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

    def getTopics(self):
        self.topicList = self.dataset.fitLDA(self.nTopics, self.nTopWords)
        self.printHeader("Topic list", True)
        for each in range(0, len(self.topicList)):
            print "Topic " + str(each) + ": " + ' '.join(self.topicList[each])

    def setTopic(self):
        self.topicID = int(raw_input("Enter topic: "))
        self.graphSelection()

    def graphSelection(self):
        self.printHeader("Graph selection", True)
        if int(raw_input("Show time vs. frequency chart for " + self.type + " type? Enter 1 for 'yes': ")) == 1:
            graphData = self.dataset.getDataPoints(self.topicList[self.topicID], 1)
            Chart(graphData, 1, "Years", "Frequency", ' '.join(self.topicList[self.topicID]))
        if int(raw_input("Show type vs. frequency chart? Enter 1 for 'yes': ")) == 1:
            graphData = self.dataset.getDataPoints(self.topicList[self.topicID], 2)
            Chart(graphData, 2, "Type", "Frequency", ' '.join(self.topicList[self.topicID]))
        
def main():
    mm = MainModule()
    mm.setDataset()
    mm.setNTopics()
    mm.setNTopWords()
    mm.setType()
    mm.getTopics()
    mm.setTopic()

main()
