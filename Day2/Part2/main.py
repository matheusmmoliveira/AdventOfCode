import re


def get_lowest_number(color_list: list[str]) -> int:
    int_list = [int(i) for i in color_list]
    int_list.sort()
    return int_list[-1]


if __name__ == '__main__':
    file_to_execute = "../input"
    with open(file_to_execute) as f:
        games = f.read().splitlines()

    total_sum = 0
    for game in games:
        red = re.findall(r'(\d+) red', game)
        green = re.findall(r'(\d+) green', game)
        blue = re.findall(r'(\d+) blue', game)
        total_sum += get_lowest_number(red) * get_lowest_number(green) * get_lowest_number(blue)

    print(total_sum)
