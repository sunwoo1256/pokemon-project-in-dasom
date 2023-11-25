'''
지진
깨물어부수기
칼춤
스톤샤워
인파이트
플레어드라이브
파도타기
하이드로펌프
풀묶기
아쿠아제트
아쿠아브레이크
엄청난힘
시저크로스
화염방사
사이코키네시스
에너지볼
기합구슬
역린
난동부리기
누르기
아이언헤드
'''
class Skill:
    def __init__(self):
        raise NotImplementedError("이름, 데미지")

    def __str__(self):
        return self.name

class Earthquake(Skill):    #물리
    def __init__(self):
        self.name = "지진"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage

class Crunch(Skill):    #물리
    def __init__(self):
        self.name = "깨물어부수기"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage
    
class Swords_Dance(Skill):  #특수
    def __init__(self):
        self.name = "칼춤"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.c / 50) / p2.d) + 2)
        return self.damage


class Rock_Slide(Skill):    #물리
    def __init__(self):
        self.name = "스톤샤워"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage


class Close_Combat(Skill):  #물리
    def __init__(self):
        self.name = "인파이트"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage


class Flare_Blitz(Skill):  #물리
    def __init__(self):
        self.name = "플레어드라이브"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage

class Surf(Skill):  #특수
    def __init__(self):
        self.name = "파도타기"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.c / 50) / p2.d) + 2)
        return self.damage

class Hydro_Pump(Skill):   #특수
    def __init__(self):
        self.name = "하이드로펌프"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.c / 50) / p2.d) + 2)
        return self.damage

class Grass_Knot(Skill):   #특수
    def __init__(self):
        self.name = "풀묶기"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.c / 50) / p2.d) + 2)
        return self.damage

class Aqua_Jet(Skill):   #특수
    def __init__(self):
        self.name = "아쿠아제트"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.c / 50) / p2.d) + 2)
        return self.damage

class Liquidation(Skill):  #물리
    def __init__(self):
        self.name = "아쿠아브레이크"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage

class Superpower(Skill):  #물리
    def __init__(self):
        self.name = "엄청난힘"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage
    
    
class X_Scissor(Skill):  #물리
    def __init__(self):
        self.name = "시저크로스"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage
    
class Flamethrower(Skill):   #특수
    def __init__(self):
        self.name = "화염방사"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.c / 50) / p2.d) + 2)
        return self.damage
    
class Psychic(Skill):   #특수
    def __init__(self):
        self.name = "사이코키네시스"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.c / 50) / p2.d) + 2)
        return self.damage
    
class Energy_Ball(Skill):   #특수
    def __init__(self):
        self.name = "에너지볼"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.c / 50) / p2.d) + 2)
        return self.damage

class Focus_Blast(Skill):   #특수
    def __init__(self):
        self.name = "기합구슬"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.c / 50) / p2.d) + 2)
        return self.damage

class Outrage(Skill):  #물리
    def __init__(self):
        self.name = "역린"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage

class Thrash(Skill):  #물리
    def __init__(self):
        self.name = "난동부리기"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage

class Body_Slam(Skill):  #물리
    def __init__(self):
        self.name = "누르기"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage


class Iron_Head(Skill):  #물리
    def __init__(self):
        self.name = "아이언헤드"

    def attack(self, p1, p2):
        self.damage = int(((22 * 100 * p1.a / 50) / p2.b) + 2)
        return self.damage


