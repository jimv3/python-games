MIN_PLAYERS = 1
MAX_PLAYERS = 4


def get_number_of_players():
    number_of_players = 0
    while number_of_players < MIN_PLAYERS or number_of_players > MAX_PLAYERS:
        print(f'How many players ({MIN_PLAYERS} - {MAX_PLAYERS})?', end=' ')
        try:
            number_of_players = int(input())
        except ValueError:
            print('Please enter only numbers')

    return number_of_players


def get_player_names(number_of_players):
    player_names = []
    for i in range(number_of_players):
        print(f'What is the name of bowler {i + 1}?', end=' ')
        player_names.append(input())
    return player_names


def execute_turn(frame):
    ball1 = ''
    ball2 = None
    ball3 = None
    while ball1 not in '0 1 2 3 4 5 6 7 8 9 X'.split():
        print('Ball1 score (0-9 or X)', end=' ')
        ball1 = input().upper()
    while ball1 != 'X' and ball2 not in '0 1 2 3 4 5 6 7 8 9 S'.split():
        print('Ball2 score (0-9 or S)', end=' ')
        ball2 = input().upper()
    if frame == 10 and (ball1 == 'X' or ball2 == 'S'):
        while ball3 not in '0 1 2 3 4 5 6 7 8 9 X'.split():
            print('Ball3 score (0-9 or X)', end=' ')
            ball3 = input().upper()
    return (ball1, ball2, ball3)


if __name__ == '__main__':
    current_frame = 1
    number_of_players = get_number_of_players()
    player_names = get_player_names(number_of_players)
    players = {}
    for name in player_names:
        players[name] = []
    print(players)
    while current_frame <= 10:
        for name, scores in players.items():
            print(f'It is {name}\'s turn')
            scores.append(execute_turn(current_frame))
        current_frame += 1
    print(players)
