import csv


def record_action(Players, x, y, layer, facing):
    data = []
    if facing != 'x':
        data = [str(Players), str(x), str(y), str(layer), facing]
    else:
        data = [str(Players), str(x), str(y), str(layer)]
    with open('saved_game.thisisnotavirus', 'a') as f:
        file = csv.writer(f)
        file.writerow(data)


def load_game():
    with open('saved_game.thisisnotavirus', 'r') as f:
        file = csv.reader(f, delimiter=',')
        action = []
        for row in file:
            action.append(list(row))

    return action


def extract_data(action, index):
    facing = ''
    print(index)
    if index < 6:
        facing = action[index][4]
    p_index = int(action[index][0])
    e_index = (p_index + 1) % 2
    x = int(action[index][1])
    y = int(action[index][2])
    layer = int(action[index][3])

    return p_index, e_index, x, y, layer, facing
