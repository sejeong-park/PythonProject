# 파이썬 클래스
# OOP (객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 예제 1
class Dog: # 모든 클래스는 object를 상속
    # 클래스 속성
    species = 'firstdog'

    # 모든 클래스는 초기화 메소드를 가짐 -> 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Dog)

# 인스턴스화
a = Dog('mikky',2)
b = Dog('baby', 3)
c = Dog('baby', 3)
# 비교
print(a == b,b==c, id(a), id(b), id(c))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인    -> 각 인스턴스에 속해있는 속성값을 확인할 수 있음(직접 접근)
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

# 직접접근
print(Dog.species)  # 클래스로 바로 접근 가능
print(a.species)    # 인스턴스화된 변수로도 바로 접근 가능
print(b.species)


class Car:
    # 클래스의 생성자
    def __init__(self, name, color):
        self.name = name
        self.color = color

    #클래스의 메소드
    def show_info(self):
        print("이름:", self.name, "/색상: ", self.color)

    # Setter 메소드
    def set_name(self, name):
        # 이름을 바꾸는! 값을 변경하는
        self.name = name    # name으로 받는 매개변수를 통해 이름을 바꾸겠다!

    # 클래스 소멸자 -> 메모리 할당 해제
    def __del__(self):
        print('인스턴스를 소멸시킵니다.')

car1 = Car('소나타','빨간색')
car1.show_info()

print(car1.name, "을(를) 구매했습니다!")

car1.set_name('세정')
print(car1.name, "을(를) 구매했습니다!")

del car1 # car1 처리가 끝난 후에 메모리 상에 할당을 해제하기 위해 소멸자를 출력하도록
# 성공적으로 제거까지 이루어짐

