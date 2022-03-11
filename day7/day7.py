# hang man

# 순서도
# 랜덤의 단어 생성 -> 단어의 알파벳 갯수만큼 빈 칸을 생성 -> 사용자는 문자를 답한다.
# -> 이 문자가 있는가 Yes or No -> Yes : 알맞은 빈칸에 그 문자 넣기 / No : hangman에 그림이 그려진다.
# Yes일 경우 -> 빈칸이 다 채워졌는가? Yes or No -> Yes : 당신이 이겼습니다. 출력. / No: 사용자가 다른 문자를 선택 할 수 있게 문자를 답하는 곳으로 돌아가기
# No 일 경우 -> 그림이 다 그려졌는가? Yes or No -> Yes : 당신이 졌습니다. 게임 오버 출력. / No : 사용자가 다른 문자를 선택 할 수 있게 문자를 답하는 곳으로 돌아가기




# 무작위 단어 고르고 정답 확인하기


import random

word_list = ["hello","bye","hi"]
# 내가 처음 해 본 것
# blink = "-"

# random_word = random.randint(0,len(word_list)-1)
# random_blink = len(word_list[random_word])


# 결과
# chosen_word = random.choice(word_list)
# guess = input("Guess a letter : ").lower()

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("wrong")
        
        
# 빈 칸을 맞춘 글자로 바꾸기

# 1 단계)
# chosen_word의 글자 수 만큼 "_"로 표현하는 리스트를 생성하기.
# ex) hello 일 경우 5개의 _로 이루어진 리스트를 만들어 빈칸을 표시한다.

# 2 단계)
# 유저가 글자를 맞췄을때 빈칸을 글자로 바꾸어주는 것이다.
# ex) 단어가 hello 일 경우 유저가 l을 맞췄다고 하면 ["_","_","l","l","_"]가 되는 것이다.

# 3 단계)
# 위의 상황을 출력하여 보이게 할 것.

# chosen_word = random.choice(word_list)
# print(f"테스트용입니다. 선택된 단어는 {chosen_word} 입니다.")
# word_len =len(chosen_word)

# # 1단계

# display = []
# for letter in chosen_word:
# # for _ in range(word_len):
# # 1번이나 2번이나 똑같은 결과를 보여주기 때문에 어떤 것을 사용해도 무관
# # 단 1번의 경우는 단어가 hello 일 경우 1-5까지 2번의 경우는 0-4까지임.
#     display +="_"
# print(display)

# guess = input("Guess a letter : ").lower()
# # 2단계

# for positon in range(word_len):
#     letter = chosen_word[positon]
#     if letter == guess:
#         display[positon] = letter
        

# # 3단계       
# print(display)



# 플레이어가 승,패 확인하기.

# 1단계 while 반복문을 이용하여서 display 리스트에 빈칸이 없어질 때만 게임을 끝내야한다.
# 리스트에 빈 칸이 없을 경우 승리를 알려줘야한다.



# chosen_word = random.choice(word_list)
# print(f"테스트용입니다. 선택된 단어는 {chosen_word} 입니다.")
# word_len =len(chosen_word)

# display = []
# for letter in chosen_word:
#     display +="_"
# print(display)

# # 1단계

# end_of_game = False

# while end_of_game == False:
#     guess = input("Guess a letter : ").lower()

#     for positon in range(word_len):
#         letter = chosen_word[positon]
#         if letter == guess:
#             display[positon] = letter
        
#     print(display)
    
#     if "_" not in display:
#         end_of_game = True
#         print("You win")



# 플레이어의 남은 목숨을 세는 법.

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# 1단계)
# 목숨을 나타내는 변수가 필요하며 목숨의 기본 값은 6이다.

# 2단계
# 유저가 선택한 값이 단어에 없을 경우 목숨 하나를 줄이고 목숨값이 0이되면
# you lose 를 출력하며 게임이 종료됩니다.

# 3단계
# 유저의 남은 목숨에 따라서 그림이 출력되어야한다.
# 그림이 완성되면 목숨값이 0인것이다.

chosen_word = random.choice(word_list)
print(f"테스트용입니다. 선택된 단어는 {chosen_word} 입니다.")
word_len =len(chosen_word)

display = []
for letter in chosen_word:
    display +="_"
print(display)

end_of_game = False
lives = 6

while end_of_game == False:
    guess = input("Guess a letter : ").lower()
    

    for positon in range(word_len):
        letter = chosen_word[positon]
        if letter == guess:
            display[positon] = letter
    if guess not in chosen_word:
        lives-=1
        if lives ==0:
            end_of_game = True
        print("You lose")
        
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You win")
        
    
    print(stages[lives])




