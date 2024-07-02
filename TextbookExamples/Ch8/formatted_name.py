def formatted_name(first, last, middle = ''):
    if middle:
        full = f"{first.title()} {middle.title()} {last.title()}"    
    else:
        full = f"{first.title()} {last.title()}"

    return full

# no middle name
name = formatted_name('jimi', 'hendrix')
print(name)

# with middle name
name = formatted_name('booker', 'washington', 't.')
print(name)
