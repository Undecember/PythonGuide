import os

def clearScreen():
    if os.name == 'nt': os.system('CLS')
    else: os.system('clear')

def enterToContinue(clear = False, msg = '계속'):
    if type(clear) == str: clear, msg = False, clear
    input(f'엔터쳐서 {msg} ')
    if clear: clearScreen()

def printThenEval(code, result = None):
    print('\033[95m=============코드=============')
    print(code)
    print('\033[92m===========실행결과===========\n')
    if result == None: exec(code)
    else: print(result)
    print('\033[97m')

# start

print('\033[97m')
clearScreen()
print('''
목차
1. Python 몇몇 기본 함수
2. Python만의 ㅈ같은 문법
3. 모듈이란
4. 시퀀셜 타입들 - List, Tuple, 문자열
5. 함수
6. 인덱싱 / 슬라이싱

이 프로그램은 python 코드와 그 실행 결과를 쌍으로 알려주면서 공부를 도와준다.
예시로 알려주는 코드마다 바로 실행결과를 보지 말고, 코드만 먼저 보고 실행결과를 예측해보면서 공부할 것!!
하지만 print만 써서 도배돼있는 코드는 그냥 설명용이니까 결과만 꼼꼼하게 봐도 된다.
보다보면 뭔 소린지 알 듯

이 프로그램을 되도록 30번 이상 (최소 10번은) 꼼꼼하게 익히면서 실행하도록.
백번을 봐도 대충보면 효과없음
한번을 보더라도 꼼꼼하게 공부할 것

학습지 15페이지부터는 이걸로 다른 파트 공부하고 나서 학습지로 보기만 해도 다 공부될듯
이 프로그램으로 공부 좀 한 후에 학습지 15~21페이지를 나중에 공부할 것
''')

enterToContinue(True)
#
#
# Python functions
#
#

print('''
1. Python의 몇몇 기본 함수
''')

enterToContinue(True)
# print

printThenEval('''
print('출력할 텍스트')

print('출력할 것 1', 2, 3.0)    # 여러 개를 넣으면 띄어쓰기 한 개로 끊어서 다 출력해준다.
''')

enterToContinue('예시 더보기')
printThenEval('''
print('end 옵션으로 마지막에 출력할 내용 설정가능', end = ';;뷁;\\n\\n')
print('<< 이렇게 end가 끝에 출력됨')
print('end 옵션을 안 적으면 기본값은 \\\'\\\\n\\\'')
print('<< 이렇게 엔터가 쳐짐')
''')

enterToContinue(True, '다음 함수 보기')
# input

printThenEval('''
print('아래와 같이 input(msg) 꼴로 msg 출력 후 문자열 입력을 받을 수 있음')
txt = input('여기에 아무거나 입력하기 : ')
print(txt)
print('input에 print기능이 굳이 있는 이유는?')
print('보통 뭔가 입력받기 전에 뭘 입력해달라는 건지 출력하기 때문에.')
print('그냥 입력만 받으려면 msg부분은 생략하고 input()으로 쓰면 됨')
''')

enterToContinue(True, '다음 함수 보기')
# abs

printThenEval('''
print('abs는 절댓값 (absolute value)')
print(abs(-3))
print(abs(-5))
print(abs(7))
''')

enterToContinue(True, '다음 함수 보기')
# round
printThenEval('''
print('round는 반올림하는 함수')
print(round(3.5))      # 정수로 반올림
print(round(3.357, 2)) # 소수 둘째자리로 반올림
''')

enterToContinue(True, '다음 함수 보기')
# int
printThenEval('''
print('int는 정수로 변환하는 함수 (integer)')
print(int('1374'))
print(int('-35'))
''')

enterToContinue(True, '다음 함수 보기')
# chr/ord
printThenEval('''
print('chr은 정수를 문자로, ord는 문자를 정수로, 아스키코드 변환')
print(chr(65))
print(ord('A'))
''')

enterToContinue(True)
#
#
# Python grammars
#
#

