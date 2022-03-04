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

