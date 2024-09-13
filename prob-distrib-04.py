# Probability Distribution - Normal Distribution
# Problem Statement:
#
# Generate a normal distribution dataset and calculate the probability of a value being within 1 standard deviation from the mean.
# 

import numpy as np
import scipy.stats as stats

# Generate a normal distribution dataset
mean = 0
std_dev = 1
data = np.random.normal(mean, std_dev, 1000)

# Probability of being within 1 standard deviation from the mean
within_one_std_dev = stats.norm.cdf(1, loc=mean, scale=std_dev) - stats.norm.cdf(-1, loc=mean, scale=std_dev)

print(f"Probability of being within 1 standard deviation from the mean: {within_one_std_dev}")
