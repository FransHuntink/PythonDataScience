from csv import writer
from DataGenerator import DataGenerator

# Figure out why this doesn't work?
#rom faker import Faker
#fake = Faker()

#fake.name()
# 'Lucy Cechtelar'

generator = DataGenerator()

row_contents = ['Stens Duinderdam','Stentor@gmail.com']

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


name = generator.GenerateName()
email = generator.GenerateEmail()
gender = generator.GenerateGender()
openness = generator.GenerateOpenness()
conscientiousness = generator.GenerateConscientiousness()
extraversion = generator.GenerateExtraversion()
agreeagbleness = generator.GenerateAgreeableness()
neuroticism = generator.GenerateNeuroticism()
sexualPreferences = generator.GenerateSexualPreference()

rel = generator.GenerateRelationshipPreference(True)


print(rel)



#append_list_as_row('data.csv', row)
