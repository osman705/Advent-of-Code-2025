
with open("day1data.txt") as file:
    data = file.read()


def parse_instruction(instruction):
    """Extract direction and steps from instruction string like 'R25'"""
    direction = instruction[0]
    steps = int(instruction[1:])
    return direction, steps


def move_dial(current_position, direction, steps):
    """Calculate new position after moving in given direction"""
    if direction == 'R':
        return (current_position + steps) % 100
    else:  # direction == 'L'
        return (current_position - steps) % 100


def count_zero_visits(instructions, starting_position=50):
    """Count how many times we land on 0 following all instructions"""
    current_position = starting_position
    zero_count = 0
    
    for instruction in instructions:
        direction, steps = parse_instruction(instruction)
        current_position = move_dial(current_position, direction, steps)
        
        if current_position == 0:
            zero_count += 1
    
    return zero_count

instructions = data.strip().split('\n')

#print(count_zero_visits(instructions, 50))

