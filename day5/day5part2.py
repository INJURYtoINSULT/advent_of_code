import md5
puzzle_input = "ojvtpuvg"
m = md5.new()
m.update(puzzle_input)
password = list("        ")
iterator = 0

while True:
    c = m.copy()

    c.update(str(iterator))
    test = c.hexdigest()
    if test.startswith('00000'):
        if test[5].isdigit() and int(test[5]) < 8:
            if password[int(test[5])] == ' ':
                password[int(test[5])] = test[6]
        if " " not in password:
            break
    iterator += 1
password = ''.join(password)
print password
