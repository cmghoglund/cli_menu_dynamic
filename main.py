import os
import importlib
import inspect

menu_module = importlib.import_module("menu_functions")

def create_menu(module):
    dict_of_functions = dict(inspect.getmembers(module, inspect.isfunction))

    menu = {str(i+1): func for i, func in enumerate(
            sorted(dict_of_functions.values(),
            key=lambda x: inspect.getsourcelines(x)[1]))}

    return menu

def display_menu(menu):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Choose an option (1-{len(menu)}, or 'q' to quit):\n")
    for key, value in menu.items():
        print(f"{key:>2}. {value.__name__.replace('_', ' ').capitalize()}")

menu = create_menu(menu_module)

while True:
    display_menu(menu)

    choice = input(f"\n-> ")

    match choice.lower():
        case 'q':
            print("\nExiting program...\n")
            break
        case key if key in menu:
            menu[key]()
        case _:
            print(f"\nInvalid choice '{choice}'. Please choose a valid option.")

    input("\nPress Enter to continue...")