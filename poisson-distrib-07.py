# Working with Poisson Distribution
# Problem Statement:
#
# Assume that a call center receives an average of 4 calls per minute. 
# Calculate the probability that exactly 5 calls will be received in a given minute.
#

import scipy.stats as stats

# Given values
average_calls_per_minute = 4
k = 5  # Number of calls

# Poisson probability
P_k_calls = stats.poisson.pmf(k, average_calls_per_minute)

print(f"Probability of receiving exactly 5 calls in a minute: {P_k_calls}")
