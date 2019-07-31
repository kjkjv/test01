a = f'{"hi":<10}'
print(a)

a = f'{"hi":>10}'
print(a)

a = f'{"hi":^10}'
print(a)

a = f'{"hi":=^10}'
print(a)

a = f'{"hi":!<10}'
print(a)

y=3.1654161
f'{y:0.4f}'
f'{y:10.4f}'

f'{"python":!^12}'
"{0:!^12}".format('python')

a = "hobby"
a.count('b')

a = "python is the best choice"
a.find('b')
a.find('k')
a.find('p')
a.index("k")

",".join('acdf')
",".join(['a', 'v'])

a = "hi"
a.upper()




n = int(input('n:'))+1          # n의 값을 입력하는데 숫자열로 바꿔주고 range를 의식해서 +1로
a = range(1,n)                  # range 범위를 설정
c = 0                           # 리스트 대신 변수로 만들고 싶으면 0의 변수를 만들어준다
for b in a:                     # for 문은 in 과 함께 for 새로운 변수 in 리스트
    if b%3!=0 and b%5!=0 :      # 3의 배수가 아니고 5의 배수가 아니면 true, true가 나오면 바로 밑으로 간다. 나머지는 버림
        c = c+b                 # 나오는 b값에 c값을 계속해서 추가하여 더한다. sum 함수를 사용하지 않아도 괜춘

print(c)


a = [1,2,3]
a
print(a)
a[0]
a[0]+a[2]
a[-1]
a = [1,2,3, ['a','b','c']]
a[0]
a[-1]
a[3]
a[-1][0]
a[-1][1]
a[-1][2]
a = [1,2,['a','b',['life','is']]]
a[2][2][0][0]



for x in range(2,10):
    for y in range(1,10):
        print('{}*{}={} '.format(x,y,x*y))


numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers=[]

for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)
print(odd_numbers)

odd_numbers = [number for number in numbers if number % 2 == 1]


count = 0
while count < 10 :
    count = count + 1
    if count % 2 != 1:
        continue
    print(count)


# while True:
#     name = input("당신의 이름은:")
#     if name =='종료':
#         print('종료합니다.')
#     print('{}님, 안녕하세요?'.format(name))



print('안녕하세요 배송봇입니다.')
print('배송을 위해 개인정보를 수집하겠습니다.')
print('아래의 답변을 적어주세요!')


#  if 문 하고 elif 사이에 다른 문장이 있어서 안됌
while True :
    agree = input('개인정보 수집에 동의합니까? yes/no')
    if agree == 'no':
        print('동의하셔야만 이용이 가능합니다.')
        break
    name = input('성함이 어떻게 되나요?')
    phone = input('{}님, 연락처가 어떻게 되나요?'.format(name))
    agree_phone = input('고객님 {} 이 번호가 맞습니까? yes/no'.format(phone))
    elif agree_phone == 'no':
            print('다시 입력해주세요.')
            break
    else :
        print('주문이 완료되었습니다. 감사합니다')
        break



while True :
    agree = input('개인정보 수집에 동의합니까? yes/no')
    if agree == 'no':
        print('동의하셔야만 이용이 가능합니다.')
        break
    elif agree == 'yes':
        name = input('성함이 어떻게 되나요?')
        phone = input('{}님, 연락처가 어떻게 되나요?'.format(name))

        agree_phone = input('고객님 {} 이 번호가 맞습니까? yes/no'.format(phone))
        while (agree_phone == 'no'):
            print('다시 입력해주세요.')
            phone = input('{}님, 연락처가 어떻게 되나요?'.format(name))
            agree_phone = input('고객님 {} 이 번호가 맞습니까? yes/no'.format(phone))
        print('주문이 완료되었습니다. 감사합니다')
        break
    else:
        print('yes 또는 no 를 입력해주십시오. 저는 이만.')
        break

x = {'name':'홍길동','birth':1128,'age':30}
print(x)

s1 = set([1,2,3])
l1 = list(s1)
type(l1)
l1[0]
t1 = tuple(s1)
type(t1)
t1[0]

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

s1&s2
s1.intersection(s2)

s1|s2
s1.union(s2)

s1-s2
s2-s1
s1.difference(s2)
s2.difference(s1)

s1 = set([1,2,3])
s1.add(4)
s1

