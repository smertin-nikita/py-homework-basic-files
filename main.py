import os
import collections as c

cook_book = {}
Ingredient = c.namedtuple('Ingredient', ['ingredient_name', 'quantity', 'measure'])

file_path = os.path.join(os.getcwd(), '2.4.files/recipes.txt')
with open(file_path, encoding='utf-8') as f:
    for line in f:
        if line != '\n':
            dishes = line.rstrip('\n')
            cook_book[dishes] = []

            for ingredient in range(int(next(f))):
                ingredient_name, quantity, measure = next(f).rstrip('\n').split(' | ')
                cook_book[dishes].append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })


print(cook_book)
