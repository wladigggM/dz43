class Poison:
    def __init__(self, name, price, ingredients: list):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def item_counter(self):
        counter_podorojnik = 0
        counter_petrushka = 0
        counter_cheremuha = 0
        for item in self.ingredients:
            if item == 'подорожник':
                counter_podorojnik += 1
            elif item == 'петрушка':
                counter_petrushka += 1
            elif item == 'черемуха':
                counter_cheremuha += 1
        result = {'подорожник': counter_podorojnik, 'петрушка': counter_petrushka, 'черемуха': counter_cheremuha}
        return result

    def checker(self):
        if self.name == 'целебное':
            if self.item_counter()['подорожник'] >= 3:
                print('"ЦЕЛЕБНОЕ ЗЕЛЬЕ" было изготовлено')
                for i in range(3):
                    self.ingredients.remove('подорожник')

            else:
                print("Нехватает ресурсов для создания целебного зелье")
        elif self.name == 'приятель':
            if self.item_counter()['петрушка'] >= 1 and self.item_counter()['подорожник'] >= 2:
                print('Зелье "ПРИЯТЕЛЬ" было изготовленно')
                self.ingredients.remove('петрушка')
                for i in range(2):
                    self.ingredients.remove('подорожник')
            else:
                print("Нехватает ресурсов для создания зелья ПРИЯТЕЛЬ")
        elif self.name == 'прилив':
            if self.item_counter()['черемуха'] >= 3 and self.item_counter()['петрушка'] >= 2 \
                    and self.item_counter()['подорожник'] >= 1:
                print('Зелье "ПРИЛИВ СИЛ" было изготовленно')
                for i in range(3):
                    self.ingredients.remove('черемуха')
                for i in range(2):
                    self.ingredients.remove('петрушка')
                self.ingredients.remove('подорожник')
            else:
                print("Нехватает ресурсов для создания зелья ПРИЛИВ СИЛ")

    def edit_ingredients(self, new_ingredients: list):
        self.ingredients = new_ingredients

# Задание делалось согласно ТЗ.

# my_checker = Poison('зелье', 1000, my_inventory)
#
# my_checker.checker()
