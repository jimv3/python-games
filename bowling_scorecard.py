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
    ball1 = 0
    ball2 = 0
    ball3 = 0

    def get_score(ball, mark, remaining=10):
        val = ''
        score = 0
        choices = [str(x) for x in range(remaining)] + [mark]
        while val not in choices:
            print(f'    Ball {ball} (0-{remaining - 1} or {mark})', end=' ')
            val = input().upper()
        if val == 'X':
            score = 10
        elif val == '/':
            score = remaining
        else:
            score = int(val)
        return score
    ball1 = get_score(1, 'X')
    if ball1 != 10 or frame == 10:
        if ball1 == 10:
            ball2 = get_score(2, 'X')
        else:
            ball2 = get_score(2, '/', 10 - ball1)
    if frame == 10:
        if ball2 == 10 or ball1 + ball2 == 10:
            ball3 = get_score(3, 'X')
        elif ball1 == 10:
            ball3 = get_score(3, '/', 10 - ball2)
    return (ball1, ball2, ball3)


def print_scores(players):
    def calculate_score(scores):
        score = 0
        for f, s in enumerate(scores):
            if f == 9:
                score += sum(s)
            elif f == 8:
                if s[0] == 10:
                    score += 10 + scores[f+1][0] + scores[f+1][1]
                elif sum(s) == 10:
                    score += 10 + scores[f+1][0]
                else:
                    score += sum(s)
            else:
                if s[0] == 10:
                    if scores[f+1][0] != 10:
                        score += 10 + sum(scores[f+1])
                    else:
                        score += 20 + scores[f+2][0]
                elif sum(s) == 10:
                    score += 10 + scores[f+1][0]
                else:
                    score += sum(s)
        return score

    for k, v in players.items():
        s = calculate_score(v)
        print(f'{k} --> {s}')


if __name__ == '__main__':
    current_frame = 1
    number_of_players = get_number_of_players()
    player_names = get_player_names(number_of_players)
    players = {}
    for name in player_names:
        players[name] = [(0, 0, 0) for _ in range(10)]
    while current_frame <= 10:
        print(f'FRAME {current_frame}')
        for name, scores in players.items():
            print(f' >> {name}')
            scores[current_frame - 1] = execute_turn(current_frame)
        current_frame += 1
        print_scores(players)
