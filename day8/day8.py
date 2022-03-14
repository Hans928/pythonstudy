# 입력값을 넣을 수 있는 함수

# 위 함수를 이용하여 암호 프로그램을 만들 것이다.
# 이 암호 프로그램은 카이사르 암호
# 카이사르 암호란 고전적인 암호화 방식이다.
# 카이사르가 민감한 군령을 보낼때 각각의 알파벳의 정해진 만큼 뒤의 알파벳을 
# 사용해서라고 한다.
# ex) 정해진 숫자가 3일 경우 a는 d가 되고 b는 e가 되는 방식이다.



def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
    
greet()

# def my_function(somthing):
#     # Do this with something
#     # Then do this something
#     #Finally do this something

# usb를 꽂는 것과 비슷하다. 다른 usb를 꽂으면 컴퓨터에서는 다른 파일이 보이는 것처럼
# something에 입력한 값에 따라 다른 결과를 출력한다.

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do? {name}?")

greet_with_name("hans")    
greet_with_name("kyle") 

# name = hans
# name은 변수이고 넣어준 데이터 hans와 같다.
# name은 parameter, 데이터 즉 hans는 argument
# argument란 호출되는 데이터. 즉 그 데이터의 실제값
# parameter 그 데이터 이름으로 함수 안에서 그 변수가 사용될 때 쓰인다. 즉 함수에 전달된 데이터의 이름



# 여러 개의 입력값을 받는 함수

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("hans","Nowhere")
greet_with("Nowhere","hans")

# 파이썬 코딩에서는 함수를 호출할 때 어떤 파라미터에 어떤 데이터가 할당 될지 특정하지않고
# 위치만으로 결정하기 때문에 위치인자라고 한다. 
# 함수에서 파라미터의 순서대로 들어가기 때문에 함수를 호출하는 기본적인 방법이다.
# 즉 결과가 원하는 데로 안나오면 파라미터의 순서에 맞게 입력했는지 확인해봐야한다.

# 그래서 더 확실하게 하려면 키워드 인자를 사용하면 좋다.
# 함수에 아규먼트만 딱 넣는 것 보단, 각각의 파라미터의 이름과 등호를 이용해 할당하는 법이다.

greet_with(location="nowhere",name="hans")


