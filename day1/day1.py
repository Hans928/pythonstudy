#출력형 / 괄호 내의 문장을 출력함.


# print("Day 1 - Python Print Function")
# print("The function is declared like this :")
# print("print('what to print')")
# print("Hello world!\nHello world!")
# print("hello" + " " + "hansol")
# print("hello"+ '"+"' + "world")


#Syntax Error -> 문법 상 오류. ex) 큰따옴표나 괄호가 제대로 안 닫힘.
#indentation Error -> 들여쓰기 오류. 코드는 언제나 문장 맨 앞에서 시작해야하함. 앞에 공백이 있으면 안 됨


#입력형 / 입력 값을 받을 수 있음

# input("What is your name?")

# print("Hello " + input("What's your name?")+"!")
#input 함수 실행 -> 이름 입력받고 -> Hello 이름! 출력

#ctrl+/ 드래그 되어있는 문장 전체 주석

#입력값을 받은 후 입력값의 문자열 길이를 구하기


# print(len(input("What is your name? ")))


#파이썬 변수

#name 이라는 변수를 선언해줌으로써 변수안에 입력값을 저장 가능함

# name = input("What is your name? ") 
# print(name)
# ex) 전화번호부에 전화번호만 적어놓으면 나중에 이게 누구 전화번호인지 알 수 없다. 
# 누구의 번호인지 이름도 적어야한다. 변수가 전화번호부의 이름과 같은 역할이다. 
# 다음에 번호가 필요할때면 이름만 검색해서 알 수 있다. 
# 코드로 치면 변수 선언만 하면 변수 내에 저장된 데이터를 사용 가능한 것이랑 같은 의미이다.

# name = "hans"
# print(name)
# name = "sol"
# print(name)

#변수의 내용은 언제나 쉽게 변경 가능하다. 다시 선언해주면 된다.

#입력받은 값의 길이 구하는 코드를 변수를 이용하여 좀 더 간단히 만드는 방법

# name = input("What is your name? ")
# length = len(name)
# print(length)



# 변수 게임(둘의 내용 바꾸기.)

# a = input("a : ")
# b = input("b : ")

# c =  a
# a = b
# b = c

# print("a = "+ a)
# print("b = "+ b)


# 변수 이름 짓기 (원하는 대로 지정해도 되긴하지만 하지만 가독성을 생각해야한다.)
# 중간에 공백이 들어가야할 경우  _ 를 사용한다.
# 변수의 시작이 숫자면 안된다. 혹은 기능이 들어간 print 나 input 같은 단어를 쓰면 안된다.

# NameError => 이름이 지정되지 않음. 오타이거나 지정 안된 변수를 사용했을 경우

