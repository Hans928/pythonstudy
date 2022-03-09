# 반복문

# for문

from pickle import HIGHEST_PROTOCOL


fruits = ["apple","peach","pear"]

for fruit in fruits: # for 키워드 단일항목 in 키워드 반복 수행하고 싶은 리스트명
    print(fruit)
    # 반복문은 동일한 줄의 코드를 여러차례 수행하게 해준다.
    # 위의 경우는 출력문을 세 번 실행하고 있지만 for문은 그저 단일문을 실행하는데 그치지않는다.
    # 전체 블록문을 거듭하여 실행 가능하다.
    print(fruit + " pie")
    # 들여쓰기가 매우 중요하다.
    # for 반복문 내부에 있으며 그 안의 내용은 다 반복해서 수행하기 때문이다
print(fruits)


# 평균 키
# 학생 키 리스트로 부터 평균 키를 구하라.


# student_heights = input("학생들의 키 리스트를 적으시오 ").split()
# for n in range(0,len(student_heights)):
#     student_heights[n] = int(student_heights[n])
    
    
# print(student_heights)


# print(len(student_heights)) # 리스트의 크기를 구하는 함수
# print(sum(student_heights)) # 리스트 항목의 합을 구하는 함수
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average = round(total_height / number_of_students)
# print(average)
# 하지만 이번엔 위의 함수를 사용하지 않고 for문을 사용해서 평균을 구할 것입니다.

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# number_of_students = 0
# for student in student_heights:
#     number_of_students+=1
# print(number_of_students)

# print(round(total_height/number_of_students,1))




# 가장 높은 점수를 출력하는 코드

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# print(max(student_scores)) # 항목 내 최대값
# print(min(student_scores)) # 항목 내 최소값
# # 위의 방법을 사용하지 않고 for문으로 구현 해 볼 것

# highest_score = 0
# for score in student_scores:
#     if score>highest_score:
#         highest_score = score
        
# print(f"제일 높은 점수는 {highest_score}")



# for 반복문과 range 함수
# for number in range(1,10): #1~9까지 출력
#     print(number)

# for number in range(1,10 ,3): #1~9까지 출력 3씩 커짐
#     print(number)

# 1부터 100까지 더하기.
# total = 0

# for number in range(1,101):
#     total+=number

# print(total)

# 1부터 100까지의 숫자중 짝수를 다 더하시오(1과 100을 포함할 것)
# total = 1
# for number in range(2,101,2):
#     total+=number
# print (total)

# total2 = 1
# for number in range(1,101):
#     if number %2==0:
#         total2+=number
# print(total2)

#FizzBuzz

# 차례대로 숫자를 하나씩 말하는 데 3의 배수일 경우엔 fizz라고 말한다. 5의 배수에선 buzz 라고 말한다
# 3과 5의 배수일 경우엔 fizzbuzz라고 말한다.


# for game in range(1,101):
#     if game %3==0 and game%5==0:
#         print("FizzBuzz")
#     elif game %3 ==0:
#         print("Fizz")
#     elif game %5 ==0:
#         print("Buzz")
#     else:
#         print(game)
        
        
# 비밀번호 생성기

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pw_letters = int(input("문자가 몇개 포함되길 원합니까? "))
pw_symbols = int(input("특수기호는 몇 개가 포함되길 원합니까? "))
pw_numbers = int(input("숫자는 몇 개가 포함되길 원합니까? "))

# easy level 글,기호,숫자 순서대로
# fdje$#23

password =""
for char in range(1,pw_letters+1):
    #ex) pw =4  1~4
    
    # random_char = random.choice(letters)
    # password +=random_char 
    # 한 줄로 줄이면 아래와 같음.
    password += random.choice(letters)
for char in range(1,pw_symbols+1):
    password += random.choice(symbols)
for char in range(1,pw_numbers+1):
    password +=random.choice(numbers)
print(password)

# hard level 랜덤
# j3fr$d2*

password_list = []

for char in range(1,pw_letters+1):
    password_list.append(random.choice(letters))
    #+=나 append나 같은 작업을 수행함
for char in range(1,pw_symbols+1):
    password_list += random.choice(symbols)
for char in range(1,pw_numbers+1):
    password_list +=random.choice(numbers)

random.shuffle(password_list)
print(password_list)

password2 =""

for char in password_list:
    password2 += char
print(f"당신의 비밀번호는 {password2}")
