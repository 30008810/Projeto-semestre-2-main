import re

class UserInfo:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def create_user(self, name, age, phone_number):
        dict_info = {"Name": " ", "Age": int, "Phone_number": int}
        phone_number = input("Diga-nos o seu número de telemóvel, por favor.")
        name = input("Diga-nos o seu nome, por favor.")
        age = input("Diga-nos a sua idade, por favor.")
        
        for i in range(10):
            phone_no = re.fullmatch("[8-9][0-9]{9}", phone_number)

        if phone_no != None:
            dict_info["Name"] = name
            dict_info["Age"] = age
            dict_info["Phone_number"] = phone_number