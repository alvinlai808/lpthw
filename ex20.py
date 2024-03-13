from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

# Each call to f.readline() will read one line from f. 
# After this the f's file pointer will be at the start of the next line.
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape")

rewind(current_file)

print("Let's print three lines:")

# current_line is simply a pointer that needs to be manually updated to accurately represent which line readline() reads from
# readline() automatically moves to the next line
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
