import pandas as pd
travel = pd.read_csv("first_years_dataset_2.csv")
type(travel)

field_age = travel['Age']
field_age = field_age.apply (pd.to_numeric, errors='coerce')       #for dropping all the elements with NaN values
field_age = field_age.dropna()

print("dataset with no NaN value in Age column: ")
print(field_age)
print(" \n")
print("The mean of all the ages is: ")
print(field_age.mean())