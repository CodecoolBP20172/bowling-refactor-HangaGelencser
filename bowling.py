def score(game):
    result = 0
    frame = 1
    in_first_half = True

    for roll in range(len(game)):
        if game[roll] == '/':
            result += 10 - get_value(game[roll-1])
        else:
            result += get_value(game[roll])

        if frame < 10 and get_value(game[roll]) == 10:
            if game[roll] == '/':
                result += get_value(game[roll+1])
            elif game[roll].upper() == 'X':
                result += get_value(game[roll+1])
                if game[roll+2] == '/':
                    result += 10 - get_value(game[roll+1])
                else:
                    result += get_value(game[roll+2])

        if not in_first_half:
            frame += 1
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
        if game[roll].upper() == 'X':
            in_first_half = True
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
