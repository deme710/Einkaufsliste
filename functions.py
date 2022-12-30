FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as readfile:
        old_todos = readfile.readlines()
    return old_todos


def write_todos(todos_arg, filepath=FILEPATH):
    """" Write the to-do items list in the text file."""
    with open(filepath, "w") as write_file:
        write_file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")