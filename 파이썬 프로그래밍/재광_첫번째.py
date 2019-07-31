# # csv flie을 읽어서 data frame을 작성한다.
f = open('C:/Users/CPB06GameN/Desktop/파일.csv','r',encoding='UTF=8')
result = f.read()
print(result)

# # - data frame의 변수 항목을 리스트로 만든다.
f = open('C:/Users/CPB06GameN/Desktop/파일.csv','r',encoding='UTF=8')
lines = f.readline().split(',')
print(lines)

# # - dataframe의 data와 변수의 수를 출력한다.
a = len(lines)
print(a)

# # - data frame의 앞부분 일정 부분의 내용을 출력한다.
dkv = lines[0:5]
print(dkv)

# # - data frame의 뒷부분 일정 부분의 내용을 출력한다.
enl = lines[5:10]
print(enl)
#
# # - data frame의 변수 이름을 변경하는 기능을 제공한다.
name1 = input('변경할 변수를 입력하세용=')
name2 = input('새로운 변수를 입력하세용=')
dict = {'h1':0,'h2':1,'h3':2,'h4':3,'h5':4,'h6':5,'h7':6,'h8':7,'h9':8,'h10':9}
def rename():
    print('lines',lines)
    lines[dict[name1]] = name2
    print('lines', lines)                # 출력의 순서를 고려하라
rename()                                 # 마지막에 함수를 호출하여 결과를 확인.
#
# # - data frame에 파생 변수를 추가하는 기능을 제공한다.
n = input('추가할 변수를 입력하세용=')
def plus():
    lines.append(n)
    print(lines)
plus()

# 이건 앞에 것을 삭제한 것입니당
del lines[10]                              # del은 인덱스를 삭제, remove는 요소를 삭제
print(lines)

# - data frame 에서 필요한 변수를 추출하는 기능을 제공한다.
dict = {'h1':0,'h2':1,'h3':2,'h4':3,'h5':4,'h6':5,'h7':6,'h8':7,'h9':8,'h10':9}
print(dict)
def extraction():
    while True :
        n = input('추출할 변수를 입력하세요=',)
        a = '없다면 종료를 입력하세요'
        print(a)
        l = {lines[dict[n]]}
        print(l)
        if n == '종료':
            break
extraction()

# # - data frame에서 조건에 따른 data를 추출하는 기능을 제공한다.
def terms_extraction():
    # if
    # else

# dataframe의 data를 정렬하는 기능을 제공한다. (오름 /내림차순 기능 별도 제공 )
def arrayal():
    n = int(input('오름차순은 1번, 내림차순 2번='))
    if n == 1:
        lines.sort()
        print(lines)
    else:
        n == 2
        lines.sort(reverse=True)
        print(lines)
arrayal()