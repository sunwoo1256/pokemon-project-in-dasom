import random
import npc
import items

class map:
    def battle(self, p1, p2, player):
        while p1.is_alive() and p2.is_alive():
            print("{}은(는) 무엇을 할까".format(p1))
            print("1. 싸운다")
            print("2. 도망간다")
            print("3. 가방")
            print("4. 포켓몬")
            a = int(input())
            if a ==1:
                print("0. 나가기")
                for i, skill in enumerate(p1.skill, 1):
                    print("{}. {}".format(i, str(skill)))
                b = int(input())
                if b==0:
                    continue
                sk = p1.skill[b-1]
                print("{}의 {}!".format(p1, sk))
                p2.h -= sk.attack(p1, p2)
                if p2.is_alive():
                    print("{}의 남은 체력: {}".format(p2, p2.h))
                    sk = p2.skill[b-1]
                    print("{}의 {}!".format(p2, sk))
                    p1.h -= sk.attack(p2, p1)
                    if p1.is_alive():
                        print("{}의 남은 체력: {}".format(p1, p1.h))
                    else:
                        print("{}가 기절했다.".format(p1))
                        a = 4
                else:
                    print("{}를 물리쳤다.".format(p2))
                    player.gold += 500
                    break                    
            if a==2:
                print("{}에게서 도망쳤다".format(p2))
                break
            if a==3:
                print("0. 나가기")
                player.print_bag()
                print("사용할 아이템을 선택하세요: ")
                b = int(input())
                if b==0:
                    continue
                item = player.bag[b-1]
                if isinstance(item, items.Ball):
                    r = random.randint(1, 10)
                    print("{}을 던졌다!".format(item))
                    if r < item.per:
                        player.pokemon_list.append(p2)
                        player.bag.remove(item)
                        print("{}를 잡았다!".format(p2))
                        break
                    else:
                        player.bag.remove(item)
                        print("{}를 놓쳤다!".format(p2))
                if isinstance(item, items.Heal):
                    p1.h += item.heal
                    print("{}의 체력이 회복되었다".format(p1))
                    sk = random.choice(p2.skill)
                    print("{}의 {}!".format(p2, sk))
                    p1.h -= sk.attack(p2, p1)
                    print("{}의 남은 체력: {}".format(p1, p1.h))

            if a==4:
                print("0. 나가기")
                player.print_pokemon()
                
                print("바꿀 포켓몬을 선택하세요.")
                b = int(input())
                if b==0:
                    continue
                p1 = player.pokemon_list[b-1]

            if a not in [1, 2, 3, 4]:
                print("잘못된 입력입니다.")


    def buy(self, player):
        print("가진돈: {}".format(player.gold))
        npc.seller().print_sell_list()
        print("0. 나가기")
        a = int(input("구매할 상품의 번호를 입력: "))
        if a==0:
            return
        item = npc.seller().sell_list[a-1]
        b = int(input("구매할 상품의 수량을 입력: "))
        val = item.value * b
        if(val <= player.gold):
            player.gold -= val
            for i in range(b):
                player.bag.append(item)
                return self.buy(player)
        else:
            print("gold가 부족합니다.")
            return self.buy(player)


    def npc_battle(self, p1, p2, player, rnpc):
        while p1.is_alive() and p2.is_alive():
            print("{}은(는) 무엇을 할까".format(p1))
            print("1. 싸운다")
            print("2. 가방")
            print("3. 포켓몬")
            a = int(input())
            if a ==1:
                print("0. 나가기")
                for i, skill in enumerate(p1.skill, 1):
                    print("{}. {}".format(i, str(skill)))
                b = int(input())
                if b==0:
                    continue
                sk = p1.skill[b-1]
                print("{}의 {}!".format(p1, sk))
                p2.h -= sk.attack(p1, p2)
                if p2.is_alive():
                    print("{}의 남은 체력: {}".format(p2, p2.h))
                    sk = p2.skill[b-1]
                    print("{}의 {}!".format(p2, sk))
                    p1.h -= sk.attack(p2, p1)
                    if p1.is_alive():
                        print("{}의 남은 체력: {}".format(p1, p1.h))
                    else:
                        print("{}가 기절했다.".format(p1))
                        a = 3
                else:
                    print("{}에게서 승리했다.".format(rnpc))
                    player.npc_win = True
                    break                    

            if a==2:
                print("0. 나가기")
                player.print_bag()

                print("사용할 아이템을 선택하세요: ")
                b = int(input())
                if b==0:
                    continue
                item = player.bag[b-1]
                if isinstance(item, items.Ball):
                    print("트레이너와의 배틀에선 사용할 수 없습니다!")
                if isinstance(item, items.Heal):
                    p1.h += item.heal
                    print("{}의 체력이 회복되었다".format(p1))
                    sk = random.choice(p2.skill)
                    print("{}의 {}!".format(p2, sk))
                    p1.h -= sk.attack(p2, p1)
                    print("{}의 남은 체력: {}".format(p1, p1.h))

            if a==3:
                print("0. 나가기")
                player.print_pokemon()
                
                print("바꿀 포켓몬을 선택하세요")
                b = int(input())
                if b==0:
                    continue
                p1 = player.pokemon_list[b-1]

            if a not in [1, 2, 3]:
                print("잘못된 입력입니다.")

    def clear(self, player):
        player.victory = True

        