s1.update([4,5,6])
s1
s1.add(4)
s1

s1 = set([1,2,3])
s1.remove(3)
s1

a = True
b = False

type(b)
1==1
1>2

a = [1,2,3,4]
while a :
    a.pop()

class Singer:
    def sing(self):
        return 'LALALALAL~'

ricky = Singer()
ricky.sing()


class Boxer():
    def punch(self):
        return '쨉쨉'
hong_man=Boxer()
hong_man.punch()


class Caracer():
    def booster(self):
        return '부우우우우웅'
worhkd = Caracer()
worhkd.booster()


class Pen():
    def monami(self):
        return '스스슥'
bolpen = Pen()
bolpen.monami()

class Computer():
    def hp(self):
        return 'As 가능합니다'
hansung = Computer()
hansung.hp()

init = 초기값을 넣는다.


# ==================================================================================
class FourCal:
    def __init__(self, first, scond):
        self.first = first
        self.scond = scond

    def setdata(self, first, scond):
        self.first = first
        self.scond = scond

    def add(self):
        result = self.first + self.scond
        return result

    def sub(self):
        result = self.first - self.scond
        return result

    def mul(self):
        result = self.first * self.scond
        return result

    def div(self):
        result = self.first / self.scond
        return result


a = FourCal(5, 3)
print(a.first)
print(a.scond)
a.add()
a.mul()
a.div()


class Morefourcal(FourCal):
    pass


a = Morefourcal(1, 2)
a.add()


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.scond
        return result


a = MoreFourCal(2, 3)
a.pow()


class SafeFourCal(FourCal):
    def div(self):
        if self.scond == 0:
            return 0
        else:
            self.first / self.scond


a = SafeFourCal(3, 0)
a.div()

a = FourCal(0, 5)
a.mul()


class Newfourcal(FourCal):
    def mul(self):
        if self.first or self.scond == 0:
            return 'Fail'
        else:
            self.first * self.scond


a = Newfourcal(3, 0)
a.mul()


class Family:
    lastname = '김'


print(Family.lastname)

a = Family
b = Family
print(a.lastname)
print(b.lastname)

Family.lastname = '최'
print(Family.lastname)
print(a.lastname)
print(b.lastname)


class Fridge:
    def __init__(self):
        self.isOpened = False
        self.foods = []

    def open(self):
        self.isOpened = True
        print('냉장고 문을 열었어요')

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print('냉장고 속에 음식이 들어갔네')
        else:
            print('냉장고 문이 닫혔음')

    def close(self):
        self.isOpened = False
        print('냉장고 문을 닫음')


class Food:
    pass


import fridge
f = fridge.Fridge()
apple = fridge.Food()
elephant = fridge.Food()


class Singer:
    def sing(self):
        return 'alalalal'

worhkd = Singer()
worhkd.sing()

worjs = Singer()
worjs.sing()


class Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        print('qowhk',self.name,'asdf',self.color)

    def info(self):
        print('이름',self.name,'색깔',self.color)

worhkd = Cat('재광','검정색')
worhkd2 = Cat('재광','흰색')

print(worhkd.info())
print(worhkd2.info())

print(worhkd.__init__('dfq','fdfq'))


class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{}(나이 {}세)'.format(self.name,self.age)

worhkd= Human('재광','29')
print(worhkd)

# ==================================================================
class Car():
    def __init__(self):
        print('생성자')
        self.car_name = '소나타'
        self.car_drv = '전륜'
        self.car_speed = '0'
        self.car_direction = '앞쪽'
        self.car_fuel = '휘발유'
        self.car_state = '정상'

    def set_car_name(self,name):
        self.car_name = name
        print('차종이 [',self.car_name,']으로 변경되었다.')

    def get_car_name(self):
        return self.car_name

    def set_car_drv(self,drv):
        self.car_drv = drv
        print('자동차의 구동방식이[',self.car_drv,']로 변경')


    def get_car_drv(self):
        return self.car_drv

    def set_car_fuel(self,fuel):
        self.car_fuel = fuel
        print('차의 연료 방식[",self.car_fuel,"]로 변경')

    def get_car_fuel(self):
        return self.car_fuel

    def set_car_state(self,state):
        self.cat_state = state
        print('차 상태[:,self.car_state"]로 변경')

    def get_car_state(self):
        return self.car_state

    def set_car_speed(self,speed):
        self.car_speed = speed
        print('속력이 시속[',self.car_speed,']으로 변경')

    def get_car_speed(self):
        return self.car_speed



    def turn(self,direction):
        self.car_direction = direction
        print('방향이[",self.car_direction,"]으로 변경')

    def stop(self):
        self.car_direction = '정지'
        print('차량 정지')

    def start(self):
        print('차량 시동 걸림')

    def move_forward(self):
        self.car_direction = '앞쪽'
        print('차 출발,",self.car_speed,"입니다')

    def move_backward(self):
        self.car_direction = '뒤쪽'
        print('차량 후진 속도 [,self.car_speed,"]')

    def __del__(self):
        print('[",self.car_name,"]자동차 제거')

