import items
import pokemon
class Player:
    def __init__(self):
        self.bag = [items.Monster_ball(), 
                    items.Monster_ball(),
                    items.Monster_ball(),
                    items.Monster_ball(),
                    items.Monster_ball(),
                    items.Potion(),
                    items.Potion(),
                    items.Potion()]

        self.gold = 10000
        self.pokemon_list = []
        self.victory = False
        self.npc_win = False


    def choose(self, pokes):
        for i, poke in enumerate(pokes, 1):
            print("{}. {}".format(i, str(poke)))
        c = int(input("스타팅포켓몬 선택: "))
        a = pokes[c-1]
        self.pokemon_list.append(a) 

    def print_pokemon(self):
        print("내 포켓몬:")
        for i, poke in enumerate(self.pokemon_list, 1):
            print("{}. {}".format(i, str(poke)))
        print()
        
    def print_bag(self):
        print("가방:")
        print("gold:", self.gold)
        for i, item in enumerate(self.bag, 1):
            print("{}. {}".format(i, str(item)))
        print()
        
