#상처약
class Heal:
    def __init__(self):
        raise NotImplementedError("가격, 회복량, 되팔기 정의")

    def __str__(self):
        return self.name

class Potion(Heal):
    def __init__(self):
        self.name = "상처약"
        self.value = 200
        self.resell = 100
        self.heal = 20

class Super_potion(Heal):
    def __init__(self):
        self.name = "좋은상처약"
        self.value = 700
        self.resell = 350
        self.heal = 60

class Hyper_potion(Heal):
    def __init__(self):
        self.name = "고급상처약"
        self.value =1200
        self.resell = 600
        self.heal = 120


#몬스터볼
class Ball:
    def __init__(self):
        raise NotImplementedError("가격 정의")

    def __str__(self):
        return self.name

class Monster_ball(Ball):
    def __init__(self):
        self.name = "몬스터볼"
        self.value = 200
        self.per = 4
        #확률: 40%

class Super_ball(Ball):
    def __init__(self):
        self.name = "수퍼볼"
        self.value = 600
        self.per = 6
        #확률: 60%

class Hyper_ball(Ball):
    def __init__(self):
        self.name = "하이퍼볼"
        self.value = 800
        self.per = 8
        #확률: 80%





