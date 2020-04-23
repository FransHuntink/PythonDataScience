import random
from random import randrange
import numpy as numpy

class DataGenerator():
    
    # Generator methods that
    # generate meta data
    def GenerateName(self):
        return "Sten Dreundam"

    def GenerateEmail(self):
        name = self.GenerateName()
        return name + "@gmail.com"

    def Gender(self):
        num = random.uniform(0, 1)
        if(num > 0.5):
            return 'male'
        else:
            return 'female' 

    def GenerateAge(self):
        num = random.randint(18, 50)
        return num

    def GeneratePhone(self):
        return 59483733637

    # Generator methods that generate
    # personality indicators based on the
    # 'big five' personality indicators
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

    # The following preferences indicate personal preference
    # towards topics that could potentially be relevant for
    # matching two people in-app

    # Generate a number (0-2) based on a distribution
    # that indicates gender interested in where:
    # 0 = heterosexual
    # 1 = gay
    # 2 = bi 
    # 3 = other
    def Sexuality(self, asString):
        num = numpy.random.choice(numpy.arange(0, 4), p=[0.7, 0.2, 0.05, 0.05])
        
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

    # Generate a number (0-2) based on a distribution
    # that indicates the preference of stance on drugs
    # 0 = Not into pets
    # 1 = Neutral
    # 2 = Very much into pets
    def PetsPreference(self, asString):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.2, 0.5, 0.3])

        if(asString == False):
            return num
        else:
            if(num == 0):
                return "opposed"
            elif(num == 1):
                return "neutral"
            else:
                return "enthousiast"


    # Generate a number (0-2) based on a distribution
    # that indicates the preference of stance on drugs
    # 0 = Opposed to any drug use
    # 1 = Neutral 
    # 2 = Okay with soft and hard drugs
    def DrugsPreference(self, asString):
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
    
    # Generate a number (0-4) based on a distribution
    # that indicates the preference of sports
    # 0 = Not into sports
    # 1 = Somewhat into spots
    # 2 = Sport enthousiast

    def SportsPreference(self, asString):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.3, 0.4, 0.3])

        if(asString == False):
            return num
        else:
            if(num == 0):
                return "none"
            elif(num == 1):
                return "neutral"
            elif(num == 2):
                return "enthousiast"

    # Generate a number (0-2) based on a distribution
    # that indicates the preference of physique
    # 0 = Does not work out
    # 1 = Neutral (1-2x per week)
    # 2 = Frequently works out ( > 2x per week)
    def WorkoutPreference(self, asString):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.4, 0.2, 0.4])

        if(asString == False):
            return num
        else:
            if(num == 0):
                return "none"
            elif(num == 1):
                return "occasionally"
            elif(num == 2):
                return "enthousiast"
    
    # Generate a number (0-2) based on a distribution
    # that indicates the importance of......TODO
    # def EnvironmentImportance(self, asString):
    # num = numpy.random.choice(numpy.arange(0, 3), p=[0.5, 0.3, 0.2])
    # return num

    # Generate a number (0-2) based on a distribution
    # that indicates whether the person likes traveling where:
    # 0 = Not a traveler
    # 1 = Neutral
    # 2 = Frequent traveler
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



    # Generate a number (0-1) based on a distribution
    # that indicates the preference of stance on drugs
    # 0 = Indoor person
    # 1 = Neutral/neither indoor nor outdoor
    # 2 = Outdoor person
    def GenerateOutdoorsPreference(self, asString):
       num = numpy.random.choice(numpy.arange(0, 3), p=[0.2, 0.6, 0.2])
       if(asString == False):
            return num
       else:
            if(num == 0):
                return "indoor"
            elif(num == 1):
                return "neutral"
            elif(num == 2):
                return "outdoor"


    # generates a number  based on a distribution
    # that indicates the preference on smoking
    # where:
    # 0 = does not smoke 
    # 1 = smokes every now and then
    # 2 = heavy smoker
    def SmokingPreference(self, asString):
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

    # Generate a number (0-1) based on a distribution
    # that indicates the preference of type of
    # relationship where:
    # 0 = closed 
    # 1 = open
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

        openness = self.GenerateOpenness()
        conscientiousness = self.GenerateConscientiousness()
        extraversion = self.GenerateExtraversion()
        agreeableness = self.GenerateAgreeableness()
        neuroticism = self.GenerateNeuroticism()

        # Generate preference portion of the data

        pets = self.PetsPreference(True)
        sports = self.SportsPreference(True)
        workout = self.WorkoutPreference(True)
        travel = self.TravelPreference(True)
        outdoors = self.GenerateOutdoorsPreference(True)
        smoking = self.SmokingPreference(True)
        relationship = self.RelationshipPreference(True)

        row = [name, gender, age, sexuality, openness, conscientiousness, extraversion, agreeableness, neuroticism, pets, sports, workout, travel, outdoors, smoking, relationship]

        return row
