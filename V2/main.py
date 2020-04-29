from csv import writer
from generator import DataGenerator

# Figure out why this doesn't work?
#rom faker import Faker
#fake = Faker()

#fake.name()
# 'Lucy Cechtelar'

generator = DataGenerator()

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

#rowNames = ['name', 'gender', 'age', 'sexuality', 'openness', 'conscientiousness', 'extraversion', 'agreeableness', 'neuroticism', 'pets', 'sports', 'workout', 'travel', 'outdoors', 'smoking', 'relationshipType']
#append_list_as_row('data.csv', rowNames)

for x in range(0, 15):
    append_list_as_row('data.csv', generator.GeneratePersonData())


