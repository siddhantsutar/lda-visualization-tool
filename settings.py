class Settings:
    def __init__(self):
        self.dir = str
        self.TopicModelType = int
        self.WordsPerTopic = int
        self.Graph = int

    def settings(self):
        settings = open("settings.txt",r+)
        count = 1
        while (count <= 4):
            a = settings.readline()
            if (a != None):
                if (count == 1):
                    self.dir = a
                if (count == 2):
                    self.TopicModelType = int(a)
                if (count == 3):
                    self.WordsPerTopic = int(a)
                if (count == 4):
                    self.Graph = int(a)

                count += 1
                
        settings.close()
        
        
        
        choice = int(5)
        while (choice > 4 or choice < 1):
            choice = int("Enter the number of your choice:\n1.Directory\n2.Topic Model Type\n3.Words Per Topic\n4.Graph\n")
            if (choice > 4 or choice < 1):
                print("You entered an invalid choice. Try again.\n")

            if choice == 1:
                self.dir = str("Enter the name of your output directory.\n")
                

            if choice == 2:
                model_type = int(0)
                while (model_type > 2 or model_type < 1):
                    model_type = int("Enter the number of your choice:\n1.Enhancements\n2.Bugs\n")
                    if (model_type > 2 or model_type < 1):
                        print("Your entered and invalid choice. Try again.\n")
                self.TopicModelType = model_type


            if choice == 3:
                self.WordsPerTopic = int("Enter the number of words per topic.\n")

            if choice == 4:
                trash = 1
                #I don't know what to put here.

            cont = 't'
            while (cont != 'y' or cont != 'n'):
                cont = str("Would you like to continue to modify settings? (y/n)\n")
                if (cont != 'y' or cont != 'n'):
                    print("You entered and invalid choice. Try again. \n")
            if cont == 'y':
                choice = 5

            if cont == 'n':
                choice = 1

        settings = open("settings.txt",w)
        count = 1
        while (count <= 4):
            if (count == 1):
                settings.writeline(self.dir)
            if (count == 2):
                settings.writeline(self.TopicModelType)
            if (count == 3):
                settings.writeline(self.WordsPerTopic)
            if (count == 4):
                settings.writeline(self.Graph)

        settings.close()

        return


                
            
