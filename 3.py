def dict_():
    input()
    codes = {}
    str = input()
    while (not '}' in str):
        city = str.split(':')[0].split("'")[1]
        numbers  = [i[1:-1] for i in str.split ('[')[1].split (']')[0].split(', ')]
        for i in numbers:
            codes[i] = city
        str = input()
    return codes


def find_tuple():
    number = input()
    codes = dict_()
    answer = []
    if (number.split(' ')[0] == '+7'):
        answer.append(True)
    else:
        answer.append(False)
    answer.append(codes[number.split('(')[1].split(')')[0]])
    answer.append(number.split(') ')[1])
    print(tuple(answer))


find_tuple()
