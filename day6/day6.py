# 함수

print("hello")
num_char = len("hello")
print(num_char)
# 출력함수와 len함수로 각각 출력 됨


# 함수를 만드는 이유. 똑같은 동작을 여러번 반복해서 행할 때 쓰기 간편함
# ex) 매일 아침 로봇을 우유 사오라고 시킬 경우, 집에서 가게까지 가는 걸음과 방향전환, 가게 도착 후 우유 고르고 돈 내는 행동과 집으로 돌아오는 길까지
# 하나하나를 코드로 짜고 매일 이 코드를 전부 입력해줘야 하지만 함수를 사용하면 특정함수에 위의 행동을 코드로 넣어주고선 매일매일 함수만 실행시키면 된다.

# 나만의 특정 함수를 만드는 키워드 def

def my_function():
    #Do this
    #Then do this
    #Finally do this
    
    print("hello")
    print("bye")
    
#함수 호출
my_function()


# while 반복문 : 특정조건이 참일경우 계속 반복된다.

a=10
while a >=0:
    print(a)
    a-=1

# while somthing_is_true:
    #Do this
    #Then do this
    #Then do this
    
