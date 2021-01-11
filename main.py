from Person import Person
from flask import Flask


def main():
    p1 = Person("John", 36)
    p1.myfunc()
    dic = {}
    dic[1] = "Pear"
    print(dic[1])


print("This is a test")


if __name__ == '__main__':
    main()
