import input

def parse_input():
    return [int(line) for line in input.get_lines('day1')]

parsed_input = parse_input()
    
def number_larger_than_previous(input):
    count = 0
    prev = input[0]
    for i in range(1, len(input)):
        if input[i] > prev:
            count += 1
        prev = input[i]

    return count

print('day 1, part 1: %d' % number_larger_than_previous(parsed_input))

sliding_window_input = list(zip(parsed_input, parsed_input[1:], parsed_input[2:]))
sliding_window_sums = [sum(i) for i in sliding_window_input]

print('day 1, part 2: %d' % number_larger_than_previous(sliding_window_sums))
