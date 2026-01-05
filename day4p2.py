with open('day4data.txt') as file:
    data = file.read()

def remove_accessible(paper_string):

    paper_lines = paper_string.split("\n")
    accessible = 0
    old_accessible = 100 #Placeholder
    old_paper_lines = paper_lines
    new_paper_lines = []

    while accessible != old_accessible:
        old_accessible = accessible
        for i in range(len(old_paper_lines)):
            line_length = len(old_paper_lines[0])
            new_line = ""
            for j in range(line_length):
                if old_paper_lines[i][j] == ".":
                    new_line += "."
                    continue
                if old_paper_lines[i][j] == "x":
                    new_line += "x"
                    continue
                if (i == len(old_paper_lines)-1 or not i) and (j == line_length-1 or not j):
                    new_line += "x"
                    accessible += 1
                    continue
                if not i:
                    adjacent = [old_paper_lines[i][j-1], old_paper_lines[i][j+1], old_paper_lines[i+1][j-1], old_paper_lines[i+1][j], old_paper_lines[i+1][j+1]]
                elif i == len(old_paper_lines)-1:
                    adjacent = [old_paper_lines[i-1][j-1], old_paper_lines[i-1][j], old_paper_lines[i-1][j+1], old_paper_lines[i][j-1], old_paper_lines[i][j+1]]
                elif not j:
                    adjacent = [old_paper_lines[i-1][j], old_paper_lines[i+1][j], old_paper_lines[i-1][j+1], old_paper_lines[i][j+1], old_paper_lines[i+1][j+1]]
                elif j == line_length-1:
                    adjacent = [old_paper_lines[i-1][j-1], old_paper_lines[i][j-1], old_paper_lines[i+1][j-1], old_paper_lines[i-1][j], old_paper_lines[i+1][j]]
                else:
                    adjacent = [old_paper_lines[i-1][j-1], old_paper_lines[i-1][j], old_paper_lines[i-1][j+1], old_paper_lines[i][j-1], old_paper_lines[i][j+1], old_paper_lines[i+1][j-1], old_paper_lines[i+1][j], old_paper_lines[i+1][j+1]]
                if adjacent.count("@") < 4:
                    accessible += 1
                    new_line += "x"
                else:
                    new_line += "@"
            new_paper_lines.append(new_line)
        old_paper_lines = new_paper_lines
        new_paper_lines = []
    return accessible

print(remove_accessible(data))