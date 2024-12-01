def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip().split("\n")