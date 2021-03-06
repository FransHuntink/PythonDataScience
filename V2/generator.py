from random import randrange
from faker import Faker
import numpy as numpy
import random

class DataGenerator():
    
    # Methods that generate meta user data
    def GenerateName(self):
        fake = Faker()
        return fake.name()
        #return "Steen Dreundam"

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
        num = numpy.random.choice(numpy.arange(0, 5), p=[0.2, 0.3, 0.2, 0.1, 0.2])
        return num

    def WorkoutsPerWeek(self):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.3, 0.5, 0.2])

        if(num == 0):
            return 'Never' 
        elif(num == 1):
            return 'Ocassionally'
        elif(num == 2):
            return 'Often'
        


    # Methods that generate categorical/string data
    def Sexuality(self, asString):
        num = numpy.random.choice(numpy.arange(0, 4), p=[0.89, 0.055, 0.025, 0.03])
        
        if(asString == False):
            return num
        else:
            if(num == 0):
                return 'hereosexual' 
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
                return "occasionally"
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


    def GeneratePersonData(self):
        name = self.GenerateName()
        gender = self.Gender()
        sexuality = self.Sexuality(True)
        phone = self.GeneratePhone()
        age = self.GenerateAge()

        # Personality portion of the data

        #openness = self.GenerateOpenness()
       # conscientiousness = self.GenerateConscientiousness()
       # extraversion = self.GenerateExtraversion()
       # agreeableness = self.GenerateAgreeableness()
       # neuroticism = self.GenerateNeuroticism()

        # Generate preference portion of the data

        pets = self.AmountOfPets()
        sports = self.PlaysSports(True)
        workout = self.TravelPreference(True)
        travel = self.TravelPreference(True)
        outdoors = self.OutdoorPreference(True)
        smoking = self.SmokePreference(True)
        relationship = self.RelationshipPreference(True)

        row = [name, gender, age, sexuality, pets, sports, workout, travel, outdoors, smoking, relationship]

        return row
