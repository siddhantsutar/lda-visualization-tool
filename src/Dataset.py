###########################################################################
# File: Dataset.py                                                        #
# Description: Preprocess and process the given dataset to fit LDA model. #
###########################################################################

import lda
import textmining
import numpy as np
import pandas as pd
import logging
logging.getLogger("lda").setLevel(logging.CRITICAL) #Ignore pesky warnings thrown by lda module

class Dataset(object):
    def __init__(self, filename):
        self.fields = ["Issue_ID", "Title/Description", "Importance/Type", "Creation_Date", "Resolve_Date"]
        self.data = pd.read_csv(filename, low_memory=False, usecols=self.fields)
        self.typeData = None
        self.model = None
        self.dataCleanup()
        self.uniqueTypes = (self.data["Importance/Type"].unique())[:-2] #For chart data
        self.uniqueYears = [] #For chart data

    def dataCleanup(self): #Preprocess
        self.data[self.data["Issue_ID"].apply(lambda x: str(x).isdigit())] #Remove non-integers from Issue_ID
        self.data = self.data[self.data != "null"] #Remove rows containing "null"
        self.data["Title/Description"] = self.data["Title/Description"].str.replace("quot", "") #Remove "quot"
        self.data["Creation_Date"] = self.data["Creation_Date"].apply(lambda x: int((str(x).split(' ')[0].split('/')[2]) if isinstance(x, basestring) else 0)) #Modify date to just contain year

    def updateByType(self, getType): #For chart type 1 (single line chart)
        self.typeData = self.data[self.data["Importance/Type"] == getType]
        self.uniqueYears = sorted(self.typeData["Creation_Date"].unique())[1:]
        
    def fitLDA(self, nTopics, nTopWords): #Fit LDA model
        topicsList = []
        tdm = textmining.TermDocumentMatrix(tokenizer=textmining.simple_tokenize_remove_stopwords)
        for index, row in self.typeData.iterrows():
            if isinstance(row["Title/Description"], basestring):
                tdm.add_doc(row["Title/Description"])
        temp = list(tdm.rows(cutoff=1))
        vocab = tuple(temp[0])
        X = np.array(temp[1:])
        self.model = lda.LDA(n_topics=nTopics, n_iter=500, random_state=1)
        self.model.fit_transform(X)
        topicWord = self.model.topic_word_  # model.components_ also works
        topWords = nTopWords
        for i, topic_dist in enumerate(topicWord):
            topicWords = np.array(vocab)[np.argsort(topic_dist)][:-topWords:-1]
            topicsList.append(topicWords)
        return topicsList

    def getDataPoints(self, topic, typeID): #Get data points for constructing relevant Chart object
        dataPoints = None
        if typeID == 1: #By time
            dataPoints = dict.fromkeys(self.uniqueYears, 0)
            field = "Creation_Date"
            bufferData = self.typeData
        elif typeID == 2: #By type
            dataPoints = dict.fromkeys(self.uniqueTypes, 0)
            field = "Importance/Type"
            bufferData = self.data
        elif typeID == 3: #By time and type
            dataPoints = dict.fromkeys(self.uniqueYears, 0)
            bufferData = self.data
            for key in dataPoints:
                dataPoints[key] = dict.fromkeys(self.uniqueTypes, 0)
            bufferData = self.data
        for index, row in bufferData.iterrows():
            if (isinstance(row["Title/Description"], basestring)):
                if (any(word in row["Title/Description"] for word in topic)):
                    try:
                        if typeID == 3:
                            dataPoints[row["Creation_Date"]][row["Importance/Type"]] += 1
                        else:
                            dataPoints[row[field]] += 1
                    except:
                        continue
        return dataPoints
