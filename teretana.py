import mysql.connector
import random 
import datetime
import time
import os




mydb = mysql.connector.connect (

    host = "localhost",
    user="root",
    password="root123456789",
    database="teretana"
)

mycursor = mydb.cursor()

#stavio sam sve u funkciju iz razloga da se korisnik uvijek može vratiti na glavni meni
def main():

    os.system("cls")
    print("-"*55)
    print("Dobrodošli u Strong & Healthy ")
    print("-"*55)

    #informacije za članstvo i pristup podacima/izmjeni passworda

    print("Ukoliko se želite učlaniti izaberite opciju: 1) ")
    print("Ako želite pristupiti izmjeni username i passworda izaberite opciju 2) ")
    print("Ako želite pristupiti planu vježbanja izaberite opciju 3)")

    #biranje opcije 1,2 ili 3
    izbor_opcije = input(str("Unesite opciju: "))

    #članstva koja se nude / ovo čak, po potrebi i mijenjati jer se ne radi više o članarini za teretanu nego aplikaciji
    if izbor_opcije == "1":
        while True: 
            os.system("cls")
            print("Članstva koja imamo u ponudi su sljedeća: ")
            print("")
            print("1) Jednomjesečno po cijeni od 50 KM")
            print("2) Tromjesečno po cijeni od 130 KM")
            print("3) Polugodišnje po cijeni od 265 KM")
            print("4) Godišnje po cijeni od 500 KM")
            print("")
            print("5) Za povratak u glavni meni pritisnite 0)")
            print("")

            user_input = input(str("Molimo unesite broj članstva koje želite koristiti: "))
            if user_input == "1":
                print("Izabrali ste jednomjesečno članstvo po cijeni od 50 KM")
                break
            elif user_input == "2":
                print("Izabrali ste tromjesečno članstvo po cijeni od 130 KM")
                break
            elif user_input == "3":
                print("Izabrali ste polugodišnje članstvo po cijeni od 265 KM")
                break
            elif user_input == "4":
                print("Izabrali ste godišnje članstvo po cijeni od 500 KM")
                break
            elif user_input == "0":
                main()
            else:
                print("-"*55)
                print("Pogrešan unos")
                print("-"*55)

        #potvrda plaćanja

        while True:
            provjera_placanja = input("Molimo da potvrdite vaše plaćanje sa da/ne: ")
            if provjera_placanja == "da":  
                break
            
            else: 
                print("Odbili ste opciju plaćanja. Molimo pokušajte ponovo.")
                exit()
                
        #informacije o novom klijentu

        ime_klijenta = input("Molimo unesite Vaše ime: ")
        prezime_klijenta = input("Molimo unesite Vaše prezime: ")
        username = input(str("Molimo unesite Vaš username: "))
        passwd = input(str("Molimo unesite password: "))
        jmbg_klijenta = input(str("Molimo unesite Vaš JMBG: "))
        id_kartice_lista = []

        for i in range(0,5):
            id_kartice_lista.append(random.randint(1,99))

        id_kartice = ''.join(map(str,id_kartice_lista))

        print("ID vaše kartice:",id_kartice)
        print("Molimo da zapamtite ID kartice, biće vam potreban za eventualnu izmjenu podataka.")
        if user_input == "1": 
            ime_clanstva = "jednomjesecno"
            trajanje_clanstva = "30 dana"
            a = 30
        elif user_input == "2": 
            ime_clanstva = "tromjesecno"
            trajanje_clanstva = "90 dana"
            a = 90
        elif user_input == "3": 
            ime_clanstva = "polugodisnje"
            trajanje_clanstva = "182 dana"
            a = 182
        elif user_input == "4": 
            ime_clanstva = "godisnje"
            trajanje_clanstva = "365 dana"
            a = 365
        else: 
            print("Pogrešan unos. Molimo unesite tačne podatke")

        date = datetime.datetime.now()
        clanstvo_pocelo = date.date().isoformat()
        clanstvo_zavrsava = datetime.datetime.now() + datetime.timedelta(a)

        #BMI kalkulator
        print("-"*55)
        print("Dobrodošli u BMI kalkulator.")
        print("-"*55)
        while True: 
            try:
                visina = int(input("Unesite visinu / cm : "))
                tezina = int(input("Unesite težinu / kg: "))
                
                bmi = tezina / (visina*visina/10000)
                print("")
                print("Vaš BMI iznosi: ",bmi)
                print("")
                
                
                if bmi < 18.5:
                    print("Pothranjeni ste. Slijedite naše instrukcije da bi povećali svoju tjelesnu težinu.")
                if bmi >=18.5 and  bmi < 25:
                    print("Imate normalnu tjelesnu težinu. Nastavite vježbati i hranite se zdravo.")
                if bmi >=25 and bmi < 30:
                    print("Imate povišenu tjelesnu težinu. Preuzmite svoj plan vježbanja.")
                if bmi >=30 and bmi <35: 
                    print("Debljina 1.razreda (gojaznost). Izrazito ste izloženi riziku za razvoj bolesti.")
                if bmi >=35 and bmi <40: 
                    print("Debljina 2.razreda (gojaznost). Izrazito ste izloženi riziku za razvoj bolesti.")
                if bmi > 40: 
                    print("Debljina 3.razreda (teška gojaznost). Izrazito ste izloženi riziku za razvoj bolesti.")
                break
            
            except: 
                print("Neispravan unos. Molimo unesite brojeve.")

        print("")
        #RFM masti u tijelu i računanje rizika za razvoj bolesti
        print("Računanje rizika za razvoj bolesti...")
        time.sleep(1.1)
        print("")
        
        while True: 
            try:

                obim_struka = float(input("Unesite obim struka / cm: "))
                spol = input(str("Unesite kojeg ste spola M/Ž : "))
                #nakon što se izračuna procenat masti dodijeliće se i trening koji bi korisnici trebali da koriste, ovisno o tome u koju kategoriju spadaju
                if spol.upper() == "M":
                        
                        rfm = 64 - (20*visina/obim_struka)
                        print("Procenat masti u tijelu iznosi: ",rfm, "%")

                        if rfm <6:
                            print("Minimum masti. Preuzmite programe za kvalitetnu ishranu i vježbu.")
                            print("Na osnovu analize trenutnog stanja za Vas smo izabrali trening za dobijanje kilaže i mišićne mase.")

                        elif rfm >=6 and rfm <14:
                            print("Vrhunski atleta. Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je NIZAK.")
                            print("Na osnovu analize trenutnog stanja za Vas smo izabrali trening snage.")
                        
                        elif rfm >=14 and rfm <18:
                            print("Fitnes tip. Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je NIZAK.")
                            print("Na osnovu analize trenutnog stanja za Vas smo izabrali program treninga za jačanje trbušnog zida.")
                
                        elif rfm >=18 and rfm <25: 
                            print("Prihvatljivo stanje. Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je NIZAK.")
                            print("Na osnovu analize trenutnog stanja za Vas smo izabrali trening definicije.")
                        
                        elif rfm >25:
                            print("Stanje pretilosti. Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je VISOK. Počnite vježbati i hranite se zdravo.")
                            print("Na osnovu analize trenutnog stanja za Vas smo izabrali trening definicije.")
                        break
                    
                    
                #Žene: 76 – (20 x visina/opseg struka) = RFM

                elif spol.upper() =="Ž":
                        #nakon što se izračuna procenat masti dodijeliće se i trening koji bi korisnici trebali da koriste, ovisno o tome u koju kategoriju spadaju

                        rfm = 76 - (20*visina/obim_struka)
                        print("Procenat masti u tijelu iznosi: ",rfm,"%")

                        if rfm <14:
                            print("Minimum masti. Preuzmite programe za kvalitetnu ishranu i vježbu.")
                            print("Na osnovu analize trenutnog stanja za Vas smo izabrali trening za dobijanje kilaže i mišićne mase.")

                        elif rfm >=14 and rfm <21:
                            print("Vrhunski atleta. Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je NIZAK.")
                            print("Na osnovu analize trenutnog stanja za Vas smo izabrali trening snage.")

                        elif rfm >=21 and rfm <25:
                            print("Fitnes tip. Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je NIZAK.")
                            print("Na osnovu analize trenutnog stanja za Vas smo izabrali program treninga za jačanje trbušnog zida.")

                        elif rfm >=25 and rfm <32: 
                            print("Prihvatljivo stanje. Počnite vježbati i hranite se zdravo. Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je NIZAK.")
                            print("Na osnovu analize trenutnog stanja za Vas smo izabrali trening definicije.")

                        elif rfm >=32:
                            print("Stanje pretilosti. Počnite vježbati i hranite se zdravo. Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je VISOK.")
                            print("Na osnovu analize trenutnog stanja za Vas smo izabrali trening definicije.")
                        break

                else:
                    print("Pogrešan unos, molimo unesite jednu od dvije navedene opcije M/Ž")
            except:
                print("Neispravan unos. Molimo unesite brojeve.")

        #unos podataka u tabelu u mysql

        klijenti = (ime_klijenta,prezime_klijenta,username,passwd,jmbg_klijenta,id_kartice,ime_clanstva,clanstvo_pocelo,clanstvo_zavrsava,trajanje_clanstva,bmi,rfm)
        mycursor.execute("INSERT INTO klijenti(ime_klijenta,prezime_klijenta,username,passwd,jmbg_klijenta,id_kartice,ime_clanstva,clanstvo_pocelo,clanstvo_zavrsava,trajanje_clanstva,bmi,rfm) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",klijenti)
        mydb.commit()
        print("-"*55)
        print(ime_klijenta,prezime_klijenta," registrovani ste kao novi član. Hvala što ste nas izabrali.")
        print("-"*55)
            

    elif izbor_opcije == "2":
        #opcija za pristup podacima ili izmjene username i passworda
        

        if izbor_opcije == "2":
            mycursor.execute("SELECT username,passwd FROM klijenti")
            values = mycursor.fetchall()
            username = input(str("Molimo unesite svoj username: "))
            passwd = input(str("Molimo unesite svoj password: "))
            for i in values: 
                if (username,passwd) in values:
                    print("-"*55)
                    print("Dobrodošli")
                    print("-"*55)
                    break
                else: 
                    print("Neispravan unos")
                    exit()

            while True: 
                
                os.system("cls")
                print("Pristupate meniju za mijenjanje podataka...")
                time.sleep(1.3) 
                print("Mijenjanje podataka 1)")
                print("Za izlaz izaberite opciju 0)")
                print("")
                userchange = input(str("Molimo unesite opciju: "))

                if userchange == "1":

                    mycursor.execute("SELECT id_kartice FROM klijenti")
                    result = mycursor.fetchall()
                    novi_id = input(str("Unesite vaš ID:"))

                    for i in result:

                        if  (novi_id,) in result:
                            
                            username = input(str("Unesite svoj novi username: "))
                            passwd = input(str("Unesite svoj novi password: "))
                            sql = "UPDATE klijenti SET username = %s, passwd = %s WHERE id_kartice = %s"
                            val = (username,passwd,novi_id)
                            mycursor.execute(sql,val)
                            mydb.commit()

                            print("Uspješno ste updateovali svoj username i password.")
                            exit()

                        else: 
                            print("Molimo unesite ispravne podatke: ")
                            break

                elif userchange ==  "0":
                    main()   

                else: 
                    print("Hvala Vam na povjerenju! STAY STRONG!")
                    exit()


    elif izbor_opcije == "3":
        #login
        #biranje opcije za vrste treninga / trening je već prethodno predložen prilikom testiranja tako da bi korisnici morali da izaberu program koji im je dodijeljen
        mycursor.execute("SELECT username,passwd FROM klijenti")
        values = mycursor.fetchall()
        username = input(str("Molimo unesite svoj username: "))
        passwd = input(str("Molimo unesite svoj password: "))
        for i in values: 
            if (username,passwd) in values:
                os.system("cls")
                print("-"*55)
                print("Dobrodošli u Strong & Healthy program:")
                print("-"*55)
                print("Program treninga za jačanje trbušnog zida: 1)")
                print("Program treninga za mišićnu definiciju: 2)")
                print("Program treninga za dobijanje mase i kilaže: 3)")
                print("Program treninga za izgradnju mišića i snage: 4)")
                print("")
                biranje_treninga = input("Molimo izaberite trening koji radite: ")
                #program za jačanje trbušnog zida 
                if biranje_treninga == "1":
                    os.system("cls")
                    print("-"*55)
                    print("Dobrodošli u program treninga za jačanje trbušnog zida")
                    print("-"*55)
                    print("")

                    while True:

                        print("")
                        print("Za odabir programa za vježbanje pritisnite 1)")
                        print("Za detaljne informacije o treningu pritisnite 2)")
                        print("Za povratak u glavni meni pritisnite 0)")
                        print("")

                        izbor_treninga = input(str("Molimo unesite jednu od navedenih opcija (1/2/0): "))

                        if izbor_treninga == "1":

                            os.system("cls")
                            print("Program treninga za jačanje trbušnog zida sastoji se od 4 programa.")
                            print("Trajanje treninga: 4 sedmice")
                            print("")
                            print("Program br.1) ")
                            print("Program br.2) ")
                            print("Program br.3) ")
                            print("Program br.4) ")
                            print("")
                            program = input(str("Molimo izaberite program koji trenutno radite: "))

                            if program == "1":
                                os.system("cls")
                                print("")
                                print("Počinjemo sa prvim programom u trajanju od jedne sedmice.")
                                print("")
                                print("Program br. 1")
                                print("")
                                print("Sedmični izbor vježbi po danima: ")
                                print("")
                                print("Ponedjeljak 1)")
                                print("Utorak 2)")
                                print("Srijeda 3)")
                                print("Četvrtak 4)")
                                print("Petak 5)")
                                print("Subota 6)")
                                print("Nedjelja 7)")
                                print("")

                                dani = input(str("Izaberite odgovarajući dan: "))
                                
                                if dani == "1":

                                    os.system("cls")
                                    print("Ponedjeljak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Walk Outs (from knees):              \t\t\t\tSerije:1      \tPonavljanja: 10")
                                    print("DB Crunch (light DB behind head):    \t\t\t\tSerije:1      \tPonavljanja: 20")
                                    print("Plank:                               \t\t\t\tSerije:1      \tTrajanje: 1 minuta")
                                    print("Band Hold (on back):                 \t\t\t\tSerije:10     \tTrajanje: 3 sekunde izdržaj")

                                elif dani == "2":

                                    os.system("cls")
                                    print("Utorak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("DB Pullovers:                        \t\t\t\tSerije:3      \tPonavljanja: 8")
                                    print("Plate Arches:                        \t\t\t\tSerije:3      \tPonavljanja: 5 (obje strane)")
                                    print("Side Bridge:                         \t\t\t\tSerije:1      \tTrajanje: 20-30 sekundi (obje strane)")
                                    print("Side Bends / Dumbbell:               \t\t\t\tSerije:3      \tPonavljanja: 10 (obje strane)")

                                
                                elif dani == "3":

                                    os.system("cls")
                                    print("Srijeda")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Dead Bugs:                           \t\t\t\tSerije:3      \tTrajanje: 10 sekundi izdržaj")
                                    print("Supermans:                           \t\t\t\tSerije:3      \tPonavljanja: 10")
                                    print("Hyperextensions:                     \t\t\t\tSerije:2      \tPonavljanja: 10")
                                    print("Glute Bridge:                        \t\t\t\tSerije:2      \tTrajanje: 30 sekundi")


                                if dani == "4":

                                    os.system("cls")
                                    print("Ponedjeljak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Walk Outs (from knees):              \t\t\t\tSerije:1      \tPonavljanja: 10")
                                    print("DB Crunch (light DB behind head):    \t\t\t\tSerije:1      \tPonavljanja: 20")
                                    print("Plank:                               \t\t\t\tSerije:1      \tTrajanje: 1 minuta")
                                    print("Band Hold (on back):                 \t\t\t\tSerije:10     \tTrajanje: 3 sekunde izdržaj")

                                elif dani == "5":

                                    os.system("cls")
                                    print("Utorak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("DB Pullovers:                        \t\t\t\tSerije:3      \tPonavljanja: 8")
                                    print("Plate Arches:                        \t\t\t\tSerije:3      \tPonavljanja: 5 (obje strane)")
                                    print("Side Bridge:                         \t\t\t\tSerije:1      \tTrajanje: 20-30 sekundi (obje strane)")
                                    print("Side Bends / Dumbbell:               \t\t\t\tSerije:3      \tPonavljanja: 10 (obje strane)")

                                
                                elif dani == "6":

                                    os.system("cls")
                                    print("Srijeda")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Dead Bugs:                           \t\t\t\tSerije:3      \tTrajanje: 10 sekundi izdržaj")
                                    print("Supermans:                           \t\t\t\tSerije:3      \tPonavljanja: 10")
                                    print("Hyperextensions:                     \t\t\t\tSerije:2      \tPonavljanja: 10")
                                    print("Glute Bridge:                        \t\t\t\tSerije:2      \tTrajanje: 30 sekundi")

                                elif dani == "7":

                                    os.system("cls")
                                    print("Nedjelja")
                                    print("")
                                    print("ODMOR")
                                    print("")

                            
                            elif program == "2":

                                os.system("cls")
                                print("")
                                print("Počinjemo sa drugim programom u trajanju od jedne sedmice.")
                                print("")
                                print("Program br. 1")
                                print("")
                                print("Sedmični izbor vježbi po danima: ")
                                print("")
                                print("Ponedjeljak 1)")
                                print("Utorak 2)")
                                print("Srijeda 3)")
                                print("Četvrtak 4)")
                                print("Petak 5)")
                                print("Subota 6)")
                                print("Nedjelja 7)")
                                print("")

                                dani = input(str("Izaberite odgovarajući dan: "))

                                if dani == "1":

                                    os.system("cls")
                                    print("Ponedjeljak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Walk Outs (from knees):              \t\t\t\tSerije:1      \tPonavljanja: 10")
                                    print("DB Crunch (light DB behind head):    \t\t\t\tSerije:2      \tPonavljanja: 20")
                                    print("Planks:                              \t\t\t\tSerije:2      \tTrajanje: 1 minuta")
                                    print("Band Hold (kneeling):                \t\t\t\tSerije:2      \tTrajanje: 30 sekundi")

                                elif dani == "2":

                                    os.system("cls")
                                    print("Utorak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("DB Pullovers:                        \t\t\t\tSerije:3      \tPonavljanja: 8")
                                    print("Plate Arches:                        \t\t\t\tSerije:3      \tPonavljanja: 5")
                                    print("Side Bridge:                         \t\t\t\tSerije:1      \tTrajanje: 30 sekundi")
                                    print("Side Bends / Dumbbell:               \t\t\t\tSerije:1      \tPonavljanje: 10 obje strane")


                                elif dani == "3":

                                    os.system("cls")
                                    print("Srijeda")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Dead Bugs:                           \t\t\t\tSerije:3      \tTrajanje: 10 sekundi izdržaj")
                                    print("Supermans:                           \t\t\t\tSerije:3      \tPonavljanja: 10 sa pločom")
                                    print("Hyperextensions:                     \t\t\t\tSerije:3      \tPonavljanja: 10 sa pločom")
                                    print("Glute Bridge:                        \t\t\t\tSerije:3      \tTrajanje: 10 sekundi sa bučicama")

                                elif dani == "4":

                                    os.system("cls")
                                    print("Četvrtak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Walk Outs (from knees):              \t\t\t\tSerije:1      \tPonavljanja: 10")
                                    print("DB Crunch (light DB behind head):    \t\t\t\tSerije:2      \tPonavljanja: 20")
                                    print("Planks:                              \t\t\t\tSerije:2      \tTrajanje: 1 minuta")
                                    print("Band Hold (kneeling):                \t\t\t\tSerije:2      \tTrajanje: 30 sekundi")

                                elif dani == "5":

                                    os.system("cls")
                                    print("Petak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("DB Pullovers:                        \t\t\t\tSerije:3      \tPonavljanja: 8")
                                    print("Plate Arches:                        \t\t\t\tSerije:3      \tPonavljanja: 5")
                                    print("Side Bridge:                         \t\t\t\tSerije:1      \tTrajanje: 30 sekundi")
                                    print("Side Bends / Dumbbell:               \t\t\t\tSerije:1      \tPonavljanje: 10 obje strane")


                                elif dani == "6":

                                    os.system("cls")
                                    print("Subota")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Dead Bugs:                           \t\t\t\tSerije:3      \tTrajanje: 10 sekundi izdržaj")
                                    print("Supermans:                           \t\t\t\tSerije:3      \tPonavljanja: 10 sa pločom")
                                    print("Hyperextensions:                     \t\t\t\tSerije:3      \tPonavljanja: 10 sa pločom")
                                    print("Glute Bridge:                        \t\t\t\tSerije:3      \tTrajanje: 10 sekundi sa bučicama")

                                elif dani == "7":

                                    os.system("cls")
                                    print("Nedjelja")
                                    print("")
                                    print("ODMOR")
                                    print("")


                            elif program == "3":

                                os.system("cls")
                                print("")
                                print("Počinjemo sa trećim programom u trajanju od jedne sedmice.")
                                print("")
                                print("Program br. 1")
                                print("")
                                print("Sedmični izbor vježbi po danima: ")
                                print("")
                                print("Ponedjeljak 1)")
                                print("Utorak 2)")
                                print("Srijeda 3)")
                                print("Četvrtak 4)")
                                print("Petak 5)")
                                print("Subota 6)")
                                print("Nedjelja 7)")
                                print("")

                                dani = input(str("Izaberite odgovarajući dan: "))

                                if dani == "1":

                                    os.system("cls")
                                    print("Ponedjeljak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Walk Outs (from knees):              \t\t\t\tSerije:1      \tPonavljanja: 20")
                                    print("DB Crunch (heavy dumbbell):          \t\t\t\tSerije:2      \tPonavljanja: 10 sa ispruženim rukama")
                                    print("Plank:                               \t\t\t\tSerije:1      \tTrajanje: 1 minuta")
                                    print("Band Hold (kneeling):                \t\t\t\tSerije:10     \tTrajanje: max")

                                elif dani == "2":

                                    os.system("cls")
                                    print("Utorak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("DB Pullovers:                        \t\t\t\tSerije:3      \tPonavljanja: 8")
                                    print("Plate Arches:                        \t\t\t\tSerije:3      \tPonavljanja: 5")
                                    print("Side Bridge:                         \t\t\t\tSerije:1      \tTrajanje: 30 sekundi")
                                    print("Side Bends / Dumbbell:               \t\t\t\tSerije:1      \tPonavljanje: 10 obje strane")


                                elif dani == "3":

                                    os.system("cls")
                                    print("Srijeda")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Dead Bugs:                           \t\t\t\tSerije:3      \tTrajanje: 10 sekundi izdržaj")
                                    print("Supermans:                           \t\t\t\tSerije:3      \tPonavljanja: 10 sa pločom")
                                    print("Reverse Hyperextensions:             \t\t\t\tSerije:3      \tPonavljanja: 10 sa pločom")
                                    print("Glute Bridge:                        \t\t\t\tSerije:3      \tTrajanje: 10 sekundi sa bučicama")


                                if dani == "4":

                                    os.system("cls")
                                    print("Četvrtak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Walk Outs (from knees):              \t\t\t\tSerije:1      \tPonavljanja: 20")
                                    print("DB Crunch (heavy dumbbell):          \t\t\t\tSerije:2      \tPonavljanja: 10 sa ispruženim rukama")
                                    print("Plank:                               \t\t\t\tSerije:1      \tTrajanje: 1 minuta")
                                    print("Band Hold (kneeling):                \t\t\t\tSerije:10     \tTrajanje: max")

                                elif dani == "5":

                                    os.system("cls")
                                    print("Petak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("DB Pullovers:                        \t\t\t\tSerije:3      \tPonavljanja: 8")
                                    print("Plate Arches:                        \t\t\t\tSerije:3      \tPonavljanja: 5")
                                    print("Side Bridge:                         \t\t\t\tSerije:1      \tTrajanje: 30 sekundi")
                                    print("Side Bends / Dumbbell:               \t\t\t\tSerije:1      \tPonavljanje: 10 obje strane")


                                elif dani == "6":

                                    os.system("cls")
                                    print("Subota")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Dead Bugs:                           \t\t\t\tSerije:3      \tTrajanje: 10 sekundi izdržaj")
                                    print("Supermans:                           \t\t\t\tSerije:3      \tPonavljanja: 10 sa pločom")
                                    print("Reverse Hyperextensions:             \t\t\t\tSerije:3      \tPonavljanja: 10 sa pločom")
                                    print("Glute Bridge:                        \t\t\t\tSerije:3      \tTrajanje: 10 sekundi sa bučicama")

                                elif dani == "7":

                                    os.system("cls")
                                    print("Nedjelja")
                                    print("")
                                    print("ODMOR")
                                    print("")


                            elif program == "4":

                                os.system("cls")
                                print("")
                                print("Počinjemo sa četvrtim programom u trajanju od jedne sedmice.")
                                print("")
                                print("Program br. 1")
                                print("")
                                print("Sedmični izbor vježbi po danima: ")
                                print("")
                                print("Ponedjeljak 1)")
                                print("Utorak 2)")
                                print("Srijeda 3)")
                                print("Četvrtak 4)")
                                print("Petak 5)")
                                print("Subota 6)")
                                print("Nedjelja 7)")
                                print("")

                                dani = input(str("Izaberite odgovarajući dan: "))

                                if dani == "1":

                                    os.system("cls")
                                    print("Ponedjeljak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Walk Outs:                           \t\t\t\tSerije:3      \tPonavljanja: 5 stojeći ili iz čučnja")
                                    print("DB Crunch (heavy dumbbell:           \t\t\t\tSerije:3      \tPonavljanja: 10 sa ispruženim rukama")
                                    print("Plank:                               \t\t\t\tSerije:3      \tTrajanje: 1 minuta")
                                    print("Band Hold (kneeling):                \t\t\t\tSerije:3      \tTrajanje: max")


                                elif dani == "2":

                                    os.system("cls")
                                    print("Utorak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("DB Pullovers + Crunch(on swiss ball):\t\t\t\tSerije:5      \tPonavljanja: 10")
                                    print("Plate Arches:                        \t\t\t\tSerije:5      \tPonavljanja: 8")
                                    print("Side Bridge:                         \t\t\t\tSerije:5      \tTrajanje: 30 sekundi/prvih 10 sekundi sa podignutom nogom")
                                    print("Side Bends / Dumbbell:               \t\t\t\tSerije:5      \tPonavljanje: 10 obje strane")


                                elif dani == "3":

                                    os.system("cls")
                                    print("Srijeda")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Dead Bugs / Dumbbell:                \t\t\t\tSerije:3      \tTrajanje: 10 sekundi izdržaj")
                                    print("Supermans:                           \t\t\t\tSerije:3      \tPonavljanja: 10 sa pločom")
                                    print("Reverse Hyperextensions:             \t\t\t\tSerije:3      \tPonavljanja: 10 na bench klupi, svako ponavljanje - izdržaj 3 sekunde")
                                    print("Glute Bridge / Dumbbel:              \t\t\t\tSerije:3      \tTrajanje: 10 sekundi sa bučicama")


                                if dani == "4":

                                    os.system("cls")
                                    print("Četvrtak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Walk Outs:                           \t\t\t\tSerije:3      \tPonavljanja: 5 stojeći ili iz čučnja")
                                    print("DB Crunch (heavy dumbbell):          \t\t\t\tSerije:3      \tPonavljanja: 10 sa ispruženim rukama")
                                    print("Plank:                               \t\t\t\tSerije:3      \tTrajanje: 1 minuta")
                                    print("Band Hold (kneeling):                \t\t\t\tSerije:3      \tTrajanje: max")


                                elif dani == "5":

                                    os.system("cls")
                                    print("Petak")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("DB Pullovers + Crunch(on swiss ball):\t\t\t\tSerije:5      \tPonavljanja: 10")
                                    print("Plate Arches:                        \t\t\t\tSerije:5      \tPonavljanja: 8")
                                    print("Side Bridge:                         \t\t\t\tSerije:5      \tTrajanje: 30 sekundi/prvih 10 sekundi sa podignutom nogom")
                                    print("Side Bends / Dumbbell:               \t\t\t\tSerije:5      \tPonavljanje: 10 obje strane")


                                elif dani == "6":

                                    os.system("cls")
                                    print("Subota")
                                    print("")

                                    print(f"Vježbe:                             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("")

                                    print("Dead Bugs / Dumbbell:                \t\t\t\tSerije:3      \tTrajanje: 10 sekundi izdržaj")
                                    print("Supermans:                           \t\t\t\tSerije:3      \tPonavljanja: 10 sa pločom")
                                    print("Reverse Hyperextensions:             \t\t\t\tSerije:3      \tPonavljanja: 10 na bench klupi, svako ponavljanje - izdržaj 3 sekunde")
                                    print("Glute Bridge / Dumbbel:              \t\t\t\tSerije:3      \tTrajanje: 10 sekundi sa bučicama")

                                elif dani == "7":

                                    os.system("cls")
                                    print("Nedjelja")
                                    print("")
                                    print("ODMOR")
                                    print("")

                                    print("Čestitam uspješno ste zavšili trening za jačanje trbušnog zida")
                                    exit()

                        #detalji i informacije o treningu
                        elif izbor_treninga == "2":
                        
                            os.system("cls")
                            print("Cilj treninga: Pojačati snagu trbušnog zida.")
                            print("Trajanje treninga: 4 sedmice.")
                            print("Trajanje jednog treninga: sa uvodnim dijelom oko 35 minuta")
                            print("")
                            print("Cilj je odraditi trening u kontinuitetu sa jednim slobodnim danom. Budite posebno oprezni i svakako slušajte svoje tijelo.")
                            print("Ako osjetite bol ili osjećate umor u trbušnom zidu, uzmite slobodan dan.")
                            print("Ovaj program se radi sa progresijom, tako da se vježbe i propisana ponavljanja malo razlikuju iz sedmice u sedmicu.")


                        elif izbor_treninga == "0":
                            main()

                        else: 
                            print("Pogrešan unos, molimo pokušajte ponovo.")


                #trening za mišićnu definiciju
                elif biranje_treninga == "2":
                    os.system("cls")
                    print("-"*55)
                    print("Dobrodošli u program treninga za mišićnu definiciju")
                    print("-"*55)
                    print("")
                    while True:
                        print("")
                        print("Za odabir programa za vježbanje pritisnite 1)")
                        print("Za detaljne informacije o treningu pritisnite 2)")
                        print("Za povratak u glavni meni pritisnite 0)")
                        print("")
                        izbor_treninga = input(str("Molimo unesite jednu od navedenih opcija (1/2/0): "))

                        if izbor_treninga == "1":

                            os.system("cls")
                            print("Program treninga za mišićnu definiciju sastoji se od 3 programa. ")
                            print("")
                            print("Program br.1) ")
                            print("Program br.2) ")
                            print("Program br.3) ")
                            print("")
                            program = input(str("Molimo izaberite program koji trenutno radite: "))
                            if program == "1":
                                os.system("cls")
                                print("")
                                print("Počinjemo sa prvim programom u trajanju od dvije sedmice.")
                                print("")
                                print("Program br. 1")
                                print("")
                                print("Sedmični izbor vježbi po danima: ")
                                print("")
                                print("Ponedjeljak 1)")
                                print("Utorak 2)")
                                print("Srijeda 3)")
                                print("Četvrtak 4)")
                                print("Petak 5)")
                                print("Subota 6)")
                                print("Nedjelja 7)")
                                print("")

                                dani = input(str("Izaberite odgovarajući dan: "))
                                
                                if dani == "1":
                                    os.system("cls")
                                    print("Ponedjeljak")
                                    print("")

                                    print(f"Mišićne grupe i vježbe:             \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)

                                    print("Prsa")
                                    print("")
                                    print("Bench press:                         \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Incline Bench Press:                 \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Dumbbell Flys:                       \t\t\t\tSerije:2      \tPonavljanja: 15")
                                    print("Pullover:                            \t\t\t\tSerije:2      \tPonavljanja: 15")

                                    print("")
                                    print("")

                                    print("Triceps")
                                    print("")
                                    print("Face Pull:                           \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Lat Pulldown:                        \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Kick Back:                           \t\t\t\tSerije:2      \tPonavljanja: 12")

                                    print("")
                                    print("")

                                    print("Trbuh")
                                    print("")
                                    print("Bulgarian Split Squat:               \t\t\t\tSerije:3      \tPonavljanja: max")
                                    print("Leg-Lift:                            \t\t\t\tSerije:3      \tPonavljanja: max")

                                    print("")
                                    print("")

                                    print("Listovi:")
                                    print("")
                                    print("Calf Raise:                          \t\t\t\tSerije:3      \tPonavljanja: 15-20")
                                    print("Leg Press Toe Raises :               \t\t\t\tSerije:3      \tPonavljanja: 15-20")
                                    
                                    
                                elif dani == "2":
                                    os.system("cls")
                                    print("")
                                    print("Utorak")
                                    print("")
                                    print("Aerobni trening kombinacija traka za trčanje i veslački erogometar u trajanju od 45 minuta, 2-3 sata nakon obroka.")
                                    
                                elif dani == "3":
                                    os.system("cls")
                                    print("")
                                    print("Srijeda")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:              \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("Leđa:")
                                    print("")
                                    print("The Classic Pull-Up                   \t\t\t\tSerije:3      \tPonavljanja: max")            
                                    print("Barbell Row:                          \t\t\t\tSerije:3      \tPonavljanja: 12")
                                    print("Hyperextension:                       \t\t\t\tSerije:3      \tPonavljanja: 15")
                                    print("")
                                    print("")
                                    print("Biceps:")
                                    print("")
                                    print("Barbell curls:                        \t\t\t\tSerije:3      \tPonavljanja: 12") 
                                    print("Seated Dumbbell Curl:                 \t\t\t\tSerije:3      \tPonavljanja: 12") 
                                    print("Concentration curl                    \t\t\t\tSerije:2      \tPonavljanja: 12") 
                                    print("")
                                    print("")
                                    print("Podlaktice:")
                                    print("Forearms Roller                       \t\t\t\tSerije:3      \tPonavljanja: max") 
                                    print("")
                                    print("")
                                    print("Listovi:")
                                    print("Calf Raise:                           \t\t\t\tSerije:3      \tPonavljanja: max") 
                                    
                                elif dani == "4":
                                    os.system("cls")
                                    print("")
                                    print("Četvrtak")
                                    print("")

                                    print("ODMOR")
                                    
                                elif dani == "5":
                                    os.system("cls")
                                    print("")
                                    print("Petak")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:              \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("Ramena:")
                                    print("")
                                    print("Overhead press:                       \t\t\t\tSerije:3      \tPonavljanja: 12-15")            
                                    print("Standing Dumbbell Lateral:            \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Dumbbell Rear Delt Raise:             \t\t\t\tSerije:3      \tPonavljanja: 15")
                                    print("")
                                    print("")

                                    print("Trbuh:")
                                    print("Bulgarian Squat:                      \t\t\t\tSerije:2      \tPonavljanja: 15-20") 
                                    print("Russian Twist:                        \t\t\t\tSerije:2      \tPonavljanja: max") 

                                    print("")
                                    print("")
                                    print("Noge:")
                                    print("")
                                    print("Squat:                                \t\t\t\tSerije:4      \tPonavljanja: 12")
                                    print("Seated Leg Curl:                      \t\t\t\tSerije:3      \tPonavljanja: 12")
                                    print("Barbell Lunge:                        \t\t\t\tSerije:3      \tPonavljanja: 12")
                                
                                elif dani == "6":
                                    os.system("cls")
                                    print("")
                                    print("Subota")
                                    print("")
                                    print("Aerobni trening, trčanje vani (meka podloga) u trajanju 45 minuta, ujutro prije doručka.")

                                    
                                elif dani == "7":
                                    os.system("cls")
                                    print("Nedjelja")
                                    print("")
                                    print("ODMOR")
                                    print("")
                                    print("NAPOMENA: Nakon što završite prvi trening program, izaberite naredni. ")

                                else: 
                                    print("Pogrešan unos.")
                            elif program == "2":
                    
                                os.system("cls")
                                print("Program se provodi nakon uspješno izvršenog prvog programa.")
                                print("")
                                print("Program br. 2")
                                print("")
                                print("Sedmični izbor vježbi po danima: ")
                                print("")
                                print("Ponedjeljak 1)")
                                print("Utorak 2)")
                                print("Srijeda 3)")
                                print("Četvrtak 4)")
                                print("Petak 5)")
                                print("Subota 6)")
                                print("Nedjelja 7)")
                                print("")

                                dani = input(str("Izaberite odgovarajući dan: "))
                                if dani == "1":
                                    os.system("cls")
                                    print("")
                                    print("Ponedjeljak")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                     \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*100)
                                    print("Prsa:")
                                    print("")
                                    print("Bench press:                                 \t\t\t\tSerije:4      \tPonavljanja: 12-15")
                                    print("Incline Dumbbell Bench Press:                \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Decline Bench Press:                         \t\t\t\tSerije:3      \tPonavljanja: 12")
                                    print("Dumbell Fly:                                 \t\t\t\tSerije:2      \tPonavljanja: 10-12")

                                    print("")
                                    print("")
                                    print("Noge:")
                                    print("")
                                    print("Squat:                                       \t\t\t\tSerije:4      \tPonavljanja: 12")
                                    print("Leg Extension:                               \t\t\t\tSerije:2      \tPonavljanja: 12")
                                    print("Stiff Leg Deadlift:                          \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Leg Curl:                                    \t\t\t\tSerije:3      \tPonavljanja: 12")

                                    print("")
                                    print("")
                                    print("Trbuh:")
                                    print("")
                                    print("Standing Forward Bend:                       \t\t\t\tSerije:2      \tPonavljanja: max")
                                    print("Swiss Ball :                                 \t\t\t\tSerije:3      \tPonavljanja: max")
                                    print("")
                                    
                                elif dani == "2":
                                    os.system("cls")
                                    print("")
                                    print("Utorak:")
                                    print("")

                                    print("Aerobni trening kombinacija steper i orbitrack u trajanju 45 minuta, 2-3 sata nakon obroka.")
                                    print("")
                                    print("")
                                
                                elif dani == "3":
                                    os.system("cls")
                                    print("Srijeda:")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                     \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("Leđa:")
                                    print("")
                                    print("Behind The Head Lat Pulldown:                \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("T - Bar Row:                                 \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Hyperextension:                              \t\t\t\tSerije:3      \tPonavljanja: 15")

                                    print("")
                                    print("")
                                    print("Biceps:")
                                    print("")
                                    print("Preacher Dumbbell Curl:                      \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Dumbbell Hammer Curl:                        \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Concentration Biceps Curl:                   \t\t\t\tSerije:3      \tPonavljanja: 12")

                                    print("")
                                    print("")
                                    print("Podlaktice:")
                                    print("")
                                    print("Barbell Behind The Back Wrist Curl:          \t\t\t\tSerije:3      \tPonavljanja: 12-15")

                                    print("")
                                    print("")
                                    print("Listovi:")
                                    print("")
                                    print("Calf Raise:                                  \t\t\t\tSerije:5      \tPonavljanja: 15-20")

                                    print("")
                                    
                                elif dani == "4":
                                    os.system("cls")
                                    print("")
                                    print("Četvrtak:")
                                    print("ODMOR")
                                    print("")
                                    
                                elif dani == "5":
                                    os.system("cls")
                                    print("")
                                    print("Petak:")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                     \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("Ramena:")
                                    print("")
                                    print("Dumbbell Bench Press:                        \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Barbell Row:                                 \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Dumbbell Rear Delt Raise:                    \t\t\t\tSerije:3      \tPonavljanja: 12")

                                    print("")
                                    print("")
                                    print("Trapez:")
                                    print("")
                                    print("Dumbbell Shrug:                              \t\t\t\tSerije:3      \tPonavljanja: 15")
                                    print("")
                                    print("")
                                    print("Triceps:")
                                    print("Skull Crusher:                               \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Triceps Extension:                           \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Kick Back:                                   \t\t\t\tSerije:2      \tPonavljanja: 12-15")

                                    print("")
                                    print("")
                                    print("Trbuh:")
                                    print("")
                                    print("Leg Raises:                                  \t\t\t\tSerije:3      \tPonavljanja: max")
                                    print("Crunches:                                    \t\t\t\tSerije:3      \tPonavljanja: max")


                                    print("")
                                    print("")
                                    print("Listovi:")
                                    print("")
                                    print("Calf Raise:                                  \t\t\t\tSerije:5      \tPonavljanja: 15-20")
                                    print("")
                                    
                                elif dani == "6":
                                    os.system("cls")
                                    print("")
                                    print("Subota")
                                    print("")
                                    print("Aerobni trening, trčanje vani (meka podloga) u trajanju 45 minuta, ujutro prije doručka.")
                                    
                                elif dani == "7":
                                    os.system("cls")
                                    print("")
                                    print("Nedjelja")
                                    print("")
                                    print("ODMOR")
                                    print("")
                                    print("NAPOMENA: Nakon što završite drugi trening program, izaberite naredni. ")
                                    
                                else: 
                                    print("Pogrešan unos, molimo unesite jedan od ponuđenih dana u sedmici. ")


                            elif program == "3":
                                os.system("cls")
                                print("Program se provodi nakon uspješno izvršenog drugog programa. ")
                                print("")
                                print("Program br.3")
                                print("")
                                print("Sedmični izbor vježbi po danima: ")
                                print("")
                                print("Ponedjeljak 1)")
                                print("Utorak 2)")
                                print("Srijeda 3)")
                                print("Četvrtak 4)")
                                print("Petak 5)")
                                print("Subota 6)")
                                print("Nedjelja 7)")
                                print("")

                                dani = input(str("Izaberite odgovarajući dan: "))
                                if dani == "1":

                                    os.system("cls")
                                    print("")
                                    print("Ponedjeljak")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                     \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*100)
                                    print("Prsa:")
                                    print("")
                                    print("")
                                    print("Incline Barbell Bench Press:                 \t\t\t\tSerije:4      \tPonavljanja: 12-15")
                                    print("Dumbbell Bench Press:                        \t\t\t\tSerije:3      \tPonavljanja: 12")
                                    print("Decline Dumbbell Fly:                        \t\t\t\tSerije:3      \tPonavljanja: 12")
                                    print("Pullover:                                    \t\t\t\tSerije:3      \tPonavljanja: 10")

                                    print("")
                                    print("")
                                    print("Triceps:")
                                    print("")
                                    print("Close Grip Bench Press:                      \t\t\t\tSerije:3      \tPonavljanja: 15")
                                    print("Triceps Pushdown:                            \t\t\t\tSerije:3      \tPonavljanja: 12-15")

                                    print("")
                                    print("")
                                    print("Trbuh:")
                                    print("")
                                    print("Bulgarian Squat:                             \t\t\t\tSerije:3      \tPonavljanja: max")
                                    print("Standing Forward Bend:                       \t\t\t\tSerije:3      \tPonavljanja: max")

                                    print("")
                                    print("")
                                    print("Listovi:")
                                    print("")
                                    print("Calf Raise:                                  \t\t\t\tSerije:4      \tPonavljanja: 15-20")
                                    
                                elif dani == "2":
                                    os.system("cls")
                                    print("")
                                    print("Utorak:")
                                    print("")
                                    print("Aerobni trening, kombinacija bicikl i veslački ergometar u trajanju 45 minuta, 2-3 sata nakon obroka.")
                                    

                                elif dani == "3":

                                    os.system("cls")
                                    print("")
                                    print("Srijeda")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                     \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*100)
                                    print("Leđa:")
                                    print("")
                                    print("Pull Ups:                                    \t\t\t\tSerije:3      \tPonavljanja: max")
                                    print("One Arm Dumbell Row:                         \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Hyperextension:                              \t\t\t\tSerije:3      \tPonavljanja: 15")

                                    print("")
                                    print("")
                                    print("Biceps:")
                                    print("")
                                    print("Barbell Curls:                               \t\t\t\tSerije:3      \tPonavljanja: 15")
                                    print("One Arm Preacher Hammer Dumbbell Curl:       \t\t\t\tSerije:3      \tPonavljanja: 15")
                                    print("Concentration Biceps Curls:                  \t\t\t\tSerije:3      \tPonavljanja: 12")

                                    print("")
                                    print("")
                                    print("Podlaktice:")
                                    print("")
                                    print("One-Arm Dumbbell Wrist Curl Over a Bench:    \t\t\t\tSerije:3      \tPonavljanja: 15-20")

                                elif dani == "4":

                                    os.system("cls")
                                    print("")
                                    print("Četvrtak")
                                    print("")
                                    print("ODMOR")

                                elif dani == "5":

                                    os.system("cls")
                                    print("")
                                    print("Petak")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                     \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*100)
                                    print("Ramena:")
                                    print("")
                                    print("Overhead Press Behind Neck:                  \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Barbell Row:                                 \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                    print("Dumbbell Rear Delt Raise:                    \t\t\t\tSerije:3      \tPonavljanja: 15")

                                    print("")
                                    print("")
                                    print("Trapez:")
                                    print("")
                                    print("Barbell Shrug):                             \t\t\t\tSerije:3      \tPonavljanja: 15")
                                    print("Dumbbell Shrug ):                           \t\t\t\tSerije:2      \tPonavljanja: 15")

                                    print("")
                                    print("")
                                    print("Trbuh:")
                                    print("")
                                    print("Bulgarian Squat:                            \t\t\t\tSerije:3      \tPonavljanja: max")
                                    print("Elbow To Knee Crunch:                       \t\t\t\tSerije:3      \tPonavljanja: max")

                                    print("")
                                    print("")
                                    print("Listovi:")
                                    print("")
                                    print("Calf Raise:                                 \t\t\t\tSerije:3      \tPonavljanja: max")
                                    

                                elif dani == "6":
                                    os.system("cls")
                                    print("")
                                    print("Subota:")
                                    print("")
                                    print("Aerobni trening, trčanje vani (meka podloga) u trajanju 45 minuta, ujutro prije doručka.")
                                    

                                elif dani == "7":

                                    os.system("cls")
                                    print("")
                                    print("Nedjelja")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                     \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*100)
                                    print("Noge:")
                                    print("")
                                    print("Squat:                                       \t\t\t\tSerije:3      \tPonavljanja: 15")
                                    print("Leg Extension:                               \t\t\t\tSerije:2      \tPonavljanja: 15")
                                    print("Stiff Leg Deadlift:                          \t\t\t\tSerije:3      \tPonavljanja: 15")
                                    print("Leg Curl:                                    \t\t\t\tSerije:2      \tPonavljanja: 15")
                                    print("Dumbell Lunge:                               \t\t\t\tSerije:3      \tPonavljanja: 12")

                                    print("")
                                    print("")
                                    print("Trbuh:")
                                    print("")
                                    print("Bulgarian Squat:                             \t\t\t\tSerije:3      \tPonavljanja: max")
                                    print("Leg Raise:                                   \t\t\t\tSerije:3      \tPonavljanja: max")
                                    print("")
                                    print("Čestitamo uspješno ste završili programe treninga za mišićnu definiciju.")
                                

                            else:
                                print("Pogrešan unos, molimo unesite jedan od tri programa. ")
                                
                        elif izbor_treninga =="2":
                            #detalji i informacije o treningu
                            os.system("cls")
                            print("Cilj treninga: Mišićna definicija, topljenje potkožnog masnog tkiva.")
                            print("Oblik rada: Stanični.")
                            print("")
                            print("Trajanje treninga: s uvodnim dijelom oko 75 minuta.")
                            print("Odmor: Između serija 45-60 sekundi a između vježbi 2-3 minute.")
                            print("")
                            print("Prehrana: Preporuka dnevnog unosa proteina je 2 gr/kg tjelesne težine. Unos ugljikohidrata je oko 2.5 gr/kg tjelesne težine. Dnevni unos tekućine minimalno 2 litre.")
                            print("")
                            print("Suplementacija: Najčešće preporuke za suplementaciju su 'Whey' protein nakon treninga, glutamin, BCAA, te L-carnitine, međutim, kako su potrebe za dodacima prehrani individualne, savjetujemo da se o načinu uzimanja, količini i vrsti preparata savjetujete sa vašim individualnim trenerom koji će suplementaciju prilagoditi vašim potrebama i mogućnostima.")
                            print("")
                            print("Napomena: Prikazana su tri programa koji slijede jedan drugog i čine jedan ciklus. Svaki od programa provodi se po dvije sedmice a to znači da ciklus traje ukupno 6 sedmica, nakon čega slijedi testiranje i nadopuna programa. Program je namijenjen iskusnijim vježbačima i primjenjuje se nakon provedenog ciklusa treninga za razvoj mišićne mase.")
                            print("")
                            print("Aerobni trening: Služi za topljenje potkožnog masnog tkiva, adaptaciju organizma na aerobni rad, te poboljšanje kardiovaskularnih i respiratornih sposobnosti.Aerobni trening provodi se u frekvenciji od 60-75%. Aerobni trening provodi se u fitness centru na kardio spravama ili vani, te je poželjno korištenje pulsmetra. Također možete koristiti metodu mjerenja pulsa u 15 sekundi koji ćete zatim pomnožiti sa 4.")

                        elif izbor_treninga == "0":
                            main()
                        else: 
                            print("Pogrešan unos, molimo pokušajte ponovo.")

                #trening za dobijanje mase i kilaže
                elif biranje_treninga == "3":
                    
                    os.system("cls")
                    print("-"*55)
                    print("Dobrodošli u program treninga za dobijanje mase i kilaže")
                    print("-"*55)

                    while True:
                        print("")
                        print("Za odabir programa za vježbanje pritisnite 1)")
                        print("Za detaljne informacije o treningu pritisnite 2)")
                        print("Za povratak u glavni meni pritisnite 0)")
                        print("")
                        izbor_treninga = input(str("Molimo unesite jednu od navedenih opcija (1/2/0): "))

                        if izbor_treninga == "1":

                            os.system("cls")
                            print("Program treninga za dobijanje mase i kilaže sastoji od 2 programa. ")
                            print("")
                            print("Program br.1) ")
                            print("Program br.2) ")
                            print("")

                            program = input(str("Molimo izaberite program koji trenutno radite: "))

                            if program == "1":
                                os.system("cls")
                                print("")
                                print("Počinjemo sa prvim programom u trajanju od dvije sedmice.")
                                print("")
                                print("Program br. 1")
                                print("")
                                print("Sedmični izbor vježbi po danima: ")
                                print("")
                                print("Ponedjeljak 1)")
                                print("Utorak 2)")
                                print("Srijeda 3)")
                                print("Četvrtak 4)")
                                print("Petak 5)")
                                print("Subota 6)")
                                print("Nedjelja 7)")
                                print("")

                                dani = input(str("Izaberite odgovarajući dan: "))

                                if dani == "1":
                                    os.system("cls")

                                    print("Ponedjeljak")
                                    print("")

                                    print(f"Mišićne grupe i vježbe:                 \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)

                                    print("Prsa i tricepsi")
                                    print("")
                                    print("Bench Press:                             \t\t\t\tSerije:3      \tPonavljanja: 6-8")
                                    print("Weighted Dip:                            \t\t\t\tSerije:4      \tPonavljanja: 6-8")
                                    print("Close-Grip Barbell Bench Press:          \t\t\t\tSerije:4      \tPonavljanja: 6-8")
                                    print("Dumbbell Lying Triceps Extension:        \t\t\t\tSerije:3      \tPonavljanja: 6-8")

                                    print("")
                                    print("")

                                elif dani == "2":

                                    os.system("cls")
                                    print("")
                                    print("Utorak")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                 \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("Noge, listovi i trbuh:")
                                    print("")
                                    print("Smith Machine Squat:                     \t\t\t\tSerije:3      \tPonavljanja: 6-8")            
                                    print("Leg Press:                               \t\t\t\tSerije:4      \tPonavljanja: 6-8")
                                    print("Barbell Hack Squat:                      \t\t\t\tSerije:4      \tPonavljanja: 6-8")
                                    print("Romanian Deadlift:                       \t\t\t\tSerije:4      \tPonavljanja: 6-8") 
                                    print("Standing Calf Raise:                     \t\t\t\tSerije:3      \tPonavljanja: 20") 
                                    print("Hanging Leg Raise:                       \t\t\t\tSerije:2      \tPonavljanja: 20")
                                    print("Cable Crunch:                            \t\t\t\tSerije:2      \tPonavljanja: 20") 

                                elif dani == "3":
                                    os.system("cls")
                                    print("")
                                    print("Srijeda")
                                    print("")
                                    print("ODMOR")
                                    print("")

                                elif dani == "4":

                                    os.system("cls")
                                    print("")
                                    print("Četvrtak")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                 \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("Ramena i trapez:")
                                    print("")
                                    print("Overhead Dumbbell Press:                 \t\t\t\tSerije:3      \tPonavljanja: 6-8")            
                                    print("Arnold Press:                            \t\t\t\tSerije:4      \tPonavljanja: 6-8")
                                    print("Barbell Upright Row:                     \t\t\t\tSerije:4      \tPonavljanja: 6-8")
                                    print("Bent-Over Lateral Raise:                 \t\t\t\tSerije:4      \tPonavljanja: 6-8") 
                                    print("Dumbbell Shrug:                          \t\t\t\tSerije:3      \tPonavljanja: 6-8") 

                                elif dani == "5":

                                    os.system("cls")
                                    print("")
                                    print("Petak")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                 \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("Leđa,biceps,trbuh:")
                                    print("")
                                    print("Barbell Deadlift:                        \t\t\t\tSerije:3      \tPonavljanja: 6-8")            
                                    print("Barbell Bent-Over Row:                   \t\t\t\tSerije:4      \tPonavljanja: 6-8")
                                    print("T-Bar Row:                               \t\t\t\tSerije:4      \tPonavljanja: 6-8")
                                    print("Barbell Biceps Curl:                     \t\t\t\tSerije:4      \tPonavljanja: 6-8") 
                                    print("Incline Dumbbell Biceps Curl             \t\t\t\tSerije:4      \tPonavljanja: 6-8") 
                                    print("Barbell Preacher Curl:                   \t\t\t\tSerije:3      \tPonavljanja: 6-8")
                                    print("Crunch:                                  \t\t\t\tSerije:2      \tPonavljanja: 20") 
                                    print("Reverse Crunch                           \t\t\t\tSerije:2      \tPonavljanja: 20") 


                                elif dani == "6":

                                    os.system("cls")
                                    print("")
                                    print("Subota")
                                    print("")
                                    print("ODMOR")
                                    print("")

                                elif dani == "7":

                                    os.system("cls")
                                    print("")
                                    print("Nedjelja")
                                    print("")
                                    print("ODMOR")
                                    print("")

                                    print("NAPOMENA: Nakon što završite prvi trening program u trajanju od dvije sedmice, izaberite naredni. ")

                                else:
                                    os.system("cls")
                                    print("Pogrešan unos, molimo pokušajte ponovo.")


                            if program =="2":

                                os.system("cls")
                                print("")
                                print("Počinjemo sa prvim programom u trajanju od dvije sedmice.")
                                print("")
                                print("Program br. 1")
                                print("")
                                print("Sedmični izbor vježbi po danima: ")
                                print("")
                                print("Ponedjeljak 1)")
                                print("Utorak 2)")
                                print("Srijeda 3)")
                                print("Četvrtak 4)")
                                print("Petak 5)")
                                print("Subota 6)")
                                print("Nedjelja 7)")
                                print("")

                                dani = input(str("Izaberite odgovarajući dan: "))

                                if dani == "1":
                                    os.system("cls")

                                    print("Ponedjeljak")
                                    print("")

                                    print(f"Mišićne grupe i vježbe:                 \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)

                                    print("Prsa i leđa")
                                    print("")
                                    print("Dumbbell Flye:                           \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Barbell Bench Press:                     \t\t\t\tSerije:4      \tPonavljanja: 10-12")
                                    print("Warrior Fit Incline Dumbell Bench Press: \t\t\t\tSerije:4      \tPonavljanja: 10-12")
                                    print("Cable Crossover:                         \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Rack Pull:                               \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Lat Pulldown:                            \t\t\t\tSerije:4      \tPonavljanja: 10-12")
                                    print("Single-Arm Neutral-Grip Dumbell Row:     \t\t\t\tSerije:4      \tPonavljanja: 10-12")
                                    print("Seated Dumbell Shoulder Press:           \t\t\t\tSerije:3      \tPonavljanja: 10-12")

                                    print("")
                                    print("")

                                if dani == "2":

                                    os.system("cls")
                                    print("")
                                    print("Utorak")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                 \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("Noge, listovi i trbuh:")
                                    print("")
                                    print("Barbell Squat:                           \t\t\t\tSerije:3      \tPonavljanja: 10-12")            
                                    print("Leg Press:                               \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Barbell Hack Squat:                      \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Romanian Deadlift:                       \t\t\t\tSerije:3      \tPonavljanja: 10-12") 
                                    print("Lying Leg Curl:                          \t\t\t\tSerije:3      \tPonavljanja: 10-12") 
                                    print("Seated Calf Raise:                       \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Donkey Calf Raise:                       \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Reverse Crunch:                          \t\t\t\tSerije:2      \tPonavljanja: 12") 
                                    print("Hanging Knee Raise:                      \t\t\t\tSerije:2      \tPonavljanja: 12") 
                                    print("Double Crunch:                           \t\t\t\tSerije:2      \tPonavljanja: max")

                                elif dani == "3":
                                    os.system("cls")
                                    print("")
                                    print("Srijeda")
                                    print("")
                                    print("ODMOR")
                                    print("")

                                elif dani == "4":

                                    os.system("cls")
                                    print("")
                                    print("Četvrtak")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                 \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("Ramena i trapez:")
                                    print("")
                                    print("Cable Lateral Raise:                     \t\t\t\tSerije:3      \tPonavljanja: 10-12")            
                                    print("Arnold Press:                            \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Smith Machine Overhead Press:            \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Leaning Dumbbell Lateral Raise:          \t\t\t\tSerije:3      \tPonavljanja: 10-12") 
                                    print("Reverse Pec Deck Flye:                   \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Dumbbell Shrug:                          \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Incline Dumbbell Shrug:                  \t\t\t\tSerije:3      \tPonavljanja: 10-12")


                                elif dani == "5":

                                    os.system("cls")
                                    print("")
                                    print("Petak")
                                    print("")
                                    print(f"Mišićne grupe i vježbe:                 \t\t\t\tSerije:       \tPonavljanja:")
                                    print(f"-"*98)
                                    print("Triceps, biceps, trbuh:")
                                    print("")
                                    print("Lying Barbell Extension:                 \t\t\t\tSerije:3      \tPonavljanja: 10-12")            
                                    print("Weighted Bench Dip:                      \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Reverse-Grip Pressdown:                  \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Close-Grip EZ-Bar Biceps Curl:           \t\t\t\tSerije:3      \tPonavljanja: 10-12")
                                    print("Preacher Curl With Cable:                \t\t\t\tSerije:3      \tPonavljanja: 10-12") 
                                    print("Hanging Leg Raise:                       \t\t\t\tSerije:2      \tPonavljanja: 20") 
                                    print("Double Crunch:                           \t\t\t\tSerije:2      \tPonavljanja: 20")
                            

                                elif dani == "6":

                                    os.system("cls")
                                    print("")
                                    print("Subota")
                                    print("")
                                    print("ODMOR")
                                    print("")

                                elif dani == "7":

                                    os.system("cls")
                                    print("")
                                    print("Nedjelja")
                                    print("")
                                    print("ODMOR")
                                    print("")
                                    print("Čestitamo uspješno ste završili programe treninga za dobijanje mase i kilaže.")
                                    exit()

                                else:
                                    os.system("cls")
                                    print("Pogrešan unos, molimo pokušajte ponovo.")
                        #detalji i informacije o treningu
                        elif izbor_treninga == "2":
                            os.system("cls")
                            print("Cilj treninga: Dobijanje kilaže i mišićne mase")
                            print("")
                            print("Program je dizajniran tako da se kroz progresivno podizanje težine i intenziteta treninga dobije veća kilaža i mišićna masa.")
                            print("Trajanje treninga: sa uvodnim dijelom oko 75 minuta.")
                            print("Odmor: Između serija 2 minute a između vježbi 2-3 minute.")
                            print("Najbolji princip treninga ove vrste jeste 'hit-and-run'. To znači da treninzi trebaju biti relativno kratki i intenzivni. Broj ponavljanja je nizak, najbolje ograničiti na 6-8. Trening se bazira na osnovnim (višezglobnim) vježbama (čučanj, deadlift, bench press), a tek nakon toga slijede izolacijske vježbe.")
                            print("")
                            print("Jednako važno kao trening i prehrana je odmor i oporavak. Treba ciljati na barem 7-8 sati noćnog sna, a korisno će biti i kraće drijemanje preko dana (posebnonakon treninga, obroka i suplementacije nakon treninga).")
                            print("")
                            print("Prehrana: Obroke treba rasporediti kroz dan (cca svaka 2-2,5 sata). U redu je imati i noćni obrok (ako procijenimo da takva praksa ne ometa odmor i oporavak).")
                            print("Napomena: Prikazana su dva programa koji slijede jedan drugog. Svaki od programa provodi se po tri sedmice i to znači da ciklus traje ukupno 6 sedmica.")

                        elif izbor_treninga == "0":
                            main()


                        else: 
                            os.system("cls")
                            print("Pogrešan unos, molimo pokušajte ponovo.")

                #trening snage - dodatni trening za sve koji su u dobroj formi
                elif biranje_treninga == "4":
                    os.system("cls")
                    print("-"*55)
                    print("Dobrodošli u program treninga za izgradnju mišića i snage")
                    print("-"*55)
                    print("")


                    while True:
                        print("")
                        print("Za odabir programa za vježbanje pritisnite 1)")
                        print("Za detaljne informacije o treningu pritisnite 2)")
                        print("Za povratak u glavni meni pritisnite 0)")
                        print("")
                        izbor_treninga = input(str("Molimo unesite jednu od navedenih opcija (1/2/0): "))

                        if izbor_treninga == "1":

                            os.system("cls")
                            print("Program treninga za izgradnju mišića i snage.")
                            print("Trajanje treninga: 6 sedmica")
                            print("")
                            
                            os.system("cls")
                            print("")
                            print("Počinjemo sa prvim programom u trajanju od dvije sedmice.")
                            print("")
                            print("Program br. 1")
                            print("")
                            print("Sedmični izbor vježbi po danima: ")
                            print("")
                            print("Ponedjeljak 1)")
                            print("Utorak 2)")
                            print("Srijeda 3)")
                            print("Četvrtak 4)")
                            print("Petak 5)")
                            print("Subota 6)")
                            print("Nedjelja 7)")
                            print("")

                            dani = input(str("Izaberite odgovarajući dan: "))

                            if dani == "1":

                                os.system("cls")

                                print("Ponedjeljak")
                                print("")
                                print("Squats (Ramped):                         \t\t\t\tSerije:5      \tPonavljanja: 5")
                                print("Bench Press (Ramped):                    \t\t\t\tSerije:5      \tPonavljanja: 5")
                                print("Barbell Row (Ramped):                    \t\t\t\tSerije:5      \tPonavljanja: 5")
                                print("Upright Row:                             \t\t\t\tSerije:3      \tPonavljanja: 10")
                                print("Skullcrushers:                           \t\t\t\tSerije:3      \tPonavljanja: 10")
                                print("Dumbbell Curls:                          \t\t\t\tSerije:3      \tPonavljanja: 10")
                                print("Leg Curls:                               \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                print("Ab Wheel Roll Out:                       \t\t\t\tSerije:3      \tPonavljanja: 10-15")

                            elif dani == "2":

                                os.system("cls")
                                print("")
                                print("Utorak")
                                print("")
                                print("ODMOR")
                                print("")

                            elif dani == "3":
                                os.system("cls")
                                print("Srijeda")
                                print("")
                                print("Deadlifts (Ramped):                      \t\t\t\tSerije:5      \tPonavljanja: 5")
                                print("Romanian Deadlift:                       \t\t\t\tSerije:5      \tPonavljanja: 8-12")
                                print("Seated Overhead Press:                   \t\t\t\tSerije:5      \tPonavljanja: 8-10")
                                print("Pull Ups or Inverted Rows:               \t\t\t\tSerije:3      \tPonavljanja: 10-15")
                                print("Dips:                                    \t\t\t\tSerije:3      \tPonavljanja: 10-20")
                                print("Barbell Shrugs:                          \t\t\t\tSerije:3      \tPonavljanja: 10")
                                print("Standing or Seated Calf Raise:           \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                print("Plank:                                   \t\t\t\tSerije:3      \tPonavljanja: 60 sekundi")


                            elif dani == "4":

                                os.system("cls")
                                print("")
                                print("Četvrtak")
                                print("")
                                print("ODMOR")
                                print("")


                            elif dani == "5":
                                os.system("cls")
                                print("Petak")
                                print("")
                                print("Squats (Ramped):                         \t\t\t\tSerije:3      \tPonavljanja: 5")
                                print("Squats:                                  \t\t\t\tSerije:1      \tPonavljanja: 20")
                                print("Incline Dumbbell Bench Press:            \t\t\t\tSerije:3      \tPonavljanja: 10")
                                print("One Arm Dumbbell Row:                    \t\t\t\tSerije:3      \tPonavljanja: 10-15")
                                print("Seated Arnold Press	3	10-15:          \t\t\t\tSerije:3      \tPonavljanja: 10-15")
                                print("Cable Tricep Extensions:                 \t\t\t\tSerije:3      \tPonavljanja: 10")
                                print("Barbell Curls:                           \t\t\t\tSerije:3      \tPonavljanja: 10")
                                print("Leg Curls:                               \t\t\t\tSerije:3      \tPonavljanja: 12-15")
                                print("Ab Wheel Roll Out:                       \t\t\t\tSerije:3      \tPonavljanja: 10-15")

                            elif dani == "6":

                                os.system("cls")
                                print("")
                                print("Subota")
                                print("")
                                print("ODMOR")
                                print("")

                            elif dani == "7":

                                os.system("cls")
                                print("")
                                print("Nedjelja")
                                print("")
                                print("ODMOR")
                                print("")

                            else: 
                                print("Pogrešan odabir, molimo pokušajte ponovo.")

                        #detalji i informacije o treningu
                        elif izbor_treninga == "2":

                            os.system("cls")

                            print("Ovo je program za izgradnju mišića i snage.")
                            print("Dizajniran je za ciljanje svih glavnih i manjih mišićnih skupina, omogućujući maksimaliziranje hipertrofije(procesa izgradnje mišića) korištenjem progresivnog otpora.")
                            print("Trajanje treninga: 6 sedmica")
                            print("Trenirat ćete 3 dana u sedmici, odmarajući se barem jedan dan između sesija. Evo primjera rasporeda:")
                            print("")
                            print("Za velike vježbe poput (squats, deadlifts, bench press, overhead press, barbell rows), odmarajte se oko 2 minute između setova.")
                            print("Za sve ostale vježbe možete koristiti odmor od 60 do 90 sekundi između setova.")
                            print("Preporučeni suplementi: multivitamin, kreatin i 'Whey protein'.")
                            print("Za date vježbe koristite istu težinu za svaki set. Kada osjetite da ste ovladali trenutnom težinom, dodajte još 5-10 kilograma na šipku. ")
                            print("Cilj je da se usredotočite na napredovanje u svakom trenutku, pa kad budete mogli, dodajte težinu.")

                        elif izbor_treninga == "0":
                            main()
                
                else:
                    print("Pogrešan unos, molimo pokušajte ponovo.")

                    
                    
                    

            else: 
                print("Neispravan unos")
                main()


main()





