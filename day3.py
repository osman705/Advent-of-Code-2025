
with open("day3data.txt") as file:
    data = file.read()


#print(data)


def find_largest_joltage(data):
    """
    Break data into a list of strings(banks), each bank is composed of batteries(chars)
    
    :param data: Description is a list of strings.
    returns: Int: Total of all (top 2 batteries in each bank)
    """

    total = 0

    list_of_individual_banks = data.split('\n') 
    banks_of_individual_int_batteries = []
    current_bank = []

    for bank in list_of_individual_banks:
        for battery in bank:
            current_bank.append(int(battery))
        
        banks_of_individual_int_batteries.append(current_bank)
        current_bank = []

    for batteries in banks_of_individual_int_batteries:
        if batteries[-1] != max(batteries):
            index_of_first_largest = batteries.index(max(batteries))
            largest_num = max(batteries)
            total += largest_num * 10 
            
            second_largest = max(batteries[index_of_first_largest + 1:])
            total += second_largest
            
        else:
            largest_num = batteries[-1]
            total += largest_num 
            total += max(batteries[:-1]) * 10 
    

    return total



#print(find_largest_joltage(data))
