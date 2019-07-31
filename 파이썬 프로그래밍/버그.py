member_csv_path = 'C:/Users/CPB06GameN/Desktop/member.csv'
member2_csv_path = 'C:/Users/CPB06GameN/Desktop/member2.csv'
# CF, CM, CB, WB, goalkeeper 로 변수 만들어 분류=====================================
f = open(member_csv_path, 'r')
result = f.read()
print(result)

f = open(member2_csv_path, 'r')
result_2 = f.read()
print(result_2)

with open(member_csv_path, 'r') as m:
    while True:
        line = m.readline()
        if not line: break

with open(member_csv_path, 'r') as m:
    header = m.readline()
    header_list = header.split()
    print(header_list)

    CF = []
    CM = []
    CB = []
    WB = []

    while True:
        line = m.readline()
        if not line:
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

f = open(member2_csv_path, 'r')
goalkeeper = f.read()
print(goalkeeper)


# ----------------------------------------------------------------------------------------------------------------------------------

class Football:

    def __init__(self):

        print('Class_Football_Game')

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

    def members2(self, list_1):

        self.member_list = []

        for x in range(0, len(list_1) - 1):
            y = list_1[x]

            self.member_1 = y.split(',')  # list의 각 객체들을 1개씩 split해서 리스트로 만든 후

            z = self.member_1[-1].rstrip('\n')  # csv 줄바꿈 현상에서 나오는 '\n' 글자를 삭제

            del (self.member_1[-1])

            self.member_1.append(z)

            self.member_list.append(self.member_1)  # 다시 member_list로 묶음

        return self.member_list

    def extraction_name(self, list_1):  # 여기서 list는 위에 members 함수로 뽑아낸 리스트를

        self.name_list = []  # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을

        for x in range(0, len(list_1)):  # 추출하는 함수

            self.name_list.append(list_1[x][0:2])

        return self.name_list

    def extraction_stats(self, list_1):  # 여기서 list는 위에 members 함수로 뽑아낸 리스트를

        self.stats_list = []  # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을

        for x in range(0, len(list_1)):  # 추출하는 함수

            self.stats_list.append(list_1[x][3:10])

        return self.stats_list

    def change_int(self, list_1):  # Str 문자열을 int 로 뽑는다.
        return [[int(y) for y in x] for x in list_1]  # isinstance() 해당 자료형인가 True

    def ability(self, list_1, list_2):  # 선수명과 스텟
        for x in range(0, len(list_1)):  # list_1 에는 선수명 목록
            list_2[x].insert(0, list_1[x][1])  # list_2 는 능력치 목록
            list_2[x].insert(0, list_1[x][0])  # list_2 는 능력치 목록
        return list_2

    # jam 중첩 안되게 수정 0718 19:19
    #     def ability(self, list_1, list_2):                # 선수명과 스텟
    #
    #         for x in range(0, len(list_1)):               # list_1 에는 선수명 목록
    #             for y in list_2[x]:
    #                 list_1.append(y)
    #             # result = list_1[x] + list_2[x]
    #             # print(list_1[x]+list_2[x])
    #             # list_2[x].insert(0, list_1[x])            # list_2 는 능력치 목록
    #
    #         return list_1

    def field_ability(self, list_3):  # list_3 은 ability에서 선수명과 능력치를 합한 것

        self.speed = {}  # self.speed 등으로 불러와서 사용 가능

        self.shot = {}  # dict 형태로 구현

        self.pass_n = {}  # 필드 플레이어용 능력치 추출기

        self.dribbling = {}

        self.defence = {}

        self.physical = {}

        self.ovr = {}

        for x in range(0, len(list_3)):
            a = {list_3[x][0]: list_3[x][1]}

            self.speed.update(a)

        for x in range(0, len(list_3)):
            b = {list_3[x][0]: list_3[x][2]}

            self.shot.update(b)

        for x in range(0, len(list_3)):
            c = {list_3[x][0]: list_3[x][3]}

            self.pass_n.update(c)

        for x in range(0, len(list_3)):
            d = {list_3[x][0]: list_3[x][4]}

            self.dribbling.update(d)

        for x in range(0, len(list_3)):
            e = {list_3[x][0]: list_3[x][5]}

            self.defence.update(e)

        for x in range(0, len(list_3)):
            f = {list_3[x][0]: list_3[x][6]}

            self.physical.update(f)

        for x in range(0, len(list_3)):
            g = {list_3[x][0]: list_3[x][7]}

            self.ovr.update(g)

        return self.speed, self.shot, self.pass_n, self.dribbling, self.defence, self.physical, self.ovr

    def gk_ability(self, list_3):  # list_3 은 ability에서 선수명과 능력치를 합한 것

        self.diving = {}  # self.speed 등으로 불러와서 사용 가능

        self.handling = {}  # dict 형태로 구현

        self.kick = {}  # 골키퍼 플레이어용 능력치 추출기

        self.reaction = {}

        self.speed_gk = {}

        self.site_selection = {}

        self.ovr_gk = {}

        for x in range(0, len(list_3)):
            a = {list_3[x][0]: list_3[x][1]}

            self.diving.update(a)

        for x in range(0, len(list_3)):
            b = {list_3[x][0]: list_3[x][2]}

            self.handling.update(b)

        for x in range(0, len(list_3)):
            c = {list_3[x][0]: list_3[x][3]}

            self.kick.update(c)

        for x in range(0, len(list_3)):
            d = {list_3[x][0]: list_3[x][4]}

            self.reaction.update(d)

        for x in range(0, len(list_3)):
            e = {list_3[x][0]: list_3[x][5]}

            self.speed_gk.update(e)

        for x in range(0, len(list_3)):
            f = {list_3[x][0]: list_3[x][6]}

            self.site_selection.update(f)

        for x in range(0, len(list_3)):
            g = {list_3[x][0]: list_3[x][7]}

            self.ovr_gk.update(g)

        return self.diving, self.handling, self.kick, self.reaction, self.speed_gk, self.site_selection, self.ovr_gk


