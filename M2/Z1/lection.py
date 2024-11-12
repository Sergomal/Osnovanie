def is_number():
    check = input("Enter a number: ")
    if check[0] == "-":
        check = check[1:]
    if check.isdigit():
        return True
    return False


if __name__ == '__main__':
    print(is_number())

    s = "qwef. dFd Kcvjh"

    s.capitalize()
    print(s)

    print(s.capitalize())

    a = 3
    c = 5
    print(a != c)
