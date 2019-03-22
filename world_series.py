'''
Probability Predictor
Evaluates probability of winning w games in a series of n games
Requires the input of the number of games in series n and
the probability of winning one game p
Assumes that p is the same for each game
'''


# world series function accepts number of games in series and win probability
def world_series(n, p):

    # number of wins needed to win the series
    wins = n//2 + 1
    q = 1 - p

    # build probability matrix
    P = [1 for i in range(wins + 1)]
    P[0] = 0

    # calculate matrix
    for i in range(1, wins + 1):
        for j in range(1, wins + 1):
            P[j] = p*P[j] + q*P[j-1]

    return P[j]


# get the parameters from the user
games = input('\nEnter the number of games in the series: \n')
probability = input('\nEnter the chances of your team winning as a positive decimal less than or equal to one: \n')

chances = world_series(int(games), float(probability))

print('\n Your team will play in a '
      + str(games) + ' game series with a '
      + str(probability)
      + ' probability of winning each game.')
print('\n Their chances of winning the series is: '
      + str(round(chances, 2))
      + ' out of 1')