# ----------------------------------------------------------------------------------------------------------------------------------

member_0 = open(member_csv_path, 'r', encoding='UTF-8')

field_member = member_0.readlines()

member_1 = open(member2_csv_path, 'r', encoding='UTF-8')

GK_member = member_1.readlines()

a = Football()

x = a.members(field_member)
# print(x)
y = a.members(GK_member)

# # 선수 이름 추출

name1 = a.extraction_name(x)

print('플드 플레이어 선수 이름', '\n', name1)

name2 = a.extraction_name(y)

print('골키퍼 플레이어 선수 이름', '\n', name2)

# 선수 번호 매김

# 선수 번호
player_num = {}
for i, name in enumerate(name1):
    player_num[i] = name
print(player_num)
# {0: 'L.Messi', 1: 'H.KANE', 2: 'A.Lacazette'.....
player_num[0]
# 키퍼 번호
gk_num = {}
for i, name2 in enumerate(name2):
    gk_num[i] = name2
print(gk_num)


# {0: 'De Gea', 1: 'Hugo Lloris', 2: 'J.Oblak', 3: 'M. ter Stegen', 4: 'W.Szczesny'}

# ------------------------------------------------------------------------------------------------


def select_player(lists, select,
                  player_dic):  # list : 선수 1명의 능력치 list  : ['son',10,20,40,80,20,50,90] # 90자리 ,ovr    [7]

    # cf = [] # 공격수 :[['son',10,20,40,80,20,50],['jam',10,20,40,80,20,50],['yum',10,20,40,80,20,50]]
    # cm = [] # 미드필더 : 형식 동일
    # cb = [] # 수비 : 형식 동일
    # wb = [] # 수비 : 형식 동일
    # gk = [] # 골키퍼
    print('HEAR::!!!!!!!!!!!!!!!!!!', lists)
    if lists[1] == 'CF':  # 공격수였음
        if position == lists[1]:
            player_dic['CF'].append(lists)
        elif position == 'CM':  # CM선택
            lists[-1] = lists[-1] - (lists[-1] * 0.3)
            player_dic['CM'].append(lists)
        elif position == 'CB':  # CB면
            print('finish')
            # lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
            # lists[-1] = int(lists[-1]) -(int(lists[-1])*0.5)

            lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
            player_dic['CB'].append(lists)

        elif position == 'WB':
            lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
            player_dic['WB'].append(lists)
        elif position == 'GK':
            lists[-1] = lists[-1] - (lists[-1] * 0.9)
            player_dic['GK'].append(lists)
        else:
            print('error1')
            pass

    elif lists[1] == 'CM':  # 공격수였음
        if position == lists[1]:
            player_dic['CM'].append(lists)
        elif position == 'CF':  # CM선택
            lists[-1] = lists[-1] - (lists[-1] * 0.3)
            player_dic['CF'].append(lists)
        elif position == 'CB':  # CB면
            lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
            player_dic['CB'].append(lists)
        elif position == 'WB':
            lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
            player_dic['WB'].append(lists)
        elif position == 'GK':
            lists[-1] = lists[-1] - (lists[-1] * 0.9)
            player_dic['GK'].append(lists)
        else:
            print('error2')
            pass

    elif lists[1] == 'CB':  # 공격수였음
        if position == lists[1]:
            player_dic['CB'].append(lists)
        elif position == 'CM':  # CM선택
            lists[-1] = lists[-1] - (lists[-1] * 0.3)
            player_dic['CM'].append(lists)
        elif position == 'CF':  # CB면
            lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
            player_dic['CF'].append(lists)
        elif position == 'WB':
            lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
            player_dic['WB'].append(lists)
        elif position == 'GK':
            lists[-1] = lists[-1] - (lists[-1] * 0.9)
            player_dic['GK'].append(lists)
        else:
            print('error3')
            pass

    elif lists[1] == 'WB':  # 공격수였음
        if position == lists[1]:
            player_dic['WB'].append(lists)
        elif position == 'CM':  # CM선택
            lists[-1] = lists[-1] - (lists[-1] * 0.3)
            player_dic['CM'].append(lists)
        elif position == 'CB':  # CB면
            lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
            player_dic['CB'].append(lists)
        elif position == 'CF':
            lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
            player_dic['CF'].append(lists)
        elif position == 'GK':
            lists[-1] = lists[-1] - (lists[-1] * 0.9)
            player_dic['GK'].append(lists)
        else:
            print('error')
            pass
    elif lists[1] == 'GK':  # 공격수였음
        if position == lists[1]:
            player_dic['GK'].append(lists)
        elif position == 'CM':  # CM선택
            lists[-1] = lists[-1] - (lists[-1] * 0.9)
            player_dic['CM'].append(lists)
        elif position == 'CB':  # CB면
            lists[-1] = lists[-1] - (lists[-1] * 0.9)
            player_dic['CB'].append(lists)
        elif position == 'WB':
            lists[-1] = lists[-1] - (lists[-1] * 0.9)
            player_dic['CF'].append(lists)
        elif position == 'CF':
            lists[-1] = lists[-1] - (lists[-1] * 0.9)
            player_dic['CF'].append(lists)
        else:
            print('error')
            pass


    else:
        print('error')

    return player_dic


