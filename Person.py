class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name + "And I am {r} years old".format(r=self.age))
        print("done")




