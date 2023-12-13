import re

if __name__ == '__main__':
    file_to_execute = "../input"
    with open(file_to_execute) as f:
        games = f.read().splitlines()

    id_sum = 0
    for game in games:
        id = re.search(r'Game (\d+):', game).group(1)
        for subset in game.split(';'):
            red = re.search(r'(\d+) red', subset)
            if red and int(red.group(1)) > 12:
                valid = False
                break
            green = re.search(r'(\d+) green', subset)
            if green and int(green.group(1)) > 13:
                valid = False
                break
            blue = re.search(r'(\d+) blue', subset)
            if blue and int(blue.group(1)) > 14:
                valid = False
                break
            valid = True
        if valid:
            id_sum += int(id)

    print(id_sum)
