def score(game):
    result = 0
    frame = 1
    in_the_game = True

    for roll in range(len(game)):
        if game[roll] == '/':
            result += 10 - get_value(game[roll-1])
        else:
            result += get_value(game[roll])

        if frame < 10 and game[roll].upper() in ('X/'):
            result += get_value(game[roll+1])
            if game[roll].upper() == 'X':
                if game[roll+2] == '/':
                    result += 10 - get_value(game[roll+1])
                else:
                    result += get_value(game[roll+2])

        if not in_the_game:
            frame += 1
        if in_the_game:
            in_the_game = False
        else:
            in_the_game = True
        if game[roll].upper() == 'X':
            in_the_game = True
            frame += 1
    return result


def get_value(char):
    if char in ("0123456789"):
        return int(char)
    elif char.upper() in ("X/"):
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
