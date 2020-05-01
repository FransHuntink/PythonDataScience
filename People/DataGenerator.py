import random
from random import randrange
import numpy as numpy
from faker import Faker

class DataGenerator():
    

    # Methods that generate meta user data
    def GenerateName(self):
        fake = Faker()
        return fake.name()

    def GenerateEmail(self):
        name = self.GenerateName()
        return name + "@gmail.com"

    def Gender(self):
        num = random.uniform(0, 1)
        if(num > 0.5):
            return 'male'
        else:
            return 'female' 

    def GeneratePhone(self):
        return 59483733637

    # Methods that generate numerical user data
    def GenerateAge(self):
        num = random.randint(18, 50)
        return num

    def GenerateOpenness(self):
        num = random.uniform(0, 1)
        return num

    def GenerateConscientiousness(self):
        num = random.uniform(0, 1)
        return num

    def GenerateExtraversion(self):
        num = random.uniform(0, 1)
        return num

    def GenerateAgreeableness(self):
        num = random.uniform(0, 1)
        return num

    def GenerateNeuroticism(self):
        num = random.uniform(0, 1)
        return num

    def AmountOfPets(self):
        num = numpy.random.choice(numpy.arange(0, 5), p=[0.3, 0.3, 0.2, 0.1, 0.1])
        return num

    def WorkoutsPerWeek(self):
        num = numpy.random.choice(numpy.arange(0, 5), p=[0.2, 0.3, 0.2, 0.1, 0.2])
        return num

    def FacebookFriends(self):
        num = random.randint(30, 1000)
        return num

    # Methods that generate categorical/string data
    def Sexuality(self, asString):
        num = numpy.random.choice(numpy.arange(0, 4), p=[0.89, 0.055, 0.025, 0.03])
        
        if(asString == False):
            return num
        else:
            if(num == 0):
                return 'heterosexual' 
            elif(num == 1):
                return 'gay'
            elif(num == 2):
                return 'bi'
            else:
                return 'other'

    def StanceOnDrugs(self, asString):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.5, 0.4, 0.1])

        if(asString == False):
            return num
        else:
            if(num == 0):
                return "opposed"
            elif(num == 1):
                return "neutral"
            else:
                return "okay"
    
    def PlaysSports(self, asString):
        num = numpy.random.choice(numpy.arange(0, 2), p=[0.6, 0.4])
        if(asString == False):
            return num
        else:
            if(num == 0):
                return "no"
            elif(num == 1):
                return "yes"

    def TravelPreference(self, asString):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.3, 0.5, 0.2])

        if(asString == False):
            return num
        else:
            if(num == 0):
                return "none"
            elif(num == 1):
                return "occasional"
            elif(num == 2):
                return "frequent"

    def OutdoorPreference(self, asString):
       num = numpy.random.choice(numpy.arange(0, 2), p=[0.4, 0.6])
       if(asString == False):
            return num
       else:
            if(num == 0):
                return "indoor"
            elif(num == 1):
                return "outdoor"

    def SmokePreference(self, asString):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.5, 0.3, 0.2])

        # Returns either a string or
        # codified version of this preference
        if(asString == False):
            return num
        else:
            if(num == 0):
                return "nonsmoker"
            elif(num == 1):
                return "occasional"
            else:
                return "heavy"

    def RelationshipPreference(self, asString):
        num = numpy.random.choice(numpy.arange(0, 2), p=[0.9, 0.1])
        
        # Either return a codified value or
        # a string based on the passed parameter
        if(asString == False):
            return num
        else:
            if(num == 0):
                return "closed"
            else:
                return "open"

    def PreviousRelationshipNum(self):
        num = numpy.random.choice(numpy.arange(0, 5), p=[0.1, 0.4, 0.25, 0.2, 0.05 ])
        return num

    def GeneratePersonData(self):

        # Generate meta
        name = self.GenerateName()

        # Personality portion of the data (numerical)
        age = self.GenerateAge()
        openness = self.GenerateOpenness()
        conscientiousness = self.GenerateConscientiousness()
        extraversion = self.GenerateExtraversion()
        agreeableness = self.GenerateAgreeableness()
        neuroticism = self.GenerateNeuroticism()

        # Generate categorical portion of the data  (yes/no data)
        sexuality = self.Sexuality(True)
        gender = self.Gender()
        sports = self.PlaysSports(True)
        travel = self.TravelPreference(True)
        outdoors = self.OutdoorPreference(True)
        smoking = self.SmokePreference(True)
        relationship = self.RelationshipPreference(True)

        # Additional metrics (numerical data)
        prevRelationshipNum = self.PreviousRelationshipNum()
        facebookFriends = self.FacebookFriends()
        workout = self.WorkoutsPerWeek()
        pets = self.AmountOfPets()

        row = [name, gender, age, sexuality, openness, conscientiousness, extraversion, agreeableness, neuroticism, pets, sports, workout, travel, outdoors, smoking, relationship, facebookFriends, prevRelationshipNum]
        
        return row
