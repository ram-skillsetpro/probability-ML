#Problem Statement:
#
# Given a standard deck of 52 cards, calculate the probability of drawing a Queen given that the card drawn is a face card (King, Queen, Jack).


# Total number of face cards (King, Queen, Jack)
face_cards = 3 * 4  # 3 face cards in each suit, 4 suits in total

# Number of Queens
queens = 4  # 4 Queens in total

# Conditional probability
conditional_probability = queens / face_cards

print(f"Probability of drawing a Queen given that the card is a face card: {conditional_probability}")