print('''
2. Python만의 ㅈ같은 문법
''')

enterToContinue(True, '설명 보기')
# semicolon

printThenEval('''
print('세미콜론에 대해\\n')
print('python은 c/c++을 포함한 다른 많은 언어와 달리 세미콜론(;)을 끝에 안 붙인다 (ㅅㅂ)')
print('세미콜론을 사용하는 다른 언어들은 세미콜론을 통해 구문의 단위를 구분한다')
print('예를 들어 a;b;는 a;와 b;로 깔끔하게 구분된다')
print('그러면 python은 세미콜론도 없이 어떻게 구문의 단위를 구분하느냐?')
print('엔터와 들여쓰기(문장 맨 앞의 탭 수)로 구분하는데, 이게 매우 ㅈ같은 부분이다')
print('사람마다 다를 수 있는 띄어쓰기 습관 및 스타일을 지좆대로 강제하고 틀리면 에러를 뿜기 때문.')
print('(개인적인 의견)')
''')

enterToContinue()
# multiple assign

printThenEval('''
print('여러 값 대입')
print('a에는 1, b에는 2를 대입하고 싶다면')
print('c/c++에서는 "a = 1, b = 2;" 로 처리하지만')
print('python에서는 "a, b = 1, 2" 로 처리한다')
print('우변과 좌변의 원소 개수는 당연히 같아야 하며, 각각은 List나 Tuple이어도 된다')
print('a, b = [1, 2] 가능')
print('(a, b) = [1, 2] 또한 가능')
''')

enterToContinue(True)
# for

printThenEval('''
print('for문의 형태\\n')
print('for (변수명) in (시퀀셜 타입의 컨테이너)')
print('또는')
print('for (변수명) in (생성기)')
print('\\n시퀀셜 컨테이너란?')
print('List, Tuple 같은 것들 (뒤에 설명)')
print('\\n생성기란?')
print('range, map 등 순차적으로 값을 \\'생성\\'해주는 것들')
''')

enterToContinue(True, '컨테이너 형태 설명 보기')
printThenEval('''
print('for (변수명) in (시퀀셜 타입 컨테이너)')
print('=> 컨테이너에서 값을 반복적으로 꺼내와서 변수에 집어넣고 for문 안쪽 코드를 실행')
''')

enterToContinue('예시 보기')
printThenEval('''
for k in [ 'yo', 'whats up', 'ssibal python' ]:
    print(k)
''')
printThenEval('''
for t in ( 1, 2, 5 ):
    print(t)
''')

enterToContinue(True, '생성기 형태 설명 보기')
printThenEval('''
print('for (변수명) in (생성기)')
print('=> 생성기에서 값을 반복적으로 생성받아서 변수에 집어넣고 for문 안쪽 코드를 실행')
''')

enterToContinue('range 설명 보기')
# range

printThenEval('''
print('range란?\\n')
print('range(s, e, d) : s부터 e가 되기 전까지(e는 포함 안 됨) d씩 더하면서 값을 생성')
print('e는 포함하지 않는 다는 것에 주의!!!!!')
print('d 생략 가능 (생략하면 기본값 1)')
print('d 생략하면 s도 생략 가능 (생략하면 기본값 0)')
''')

enterToContinue('예시 보기')
printThenEval('''
for i in range(1, 5, 2):
    print(i)
''')
printThenEval('''
for i in range(6, 3, -1):
    print(i)
''')
printThenEval('''
for i in range(3, 6):
    print(i)
''')
printThenEval('''
for i in range(3):
    print(i)
''')

enterToContinue(True, 'map 설명 보기')
# map

printThenEval('''
print('map이란?\\n')
print('map(f, l) : l에서 값을 하나씩 꺼내서 f(l)을 순차적으로 생성')
''')

enterToContinue('예시 보기')
printThenEval('''
for i in map(abs, [ 3, -4, 5, -6 ]):
    print(i)
''')

