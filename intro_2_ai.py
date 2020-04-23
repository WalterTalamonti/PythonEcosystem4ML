# Udemy Course: 
# Started: 13-April-2020
# Completed:

 # Bandit Pseudocode
 # Greedy
 # while True:
    # j = argmax(predicted bandit means)
    # x = play bandit j and get reward
    # bandits[j].update_mean(x)
# Epsilon-Greedy
# while True:
    # p = random number in [0,1]
    # if p < epsilon:
        # j = choose a random bandit
    # else:
        # j = argmax(predicted bandit means)
    # x = play bandit j and get reward
    # bandits[j].update_mean(x)

