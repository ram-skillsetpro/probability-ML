# Conditional Probability with Real-World Dataset
#Problem Statement:
#
# Use the Titanic dataset to calculate the conditional probability of survival given that the passenger was a female.
# Dataset Link: Titanic Dataset (https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)
#

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Conditional probability of survival given that the passenger is female
female_passengers = df[df['Sex'] == 'female']
P_survival_given_female = female_passengers['Survived'].mean()

print(f"Probability of survival given that the passenger is female: {P_survival_given_female}")


