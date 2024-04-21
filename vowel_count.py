vowl = ("a","e","i","o","u")
user = input ("").lower()
total = 0
for i in user:
    if i in vowl:
        total += 1
print(total)