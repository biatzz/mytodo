# Custom Function Definition

import os
def get_todos(filepath="mytdo/todos.txt"):
# def get_todos(filepath=os.path.abspath(r"FIles\todos.txt")):
   # os.path.abspath("todos.txt")
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

# def write_todos(todos_arg, filepath=os.path.abspath(r"Files\todos.txt")):
def write_todos(todos_arg, filepath="mytdo/todos.txt"):
    with open(filepath, 'w') as file:
        todos = file.writelines(todos_arg)

if __name__ == "__C2_TodoList_Latest__":
    print("Hello")