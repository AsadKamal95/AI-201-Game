def calculate_state_score(position):
    # we give a positive score to if we are close to player
    if abs(position.index(1) - position.index(2)) in [0, 1, 2, 3]:
        return 100
    elif abs(position.index(1) - position.index(2)) in [4, 5, 6]:
        return 80
    elif abs(position.index(1) - position.index(2)) in [7, 8, 9]:
        return 70
    elif abs(position.index(1) - position.index(2)) in [10, 11, 12]:
        return 60
    elif abs(position.index(1) - position.index(2)) in [13, 14, 15]:
        return 50
    elif abs(position.index(1) - position.index(2)) in [9, 10, 11, 12]:
        return 0
    #we give negative score if we are away from the missile
    elif abs(position.index(1) - position.index(2)) in [13, 14, 15, 16]:
        return -50
    elif abs(position.index(1) - position.index(2)) > 16:
        return -100

def maximize_state_score(x_p):
    #representing our state in list
    position = [0 for x in range(0, 100)]
    #ploting player position in our statelist
    position[int(x_p / 10)] = 2
    currentscore = -10000 #initial score
    bestx_pos = -1 #best x position for our missile could be
    for i in range(len(position)):
        if position[i] != 2:
            position[i] = 1 #1 represents our missile in the state list
            #calculating the score for each state
            score = calculate_state_score(position)
            position[i] = 0
            if score >= currentscore:
                currentscore = score
                #making our current position the best position if our score increases
                bestx_pos = i
    return bestx_pos*10
