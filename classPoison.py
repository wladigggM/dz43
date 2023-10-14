inventory = ['подорожник', 'подорожник', 'подорожник']


class Poison:
    def __init__(self, name, price, inventory: list):
        self.name = name
        self.price = price
        self.inventory = inventory

    def item_counter(self):
        counter_podorojnik = 0
        counter_petrushka = 0
        counter_cheremuha = 0
        for item in self.inventory:
            if item == 'подорожник':
                counter_podorojnik += 1
            elif item == 'петрушка':
                counter_petrushka += 1
            elif item == 'черемуха':
                counter_cheremuha += 1
        result = {'подорожник': counter_podorojnik, 'петрушка': counter_petrushka, 'черемуха': counter_cheremuha}
        return result

    def checker(self):
        if self.item_counter()['подорожник'] >= 3:
            print('"ЦЕЛЕБНОЕ ЗЕЛЬЕ" можно изготовить')
        else:
            print("Нехватает ресурсов для создания целебного зелье")

        if self.item_counter()['петрушка'] >= 1 and self.item_counter()['подорожник'] >= 2:
            print('Зелье "ПРИЯТЕЛЬ" можно изготовить')
        else:
            print("Нехватает ресурсов для создания зелья ПРИЯТЕЛЬ")

        if self.item_counter()['черемуха'] >= 3 and self.item_counter()['петрушка'] >= 2 \
                and self.item_counter()['подорожник'] >= 1:
            print('Зелье "ПРИЛИВ СИЛ" можно изготовить')
        else:
            print("Нехватает ресурсов для создания зелья ПРИЛИВ СИЛ")


# Задание делалось согласно ТЗ.

my_checker = Poison('зелье', 1000, inventory)

my_checker.checker()
