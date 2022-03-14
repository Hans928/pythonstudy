# encode 와 decode를 한 함수로 합쳐서 실행하는 법


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def caesar(start_text,shift_amount, cipher_direction):
    end_text =""
    if cipher_direction =="decode":
            shift_amount *= -1
            # shift가 5일시 encode는 +5 decode는 -5이므로 -1을 곱해주면 된다.
    for letter in start_text:
        positon = alphabet.index(letter)
        new_positon = positon+shift_amount
        end_text += alphabet[new_positon]
    print(f"The{cipher_direction} text is {end_text}")
    
    
caesar(start_text=text,shift_amount=shift,cipher_direction=direction)