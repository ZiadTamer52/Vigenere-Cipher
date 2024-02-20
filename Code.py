def generatekey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("".join(key))

def ciphertext(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("".join(cipher_text))


def originaltext(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("".join(orig_text))







if __name__ == "__main__" :
    string = "ZIAD"
    keyword = "AYUSH"
    key = generatekey(string, keyword)
    cipher_text = ciphertext(string, key)
    print("Cipher text : ", cipher_text)
    print("Original/Decrypted Text : ", originaltext(cipher_text, key))
