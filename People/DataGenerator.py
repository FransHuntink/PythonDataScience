import random
from random import randrange
import numpy as numpy

class DataGenerator():

    def GenerateName(self):
        return "Sten Druifdam"

    def GenerateEmail(self):
        name = self.GenerateName()
        return name + "@gmail.com"

    def GenerateGender(self):
        num = random.uniform(0, 1)
        if(num > 0.5):
            return 'male'
        else:
            return 'female' 

    def GenerateAge(self):
        return 12

    def GeneratePhone(self):
        return 59483733661737

    # Generate personality indicators
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




    # Generate personal preferences that
    # say something about what a user is looking
    # for in a partner


    # Generate sexual preference where:
    # 0: men
    # 1: female
    # 2: bi
    # TODO: Make this correspond to gender of user, so that
    # for example being interested in men is less likely 
    # for a male user than being straight
    def GenerateSexualPreference(self):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.33, 0.33, 0.33])
        return num
    
    # Describes whether a person wants pets or 
    # not 
    def GeneratePetsPreference(self):
        num = numpy.random.choice(numpy.arange(0, 2), p=[0.5, 0.5])
        return num

    
    # Generate a number (0-1) based on a distribution
    # that indicates the preference of stance on drugs
    # 0 = Opposed to any drug use
    # 1 = Okay with soft drugs
    # 2 = Okay with soft and hard drugs
    def GenerateDrugsPreference(self):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.5, 0.4, 0.1])
        return num
    
    # Generate a number (0-1) based on a distribution
    # that indicates the preference of sports
    # 0 = Soccer
    # 1 = Hockey
    # 2 = Volleyball
    # 3 = Other
    # 4 = Not into sports
    def GenerateSportsPreference(self):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.4, 0.2, 0.1, 0.1, 0.2])
        return num
    
    # Generate a number (0-1) based on a distribution
    # that indicates the preference of stance on drugs
    # 0 = 
    def GeneratePhysiquePreference(self):
        num = numpy.random.choice(numpy.arange(0, 2), p=[0.5, 0.5])
        return num
    
    def GeneratEnvironmentalPreference(self):
        num = numpy.random.choice(numpy.arange(0, 2), p=[0.5, 0.5])
        return num

    def GenerateTravelingPreference(self):
        num = numpy.random.choice(numpy.arange(0, 2), p=[0.5, 0.5])
        return num
    
    def GenerateOutdoorsPreference(self):
       num = numpy.random.choice(numpy.arange(0, 2), p=[0.5, 0.5])
       return num
    
    # generates a number  based on a distribution
    # that indicates the preference on smoking
    # where:
    # 0 = prefers non-smoker, 
    # 1 = prefers smoker,
    # 2 = doesn't care
    def GenerateSmokingPreference(self, asString):
        num = numpy.random.choice(numpy.arange(0, 3), p=[0.5, 0.3, 0.2])

        # Returns either a string or
        # codified version of this preference
        if(asString == False):
            return num
        else:
            if(num == 0):
                return "nonsmoker"
            elif(num == 1):
                return "smoker"
            else:
                return "either"

    # Generate a number (0-1) based on a distribution
    # that indicates the preference of type of
    # relationship where:
    # 0 = closed 
    # 1 = open
    def GenerateRelationshipPreference(self, asString):
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


