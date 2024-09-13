import random
#
# Problem-Statement:
# If a six sided die rolled 100000 times then:
#  - Calculate the probability of rolling a 4 on a six-sided die.
#  - Calculate the probability of rolling an even number on a six-sided die.
#

# Simulate rolling a die 100,000 times
die_rolls = [random.randint(1, 6) for _ in range(100000)]

# Probability of rolling a 4
probability_of_4 = die_rolls.count(4) / len(die_rolls)

# Probability of rolling an even number
even_numbers = [2, 4, 6]
probability_of_even = sum([die_rolls.count(x) for x in even_numbers]) / len(die_rolls)

print(f"Probability of rolling a 4: {probability_of_4}")
print(f"Probability of rolling an even number: {probability_of_even}")
