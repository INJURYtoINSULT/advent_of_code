import md5
puzzle_input = "ojvtpuvg"
m = md5.new()
m.update(puzzle_input)
password = ""
iterator = 0

while True:
    c = m.copy()
    
    c.update(str(iterator))
    test = str(c.hexdigest())
    if test.startswith('00000'):
        password += test[5]
    if len(password) == 8:
        print password
        break
    iterator += 1
