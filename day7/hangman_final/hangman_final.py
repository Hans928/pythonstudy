# 개선판

from random import random
import random
import hangman_art
import hangman_words
# from hangman_words import word_list
# => chossne_word = random.choice(word_list)
# 같은 결과

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
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
    
    
    if guess in display:
        print(f"이미 {guess}를 말하셨습니다.")
    

    for positon in range(word_len):
        letter = chosen_word[positon]
        if letter == guess:
            display[positon] = letter
    if guess not in chosen_word:
        print(f"당신이 말한{guess}는 단어에 없으며, 당신은 목숨을 하나 잃었습니다.")
        lives-=1
        if lives ==0:
            end_of_game = True
        print("You lose")
        
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You win")
        
    
    print(hangman_art.stages[lives])

