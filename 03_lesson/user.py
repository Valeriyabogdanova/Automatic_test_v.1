class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        print("Имя -",self.first_name)

    def get_last_name(self):
        print("Фамилия - ", self.last_name)

    def get_both_name(self):
        print(f'Фамилия и Имя - {self.last_name} {self.first_name}')


