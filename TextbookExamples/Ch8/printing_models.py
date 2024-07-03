def print_models(unprinted_designs, completed_models):
    """ Simulate printing each design until none are left """
    while unprinted_designs:
        current = unprinted_designs.pop()
        print(f"Printing {current}...")
        completed_models.append(current)

def show_completed_models(completed_models):
    """ Show all models that were printed """
    
    print("\nShowing all completed models...")
    for model in completed_models:
        print(f"{model.title()} done.")

# initializing varibales
unprinted_design = ['phone case', 'robot pendant', 'dodecahedron' ]
completed_models = []

# sending lists to functions
print_models(unprinted_design, completed_models)
show_completed_models(completed_models)