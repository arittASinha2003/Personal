def Atbash(Message, Type):
    if Type == 'e':
        print("\n\nThe encoded message is:\n")
    elif Type == 'd':
        print("\n\nThe decoded message is:\n")
    message = Message.upper()
    letters = list(message)
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Reverse = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    for i in range(len(letters)):
        if letters[i] in Alphabet:
            keyI = Alphabet.index(letters[i])
            letters[i] = Reverse[keyI];
    word = ""
    for c in letters:
        word += c
        print(word)

def EASCII(Message):
    print("\n\nThe encoded message is:\n")
    message = Message
    letters = list(message)
    word = ""
    for i in range(len(letters)):
        if letters[i] == ' ':
            word += " "
        else:
            ascii = [ord(c) for c in letters[i]]
            word += str(ascii[0])
            if letters[i] != letters[len(letters) - 1 ] and letters[(i + 1)] != ' ':
                word += "."
    print(word)

def EBinary(Message):
    print("\n\nThe encoded message is:\n")
    message = Message
    sb = ""
    sb += (''.join('{0:08b}'.format(ord(x), 'b') for x in message))
    print(sb)

def EVigenereLand(Message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    input_string = ""
    enc_key = ""
    enc_string = ""
    enc_key = input("What is the key?: ")
    enc_key = enc_key.upper()
    input_string = Message
    input_string = input_string.upper()
    string_length = len(input_string)
    expanded_key = enc_key
    expanded_key_length = len(expanded_key)
    while expanded_key_length < string_length:
        expanded_key = expanded_key + enc_key
        expanded_key_length = len(expanded_key)
    key_position = 0
    for letter in input_string:
        if letter in alphabet:
            position = alphabet.find(letter)
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            new_position = position + key_character_position
            if new_position > 26:
                new_position = new_position - 26
            new_character = alphabet[new_position]
            enc_string = enc_string + new_character
        else:
            enc_string = enc_string + letter
    print(enc_string)

def ECeasar(Message):
    key = input("\nWhat letter is equivalent to A?: ").upper()
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    keyI = Alphabet.index(key)
    follow = []
    j = keyI
    while j < len(Alphabet):
        follow.append(Alphabet[j])
        j += 1
    for i in range(keyI):
        follow.append(Alphabet[i])
    shift = list(follow)
    message = list(Message.upper())
    for l in range(len(message)):
        if message[l] in Alpahbet:
            ido = Alphabet.index(message[l])
            rep = shift[ido]
            message[l] = rep
    print("\n\nThe encoded message is:\n")
    word = ""
    for w in message:
        word += w
    print(word)

def DASCII(Message):
    print("\n\nThe decoded message is:\n")
    message = Message;
    word = message.split( )
    st = ""
    for i in range(len(word)):
        letter = word[i].split(".")
        for j in range(len(letter)):
            num = int(letter[j])
            ascii = chr(num)
            st += ascii
        st += " "
    print(st)

def DBinary(Message):
    print("\n\nThe decoded message is:\n")
    str_data = ''
    for i in range(0, len(Message), 8):
        temp_data = Message[i:i + 8]
        decimal_data = int(temp_data, 2)
        str_data += chr(decimal_data)
    print(str_data)

def DVigenereLand(Message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    input_string = ""
    dec_key = ""
    dec_string = ""
    dec_key = input("What is the key?: ")
    dec_key = dec_key.upper()
    input_string = Message
    input_string = input_string.upper()
    string_length = len(input_string)
    expanded_key = dec_key
    expanded_key_length = len(expanded_key)
    while expanded_key_length < string_length:
        expanded_key = expanded_key + dec_key
        expanded_key_length = len(expanded_key)
    key_position = 0
    for letter in input_string:
        if letter in alphabet:
            position = alphabet.find(letter)
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            new_position = position - key_character_position
            if new_position > 26:
                new_position = new_position + 26
            new_character = alphabet[new_position]
            dec_string = dec_string + new_character
        else:
            dec_string = dec_string + letter
    print(dec_string)

def DCeasar(Message):
    key = input("\nWhat letter is equivalent to A?: ").upper()
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    keyI = Alphabet.index(key)
    follow = []
    for j in range(keyI, len(Alphabet)):
        follow.append(Alphabet[j])
    for i in range(keyI):
        follow.append(Alphabet[i])
    shift = list(follow)
    message = list(Message.upper())
    for l in range(len(message)):
        if message[l] in shift:
            ido = shift.index(message[l])
            rep = Alphabet[ido]
            message[l] = rep
    print("\n\nThe decoded message is:\n")
    word = ""
    for w in message:
        word += w
    print(word)

def EncodeLand():
    print("\nWhat encoding language will you use?\n")
    print("1. Atbash")
    print("2. ASCII")
    print("3. Binary")
    print("4. Vigenere")
    print("5. Ceasar")
    choice = int(input())
    Message = input("\nWhat is the message to encode?: ")
    if choice == 1:
        Atbash(Message, 'e')
    if choice == 2:
        EASCII(Message)
    if choice == 3:
        EBinary(Message)
    if choice == 4:
        EVigenereLand(Message)
    if choice == 5:
        ECeasar(Message)

def DecodeLand():
    print("\nWhat language will you be decoding?\n")
    print("1. Atbash")
    print("2. ASCII")
    print("3. Binary")
    print("4. Vigenere")
    print("5. Ceasar")
    choice = int(input())
    Message = input("\nWhat is the message to decode?: ")
    if choice == 1:
        Atbash(Message, 'd')
    if choice == 2:
        DASCII(Message)
    if choice == 3:
        DBinary(Message)
    if choice == 4:
        DVigenereLand(Message)
    if choice == 5:
        DCeasar(Message)

print("CODEBREAKER\n\n")
print("What would you like to do?\n")
print("1. ENCODE")
print("2. DECODE")
choice = int(input())
if choice == 1:
    EncodeLand()
if choice == 2:
    DecodeLand()
