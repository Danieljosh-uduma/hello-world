class Father:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work
        
    def display(self):
        print(f'you name is father {self.name}')
        print(f'you work as a {self.work} and you are {self.age} years old')