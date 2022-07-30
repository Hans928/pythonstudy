# Dictionaries

# 실제 사전과 비슷하게 작동함. 관련된 정보를 몇개의 그룹으로 묶어줄 수 있기 때문에 매우 유용
# 키(Key)와 값(Value)으로 나뉘는데 사전으로 치면 키는 단어, 값은 단어의 정의라고 칭할 수 있다.

# {Key:Value} 이렇게 생성한다.
# -> ex) {"Bug":"An erroer in a program"}
# 여러개를 넣고 싶을 때는
# -> ex) {
#           "Bug":"An erroer in a program",
#           "Function":"~~",
#           "loop":"~~~"
#        }


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing someting over and over again.",
}
# 항목이 더 없어도 끝에 , 를 찍는 이유는 나중에 추가할 때 편하게 하기 위해서이다.

print(programming_dictionary)
print(programming_dictionary["Bug"])
programming_dictionary["key"] = "value"  # 추가
print(programming_dictionary)

empty_dictionary = {}


# dictionary를 통째로 지우는 법
# programming_dictionary={}
# print(programming_dictionary)


# dictionary 안을 수정하는 방법
programming_dictionary["Bug"] = "수정"
print(programming_dictionary)

# 즉 키가 없는 값을 넣어주면 추가, 있는 값으로 하면 수정


# dictionary로 반복문 쓰는 법.

for thing in programming_dictionary:
    print(thing)  # 여기선 키만 출력됨
    # value도 출력하려면
    print(programming_dictionary[thing])


# 등급 매기는 프로그램.


# 등급 A :91점 이상 , B : 81-90, C : 71-80, F : 70미만

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

# version 1

for student in student_scores:
    if student_scores[student] >= 91:
        grade = "A"
    elif student_scores[student] >= 81:
        grade = "B"
    elif student_scores[student] >= 71:
        grade = "C"
    else:
        grade = "F"
    student_grades[student] = grade

print(student_grades)

# version2

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "A"
    elif score > 80:
        student_grades[student] = "B"
    elif score > 70:
        student_grades[student] = "C"
    else:
        student_grades[student] = "F"

print(student_grades)


# 리스트와 Dictionary중첩

# 기본 Dictionary
capitals = {
    "프랑스": "파리",
    "독일": "베를린"
}

travel_log = {
    "프랑스": ["파리", "릴"],
    "독일": ["베를린", "함부르크", "뮌헨"]
}
# 리스트 중첩
# Dictionary안 Dictionary나 리스트를 중첩하는 것보단 데이터 구조상 덜 유용함
# ["a","b",["c","d"]]

# Dictionary중첩
travel_logs = {
    "프랑스": {"방문한 도시": ["파리", "릴"], "총 방문 횟수": 3},
    "독일": {"방문한 도시": ["베를린", "함부르크", "뮌헨"], "총 방문 횟수": 4}


}

# 리스트에 Dictionary중첩
