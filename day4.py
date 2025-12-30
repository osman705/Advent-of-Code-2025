
with open('day4data.txt') as file:
    data = file.read()



lines = data.split('\n')
test_set = [list(line) for line in lines]

accessible_count = 0


for i in range(len(test_set)):
    for j in range(len(test_set[i])):
        if test_set[i][j] == '@':
            count = 0
            
            if j + 1 < len(test_set[i]) and test_set[i][j+1] == '@':
                count += 1
            if j - 1 >= 0 and test_set[i][j-1] == '@':
                count += 1
            if i + 1 < len(test_set) and test_set[i+1][j] == '@':
                count += 1
            if i - 1 >= 0 and test_set[i-1][j] == '@':
                count += 1
            if i - 1 >= 0 and j - 1 >= 0 and test_set[i-1][j-1] == '@':
                count += 1
            if i - 1 >= 0 and j + 1 < len(test_set[i]) and test_set[i-1][j+1] == '@':
                count += 1
            if i + 1 < len(test_set) and j + 1 < len(test_set[i]) and test_set[i+1][j+1] == '@':
                count += 1
            if i + 1 < len(test_set) and j - 1 >= 0 and test_set[i+1][j-1] == '@':
                count += 1

            if count < 4:
                accessible_count += 1

print(accessible_count)      
