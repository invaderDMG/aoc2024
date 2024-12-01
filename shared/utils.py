def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip().split("\n")
    
def transform_input(parsed_input):
    """
    Transforma la salida de parse_input en dos listas separadas.
    Cada subcadena se separa por espacios o tabulaciones y se distribuye
    en dos listas distintas.

    Args:
        parsed_input (list of str): Lista de cadenas de texto procesadas por parse_input.

    Returns:
        tuple: Dos listas, una con los primeros elementos y otra con los segundos.
    """
    first_list = []
    second_list = []

    for line in parsed_input:
        elements = line.split()
        first_list.append(int(elements[0]))
        second_list.append(int(elements[1]))

    return first_list, second_list