import os


def print_cook_book(cook_book):
    for dish in cook_book:
        print(dish)
        for ingredient in cook_book[dish]:
            print('     ', ingredient)
        print()


def print_shop_list(shop_list):
    for ingredient in shop_list.items():
        print(ingredient)
    print()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                if name not in shop_list:
                    shop_list[name] = {}.fromkeys(['measure', 'quantity'], 0)
                shop_list[name]['quantity'] = shop_list[name].get('quantity', 0) + ingredient['quantity'] * person_count
                shop_list[name]['measure'] = ingredient['measure']
    return shop_list


cook_book = {}

file_path = os.path.join(os.getcwd(), 'recipes.txt')
with open(file_path, encoding='utf-8') as f:
    for line in f:
        if line != '\n':
            dish = line.rstrip('\n')
            cook_book[dish] = []

            for ingredient in range(int(next(f))):
                ingredient_name, quantity, measure = next(f).rstrip('\n').split(' | ')
                cook_book[dish].append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })


print_cook_book(cook_book)
print_shop_list(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
