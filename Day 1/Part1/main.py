file_to_execute = "../input"
with open(file_to_execute) as f:
    lines = f.read().splitlines()

final_sum = 0
for line in lines:
    number = ""
    for c in line:
        if c.isdigit():
            number += c
            break
    for c in line[::-1]:
        if c.isdigit():
            number += c
            break
    sum += int(number)

print(final_sum)

