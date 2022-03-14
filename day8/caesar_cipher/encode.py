
# 카이사르 암호
# 카이사르 암호란 고전적인 암호화 방식이다.
# 카이사르가 민감한 군령을 보낼때 각각의 알파벳의 정해진 만큼 뒤의 알파벳을 
# 사용해서라고 한다.
# ex) 정해진 숫자가 3일 경우 a는 d가 되고 b는 e가 되는 방식이다.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))
len_text = len(text)
def encrypt(plain_text, shift_amount):
    cipher_text=""
    for letter in plain_text:
       positon = alphabet.index(letter) 
       #letter 가 리스트(알파벳)에서 몇번째 글자인지 알려주는 함수.
       # for문으로 plain_text의 글자 하나하나를 다 체크한다.
       new_position = positon+ shift_amount
       new_letter = alphabet[new_position]
       cipher_text +=new_letter
    print(f"암호화된 암호는 {cipher_text}입니다.")
        
encrypt(plain_text=text, shift_amount=shift)
    