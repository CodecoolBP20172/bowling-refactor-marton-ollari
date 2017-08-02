def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        result += check_spare(game, i)
        if frame < 10 and game[i] in ['x', 'X', '/']:
            if game[i].lower() == 'x':
                result += check_spare(game, i+2)
            result += get_value(game[i+1])
        if not in_first_half or game[i].lower() == 'x':
            frame += 1
            in_first_half = True
        else:
            in_first_half = False
    return result


def check_spare(game, spare):
    if game[spare] == '/':
        return (10 - get_value(game[spare-1]))
    else:
        return get_value(game[spare])


def get_value(char):
    if char.isdigit():
        return int(char)
    elif char in ['x', 'X', '/']:
        return 10
    return 0
