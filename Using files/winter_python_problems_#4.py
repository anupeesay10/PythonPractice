def average_of_scores(file_name):

    f = open(file_name, "r")
    number_of_players = f.readline()
    number_of_games = f.readline()
    game_count = 0
    score_sum = 0
    number_of_players = int(number_of_players.strip())
    number_of_games = int(number_of_games.strip())
    is_first_name = True
    for line in f.readlines():#should I use f.readlines or f.readline or f.read?
        line = line.strip()
        if len(line) == 0:
            continue #Goes back to the beginning of the for loop when there is a blank line.
        if game_count == 0:
            if is_first_name == False:
                print(name)
                print(score_sum / number_of_games)
                score_sum = 0
            is_first_name = False  #Once each name is read, it will reset and now you will get a new sum and therefore new averages.
            name = line
        else:
            score_sum = score_sum + int(line)

        game_count = (game_count + 1) % (number_of_games + 1)
    print(name)
    print(score_sum / number_of_games)



if __name__ == "__main__":
    average_of_scores("In/winter_python_problems_#4.txt")