# -------------------------------------------------------------------------------------------------
class Position:
    def __init__(self,CF,CM,CB,WB,GK):
        self.CF = CF
        self.CM = CM
        self.CB = CB
        self.WB = WB
        self.GK = GK

    def select(self,num,posit):
        self.num = num
        self.posit = posit


select_num_position = Position



player = a.members2(field_member)
print(player)
player_name = a.extraction_name(player)  # name
# print(player_name)
player_stats = a.extraction_stats(player)

# print('here!!!!!!!',a.change_int(player_stats))
player_non_str = a.ability(player_name, a.change_int(player_stats))
# print(player_non_str)

player_dic = {}
posit_list = ['CF', 'CM', 'CB', 'WB', 'GK']
for posit in posit_list:  # 포지션마다 딕셔너리 선언
    player_dic[posit] = []

while True:
    player = int(input('선수이름을 고르시오 >> '))
    if player == -1:
        break
    # print(player_num[player])
    # kipper = int(input('키퍼 이름을 고르시오 >> '))
    # print(player)
    position = input('포지션을 선택하세요')
    # print(player_non_str)
    # result = []
    # result.append(player_non_str)
    # print(result)
    # print('HERE>>>>>>>>>>',player_non_str)

    for name in player_non_str:
        # print('player_num[player][0]:',player_num[player][0])
        # print('name',name[0])
        if name[0] == player_num[player][0]:
            player_dic = select_player(name, position, player_dic)
            print(player_dic)
        else:
            pass

print(player_dic['CF'])
#[['L.Messi', 'CF', 82, 85, 85, 90, 33, 61, 60.900000000000006],['L.Messi', 'CF', 82, 85, 85, 90, 33, 61, 60.900000000000006],['L.Messi', 'CF', 82, 85, 85, 90, 33, 61, 60.900000000000006]]
# for jimmy in player_dic['CF']:
#     print(jimmy)

# print('{0:=^20}{0:=^20}{0:=^20}'.format(player_dic['CF'],player_dic['CF'],player_dic['CF']))
# print('{0:=^20}{0:=^20}{0:=^20}'.format('player_dic[CM]','player_dic[CM]','player_dic[CM]'))
# print('{0:=^15}{0:=^15}{0:=^15}{0:=^15}'.format('player_dic[WB]','player_dic[CB]','player_dic[CB]','player_dic[WB]'))
# print('{0:=^60}'.format('player_dic[GK]'))

class Position :
    def __init__(self,CF,CM,CB,WB,GK):
        self.CF = CF
        self.CB = CB
        self.CM = CM
        self.WB = WB
        self.GK = GK

    def forward(self,forward):
        self.forward = forward
        for i in player_dic['CF']:
            print('{0:=^20}'.format(i[0]),end='')

        # print('{0:=^120}'.format('0'))
    def mid(self):
        for o in player_dic['CM']:
            print('{0:=^20}'.format(o[0]),end='')

        print()
    def defensive(self,defensive):
        self.defensive = defensive
        for wb in range(len(player_dic['WB'])):
            if wb == 0:
                print('{0:=^15}'.format(player_dic['WB'][wb][0]),end='')
                for cb in player_dic['CB']:
                    print('{0:=^15}'.format(cb[0]), end='')
            else:
                print('{0:=^15}'.format(player_dic['WB'][wb][0]), end='')

    def goalkeeper(self,goalkeeper):
        self.goalkeeper = goalkeeper
        for p in player_dic['GK']:
            print('{0:=^60}'.format(p[0]))

a=Position
a.defensive(1)