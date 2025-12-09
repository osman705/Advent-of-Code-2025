
with open("day3data.txt") as file:
    data = file.read()


#print(data)



test_data = '987654321111111'



def find_largest_joltage(data):
    """
    Break data into a list of strings(banks) each bank is composed of batteries(chars)
    
    :param data: Description is a list of strings.
    returns: Int: Total of all (top 2 batteries in each bank)
    """

    #How do I find the top two ? I check each bank and split the bank into specific batteries
    # convert the batteries into a integers and sort the list. Add the last two digits together and add to the total
    #move onto the next bank etc until completion. 

    total_jolt_count = 0
    list_of_individual_banks = data.strip().split('\n') 
    list_of_integer_batteries = []
    largest_pairs = []

    for bank in list_of_individual_banks:
        #for battery in bank:
        list_of_integer_batteries.append(int(bank))
        list_of_integer_batteries.sort()
        largest_pairs.append(list_of_integer_batteries[-2:])
    
    
    

    return largest_pairs


#print(find_largest_joltage(data))