enterToContinue('주의할 개념 보기')
printThenEval('''
print('map이나 range는 list나 tuple과 원리가 다름!!!')
print('for i in range(5) 와')
print('for in [0, 1, 2, 3, 4] 는')
print('결과는 같지만 range는 for 한바퀴 돌 때마다 0, 1, 2, ...를 순차적으로 생성함')
print('반대로 []를 쓰면 0, 1, 2, ...가 이미 list에 있는 상태에서 순차적으로 꺼내옴')
print('\\n같은 이유로 map(abs, [ 3, -4, 5, -6 ]) != [ 3, 4, 5, 6 ] 임')
print('전자는 3, 4, 5, 6을 생성할 \\'준비가 된\\' map 오브젝트일 뿐이지 list가 아님!!')
''')

enterToContinue(True)
#
#
# Python modules
#
#

print('''
3. 모듈이란
''')

enterToContinue(True, '설명 보기')
# semicolon

printThenEval('''
print('모듈 : 어떤 기능을 제공하는 코드의 묶음. 함수나 변수, 클래스 등을 모아놓은 파일\\n')
print('사실상 python의 유일한 강점')
''')

enterToContinue('예시 보기')
printThenEval('''
print('모듈 이름 그대로 import')
import random
print('random은 랜덤에 관련된 함수를 제공하는 모듈')
print(random.random())
print(random.random())
print(random.random())
print('\\n.의 의미 : A.B는 A의 B를 뜻함.')
print('\\'.\\' == \\'~의\\'')
''')

enterToContinue('예시 더보기')
printThenEval('''
print('모듈 이름 그대로가 아닌 별명으로 import')
import random as rd
print('random을 rd라고 부르기로 설정. random으로 쓰면 작동하지 않음')
print(rd.random())
print(rd.random())
print(rd.random())
print('\\nrd.rd()가 아닌 이유?')
print('rd.random()에서 rd는 모듈의 이름, random은 함수의 이름.')
print('즉, rd.random()은 \\'rd라는 모듈의 random함수를 호출하겠다\\'는 뜻')
print('함수명에 별명을 붙인 게 아니라 모듈명에 별명을 붙인 것이므로 rd.random()')
''')

enterToContinue('random 모듈의 함수 예시 더보기')
printThenEval('''
print('random() : (0.0, 1.0) 구간의 랜덤 실수 생성')
print('randint(a, b) : [a, b] 구간의 랜덤 정수 생성')
print('range처럼 공부할 때 닫힌 구간, 열린 구간 꼼꼼하게 확인!')
import random as rd
print(rd.randint(3, 5))
print(rd.randint(3, 5))
print(rd.randint(3, 5))
print(rd.randint(3, 5))
''')

enterToContinue('예시 더보기')
printThenEval('''
print('거북이 갖고 노는 turtle이라는 모듈도 있는데 개노잼이니 이건 알아서 공부하시오.')
''')

enterToContinue(True)
#
#
# Sequential types
#
#

print('''
4. 시퀀셜 타입들 - List, Tuple
''')

enterToContinue(True, '설명 보기')
# semicolon

printThenEval('''
print('시퀀셜 (Sequential) : 연이은, 나열된, 줄줄이')
print('시퀀셜 타입 : 여러 오브젝트의 나열을 저장하는 타입 (c의 배열과 비슷함)')
print('\\n대표적인 시퀀셜 타입 : List, Tuple')
print('\\n*타입은 아니지만 시퀀셜한 \\'표현법\\'(은근 중요) : ')
print('comma-seperated expression (\\',\\'로 구분되어 나열된 구문)')
print('예시 : a, b, c  또는  1, 2, 3  등등')
print('앞으로 설명할 때 짧게 CSE라고 부르겠음')
''')

# enterToContinue('List 설명 보기')
# printThenEval('''
# print('c의 배열과 아주 비슷함.')
# print('\\n배열과 다른 점')
# print('1. 원소들의 타입이 서로 달라도 됨 (애초에 python은 변수의 타입을 정해놓고 쓰지 않기 때문이기도 함)')
# print('2. 크기를 변화시킬 수 있음. (원소 개수가 늘어나거나 줄어도 됨)')
# ''')

