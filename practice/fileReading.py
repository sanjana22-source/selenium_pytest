def readTextFile(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
filepath= "example1.txt"
readTextFile(filepath)



#memory efficient way to read large files without loading the entire content into memory at once
def readTextFileLineByLine(filepath):
    try:
        with open(filepath, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")

filepath= "example2.txt"
readTextFileLineByLine(filepath)

#readline() method reads a single line from the file each time it is called, which can be useful for processing large files line by line without loading the entire content into memory at once.
#readlines() method returns a list of lines in the file, which can be useful for small files but may not be efficient for large files as it loads the entire content into memory at once.
def readTextFileLine(filepath):
    with open(filepath, "r") as file:
        line = file.readline()
        line2 = file.readline()
    print(line,line2)
filepath= "example2.txt"
readTextFileLine(filepath)



def readTextFileLines(filepath):

    with open(filepath, "r") as file:
        lines = file.readlines()
    print(lines)

filepath= "example2.txt"
readTextFileLines(filepath)



def count_lines(file_path):
    count = 0
    with open(file_path, "r") as file:
        for _ in file:
            count += 1
    return count

file_path = "example2.txt"
line_count = count_lines(file_path)
print(f"The file '{file_path}' has {line_count} lines.")