import pokemon
import items

class Npc:
    def __init__(self):
        raise NotImplementedError("이름 정의")

    def __str__(self):
        return self.name

class Policeman(Npc):
    def __init__(self):
        self.name = "경찰관"
        self.pokemon = pokemon.Larvitar()

class Gambler(Npc):
    def __init__(self):
        self.name = "갬블러"
        self.pokemon = pokemon.Pinsir()


class seller(Npc):
    def __init__(self):
        self.name = "Seller"
        self.sell_list = [items.Monster_ball(), 
                          items.Super_ball(),
                          items.Hyper_ball(),
                          items.Potion(),
                          items.Super_potion(),
                          items.Hyper_potion()]

    def print_sell_list(self):
        print("판매목록:")
        for i, item in enumerate(self.sell_list, 1):
            print("{}. {}: {}".format(i, str(item), item.value))
        
