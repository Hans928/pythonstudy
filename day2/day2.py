#Data Type

#String

#문자열 : 큰따옴표나 작은 따옴표로 묶어야함.

print("hello"[4])
print("1234"[3])
# 위의 경우 1234를 숫자가 아닌 문자로 취급 즉 "123"+"123" 해도 246이 아닌 123123을 출력

#Integer

# 숫자 데이터 형식 : 소수점 이하 숫자가 없는 정수형 데이터 타입. 그냥 숫자만 치면 됨

print(123+123)
# 큰 숫자의 경우 100,000,000 이라 쓰는 경우도 있는데 ,대신 _를 사용
print(100_000_000+1)


#Float

#소수점이 있는 숫자



#Boolean

# 두가지 값만 있음. True, False

# 주로 프로그램에서 무언가를 테스트 할 때 쓴다. 이것이 참인지 거짓인지.add()


# len 함수를 사용할때 정수를 사용하면 오류가 나옴.(TypeError) ex)len(123)
# 데이터 형식을 확인하는 법 : type 함수를 사용할 것. ex)print(type(123))

# 문자열로 데이터 형식 변경 str함수를 사용
# 소수형으로 데이터 형식 변경 float 함수를 사용
# ex)
# num_char = len(input("What is your name")) // num_char의 데이터 타입 -> int
# new_num_char = str(num_char) -> num_char의 데이터값을 문자열로 변환한 값을 new_num_char에 저장.
# print("Your name has"+ num_char + "characters") // 데이터 타입이 정수라 오류가 뜬다.
# print("Your name has"+ new_num_char + "characters") // 데이터 타입이 문자열이라 오류가 안 뜬다.

# print(70 + float(100.5))
# a=100
# print(float(a))


# 두자리의 숫자를 입력받아 두 숫자의 합을 구하시오

# num = (input("number: "))
# print(int(num[0])+int(num[1]))

# 연산기호 덧셈=>+ 뺄셈=> - 곱셉=> * 나눗셈 => / 제곱 =>**
# 처리순서는 수학과 같음 괄호 -> 제곱 -> 곱,나눗셈 -> 덧,뺄셈


# BMI지수 계산기

# BMI => 몸무게 / 키의 제곱

# height = input("enter your height in m : ")
# weight = input("enter your weight in kg : ")

# bmi = int(weight)/float(height)**2
# bmi_int = int(bmi) 
# # 소수점 뒤의 부분을 다 자르고 정수부분만 살림.

# print("Your BMI is " +str(bmi_int))


#반올림 round 함수 뒤의 쉼표는 몇번째 자리에서 반올림 할 것인가를 설정
print (round(8/3,2))
print (round(2.5555555,2))

# 버림 // 자동으로 float형에서 int형으로 바꿈
# 나눗셈이 완전히 맞아 떨어져 정수로 출력할때도 뒤에 .0이 생략된 것이므로 실수형이지만 버림일 경우는 무조건 정수
print(8//3)


#F-String 
# => 데이터타입을 통합시켜줌. 그동안은 한 문장에 출력하려면 각각 데이터 타입을 맞춰줘야 했는데 그럴 필요가 없어짐

score = 100
height = 1.83
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


# 팁계산기

# total = input("총액이 얼마인가요?")
# tip = input("팁을 몇퍼센트 줄것인가요? 10,12,15 ")
# person = input("몇 명이서 먹었나요? ")

# tip_total = int(total)+int(total)*(float(tip)/100)
# total_person = round(float(tip_total)/int(person),2)

# print(f"내가 내야할 금액은 {total_person}")



