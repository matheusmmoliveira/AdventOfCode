file_to_execute = "input"
with open(file_to_execute) as f:
    lines = f.read().splitlines()

numbers_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def find_first_digit(input_line: str) -> str:
    idx = len(input_line) + 1
    for i, c in list(enumerate(input_line)):
        if c.isdigit():
            number = c
            idx = i
            break
    for n in numbers_mapping:
        s_idx = input_line.find(n)
        if s_idx != -1 and s_idx < idx:
            number = numbers_mapping[n]
            idx = s_idx

    return number


def find_last_digit(input_line: str) -> str:
    idx = -1
    for i, c in reversed(list(enumerate(input_line))):
        if c.isdigit():
            number = c
            idx = i
            break
    for n in numbers_mapping:
        try:
            s_idx = input_line.rindex(n)
        except ValueError:
            continue
        if s_idx > idx:
            number = numbers_mapping[n]
            idx = s_idx

    return number


if __name__ == '__main__':
    final_sum = 0
    for line in lines:
        first_digit = find_first_digit(line)
        second_digit = find_last_digit(line)
        final_sum += int(first_digit + second_digit)
        print(int(first_digit + second_digit), final_sum)

    # print(final_sum)
