import doctest


with open ("day2-datafile.txt") as file:
    data = file.read()


#print(data)


test_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

# Adding up all invalid IDs should produce 1227775554 if the test case works correctly

# Format is 11-22 is the first id next id is followed by a comma

#The job is to find all of the invalid IDs that appear in the given ranges.
# You can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. 
# So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs. 




def split_id(data):
    """ Split data into seperate IDs
    :input param: (data): Data is a long list of strings in the format "11-22,95-115,998-1012,1188511880-1188511890"
    :returns: returns a list of 3-tuples (list_of_id_components) in the format [('11','-','22'), ('95','-','115'), ('998','-','1012')]

    >>> split_id(test_data)
    [('11', '-', '22'), ('95', '-', '115'), ('998', '-', '1012'), ('1188511880', '-', '1188511890'), ('222220', '-', '222224'), ('1698522', '-', '1698528'), ('446443', '-', '446449'), ('38593856', '-', '38593862')]"""
    
    id_list = test_data.split(",")
    list_of_id_components = []

    for id in id_list:
        id_components = id.partition("-") # str.partition() - Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator.
        list_of_id_components.append(id_components)
        #print(f"The current id is : {id} , current id breakdown is {list_of_id_components}")
    
    return list_of_id_components




def better_split_id(data):
    """
    Same functionality as split_id - more pythonic a as a list comprehension. 
    
    :input param: (data): Data is a long list of strings in the format "11-22,95-115,998-1012,1188511880-1188511890"
    :returns: returns a list of 3-tuples in the format [('11','-','22'), ('95','-','115'), ('998','-','1012')]

    >>> better_split_id(test_data)
    [('11', '-', '22'), ('95', '-', '115'), ('998', '-', '1012'), ('1188511880', '-', '1188511890'), ('222220', '-', '222224'), ('1698522', '-', '1698528'), ('446443', '-', '446449'), ('38593856', '-', '38593862')]
    """

    return  [id.partition("-") for id in data.split(",")]



def has_repeated_pattern_twice(value_str):
    """Check if value_str is made of a pattern repeated at least twice"""
    
    length_str = len(value_str)

    # Check all possible pattern lengths from 1 to length //2
    for pattern_length in range(1, (length_str // 2) + 1):
        if length_str % pattern_length == 0:  # Pattern length divides evenly
            pattern = value_str[:pattern_length]
            repetitions = length_str // pattern_length
            
            # Does repeating this pattern recreate the full string?
            if pattern * repetitions == value_str:
                return True # Found a repeated pattern
    
    return False  # No repeated pattern found
    


def check_repeated_digits(list_of_id_components):
    """
    Checks for repeated digits within a 3 - tuple list.
    
    :param (list_of_id_components):  [('11','-','22'), ('332','-','400'), ('222220','-','222224')]
    :returns: sum_of_correct_values(int) : Summing a list of each repeated digit. 
    """
    
    number_of_invalid_values = 0
    list_of_invalids = []   

    for ids in list_of_id_components:
        if ids[0][0] == "0" or ids[2][0] == "0": # If the first character of the first digit string == "0" or the first character of the second digit string == "0" add it to the total invalid values 
            number_of_invalid_values += 1

        else:
            for values in range(int(ids[0]),int(ids[2]) + 1):
                if has_repeated_pattern_twice(str(values)):
                    list_of_invalids.append(int(values))
            
    return(sum(list_of_invalids))


print(check_repeated_digits(better_split_id(test_data)))


