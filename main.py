import os
import collections as c


def print_cook_book(cook_book):
    for dish in cook_book:
        print(dish)
        for ingredient in cook_book[dish]:
            print('     ', ingredient)
        print()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                shop_list[name] = {
                    'quantity': quantity,
                    'measure': measure
                }
    return shop_list


cook_book = {}
Ingredient = c.namedtuple('Ingredient', ['ingredient_name', 'quantity', 'measure'])

file_path = os.path.join(os.getcwd(), '2.4.files/recipes.txt')
with open(file_path, encoding='utf-8') as f:
    for line in f:
        if line != '\n':
            dish = line.rstrip('\n')
            cook_book[dish] = []

            for ingredient in range(int(next(f))):
                ingredient_name, quantity, measure = next(f).rstrip('\n').split(' | ')
                cook_book[dish].append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })


print_cook_book(cook_book)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
