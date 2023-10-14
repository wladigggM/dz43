from classPoison import *
new_ingredients = []
poison = Poison('целебное', 100, ['подорожник', 'подорожник', 'подорожник'])

while True:
    choice = input('Введите действие: ')
    if choice == '1':
        print(poison.ingredients)  # ['подорожник', 'подорожник', 'подорожник', 'петрушка', 'петрушка']
        poison.checker()
    elif choice == '2':
        ingredients = input('Введите новые ресурсы: ')
        new_ingredients.append(ingredients)
        poison.edit_ingredients(new_ingredients)
        print(poison.ingredients)  # ['подорожник', 'петрушка', 'черемуха']
