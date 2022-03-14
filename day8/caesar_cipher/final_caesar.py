# 1. 로고 삽입하기
# 2. shift에 리스트 이상의 큰 숫자를 넣었을 경우 해결하는 방법
# 3. 유저가 숫자나 기호 공백 등을 넣었을 시 그건 무시하고 문자만 암호화, 복호화하는 방법
# 4. 실행이 끝난 후 암호프로그램을 다시 시작할지 묻는 것



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text,shift_amount, cipher_direction):
    end_text =""
    if shift_amount>51:
        shift_amount%=51
    if cipher_direction =="decode":
            shift_amount *= -1
            # shift가 5일시 encode는 +5 decode는 -5이므로 -1을 곱해주면 된다.
    for char in start_text:
        if char in alphabet:
            positon = alphabet.index(char)
            new_positon = positon+shift_amount
            end_text += alphabet[new_positon]
        else:
            end_text+=char
    print(f"The{cipher_direction} text is {end_text}")
import art
print(art.logo)

start = True
while start:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    start_again = input("다시 시작하시겠습니까? Yes or No ").lower()

    if start_again =="no":
        start =False
        print("Goodbye")

    


