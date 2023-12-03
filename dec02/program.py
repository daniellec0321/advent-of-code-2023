if __name__ == '__main__':
    
    # Puzzle 1
    sum = 0
    f = open('input.txt', 'r')

    for game_id, line in enumerate(list(map(lambda l: l.rstrip(), f.readlines()))):
        # Split line by colons and semicolons
        temp, games = [x.strip() for x in line.split(':')]
        games = [x.strip() for x in games.split(';')]
        
        # Loop through games
        goodRound = True
        for game in games:
            # Split line by commas
            rounds = [x.strip() for x in game.split(',')]
            for round in rounds:
                num, color = [x.strip() for x in round.split(' ')]
                if ((color == 'blue') and (int(num) > 14)) or \
                    ((color == 'green') and (int(num) > 13)) or \
                    ((color == 'red') and (int(num) > 12)):
                    goodRound = False
                    break
            if not goodRound:
                break

        if goodRound:
            sum += (game_id+1)
    
    f.close()
    print(f'The answer to question 1 is {sum}')

    # Puzzle 2
    sum = 0
    f = open('input.txt', 'r')

    for game_id, line in enumerate(list(map(lambda l: l.rstrip(), f.readlines()))):
        # Split line by colons and semicolons
        temp, games = [x.strip() for x in line.split(':')]
        games = [x.strip() for x in games.split(';')]
        max_amounts = {'red': 0, 'green': 0, 'blue': 0}
        
        # Loop through games
        for game in games:
            rounds = [x.strip() for x in game.split(',')]
            for round in rounds:
                num, color = [x.strip() for x in round.split(' ')]
                max_amounts[color] = max(max_amounts[color], int(num))

        # Find the power
        product = max_amounts['red'] * max_amounts['green'] * max_amounts['blue']
        sum += product
    
    f.close()
    print(f'The answer to question 2 is {sum}')