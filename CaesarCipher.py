def encrypt(input):
    txt_encrypt=""
    #change shift value to increase or decrease shift in character
    shift_value=3
    for char in input:
        if char.isalpha():
            if char.isupper():
                txt_encrypt+= chr((ord(char)+ shift_value-65) % 26 + 65)
            elif char.isupper()==False:
                txt_encrypt+= chr((ord(char)+ shift_value-97) % 26 + 97)
        else:
            txt_encrypt+=char
        
    return txt_encrypt

print(encrypt("add text here"))

