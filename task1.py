with open('recipes.txt') as file:
    cook_book = {}
    for recipy_name in file:
        name = recipy_name.strip()
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

print(cook_book)
