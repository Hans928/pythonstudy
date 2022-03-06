# 조건문
# IndentationaError : 들여쓰기 오류
# 연산자 같다는 뜻일 땐 ==, = 일땐 변수 설정을 해준다는 뜻

# 홀,짝

# % => 나머지를 구해주는 연산자. ex) 7 % 2 => 1

# number = int(input("숫자를 입력하세요. : "))

# if(number%2==1):
#     print(f"{number}는 홀수입니다")
# else:
#     print(f"{number}는 짝수입니다.")



# 중첩 조건문

# print("놀이공원에 오신걸 환영합니다.")
# height = int(input("키가 몇 cm인가요? "))

# if height>=120:
#     print("입장을 환영합니다.")
#     age = int(input("몇 세이신가요?"))
#     if age>=20:
#         print("10000원입니다.")
#     elif age>=14 and age<=19:
#         print("8000원입니다.")
#     elif age>=8 and age<=13:
#         print("6000원입니다.")
#     else:
#         ("무료입장입니다.")
# else:
#     print("죄송합니다 입장이 불가합니다.")

# BMI 계산기 업데이트

# height = input("enter your height in m : ")
# weight = input("enter your weight in kg : ")

# bmi = int(weight)/float(height)**2
# bmi_float = float(round(bmi,1))
# print(f"당신의 bmi 지수는 {bmi_float}")

# if bmi_float<18.5:
#     print("저체중입니다.")
# elif bmi_float<25:
#     print("정상체중입니다.")
# elif bmi_float<30:
#     print("비만입니다.")
# elif bmi_float<35:
#     print("고도비만입니다.")
# else:
#     print("초고도비만입니다.")


# 윤년
# 윤년은 4로 나뉘어지는 해. 그러나 100으로 나눠지는 해는 예외이다. 하지만 400으로 나뉘어지면 윤년이다.
# 논리 이해가 중요하다. 순서도를 그릴 줄 알아야한다. 순서도만 그릴 줄 알면 코드 짜기는 쉽다.


# year = input("몇 년도 입니까? ")

# if int(year)%4==0:
#     if int(year)%100==0:
#         if int(year)%400==0:
#             year=1
#     else:
#         year=1          
# else :
#     year=2

# if year==1:
#     print("윤년입니다.")
# else:
#     print("윤년이 아닙니다.")


# 다중연속if문
# 위의 놀이공원에 사진 촬영 서비스의 유무에 따라 추가금액 추가 여부

# print("놀이공원에 오신걸 환영합니다.")
# height = int(input("키가 몇 cm인가요? "))

# if height>=120:
#     print("입장을 환영합니다.")
#     age = int(input("몇 세이신가요?"))
#     if age>=20:
#         price=10000
#     elif age>=14 and age<=19:
#         price=8000
#     else:
#         price=6000
        
#     picture = input("사진을 찍으시겠습니까? Y,N ")
#     if picture==("Y"):
#         price+=3000
#     else:
#         price=price
#     print(f"{price}원입니다.")
        
# else:
#     print("죄송합니다 입장이 불가합니다.")


#피자 주문

# print("피자집에 오신걸 환영합니다.")
# size = input("피자의 사이즈를 선택하세요. S,M,L ")

# price = 0

# if size ==("S"or"s"):
#     price += 15000
# elif size ==("M"or"m"):
#     price += 18000
# else:
#     price += 20000

# pepe_topping = input("페페로니 토핑을 추가하시겠습니까? Y,N ")
# if pepe_topping==("Y"or"y"):
#     if size==("S"or"s"):
#         price+=2000
#     else:
#         price+=3000

    
# ch_topping = input("치즈 토핑을 추가하시겠습니까? Y,N ")
# if ch_topping==("Y"or"y"):
#     price+=1000

# print(f"{price}원 입니다.")


#논리 연산자

# a and b : 두개의 전제가 다 참이어야한다.
# c or d : 둘 중 하나만 참이어도 된다.
# not e : e가 거짓이면 참, 참이면 거짓

# print("놀이공원에 오신걸 환영합니다.")
# height = int(input("키가 몇 cm인가요? "))

# if height>=120:
#     print("입장을 환영합니다.")
#     age = int(input("몇 세이신가요?"))
#     if age>=20:
#         price=10000
#         if age>=70:
#             price=0
#     elif age>=14 and age<=19:
#         price=8000
#     else:
#         price=6000
        
#     picture = input("사진을 찍으시겠습니까? Y,N ")
#     if picture==("Y"):
#         price+=3000
#     else:
#         price=price
#     print(f"{price}원입니다.")
        
# else:
#     print("죄송합니다 입장이 불가합니다.")


# 사랑계산기
# 본인 이름과 상대방의 이름을 적고 그 이름에 true,love 몇번 나오는지 세고 true *10 love 의 퍼센트만큼 서로 사랑한다고 계산해주는 계산기

# lower 함수 -> 알파벳 대문자를 다 소문자로 바꾼다.
# count 함수 -> 문자열에서 글자 나오는 횟수를 알려줌.ex) Kim.count(k) -> 0 대문자와 소문자 구별.

# 10점 이하이거나 90점 이상이면 점수와 함께 콜라와 멘토스 같은 사이시네요.(최악이거나 찰떡이거나) 출력
# 40-50점 사이면 점수와 함께 잘 어울리시네요. 출력
# 나머지는 그냥 점수만 알려준다.

# print("사랑계산기")
# name1= input("what is your name? \n")
# name2= input("what is your name? \n")

# combined_string = name1+name2

# low_string = combined_string.lower()

# t = low_string.count("t")
# r = low_string.count("r")
# u = low_string.count("u")
# e = low_string.count("e")

# true =  t+r+u+e

# l = low_string.count("l")
# o = low_string.count("o")
# v = low_string.count("v")
# e = low_string.count("e")

# love =  l+o+v+e

# love_score = true*10+love
# # love_score = int(str(true)+str(love)) 이렇게 해도 가능

# if love_score <=10 or love_score>=90:
#     print(f"당신의 사랑점수는 {love_score}, 콜라와 멘토스 같은 사이시네요.")
# elif love_score>=40 and love_score<=50:
#     print(f"당신의 사랑점수는 {love_score}, 잘 어울리세요")
# else:
#     print(f"당신의 사랑점수는 {love_score}")




