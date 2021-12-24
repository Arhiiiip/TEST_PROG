def return_class(n):
    if n in range(0, 128):
        return 'class A'
    if n in range(128, 192):
        return 'class B'
    if n in range(192, 224):
        return 'class C'
    if n in range(224, 240):
        return 'class D'
    if n in range(240, 256):
        return 'class E'
    return "Вы вышли за границы"


def check_nums(m, b, c):
    if 0 <= m <= 255 and 0 <= b <= 255 and 0 <= c <= 255:
        return True
    else:
        print("Вы вышли за границы")


ip_address = (input().split('.'))

if check_nums(int(ip_address[1]), int(ip_address[2]),
              int(ip_address[3])):
    print(return_class(int(ip_address[0])))
    
