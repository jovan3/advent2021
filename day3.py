import input
from collections import Counter

parsed_input = [i.strip() for i in input.get_lines('day3')]

def most_common_bit_in_row(row):
    freq = Counter(row)
    if freq['1'] > freq['0'] or freq['1'] == freq['0']:
        return '1'
    return '0'

def least_common_bit_in_row(row):
    if most_common_bit_in_row(row) == '1':
        return '0'
    return '1'
        
rows = []
for i, bit in enumerate(parsed_input[0]):
    row = [row[i] for row in parsed_input]
    rows.append(row)

gamma = int(''.join([most_common_bit_in_row(i) for i in rows]), 2)
epsilon = int(''.join([least_common_bit_in_row(i) for i in rows]), 2)

print('day 3, part 1: {0}'.format(gamma*epsilon))

def rating(common_bit_fn):
    remaining = parsed_input.copy()
    common = []
    
    for i in range(len(parsed_input[0])):
        if len(remaining) == 1:
            return remaining[0]
        
        row = [row[i] for row in remaining]
        common_bit = common_bit_fn(row)
        common.append(common_bit)
        remaining = [row_item for row_item in remaining if row_item[i] == common_bit]

    return ''.join(common)

print('day 3, part 2: {0}'.format(int(rating(most_common_bit_in_row), 2)*int(rating(least_common_bit_in_row), 2)))
