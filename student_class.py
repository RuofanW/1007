class student():
    def __init__(self, s=None):
        if (s != None):
           self.name = s[0]
           self.age = s[1]
           self.level = s[2]
        else:
           self.name = ''
           self.age = -1
           self.level = -1


    def print_info(self):
        if (self.name != ''):
            print('Name: ',self.name)
            print('Age: ',self.age)
            print('Level: ',self.level)
        else:
            print('No info has been provided')

    def add_info(self,s):
        self.name = s[0]
        self.age = s[1]
        self.level = s[2]
