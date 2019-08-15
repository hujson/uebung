import student

Studenten = []

while True:
    print("(i) immatrikulieren")
    print("(e) exmatrikulieren")
    print("(a) anzeigen aller Studenten")
    print("(s) zum schreiben in textdatei")
    print("(x) beenden")
    
    eingabe = input()
    if(eingabe == 'i'):
        name = input("Namen eingeben ")
        vorname = input("Vornamen eingeben ")
        matnr = int(input("Matrikelnummer eingeben "))
        s = student.Student(vorname, name, matnr)
        Studenten.append(s)
    elif(eingabe == 'e'):
        exnr = int(input("Matrikelnummer eingeben "))
        for i in range(len(Studenten)):
            if exnr == Studenten[i].matnr:
                Studenten.pop(i)  

    elif(eingabe == 'a'):
        for i in range(len(Studenten)):
            print(Studenten[i].name)
            print(Studenten[i].vorname)
            print(Studenten[i].matnr)
    elif(eingabe == 'x'):
        break
    elif(eingabe == 's'):
        datei = open("test.txt", "w")
        for i in range(len(Studenten)):
            datei.write(Studenten[i].name + " " + Studenten[i].vorname + " " + str(Studenten[i].matnr))
        datei.close
    else:
        print("Ungueltige Eingabe")
        continue