# enterToContinue('List 관련 문법 보기')

# printThenEval('''
# # 리스트 생성. 서로 다른 타입 가능 (심지어 리스트도 리스트의 원소가 될 수 있음)
# a = [1, 'ab', True, [10, 20]]
# print(a)

# # a의 3번 원소 (index, 즉 원소 번호는 0번부터 시작하는 점은 기본중에 기본이므로 숙지!)
# print(a[3])

# # a의 0번 원소를 10으로 설정 (a[0]에 10을 대입)
# a[0] = 10
# print(a)

# # List * 정수 연산을 하면 List를 주어진 횟수만큼 반복한 리스트를 생성
# # a를 ['ping', 'pong', 'ping', 'pong', 'ping', 'pong']로 설정
# a = ['ping', 'pong'] * 3
# print(a)

# # List + List 연산을 하면 이어붙인 새로운 리스트를 생성
# # a에 [1, 2]를 이어붙이기
# a = a + [1, 2]
# print(a)
# ''')

# enterToContinue('List 관련 문법 더보기')
# printThenEval('''
# # 리스트 생성
# a = [1, 'ab', True, [10, 20]]
# print(a)

# print()
# # a의 맨 뒤에 '원소' 갖다붙이기
# # List를 갖다붙이는 '+' 연산이랑은 다름!
# a.append(100)   # 이러면 100이 맨 뒤에 추가됨
# print(a)
# a.append([100]) # 이러면 100이 아니라 [100]이 추가되는 것.
# print(a)

# print()
# # a의 원소 제거하기
# # a.pop(제거할 index)
# # 제거된 값을 써먹을 수 있도록 리턴도 해줌
# print(a.pop(3)) # a에서 3번 원소를 제거하고 그 값을 리턴
# print(a)        # 3번이 제거된 a
# print(a.pop())  # index를 생략하면 기본값 맨 뒤로 설정됨
# print(a)        # 맨 뒤 원소가 제거된 a
# ''')

# enterToContinue('List 관련 문법 더보기')
# printThenEval('''
# # 리스트 생성
# a = [1, 'ab', True, [10, 20]]
# print(a)

# print()
# # insert로 a에 원소 추가하기
# # append와의 차이점 : 맨 뒤가 아니라 위치를 맘대로 정해서 삽입
# a.append(100)       # 이러면 100이 맨 뒤에 추가됨
# print(a)
# a.insert(1, 100)    # 이러면 맨 뒤가 아니라 1번 index에 삽입되는 것.
# print(a)

# print()
# # remove로 a의 특정 원소 제거하기
# # remove와의 차이점 : index가 아니라 값 자체를 기준으로 제거
# # 같은 값이 여러개면? : 처음 나타나는 원소를 찾아서 제거
# print(a.pop(3))         # a에서 3번 원소를 제거하고 그 값을 리턴
# print(a)                # 3번이 제거된 a
# print(a.remove('ab'))   # 'ab'를 찾아서 제거
# print(a)                # 'ab'가 제거된 a
# ''')

# enterToContinue('List 관련 문법 더보기')
# printThenEval('''
# # 리스트 생성
# a = [1, 'ab', True, [10, 20]]
# print(a)

# print()
# # insert로 a에 원소 추가하기
# # append와의 차이점 : 맨 뒤가 아니라 위치를 맘대로 정해서 삽입
# a.append(100)       # 이러면 100이 맨 뒤에 추가됨
# print(a)
# a.insert(1, 100)    # 이러면 맨 뒤가 아니라 1번 index에 삽입되는 것.
# print(a)

# print()
# # remove로 a의 특정 원소 제거하기
# # remove와의 차이점 : index가 아니라 값 자체를 기준으로 제거
# # 같은 값이 여러개면? : 처음 나타나는 원소를 찾아서 제거
# print(a.pop(3))         # a에서 3번 원소를 제거하고 그 값을 리턴
# print(a)                # 3번이 제거된 a
# print(a.remove('ab'))   # 'ab'를 찾아서 제거
# print(a)                # 'ab'가 제거된 a
# ''')

