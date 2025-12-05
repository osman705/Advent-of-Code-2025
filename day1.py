
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
        dial_amount = (current_position + steps) % 100
        return dial_amount
    else:  # direction == 'L'
        dial_amount = (current_position - steps) % 100
        return dial_amount




def count_zero_visits(instructions, starting_position=50):
    current_position = starting_position
    zero_count = 0
    rotation_count = 0 
    
    for instruction in instructions:
        direction, steps = parse_instruction(instruction)
        old_position = current_position
        
        # Get full rotations and remaining steps
        full_rotations, remaining_steps = divmod(steps, 100)
        rotation_count += full_rotations
        
        # Move the dial
        current_position = move_dial(current_position, direction, steps)
        
        # Check if remaining movement crosses 0 (not lands on it)
        if direction == 'R':
            # Crosses if we go past 99 but don't land exactly on 0
            if old_position + remaining_steps > 99 and (old_position + remaining_steps) % 100 != 0:
                rotation_count += 1

        elif direction == 'L':
            # Crosses if we go below 0 but don't land exactly on 0, and not starting at 0
            if old_position != 0 and old_position - remaining_steps < 0 and (old_position - remaining_steps) % 100 != 0:
                rotation_count += 1
        
        # Count landing exactly on 0
        if current_position == 0:
            zero_count += 1
    
    total_count = zero_count + rotation_count 
    
    return total_count




instructions = data.strip().split('\n')

print(count_zero_visits(instructions, 50))




