import doctest


with open ("day2-datafile.txt") as file:
    data = file.read()


#print(data)




test_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862"

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


"""
Steps i'm thinking currently:

Use pytest for this function with asserts for practise.
1) split data by commas to get seperate IDs - Done
2) find a way to read the individual lines up until the - seperatator to retrieve my first value, everything after the comma is my second value - Done
3) Check if the first or second value starts with 0 if not then: - Done
4) range through all values in the starting first value up to second value + 1
5) How would I check for a repeated digit? What if the first half of each string = second half of each string?  e.g 555555 = true , 556557 = false. 77777777 true, 666777 false
 
"""


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
                str_values = str(values)
                str_value_length = len(str(values))
                mid_point = str_value_length // 2
                
                
                if str_values[:mid_point] == str_values[mid_point:]: #Check if the first half and second half of the string are the same if so this is an invalid didgit
                    number_of_invalid_values += 1
                list_of_invalids.append(int(str_values))
           
    sum_of_correct_values = sum(list_of_invalids)
                    
                            
    return sum_of_correct_values




#print(check_repeated_digits(better_split_id(data)))
#print(split_id(test_data))