# enterToContinue('List 관련 문법 더보기')
# printThenEval('''
# # 리스트를 생성하는 python적인 방법
# a = [i for i in range(5) if i % 2 == 0]
# print(a)
# # [ (표현식) (for문) (if문) ] 꼴. (if는 생략 가능)
# # (for문)을 돌면서 (if문)이 참이면 (표현식)의 값을 구해서 리스트의 원소로 추가

# print()

# a = [2 ** i for i in range(2, 10)]
# print(a)

# a = [2 ** i for i in range(2, 10) if (2 ** i) % 3 == 1]
# print(a)

# a = [2 ** i for i in range(2, 10) if i % 3 == 1]
# print(a)
# ''')

# enterToContinue('2차원 List 보기')
# printThenEval('''
# # 어떤 List의 각 원소가 1차원 List면 이 List는 2차원 List
# # 어떤 List의 각 원소가 2차원 List면 이 List는 3차원 List ...

# # 2차원 List를 생성하는 방법 1
# a = []
# for i in range(3):
#     a += [[0] * 5]
# print(a)

# # 2차원 List를 생성하는 방법 2
# a = [[0 for i in range(5)] for j in range(3)]
# print(a)

# # 2차원 List를 생성하는 방법 3
# a = [[0] * 5 for i in range(3)]
# print(a)

# print('왜 a = [[0] * 5] * 3 이런 식으로 하면 안 될까?')
# ''')

# enterToContinue()
# printThenEval('''
# # 잘 만든 2차원 List a
# a = [[0] * 5 for i in range(3)]
# print(a)

# # 잘못 만든 2차원 List b
# b = [[0] * 5] * 3
# print(b)

# # 똑같이 0, 0에 3을 대입하면?
# a[0][0] = 3
# b[0][0] = 3

# print(a)
# print(b, end = '  << 이새끼는 왜이럴까?')
# ''')

# enterToContinue(True, '깊은 복사와 얕은 복사 이해하기')
# printThenEval('''
# print('"복사는 노동이다."')
# print('python의 변수들은 type이 정해져있지 않다.')
# print(' => 변수 하나 복사할 때 복사해야할 데이터 크기가 조오온나 클 수도 있다')
# print(' => List도 길이가 길면 길 수록 당연히 복사할 때 컴퓨팅파워가 많이 든다')
# print(' => 비효율적이다!!')
# print('따라서 몇몇 작은 type을 제외하고는 \\'얕은복사\\'를 쓴다')
# ''')
# enterToContinue()
# printThenEval('''
# print('얕은 복사란?')
# print('a를 b로 복사할 때, a의 내용을 새로운 메모리에 적고 b라고 부르는 게 아니라')
# print('a를 b라고도 부르겠다고 해버리는 말그대로 개꼼수다.')
# print('복사한 척만 하고 이름만 덧붙여버리는 것')
# print('int, float, bool을 제외하면 대부분 얕은 복사를 쓴다')
# ''')
# enterToContinue()
# printThenEval('''
# print('[[0] * 5] * 3 가 안 되는 이유')
# print('[0] * 5는 0을 5번 복사한다.')
# print(' => int 복사이므로 깊은 복사')
# print(' => 진짜 값이 복사되어 5개의 서로 다른 변수가 된다')
# print('[[0] * 5] * 3은 [0, 0, 0, 0, 0]을 3번 복사한다.')
# print(' => List 복사이므로 얕은 복사')
# print(' => 복사된 척만 하고 같은 메모리 공간을 쓴다.')
# print('따라서 [0][0]을 수정하면 [0], [1], [2]가 전부 같은 메모리 공간을 쓰기 때문에')
# print('[0][0], [1][0], [2][0]이 모두 수정된 것 처럼 보인다.')
# ''')
# enterToContinue('얕은 복사 예시 보기')
# printThenEval('''
# a = [1, 2, 3, 4]
# b = a       # 얕은 복사!

