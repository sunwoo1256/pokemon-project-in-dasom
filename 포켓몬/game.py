from player import Player
import pokemon
import map
import random
import npc
import items

player = Player()
mapp = map.map()

map1 = [["O", "w", "w", "w", "w", "w", "w", "w", "w", "S"],
        [" ", " ", "w", "w", " ", "w", "w", "w", "w", "w"],
        [" ", " ", "w", "w", " ", "w", "w", "w", "w", "w"],
        [" ", " ", "w", "w", " ", "w", "w", " ", "w", "w"],
        ["w", " ", "w", "S", " ", "w", " ", "S", " ", "w"],
        ["w", " ", "w", "w", "w", "w", "w", "w", "w", "w"],
        [" ", " ", "w", "w", "w", "w", "w", "w", "w", "w"],
        [" ", "w", "w", "w", "w", "S", "w", "w", "S", " "],
        [" ", "w", "w", "w", "w", "w", "w", "w", " ", "N"],
        ["S", "w", " ", "w", "w", "w", " ", " ", "N", "V"]]


start_pokes = [pokemon.Chimchar(), pokemon.Piplup(), pokemon.Turtwig()]

pokes = [pokemon.Chimchar(), pokemon.Crabby(), 
         pokemon.Aron(), pokemon.Cubone(), 
         pokemon.Larvitar(), pokemon.Mankey(), 
         pokemon.Miltank(), pokemon.Pinsir(), 
         pokemon.Piplup(), pokemon.Slowpoke(), 
         pokemon.Spoink(), pokemon.Tauros(), 
         pokemon.Turtwig()]

npcs = [npc.Gambler(), npc.Policeman()]

def printmap():
    for x in map1:
        for j in x:
            print(j, end=' ')
        print()
    


#####main#####
player.choose(start_pokes)
print("야생 몬스터와 NPC를 물리치고 무사히 Victory 타일에 도착하세요!")
print("현재 나의 위치는 x로 표시됩니다.")
print("O 타일에서 출발합니다!")
printmap()
print()
k = 0
p = 0
while not player.victory:
    print()
    print("w: 위")
    print("a: 왼쪽")
    print("s: 아래")
    print("d: 오른쪽")
    print("b: 가방")
    print("p: 포켓몬")
    a = input("입력: ")
    print()
    b=map1[0][0]
    r=random.randint(0,12)
    if(a == "a"):
        p-=1
        if(p>=0):
            b = map1[k][p]
            map1[k][p] = "x"   
        else:
            p+=1
            print("잘못된 값")

    if(a == "w"):#k-=1
        k-=1
        if(k>=0):
            b = map1[k][p]
            map1[k][p] = "x"
        else:
            k+=1
            print("잘못된 값")

    if(a == "s"):#k+=1
        k+=1
        if(k<=10):
            b = map1[k][p]
            map1[k][p] = "x"
        else:
            k-=1
            print("잘못된 값")

    if(a == "d"):#p+=1
        p+=1
        if(k<=10):
            b = map1[k][p]
            map1[k][p] = "x"
        else:
            p-=1
            print("잘못된 값")
    
    if(a == "b"):
        player.print_bag()
        heal = [item for item in player.bag if isinstance(item, items.Heal)]
        if heal:
            print("상처약을 사용하시겠습니까? y/n")
            ans = input()
            if ans == "y":
                player.print_pokemon()
                print("치유할 포켓몬을 선택하세요")
                ans = int(input())
                po = player.pokemon_list[ans-1]
                for i, item in enumerate(heal, 1):
                    print("{}. {}".format(i, str(item)))
                print("사용할 상처약을 선택하세요.")
                ans = int(input())
                item = heal[ans-1]
                po.h += item.heal
                player.bag.remove(item)

    if(a == "p"):
        player.print_pokemon()

    ##타일부분##

    if(b == "w") and r < 6:
        enemy = pokes[r]
        print("야생의 {}이(가) 나타났다!".format(enemy))
        mapp.battle(player.pokemon_list[0], enemy, player)

    if(b == "S"):
        mapp.buy(player)

    if(b == "N"):
        rnpc = random.choice(npcs)
        print("{}와의 배틀에서 승리하라!".format(rnpc))
        print("{}의 {}이(가) 나타났다.".format(rnpc, rnpc.pokemon))
        mapp.npc_battle(player.pokemon_list[0], rnpc.pokemon, player, rnpc)

    if(b == "V"):
        if player.npc_win:
            mapp.clear(player)
            print("게임 클리어!")
        else:
            print("NPC에게서 승리해야 합니다!")
    
    printmap()
    map1[k][p] = b
