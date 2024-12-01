def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip().split("\n")
    
def transform_input(parsed_input):
    first_list = []
    second_list = []

    for line in parsed_input:
        elements = line.split()
        first_list.append(int(elements[0]))
        second_list.append(int(elements[1]))

    return first_list, second_list