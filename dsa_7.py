"""def is_index(user):
    indices = []
    for letter in user:
        if letter.isalpha():
            if letter == "a":
                indices.append(-1)
            else:
                indices.append(ord(letter.lower()) -97)
        else:
            indices.append(-1)
    return indices

user = input('Enter your letter: ')
print("Position of the letter is ", is_index(user))"""
def custom_encoder(user):
    indices = []
    for letter in user:
        if letter.isalpha():
            if letter == 'a':
                indices.append(-1)
            else:
                indices.append(ord(letter.lower()) -97)
        else:
            indices.append(-1)
    return indices

print(custom_encoder('My house is beautifu'))