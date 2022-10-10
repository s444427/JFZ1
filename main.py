def test_name(word):
    state = 0
    result = 1
    next_state = 0
    for i in range(len(word)):
        char = word[i]

        if state == 0:
            if char.islower():
                result = 0
                print('0', char, "not lower")
            next_state = 1

        if state == 1:
            if char == '-' or char == ' ':
                next_state = 0
            elif char.islower():
                next_state = 1
            elif char == '.':
                next_state = 2
            else:
                result = 0
                print('1', char, 'not in conditions')

        if state == 2:
            if char != ' ':
                result = 0
                print('2', char, 'not a space')
            next_state = 0
        state = next_state

    if result == 1 and state == 1:
        print("a name")
    else:
        print("not a name")


if __name__ == '__main__':
    test_str = ['Jan Kowalski',
                'J. Kowalski',
                'J. R. Kowalski',
                'Jan R. Kowalski',
                'Jan R. Kowalski-Nowak',
                'Anna-Maria Kowalska']

    for name in test_str:
        test_name(name)
