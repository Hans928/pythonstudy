#파이썬의 무작위화, 리스트

# 각 상황마다 다른 행동을 하는 프로그램을 만드려면 일정 수준의 무작위성이 필요하다.
# ex) 가위바위보, 테트리스

# random 모듈

import random
from turtle import position

# c= random.randint(100,200) #100이상 200 이하 숫자 랜덤으로 생성
# print(c)

# 모듈이란
# 모듈은 프로그램에서 서로 다른 기능을 담당한다 
# ex) 자동차를 만들 때 타이어 제작, 차체 제작, 엔진 제작등이 각각 모듈이고 이를 합치면 차가 완성이 된다.
# 즉 random모듈은 파이썬이 유사난수를 생성하기 위한 복잡한 수식 없이 손쉽게 난수를 생성할 수 있도록 만든 모듈이다

# 자신의 모듈을 만들 수 있는 법이 있나? and 모듈의 원리는?

# 좌측의 files의 아이콘에 my_moduel.py를 생성. 하고 그 안에 값을 넣어주고 import my_module로 import를 한 후 사용하면 된다.




# 부동 소수점 난수 생성.

# random_float = random.random() # 0이상 1미만의 난수만 출력
# print(random_float)

# 만약에 0~5사이의 난수를 출력하려 한다면?
# print(random_float*5)



# 사랑계산기 v2

# love_score = random.randint(1,100)
# print(f"당신의 사랑 점수는 {love_score}")


# 동전 앞뒤

# random_side = random.randint(0,1)
# if random_side ==1:
#     print("앞면")
# else:
#     print("뒷면")
    
    

#파이썬 리스트

# 리스트 = 데이터 구조 즉 데이터를 체계화하고 저장하는 방식

# ex) 대한민국의 도 =[경기도,강원도,.....]

# 데이터의 순서를 지정해야 할 수도 있다.
# ex) 가상의 대기열에 줄을 서고 있는 모든 사람들을 저장하는 경우 사람들이 줄을 선 순서도 저장.
# => 부적절한 데이터 구조로 인해 마지막에 줄을 선 사람이 대기열을 건너 뛰면 안되기 때문

# 모든 데이터 형식을 저장 가능하며 혼합해서도 저장 가능하다.

# US_state = ["Delaware","Pennsylvania"]
# print(US_state[0])
# print(US_state[-1]) #리스트의 뒤에서 부터 시작. 마지막항목이 -1이다 -0은 없기 때문이다

# US_state[0] = "Del" # 리스트 내용 수정

# US_state.append("New Jersey") # 리스트의 마지막에 추가

# US_state.extend(["Georgia","Connecticut"]) #리스트의 마지막에 항목 여러개를 추가

# print(US_state)



# 금융가 룰렛 => 명함을 내고 계산을 누가 할 것인가


# name = input("각자의 이름을 적으시오. 각자 이름을 적은 후 ,를 찍어주세요.")
# rullet = name.split(",")
# print(rullet)
# # rd = random.randint(0,len(rullet)) # print(rullet[rd]+"가 오늘 밥을 삽니다.") / 내 방식

# num_items = len(rullet) # 리스트 데이터 갯수
# choice = random.randint(0,num_items-1) # 0부터 숫자를 세기 때문에 총 개수 -1 을 해줘야한다.
# print(rullet[choice]+"가 오늘 밥을 삽니다.")



#index error inex out of range => 항목의 갯수보다 큰 숫자를 출력하려 할때 
# ex) 50개의 주가 있는 미국의 주 리스트를 출력하는데(0~49) 50번을 출력하려 하면 위의 에러가 뜬다.
# ex) num_of_state = len(state_of america) => print(state_of_america[num_of_states])
# 위를 off-by-one 에러라고 한다.



# 중첩리스트


# dirty_dozen = ["strawberries","spinach","kale","nectarines","apples","grapes","peaches","cherries",
#                "pears","tomatoes","celery","potatoes"] #기생충이 많은 야채 순

# print(dirty_dozen)

# fruit = ["strawberries","nectarines","apples","grapes","peaches","cherries","pears"]
# vegetable = ["spinach","kale","celery","potatoes"]

# dirty_dozen = [fruit,vegetable] #중첩리스트

# print(dirty_dozen)

# print(dirty_dozen[1][1]) # 1번위치의 1번


# 보물찾기

# row1=["0","0","0"]
# row2=["0","0","0"]
# row3=["0","0","0"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("어디에 보물을 두시겠습니까? (몇 행 몇 열인지 숫자로만 입력하세요) ")


# horizonal = int(position[0])
# vertical = int(position[1])

# select_row = map[vertical-1]
# select_row[horizonal -1] ="x"
# 방법 1

# map[vertical-1][horizonal -1]="x"
# 방법 2


# print(f"{row1}\n{row2}\n{row3}")



# 가위바위보 
# 주먹은 0,보는 1, 가위는 2

choose = int(input("무엇을 내겠습니까? 주먹은 0, 보자기는 1, 가위는 2입니다. "))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)

    
computer_choose = random.randint(0,2)
print("Computer choose : \n")

if computer_choose == 0:
    print(rock)
elif computer_choose == 1:
    print(paper)
elif computer_choose ==2 :
    print(scissors)
    
if choose == 0:
    if computer_choose==0:
        print("비겼습니다.")
    elif computer_choose ==1:
        print("당신이 졌습니다.")
    elif computer_choose ==2:
        print("당신이 이겼습니다.")
elif choose ==1:
    if computer_choose==1:
        print("비겼습니다.")
    elif computer_choose ==2:
        print("당신이 졌습니다.")
    elif computer_choose==0:
        print("당신이 이겼습니다.")
elif choose ==2:
    if computer_choose==2:
        print("비겼습니다.")
    elif computer_choose ==1:
        print("당신이 이겼습니다.")
    elif computer_choose ==0:
        print("당신이 졌습니다.")

        
        
 ## 가위바위보 수정본

choose = int(input("무엇을 내겠습니까? 주먹은 0, 보자기는 1, 가위는 2입니다. "))
game_image = [rock, paper, scissors]
if choose >=3 or choose < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_image[choose])

    
    computer_choose = random.randint(0,2)
    print("Computer choose : ")

    print(game_image[computer_choose])
    

    if choose == 0 and computer_choose ==2:
        print("you win")
    elif choose == 2 and computer_choose ==0:
        print("you lose")
    elif computer_choose > choose:
        print("you lose")
    elif computer_choose < choose:
        print("you win")
    elif choose == computer_choose:
        print("draw")



