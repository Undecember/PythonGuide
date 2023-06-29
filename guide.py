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
4. 시퀀셜 타입들 - List, Tuple
5. 함수
6. 문자열
7. 파이썬의 에러들
8. 파일입출력

이 프로그램은 python 코드와 그 실행 결과를 쌍으로 알려주면서 공부를 도와준다.
예시로 알려주는 코드마다 바로 실행결과를 보지 말고, 코드만 먼저 보고 실행결과를 예측해보면서 공부할 것!!
하지만 print만 써서 도배돼있는 코드는 그냥 설명용이니까 결과만 꼼꼼하게 봐도 된다.
보다보면 뭔 소린지 알 듯

이 프로그램을 되도록 30번 이상 (최소 10번은) 꼼꼼하게 익히면서 실행하도록.
''')

enterToContinue(True)
#
#
# Python functions
#
#

print('''
* Python의 몇몇 기본 함수
''')

enterToContinue(True)
# print

printThenEval("print('출력할 텍스트')")

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
# int
printThenEval('''
print('int는 정수로 변환하는 함수 (integer)')
print(int('1374'))
print(int('-35'))
''')

enterToContinue(True)
#
#
# Python grammars
#
#

print('''
* Python만의 ㅈ같은 문법
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
print('range(s, e, d) : s부터 e 전까지 (s <= i < e) d씩 늘리면서 값을 생성')
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
for i in range(1, 6, 2):
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
print('따라서 map(abs, [ 3, -4, 5, -6 ]) != [ 3, 4, 5, 6 ] 임')
print('전자는 3, 4, 5, 6을 생성할 \\'준비가 된\\' map 오브젝트일 뿐이지 list가 아님!!')
''')

# 1. Python 주요 함수 2. Python만의 ㅈ같은 문법 3. 모듈이란 4. 시퀀셜 타입들 - List, Tuple 5. 함수 6. 문자열 7. 파이썬의 에러들 8. 파일입출력
