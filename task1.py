with open('recipes.txt') as file:
    cook_book = {}
    for recipy_name in file:
        recipy_name = recipy_name.strip()
        quantity = int(file.readline())
        ingredients = []
        for i in range(quantity):
            ingredient = file.readline().strip()
            name, qty, measure = ingredient.split('|')
            ingredients.append(
                {'ingredient_name': name,
                 'quantity': qty,
                 'measure': measure}
            )
        cook_book[recipy_name] = ingredients
        file.readline()
from pprint import pprint
pprint(cook_book, width=100)
# Task2
def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        for x in range(len(cook_book[dish])):
            item = cook_book[dish][x]
            res[item['ingredient_name']] = {'measure': item['measure'],
                                            'quantity': int(item['quantity']) * person_count}
    return res
print("Список покупок")
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
