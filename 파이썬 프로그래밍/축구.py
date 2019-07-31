# CF, CM, CB, WB, goalkeeper 로 변수 만들어 분류=====================================
f = open('C:/Users/CPB06GameN/Desktop/member.csv','r')
result = f.read()
print(result)

f = open('C:/Users/CPB06GameN/Desktop/member2.csv','r')
result_2 = f.read()
print(result_2)

with open('C:/Users/CPB06GameN/Desktop/member.csv','r') as m :
    while True :
        line = m.readline()
        if not line : break

with open('C:/Users/CPB06GameN/Desktop/member.csv','r') as m :
    header = m.readline()
    header_list = header.split()
    print(header_list)

    CF = []
    CM = []
    CB = []
    WB = []

    while True :
        line = m.readline()
        if not line :
            break
        data_list = m.readline().split(',')
        print(data_list)
        if data_list[1] == 'CF':
            CF.append(data_list)
        elif data_list[1] == 'CM':
            CM.append(data_list)
        elif data_list[1] == 'CB':
            CB.append(data_list)
        else:
            WB.append(data_list)

    print(CF)
    print(CM)
    print(CB)
    print(WB)

f = open('C:/Users/CPB06GameN/Desktop/member2.csv','r')
goalkeeper = f.read()
print(goalkeeper)

# 복잡했던 함수
# ====================[         승부닷!!         ]=======================================
# a_player = []
# b_player = []
#
# a_striking_power = sum(a_player[3:7])
# b_striking_power = sum(b_player[3:7])
#
# a_defense_power = sum(a_player[7:9] + #goalkeeper_ovr)
# b_defense_power = sum(b_player[7:9] + #goalkeeper_ovr)
#
# if a_striking_power > b_defense_power :
#     print('(A팀 사용자 이름)팀이 승리하였습니다.')
# elif a_striking_power = b_defense_power :
#     print('비겼습니다.')
# else:
#     print('(B팀 사용자 이름)팀이 승리하였습니다.')
#
# a_players = [['H.KANE', 'CF', 'TOTTENHAM', 65, 83, 73, 74, 44, 77, 79],['jam', 'CF', 'TOTTENHAM', 65, 83, 73, 74, 44, 77, 79]]
#
# a_player = ['H.KANE', 'CF', 'TOTTENHAM', 65, 83, 73, 74, 44, 77, 79]
#
#
# print(sum(a_player[3:7]))
#
#
# print(sum(a_player[7:9]))
#
# for player in a_players:
#     print(sum(player[3:7]))
#     print(sum(player[7:9]))
#
#
# for a in a_player:
#     sum(a_player[3:7])
# a_striking_power = sum(a)
# print(a)

# ovr로 통일한 값





class Football:


    def __init__(self):

        print('Class_Football_Game')


    def extraction_name(self, list_1):                # 여기서 list는 위에 members 함수로 뽑아낸 리스트를

        self.name_list = []                                # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을

        for x in range(0, len(list_1)):               # 추출하는 함수

            self.name_list.append(list_1[x][0])

        return self.name_list



    def extraction_stats(self, list_1):               # 여기서 list는 위에 members 함수로 뽑아낸 리스트를

        self.stats_list = []                               # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을

        for x in range(0, len(list_1)):               # 추출하는 함수

            self.stats_list.append(list_1[x][3:10])

        return self.stats_list

    def members(self, list_1):

        self.member_list = []

        for x in range(0, len(list_1) - 1):

            if x == 0:
                del (list_1[0])

            y = list_1[x]

            self.member_1 = y.split(',')  # list의 각 객체들을 1개씩 split해서 리스트로 만든 후

            z = self.member_1[-1].rstrip('\n')  # csv 줄바꿈 현상에서 나오는 '\n' 글자를 삭제

            del (self.member_1[-1])

            self.member_1.append(z)

            self.member_list.append(self.member_1)  # 다시 member_list로 묶음

        return self.member_list

member_0 = open('C:/Users/CPB06GameN/Desktop/member.csv', 'r', encoding='UTF-8')

field_member = member_0.readlines()



member_1 = open('C:/Users/CPB06GameN/Desktop/member2.csv', 'r', encoding='UTF-8')

GK_member = member_1.readlines()

print(GK_member)

# # 원본 데이터 - 골키퍼 플레이어용

print('원본 데이터','\n', GK_member)





a = Football()

x = a.members(field_member)

y = a.members(GK_member)



# # 선수 이름 추출

name1 = a.extraction_name(x)

print('플드 플레이어 선수 이름','\n', name1)

name2 = a.extraction_name(y)

print('골키퍼 플레이어 선수 이름','\n',name2)




# 선수 번호 매김

#선수 번호
player_num={}
for i,name in enumerate(name1):
    player_num[i]=name
print(player_num)
n = int(input('필드선수 숫자를 입력하세요 = '))
print(player_num[n])
#{0: 'L.Messi', 1: 'H.KANE', 2: 'A.Lacazette'.....

#키퍼 번호

gk_num={}
for i,name_2 in enumerate(name2):
    gk_num[i]=name_2
print(gk_num)

n = int(input('골키퍼 숫자를 입력하세요='))
print(gk_num[n])

# {0: 'De Gea', 1: 'Hugo Lloris', 2: 'J.Oblak', 3: 'M. ter Stegen', 4: 'W.Szczesny'}