# b[3] = 777
# print(a)    # 같은 메모리공간, a와 b는 두가지 이름일 뿐이므로, a[3]도 변함!
# ''')

enterToContinue(True, 'Tuple 설명 보기')
printThenEval('''
print('List와 그냥 거의 같음.')
print('유일한 차이점 : 내용물을 바꿀 수 없다. (a[3] = 4 이런거 안됨)')
print('index, count 등등 함수들도 똑같이 쓸 수 있음.')
print('단, 값을 변경할 수 없으니 당연히 뭐다? sort, reverse 이런건 안된다~')
print('심지어 [i for i in range(3)] 처럼 tuple(i for i in range(3)) 이렇게도 쓸 수 있다~')
''')

enterToContinue(True, '문자열 설명 보기')
printThenEval('''
print('문자열도 시퀀셜임? ㅇㅇ 글자들의 나열 = 글 = 문자열')
print('얘도 내용물을 바꿀 수 없다. 따라서 tuple이랑 거의 똑같')
print('a = "this is string" 이런 식')
''')

enterToContinue('문자열 관련 함수 보기')
printThenEval('''
s = 'abcde'

# 'bc'의 위치 구하기 (없으면 -1)
print(s.find('bc'))
# 'c'의 위치 구하기 (없으면 -1)
print(s.find('c'))
''')

enterToContinue()
printThenEval('''
s = ' Ab cD  e'

print(s.lstrip())               # 왼쪽 공백 제거
print(s.rstrip())               # 오른쪽 공백 제거
print(s.strip())                # 양쪽 공백 제거
print(s.upper())                # 알파벳 모두 대문자로 변경
print(s.lower())                # 알파벳 모두 소문자로 변경
print(s.replace('cD', 'Fg'))    # 'cD'를 찾아서 모두 'Fg'로 변경

# 이거 중요 까먹으면 절대 안 되는 함수
print(s.split())                # 공백 기준으로 쪼개서 각각을 원소로 하는 배열 생성

# 가장 많이 쓰이는 split 예시
l = input('두 단어 입력 : ').split()
print(l)
print(l[0])
print(l[1])
# 한 줄에 띄어쓰기로 구분된 입력 받을 때 국룰 형태임

# 문자열이 어떤 문자열의 일부인지 확인하는 법
if 'ab' in '22abcd':
    print('yes!')
else:
    print('no!')

if 'ac' in '22abcd':
    print('yes!')
else:
    print('no!')
''')

enterToContinue(True, '문자열 포매팅 설명 보기')
printThenEval('''
print('포매팅이란 : string 안에 원하는 내용을 원하는 형태로 집어넣는 것')
print('크게 3가지 방식이 있음')
''')

enterToContinue(True, '첫 번째 포매팅 방법 : % 포매팅 보기')
printThenEval('''
# 정수 포매팅
print('%d'%3)
print('%d' % 4)
print('3칸 확보 =>%3d' % 5)
print('3칸을 0으로 채우면서 확보 =>%03d' % 5)
print('8진수 %o, 16진수 %x, 16진수 대문자 %X' % (3, 4, 5))
print('%08x ~~ example -- %3d' % (3, 4))    # 추가 예시
''')
printThenEval('''
# 실수 포매팅
print('%f'%3)
print('%f' % 3.5)
print('소수점 아래 3자리까지만 표시하고 나머지 버림 =>%.3f' % 1.1435)
print('8칸 확보 =>%8f' % 1.1435)
print('8칸을 0으로 채우면서 확보 =>%08f' % 1.1435)
print('%08.3f' % 1.25825)    # 추가 예시
''')
printThenEval('''
# 문자열 포매팅
print('에붸붸%s엡붸뷉' % 'ab cd')
''')

enterToContinue(True, '두 번째 포매팅 방법 : .format 포매팅 보기')
printThenEval('''
print('{0}'.format(3))
print('{0}, {1}, and {2}'.format(1, 2.0, 'three'))
print('{0} <= this is {0}, {1} python!!'.format(3, 'fuck'))
print('{1} 순 {0} 서 {2} 뒤 {1} 죽 {0} 박죽도 {3} 가능 {2}'.format('a', 'b', 3, [2, 3]))
''')

