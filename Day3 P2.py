with open("day3data.txt") as file:
    test_data = file.read()

def total_output_joltage_2(battery_string, num_digits):
    batteries = battery_string.split("\n")
    total_output_joltage = 0
    for bank in batteries:
        digits = ""
        first_index = 0
        for i in range(num_digits):
            bank_to_check = bank[first_index:i+1-num_digits] if i != num_digits-1 else bank[first_index:]
            for power in range(9,0,-1):
                power = str(power)
                if power in bank_to_check:
                    first_index += bank_to_check.index(power) + 1
                    digits += power
                    break
        total_output_joltage += int(digits)
    return total_output_joltage
 
 
 
print(total_output_joltage_2(test_data,12))