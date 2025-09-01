"""
    Task 13:
    Demonstrate local and global scope.
    Create a global variable, and then inside a function,
    create a local variable with the same name. Print both
    to show how local and global scope works.
"""

global_var = "I am global"
def task13_scope_demo():
    local_var = "I am local"
    print("Inside function:", local_var)
    print("Inside function accessing global:", global_var)
