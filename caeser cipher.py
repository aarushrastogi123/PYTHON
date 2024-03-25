alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("Type 'encode' to encrypt and 'decode' to decrypt: ")
text=input("\nType your messages here: ").lower()
shift=int(input("\nType the shift number: "))
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
'''if direction=='encode':
    def encrypt(t,s):
        cipher_text=" "
        for letters in t:
            position= alphabets.index(letters)
            new_position=position+s
            new_letters=alphabets[new_position]
            cipher_text+=new_letters
        print(f"\nThe encrypted text is = {cipher_text}")

    encrypt(t=text,s=shift)
elif direction=='decode':
    def decrpyt(a,b):
        decipher_text=" "
        for letters in a:
            position=alphabets.index(letters)
            new_position=position-b
            decipher_text+=alphabets[new_position]

        print(f'\nThe decrypted text is = {decipher_text}')

    decrpyt(a=text,b=shift)
    '''

def caeser(d,t,s):
    end=''
    if d=='decode':
            s *= -1
    for letters in t:
        position=alphabets.index(letters)
        new_position=position+s
        end+=alphabets[new_position]
    print(f'\nThe {d}d text is {end}.')

caeser(d=direction,t=text,s=shift)           