enterToContinue('세 번째 포매팅 방법 : f-str 포매팅 보기')
printThenEval('''
# 문자열 포매팅
a = 3
b = 'abc'
c = 3.14
d = [1, 2]
print(f'a = {a}, b = {b}, c = {c}, d = {d}')
''')

enterToContinue(True, '시퀀셜 타입들 관련 함수/문법 보기')
printThenEval('''
# 여기 나오는 함수들은 대부분 List, Tuple, 문자열 공통임

a = [3, 2, 4, 1, 3]

print(len(a))   # 길이 구하기
print(max(a))   # 최대값 구하기
print(min(a))   # 최소값 구하기
print(sum(a))   # 합 구하기, 문자열은 사용불가능 (문자들의 합,, 이상하잖어)

# 3의 위치 구하기 (중복이 있으면 제일 처음 등장하는 위치)
# 찾는 값이 없으면 오류남!!
print(a.index(3))

# 3의 개수 구하기
print(a.count(3))
''')
printThenEval('''
# 인덱싱과 슬라이싱! 모든 시퀀셜 타입 (List Tuple 문자열 등등 전부 다)
# 인덱싱 : 특정 위치의 원소에 접근
# 슬라이싱 : 특정 구간을 잘라서 새로운 오브젝트 추출

a = 'abcdefg'

print(a[1:3])       # 구간 [1, 3)을 추출
print(a[:3])        # 시작구간 생략하면 0 (range와 연결지어서 기억하기)
print(a[1:])        # 끝구간 생략하면 맨 끝까지로 취급
print(a[:])         # 전체 구간
print(a[2:5:2])     # range와 연결지어서 생각해보기
print(a[::-1])      # 순서를 뒤집을 때 쓸 수 있는 테크닉! (range와 연결지어서 생각해보기)
''')
enterToContinue()
printThenEval('''
# 그렇다면 a[:]는 a의 얕은 복사일까?
# ㄴㄴ 슬라이싱은 항상 깊은 복사이다!
a = [1, 2, 3]
b = a[:]
b[2] = 4
print(a)
print(b)
''')

enterToContinue(True)
#
#
# Functions
#
#

print('''
4. 함수
''')

enterToContinue(True, '설명 보기')
# semicolon

printThenEval('''
print('함수 : 한자로 상자 함 + 수 (number)')
print('말그대로 초딩 때 배운 상자수를 생각하면 된다\\n')
print('       3        ')
print('-----|    /-----')
print('|              |')
print('|     x2       |')
print('|              |')
print('----/    |------')
print('      6         ')
print('\\n^^이거')
print('\\n즉, 인자를 받아서 뭔갈 하고 결과를 제공하는 기계, 상자, 덩어리를 의미한다')
print('다르게 말하자면 일종의 코드 묶음이다.')
''')

enterToContinue('함수관련 용어정의 보기')
printThenEval('''
print('굉장히 중요하니 절대 헷갈리지 않게 익히도록')
print('호출 (call)          : 정의된 함수를 실행하는 것')
print('반환값 (return값)    : 호출된 함수가 실행을 끝마치고 알려주는 결과값')
print('인자, 호출인자 (argument)    : 함수를 호출할 때 넘겨주는 값')
print('매개변수 (parameter)         : 인자를 저장하는 변수')
''')

enterToContinue('함수 정의하는 법과 호출하는 법 보기')
printThenEval('''
# adder라는 이름의 함수를 만든다.
# 이 함수는 매개변수 a, b를 받는다.
def adder(a, b):    # 여기!
    c = a + b
    return c

print(adder(3, 5))
# adder(3, 5)는 여기!로 이동해서 함수를 실행한 후 return값 8로 대체된다
# print(adder(3, 5)) 가 print(8)이 되는 것

# 혼동주의!
# 여기에서 인자는 3과 5이고, a와 b는 매개변수이다.
''')

