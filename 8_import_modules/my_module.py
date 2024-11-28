print('Imported my module....')

text = 'Text String'

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return 1
    return -1