def average_of_scores(file_name):

    f = open(file_name, "r")
    number_of_players = f.readline() #Will read the first line
    number_of_games = f.readline()  #Will read the second line
    game_count = 0
    score_sum = 0
    number_of_players = int(number_of_players.strip())
    number_of_games = int(number_of_games.strip())
    is_first_name = True
    for line in f.readlines(): # f.readline can be set to a variable, f.read can be set to a variable.
        line = line.strip()
        if len(line) == 0:
            continue #Goes back to the beginning of the for loop when there is a blank line.
        if game_count == 0:
            if is_first_name == False: #Why is this a double equal sign and the true statement is a single equal sign?
                print(name)
                print(score_sum / number_of_games)
                score_sum = 0
            is_first_name = False  #Once each name is read, it will reset and now you will get a new sum and therefore new averages.
            name = line
        else:
            score_sum = score_sum + int(line)

        game_count = (game_count + 1) % (number_of_games + 1) #When game count is 0, it is done counting the number of games
    print(name)
    print(score_sum / number_of_games) #Why are these print statements outside of the for loop?



if __name__ == "__main__":
    average_of_scores("Using files/In/winter_python_problems_#4.txt")
