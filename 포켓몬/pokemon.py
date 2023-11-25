'''
개체값: iv
종족값
h: hp(체력)
a: attak(공격)
b: block(방어)
c: contact(특수공격)
d: defense(특수방어)
s: speed(스피드)
'''

import random
import skills

class Pokemon:
    def __init__(self):
        raise NotImplementedError("능력치 정의할 것!")

    def is_alive(self):
        return self.h > 0

    def __str__(self):
        return self.name

#모부기
class Turtwig(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "모부기"
        self.h = int(((55 * 2) + iv) * 0.5 + 60)
        self.a = int(((68 * 2) + iv) * 0.5 +5)
        self.b = int(((64 * 2) + iv) * 0.5 +5)
        self.c = int(((45 * 2) + iv) * 0.5 +5)
        self.d = int(((55 * 2) + iv) * 0.5 +5)
        self.s = int(((31 * 2) + iv) * 0.5 +5)
        #기술: 지진, 깨물어부수기, 칼춤, 스톤샤워
        self.skill = [skills.Earthquake(), skills.Crunch(), skills.Swords_Dance(), skills.Rock_Slide()]
        

#불꽃숭이
class Chimchar(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "불꽃숭이"
        self.h = int(((44 * 2) + iv) * 0.5 + 60)
        self.a = int(((58 * 2) + iv) * 0.5 +5)
        self.b = int(((44 * 2) + iv) * 0.5 +5)
        self.c = int(((58 * 2) + iv) * 0.5 +5)
        self.d = int(((44 * 2) + iv) * 0.5 +5)
        self.s = int(((61 * 2) + iv) * 0.5 +5)
        #기술: 인파이트, 지진, 스톤샤워, 플레어드라이브
        self.skill = [skills.Close_Combat(), skills.Earthquake(), skills.Rock_Slide(), skills.Flare_Blitz()]

#팽도리
class Piplup(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "팽도리"
        self.h = int(((53 * 2) + iv) * 0.5 + 60)
        self.a = int(((51 * 2) + iv) * 0.5 +5)
        self.b = int(((53 * 2) + iv) * 0.5 +5)
        self.c = int(((61 * 2) + iv) * 0.5 +5)
        self.d = int(((56 * 2) + iv) * 0.5 +5)
        self.s = int(((40 * 2) + iv) * 0.5 +5)
        #기술: 파도타기, 하이드로펌프, 풀묶기, 아쿠아제트
        self.skill = [skills.Surf(), skills.Hydro_Pump(), skills.Grass_Knot(), skills.Aqua_Jet()]

#크랩
class Crabby(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "크랩"
        self.h = int(((30 * 2) + iv) * 0.5 + 60)
        self.a = int(((105 * 2) + iv) * 0.5 +5)
        self.b = int(((90 * 2) + iv) * 0.5 +5)
        self.c = int(((25 * 2) + iv) * 0.5 +5)
        self.d = int(((25 * 2) + iv) * 0.5 +5)
        self.s = int(((50 * 2) + iv) * 0.5 +5)
        #기술: 아쿠아브레이크, 엄청난힘, 칼춤, 스톤샤워
        self.skill = [skills.Liquidation(), skills.Superpower(), skills.Swords_Dance(), skills.Rock_Slide()]

#탕구리
class Cubone(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "탕구리"
        self.h = int(((50 * 2) + iv) * 0.5 + 60)
        self.a = int(((50 * 2) + iv) * 0.5 +5)
        self.b = int(((95 * 2) + iv) * 0.5 +5)
        self.c = int(((40 * 2) + iv) * 0.5 +5)
        self.d = int(((50 * 2) + iv) * 0.5 +5)
        self.s = int(((35 * 2) + iv) * 0.5 +5)
        #기술: 지진, 스톤샤워, 칼춤, 플레어드라이브
        self.skill = [skills.Earthquake(), skills.Rock_Slide(), skills.Swords_Dance(), skills.Flare_Blitz()]

#쁘사이저
class Pinsir(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "쁘사이저"
        self.h = int(((65 * 2) + iv) * 0.5 + 60)
        self.a = int(((125 * 2) + iv) * 0.5 +5)
        self.b = int(((100 * 2) + iv) * 0.5 +5)
        self.c = int(((55 * 2) + iv) * 0.5 +5)
        self.d = int(((70 * 2) + iv) * 0.5 +5)
        self.s = int(((85 * 2) + iv) * 0.5 +5)
        #기술: 시저크로스, 인파이트, 지진, 스톤샤워
        self.skill = [skills.X_Scissor(), skills.Close_Combat(), skills.Earthquake(), skills.Rock_Slide()]

#에버라스
class Larvitar(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "애버라스"
        self.h = int(((41 * 2) + iv) * 0.5 + 60)
        self.a = int(((64 * 2) + iv) * 0.5 +5)
        self.b = int(((45 * 2) + iv) * 0.5 +5)
        self.c = int(((50 * 2) + iv) * 0.5 +5)
        self.d = int(((50 * 2) + iv) * 0.5 +5)
        self.s = int(((50 * 2) + iv) * 0.5 +5)
        #기술: 스톤샤워, 깨물어부수기, 지진, 화염방사
        self.skill = [skills.Rock_Slide(), skills.Crunch(), skills.Earthquake(), skills.Flamethrower()]

#피그점프
class Spoink(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "피그점프"
        self.h = int(((60 * 2) + iv) * 0.5 + 60)
        self.a = int(((25 * 2) + iv) * 0.5 +5)
        self.b = int(((35 * 2) + iv) * 0.5 +5)
        self.c = int(((70 * 2) + iv) * 0.5 +5)
        self.d = int(((80 * 2) + iv) * 0.5 +5)
        self.s = int(((60 * 2) + iv) * 0.5 +5)
        #기술: 사이코키네시스, 풀묶기, 에너지볼, 기합구슬
        self.skill = [skills.Psychic(), skills.Grass_Knot(), skills.Energy_Ball(), skills.Focus_Blast()]

#망키
class Mankey(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "망키"
        self.h = int(((40 * 2) + iv) * 0.5 + 60)
        self.a = int(((80 * 2) + iv) * 0.5 +5)
        self.b = int(((35 * 2) + iv) * 0.5 +5)
        self.c = int(((35 * 2) + iv) * 0.5 +5)
        self.d = int(((45 * 2) + iv) * 0.5 +5)
        self.s = int(((70 * 2) + iv) * 0.5 +5)
        #기술: 인파이트, 지진, 스톤샤워, 역린
        self.skill = [skills.Rock_Slide(), skills.Earthquake(), skills.Close_Combat(), skills.Outrage()]

#야돈
class Slowpoke(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "야돈"
        self.h = int(((90 * 2) + iv) * 0.5 + 60)
        self.a = int(((65 * 2) + iv) * 0.5 +5)
        self.b = int(((65 * 2) + iv) * 0.5 +5)
        self.c = int(((40 * 2) + iv) * 0.5 +5)
        self.d = int(((40 * 2) + iv) * 0.5 +5)
        self.s = int(((15 * 2) + iv) * 0.5 +5)
        #기술: 파도타기, 사이코키네시스, 화염방사, 기합구슬
        self.skill = [skills.Flamethrower(), skills.Psychic(), skills.Focus_Blast(), skills.Surf()]

#켄타로스
class Tauros(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "켄타로스"
        self.h = int(((75 * 2) + iv) * 0.5 + 60)
        self.a = int(((100 * 2) + iv) * 0.5 +5)
        self.b = int(((95 * 2) + iv) * 0.5 +5)
        self.c = int(((40 * 2) + iv) * 0.5 +5)
        self.d = int(((70 * 2) + iv) * 0.5 +5)
        self.s = int(((110 * 2) + iv) * 0.5 +5)
        #기술: 난동부리기, 지진, 스톤샤워, 인파이트
        self.skill = [skills.Earthquake(), skills.Close_Combat(), skills.Thrash(), skills.Rock_Slide()]

#밀탱크
class Miltank(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "밀탱크"
        self.h = int(((95 * 2) + iv) * 0.5 + 60)
        self.a = int(((80 * 2) + iv) * 0.5 +5)
        self.b = int(((105 * 2) + iv) * 0.5 +5)
        self.c = int(((40* 2) + iv) * 0.5 +5)
        self.d = int(((70 * 2) + iv) * 0.5 +5)
        self.s = int(((100 * 2) + iv) * 0.5 +5)
        #기술: 누르기, 지진, 스톤샤워, 아이언헤드   
        self.skill = [skills.Rock_Slide(), skills.Earthquake(), skills.Body_Slam(), skills.Iron_Head()]    

#가보리
class Aron(Pokemon):
    def __init__(self):
        iv=random.randint(0, 31)
        self.name = "가보리"
        self.h = int(((53 * 2) + iv) * 0.5 + 60)
        self.a = int(((51 * 2) + iv) * 0.5 +5)
        self.b = int(((53 * 2) + iv) * 0.5 +5)
        self.c = int(((61 * 2) + iv) * 0.5 +5)
        self.d = int(((56 * 2) + iv) * 0.5 +5)
        self.s = int(((40 * 2) + iv) * 0.5 +5)
        #기술: 스톤샤워, 지진, 역린, 깨물어부수기
        self.skill = [skills.Rock_Slide(), skills.Crunch(), skills.Earthquake(), skills.Outrage()]