alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("Type 'encode' to encrypt and 'decode' to decrypt: ")
text=input("\nType your messages here: ").lower()
shift=int(input("\nType the shift number: "))


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

