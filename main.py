import string
alphabet= list((list(string.ascii_letters))*2)
def encrypt(plain_text,shift_amt):
    crpytic_text=""
    for letter in range(len(plain_text)):
        position=alphabet.index(plain_text[letter])
        shift_amt%=26
        new_position= position+shift_amt
        crpytic_text+= alphabet[new_position]
    return crpytic_text
def decrypt(plain_text,shift_amt):
    decryption_text=""
    for letter in range(len(plain_text)):
        position= alphabet.index(plain_text[letter])
        shift_amt%=26
        new_position= position-shift_amt
        decryption_text+= alphabet[new_position]
    return decryption_text
        
l= input("Do you you want to encrypt or decrypt : ").lower()
if l== "encrypt":
    p=input("the text you want to encrypt: ")
    h=int(input("The shift number: "))
    a=encrypt(p,h)
    b=a.lower()
    print(b)
else:
    n=input("The text you want to decrypt: ")
    h=int(input("The shift number: "))
    c= decrypt(n,h)
    d=c.lower()
    print(d)

