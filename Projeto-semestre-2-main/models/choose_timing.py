def timing(a):
    time1 = {
        "1": "14:00 - 16:00",
        "2": "17:00 - 19:00",
        "3": "20:00 - 22:00"
    }

    time2 = {
        "1": "14:00 - 15:30",
        "2": "16:00 - 17:30",
        "3": "18:00 - 19:30"
    }

    time3 = {
        "1": "10:00 - 12:00",
        "2": "10:00 - 12:00",
        "3": "10:00 - 12:00",
    }

    if a == 1:
        print("A que horas é que pretende assistir ao filme?")
        print(time1)
        t = input("escolha as horas")
        x = time1[t]
        print("Bom filme!")

    elif a == 2:
        print("A que horas é que pretende assistir ao filme?")
        print(time2)
        t = input("escolha as horas")
        x = time2[t]
        print("Bom filme!")

    elif a == 3:
        print("A que horas é que pretende assistir ao filme?")
        print(time3)
        t = input("escolha as horas")
        x = time3[t]
        print("Bom filme!")
    
    elif a != int:
        print("Insira um valor entre 1 e 3.")

    return 0