import csv


def record_action(Players, x, y, layer):
    with open('saved_game.thisisnotavirus', 'a') as f:
        file = csv.writer(f)
        file.writerow([str(Players), str(x), str(y), str(layer)])


def load_game():
    with open('saved_game.txt', 'r') as f:
        file = csv.reader(f)
        lines = f.readline()
        a = []
        i = 0
        for lines in f:
            a.append(list(lines))
            i += 1

        print(a[0])
        print(type(a[0]))
