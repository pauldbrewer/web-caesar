import string

def alphabet_position(letter):
    if letter in string.ascii_uppercase:
        return string.ascii_uppercase.index(letter)
    elif letter in string.ascii_lowercase:
        return string.ascii_lowercase.index(letter)

def rotate_character(char, rot):
    alphabet = string.ascii_lowercase
    alphabetUp = string.ascii_uppercase
    if char in string.ascii_lowercase:
        rotated_index = alphabet.index(char) + rot
        if rotated_index < 26:
            return alphabet[rotated_index]
        else:
            return alphabet[rotated_index % 26]
    else:
        rotated_index = alphabetUp.index(char) + rot
        if rotated_index < 26:
            return alphabetUp[rotated_index]
        else:
            return alphabetUp[rotated_index % 26]

def encrypt(text, rot):
    encrypted = ""
    for c in text:
        if not c.isalpha():
            encrypted = encrypted + c

        else:
            encrypted = encrypted + rotate_character(c, rot)
    return encrypted