enterToContinue('예시 더보기')
printThenEval('''
def sub(a, b):
    c = a - b
    return c

print(sub(a = 3, b = 5))  # 어떤 매개변수에 어떤 인자를 주는 지 정확하게 적어줄 수도 있다.
print(sub(b = 5, a = 3))  # 이러면 적는 순서도 상관없어진다.
print(sub(3, 5))          # 이러면 정의한 순서대로 들어간다.
''')

enterToContinue('예시 더보기')
printThenEval('''
def swap(a, b):
    return b, a     # 값을 여러 개 리턴할 수도 있다!

x, y = swap(1, 3)   # x, y = 3, 1 이 된다.
print(x, y)
''')

enterToContinue('예시 더보기')
printThenEval('''
def adder(a, b = 2):    # 기본값을 정해줄 수도 있다
    return a + b

print(adder(1, 4))
print(adder(1))         # b가 기본값인 2라고 자동으로 취급된다
''')

enterToContinue('예시 더보기')
printThenEval('''
def sub(a = 3, b = 2):
    return a - b

print(sub(1, 4))
print(sub(b = 1))   # 어떤 인자를 생략했고 어떤 인자를 준 건지 표기해줄 수 있다.
print(sub(a = 1))   # 주어지지 않은 인자가 자동으로 정해준 기본값으로 취급된다
print(sub(1))       # 표기를 따로 안 해주고 생략하면 앞쪽부터 채우고 뒤쪽을 기본값 취급한다
''')

enterToContinue('예시 더보기')
printThenEval('''
# 아래 코드를 해석해서 실행 흐름이 어떻게 될 지 이해하고 결과를 확인하시오

def adder(a, b):
    print('yoyo')
    return a + b

def func():
    global adder    # 이 줄은 원래는 필요없음. 없다고 생각하고 무시하셈
    x = adder(4, -1)
    print(x)
    return      # 리턴할 때 아무 것도 리턴하지 않아도 된다

func()
''')

enterToContinue(True, '지역변수 vs 전역변수 보기')
printThenEval('''
yo = 'yoyo'             # 여기는 전역이다
a = 3                   # 여기는 전역이다

def adder(a, b):
    global yo           # 여기는 지역이다
    print(yo)           # 여기는 지역이다
    return a + b        # 여기는 지역이다

print(adder(1, 2))      # 여기는 전역이다

# 함수 안은 지역, 함수 밖은 전역
# 지역에서 선언된 변수는 지역변수, 전역에서 선언된 변수는 전역변수
''')
enterToContinue()
printThenEval('''
# 위와 동일한 코드로 global 명령어를 알아보자

yo = 'yoyo'             # 전역변수 yo
a = 3                   # 전역변수 a

def adder(a, b):
    global yo           # 전역변수 yo를 지역에서 사용하겠다는 뜻.
    print(yo)           # 여기부터는 yo는 전역변수 yo이다
    return a + b

print(adder(1, 2))

# global로 알려주지 않으면
#  => 지역에서는 전역변수의 존재를 알지 못한다.
#    => 값을 사용하려고 '뭐시기 = yo 등등'을 쓰면 에러가 난다.
#    => 대입하려고 'yo = 뭐시기'를 쓰면 지역변수 yo가 새로 생성돼버린다.
#      => 지역변수로 생성돼버린 후에 나중에서야 global을 쓰려고 하면 에러가 난다.
''')
enterToContinue('추가 예시 보기')
printThenEval('''
def sub(x, y):      # 이 함수 내에서 a만 전역변수라는 점에 주의!
    global a
    a = 7
    x, y = y, x     # x에는 y, y에는 x를 대입하므로 둘이 서로 값이 바뀐다
    b = 3           # b는 global을 안 썼으니 그냥 새로 만든 지역변수!
    print(a, b, x, y)
a, b, x, y = 1, 2, 3, 4
sub(x, y)
print(a, b, x, y)
''')

