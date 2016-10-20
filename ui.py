import settings.py
import os
#based on notes and stuff document
class UserInterface():

    def __init__(self, file_name, num_topics, data_type, graph_type):

        #initializes file name, topics, data, and graph to the predetermined settings
        #still needs settings class
        self.file_name = settings.getFileName()
        self.num_topics = settings.getNumTopics()
        self.data_type = settings.getDataType()
        self.graph_type = settings.getGraphType()


    def setFileName(name,isdatapath):

        #check for correct file type
        if '.xlsx' not in name:
            print('file must be xlsx file')
            return False
        #If the user does not give a datapath, the datapath is found
        if not isdatapath:
            root=os.walk("C:\users")
            for x in root:
                for y in x[3]:
                    if y==name:
                        name=x[1]+"\\"+y
                        
        #check if file exists
        try:
            #either check for files existance or ask for path
            return True

        #exception if it doesnt exist
        except IOError:
            
            return False


    def setNumTopics(number):

        if number>0:
            self.num_topics = number
        else:
            return False

    def setDataType(choice):

        if choice == 1:
            self.data_type = 'enhancement'
            return True

        if choice == 2:
            self.data_type = 'bug'
            return True

        else:
            print('select 1 or 2')
            return False


    def setGraphType(graph):

        if self.data_type == 'enhancement':
            
            if graph == 1:
                #if user wants graph
                self.graph_type = 'line'

            else:
                #if user does not want graph
                self.graph_type = None

        if self.date_type == 'bug':

            #graph types based on notes and stuff 5b section
            if graph == 1:
                self.graph_type = 'rate'

            if graph == 2:
                self.graph_type = 'severity'

            if graph == 3:
                self.graph_type = 'severityrate'

            else:
                self.graph_type = None

        return

    def displayTopics():
        count = 0
        while count < self.num_topics:
            #prints the top n topics
            #need to adjust print statement
            print('topic')
            count += 1

        return

    def displayBarGraph():

        #call method for creating/displaying bar graph

        return

    def exitGraph():

        #close the graphs
        self.displayTopics()
                
        

        
    
            

    
