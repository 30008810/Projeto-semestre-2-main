from tokenize import blank_re
from models.show_room import ShowRoom as room
from models.user_info import UserInfo as user
import models.choose_timing as timing
import heapq

# já funciona
# so faz o print da sala para o utilizador ver como é a sala

def show_room():
    ShowRoom.show_showroom()



def register_client(name, age, phone_number):
    user = [name, age, phone_number]
    model.all_users.append(user)
    return

def check_if_client_exists(phone_number):
    for user in model.all_users:
        if user[2] == phone_number:
            return True
    return False    


def idade_limite(age):
    if age < "16":
        print("Não tem idade minima para assistir ao espetaculo.")
    else:
        print("oldshfjq")


'''
# falta comprar o bilhete     #está a dar erro, diz que faltam argumentos
def create_user(name, age, phone_number, all_users):
    # validation
    # creating the user
    user = Users(name, age, phone_number)
    return user
def phone_number(phone_number, all_users):
    pass
'''
    #for i in range(10):
        #phone_no = re.fullmatch("[8-9][0-9]{9}", phone_number)

        #if phone_no != None:
           # dict_info["Name"] = name
           # dict_info["Age"] = age
            #dict_info["Phone_number"] = phone_number

#def buy_ticket(data, index):
    #Tickets.insert_at_index(data, index)

#def delete_ticket(x):
    #Tickets.delete_element_by_value(x)
    

# falta mostrar o balanço




# falta mostrar os lugares ja reservados (acho que pode ficar quando se mostra a sala)




'''
def add_people_in_seat():
    if UserInfo.create_user != " ":
        #costumers = room.
        pass
    
# Everything related to the show
def ticketbooking():
    ShowRoom.ticket_booking()
    print(f"Escolheu o filme {ShowRoom.movie_name} e o seu lugar é {ShowRoom.seats}")
#se escolheu bilhete(vip- 12$, normql - 4$) este é preço por cada, deseja efetuar o pagamento?
def ticket_price():
    VIP = [print(f"O lugar que está a selecionar é um lugar vip, ")]
    user_output = input()
    #if input() == VIP
    
def changebooking(number, line, date):
    pass
def choose_movie_time(a):
    timing.timing(a)
class SeatManager:
    def __init__(self, n: int):
        self.unreserve = [i for i in range(1, n + 1)]
    def reserve(self, unreserve) -> int:
        return heapq.heapop(self, unreserve)
    def unreserve(self, seatnumber: int) -> None:
        heapq.heappush(self.unreserve, seatnumber)
def inexistent_seats():
    user_output = input()
    if user_output == ("A3","A4", "A5", "A10", "A11", "A12", "F3", "F4", "F5", "F10", "F11", "F12"):
        print("O lugar que escolheu não existe.\nPor favor escolha um diferente")
'''