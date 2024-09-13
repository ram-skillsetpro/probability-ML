# Problem Statement:
# A disease affects 1% of the population. A test for the disease is 99% accurate (true positive rate). 
# The false positive rate is 5%. 
# Calculate the probability that a person who tests positive actually has the disease.
#

# Given values
P_disease = 0.01  # Prior probability of having the disease
P_positive_given_disease = 0.99  # Probability of testing positive given that you have the disease
P_positive_given_no_disease = 0.05  # Probability of testing positive given that you do not have the disease
P_no_disease = 1 - P_disease  # Probability of not having the disease

# Bayes' Theorem
P_disease_given_positive = (P_positive_given_disease * P_disease) / (
    (P_positive_given_disease * P_disease) + (P_positive_given_no_disease * P_no_disease)
)

print(f"Probability of having the disease given a positive test result: {P_disease_given_positive}")