a = Car()
print(a.car_drv)
print(a.set_car_drv('후륜'))
print(a.get_car_drv())

def set_car_drv(self, drv):
    self.car_drv = drv
    print('자동차의 구동방식이[', self.car_drv, ']로 변경')


a.set_car_speed(100)
k =a.get_car_speed()
print(k)

# print = 결과값을 변수에 할당을 못함, 출력만 하고 소멸
# return = 변수에 값을 넣을 수 있다, 출력의 의무가 없다,  어딘가에 저장(변수에 할당이 가능)

class FourCal :
    def setdata(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def add(self):
        result = self.a + self.b + self.c
        return result

a = FourCal()
a.setdata(4,2,5)
a.add()

class worhkd:
    def add(self,a,b):
        self.a = a
        self.b = b
        result = self.a + self.b
        return result

tjdqo = worhkd()                   # 할당에 해당하는 class나 메소드는 ()
tjdqo.add(2,3)

class Four:
    def __init__(self,a,b):
        self.a = a
        self.b = b




f = open('새파일.txt','w')
f.close()

f = open('C/바탕화면/새파일.txt','w')
f.close()

f = open('새파일.txt','w',encoding='UTF=8')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open('새파일.txt','r',encoding='UTF=8')
line = f.readline()
print(line)
f.close()

f = open('새파일.txt','r',encoding='UTF=8')
while True:
    line = f.readline()
    if not line : break
    print(line)
f.close()


f = open('새파일.txt','r',encoding='UTF=8')
lines = f.readlines()
for line in lines:
    print(line)
f.close()


f = open("새파일.txt", 'r',encoding='UTF=8')
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
f.close()

# 형식은 리스트로 나온다.


f = open('새파일.txt','a',encoding='UTF=8')
for i in range(11,21):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()


with open('새파일.txt','a') as f:
    f.write('sdklfldsjfalj')


f1 = open("test.txt", 'w')
f1.write("Life is too short")

f2 = open("test.txt", 'r')
print(f2.read())




f = open("새파일.txt", "r",encoding='UTF=8')
while True:
    lines = f.readlines()
    if not lines :
        break
    print(lines,end="")
f.close()


f = open('공격횟수.txt','w')
f.close()


attack = 0
f = open('공격횟수.txt','w',encoding='UTF=8')
while attack<10:
    attack =attack + 1
    data = ('%d번 공격하셨습니다.\n' %attack)
    f.write(data)
f.close()


f = open('공격횟수.txt','r',encoding='UTF=8')
line = f.readline()
print(line)
f.close()

f = open('공격횟수.txt','r',encoding='UTF=8')
while True:
    line = f.readline()
    if not line : break
    print(line)
f.close()


f = open('공격횟수.txt','r',encoding='UTF=8')
while True:
    line = f.readline()
    if not line : break
    print(line)
f.close()

f = open('공격횟수.txt','r',encoding='UTF=8')
data = f.read()
print(data)
f.close


f = open('공격횟수.txt','a',encoding='UTF=8')
for i in range(11,21):
    data = ('%d번 공격하셨습니다.\n'%i)
    f.write(data)
f.close()




f = open('이자.txt','w', encoding='UTF=8')
f.close()

# 코드
f = open('이자.txt','w', encoding='UTF=8')
for i in range(100,1000,100):
    data = '%d원 이자가 쌓였습니다.\n'%i
    f.write(data)
f.close()


money = 0
f = open('이자.txt','w', encoding='UTF=8')
while money < 1000:
    money = money + 100
    data = '%d원 이자가 쌓였습니다.\n'%money
    f.write(data)
f.close()

f = open('이자.txt','r', encoding='UTF=8')
line = f.readline()
print(line)
f.close()

f = open('이자.txt','r', encoding='UTF=8')
lines = f.readlines()
for i in lines:
    if not lines : break
    print(i,end='')
f.close()

f = open('이자.txt','a', encoding='UTF=8')
for i in range(1100,2001,100):
    data = '%d원 이자가 추가 되셨습니다.\n' %i
    print(data)
    f.write(data)                               # 이걸 해야 추가가 된다.
f.close()




# ========================파일 문제 강사 답안=================================

# 파일제어실습문제.py
# class 사용

class Item:
    def __init__(self, itemname, price):
        self.itemname = itemname
        self.price = price
        self.quantity = 0
        self.amount = 0

    def setSaleData(self, quantity, amount):
        self.quantity = quantity
        self.amount = amount
        return

    def setQuantity(self, quantity):
        self.quantity += int(quantity)
        self.CalcAmount()
        return

    def CalcAmount(self):
        self.amount = self.price * self.quantity
        return

    def writeItem(self, f):
        f.write(self.itemname + ' ')
        f.write(str(self.price) + ' ')
        f.write(str(self.quantity) + ' ')
        f.write(str(self.amount) + '\n')
        return

    def __repr__(self):
        return '{0:<10} {1:>5} {2:>3} {3:>8}'. \
            format(self.itemname, self.price, self.quantity, self.amount)


class Sales:
    def __init__(self):
        self.salesInfo = {}
        self.readSalesInfo()

    def readSalesInfo(self):
        try:
            with open('items.txt', 'r') as f:
                while True:
                    data = f.readline()
                    if not data:
                        break
                    itemdata = list(data.split())
                    item = Item(itemdata[0], int(itemdata[1]))
                    item.setSaleData(int(itemdata[2]), int(itemdata[3]))
                    self.salesInfo[item.itemname] = item
        except FileNotFoundError:
            pass

        return

    def saveSalesInfo(self):
        with open('items.txt', 'w') as f:
            for key in self.salesInfo:
                self.salesInfo[key].writeItem(f)
        return

    def registrationItemInfo(self, itemInfo):
        self.salesInfo[itemInfo.itemname] = itemInfo
        return

    def updateItemInfo(self, itemInfo):
        self.salesInfo[itemInfo.itemname] = itemInfo
        return

    def searchItemInfo(self, item):
        return self.salesInfo.get(item)

    def printSalesTable(self):
        with open('salesTable.txt', 'w') as f:
            print('\n\t     {0:*^19}\n'.format(' Sales Table '))
            f.write('\n\t     {0:*^19}\n\n'.format(' Sales Table '))
            for key in self.salesInfo:
                print('\t' + str(self.salesInfo[key]))
                f.write('\t' + str(self.salesInfo[key]) + '\n')


class SalesView:
    def __init__(self):
        self.sales = Sales()

    def menu(self):
        menu = '''
1. 품목 정보 등록
2. 판매 정보 등록
3. 판매 현황표 출력
0. 종료
select menu : '''
        func_dict = {1: self.inputItem, 2: self.inputSaleInfo, 3: self.printSalesTable}

        while True:
            print(menu, end=' ')
            selectMenu = int(input())

            if selectMenu == 0:
                self.sales.saveSalesInfo()
                break
            elif 1 <= selectMenu <= 3:
                func_dict[selectMenu]()
        return

    def inputItem(self):
        print('\n')
        item = input('Input item name : ')
        price = int(input('Input price : '))

        itemInfo = Item(item, price)
        self.sales.registrationItemInfo(itemInfo)
        return

    def inputSaleInfo(self):
        print('\n')
        item = input('Input item name : ')

        itemInfo = self.sales.searchItemInfo(item)
        if itemInfo != None:
            quantity = int(input('Input quantity : '))

            itemInfo.setQuantity(quantity)
            self.sales.updateItemInfo(itemInfo)
        else:
            print('Error : {:<10} not found!!!'.format(item))
        return

    def printSalesTable(self):
        self.sales.printSalesTable()
        return


if __name__ == '__main__':
    salesView = SalesView()
    salesView.menu()



