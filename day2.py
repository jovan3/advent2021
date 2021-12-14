import input

parsed_input = [(j, int(k)) for j, k in [i.strip().split(' ') for i in input.get_lines('day2')]]

x = 0
y = 0

for command, dist in parsed_input:
    if command == 'forward':
        x += dist
    elif command == 'down':
        y -= dist
    elif command == 'up':
        y += dist

print('day 2, part 1: %d' % abs(x * y))

x = 0
y = 0
aim = 0

for command, dist in parsed_input:
    if command == 'forward':
        x += dist
        y = y - (aim*dist)
    elif command == 'down':
        aim += dist
    elif command == 'up':
        aim -= dist

print('day 2, part 2: {0}'.format(x*abs(y)))
