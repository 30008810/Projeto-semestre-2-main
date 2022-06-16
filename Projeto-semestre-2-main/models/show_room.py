from models.user_info import UserInfo

def read_show_room():
    show_room = open("sala_espetaculos.csv", "r+", encoding = "utf-8")
    seats = show_room.readlines()
    show_room.close()
    return seats

def add_seat(seat):
    show_room = open("sala_espetaculos.csv", "r+", encoding = "utf-8")
    show_room.seek()
    show_room.write(seat+", 0, 0\n")
    show_room.close()
    
class ShowRoom():
    def __init__(self, movie_name, rows, columns):
        self.movie_name = movie_name
        self.rows = rows
        self.columns = columns
    
    def getstatus(self):
        print(f"O nome do filme que escolheu é {self.movie_name}")

    def ticket_booking(self):
        if self.seats > 0:
            self.seats = self.seats - 1
        else:
            print("O lugar que escolheu já se encontra ocupado.")

class seats:
    global matrix, total_seats_booked
    matrix = []

    def __init__(self):
        self.no_of_rows = int(input("Enter the Number of Rows:"))
        self.no_of_seats = int(input("Enter the Number of Seats:"))
        
    def capacity(self):
        for i in range(self.no_of_rows + 1):
            a = []
            for j in range(self.no_of_seats + 1):
                a.append("S")
            matrix.append(a)

        total_seats = self.no_of_seats * self.no_of_rows
        return total_seats, self.no_of_rows,self.no_of_seats

    def show_the_seats(self):

        for i in range(0, self.no_of_rows + 1):
            if i == 0:
                for j in range(0, self.no_of_seats + 1):
                    print(j, end=" ")
            else:
                print(i, end=" ")
                for k in range(self.no_of_seats):
                    print(matrix[i - 1][k], end=" ")
            print()
