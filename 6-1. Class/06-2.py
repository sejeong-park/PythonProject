class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print('{}이(가) 공격을 수행합니다. [전투력: {}]'.format(self.name, self.power))

# 특정한 클래스가 다른 클래스를 상속하고자 함
class Monster(Unit):
    # 몬스터 클래스에서 name, power, attack함수를 그대로 사용가능
    def __init__(self, name,power, type):
        self.name = name
        self.power = power
        self.type = type
    # 부모 클래스에는 없지만 자식 클래스에만 있는 경우 -> 부모 클래스에서 사용 불가능
    def show_info(self):
        print("몬스터 이름:", self.name, "/ 몬스터 종류:", self.type)


unit = Unit("홍길동",375)
unit.attack()

monster = Monster("슬라임",10,"초급")
monster.attack()
#-> monster에는 attack함수가 없음에도 불구하고 Unit을 상속받았기 때문에 attack 함수를 사용할 수 있음
monster.show_info()
