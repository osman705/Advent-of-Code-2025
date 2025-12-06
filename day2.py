"""
with open ("day2-datafile.txt") as file:
    data = file.read()


#print(data)

"""


test_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862"

# Adding up all invalid IDs should produce 1227775554 if the test case works correctly

# Format is 11-22 is the first id next id is followed by a comma

#The job is to find all of the invalid IDs that appear in the given ranges.
# Valid id == anything leading with 0 e.g 0101 or anything with a repeated digit within the range i.e from 11-22 we have 11 , 22 as invalid digits. 




"""
Steps i'm thinking currently:

1) split data by commas to get seperate IDs - Done
2) find a way to read the individual lines up until the - seperatator to retrieve my first value, everything after the comma is my second value - Done
3) Check if the first or second value starts with 0 if not then:
3) loop through all values in the first value & second value for each ID 
"""

def split_id(data):
    """ Split data into seperate IDs"""
    id_list = test_data.split(",")
    list_of_id_components = []

    for id in id_list:
        id_components = id.partition("-") # str.partition() - Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator.
        list_of_id_components.append(id_components)
        #print(f"The current id is : {id} , current id breakdown is {list_of_id_components}")
    
    return list_of_id_components




