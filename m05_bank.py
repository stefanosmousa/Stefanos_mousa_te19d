
saldo = 1000 #I uppgiften så står det att man börjar med 1000 kr i sitt saldo så jag gjorde en variabel för saldo och satte in 1000 kr.
transaktioner = [] #gjorde en lista för transaktionerna som kommer spara dom.
transaktioner.append(1000) #lägger till 1000 som start för transaktionerna och lagrar föregående data

def balance(): #deffinerar variabeln balance 
    balance = 0
    for i in transaktioner: #for loop så att när man använder sig utav "balance" så kommer balance += t köras.
        balance += i

    return balance

def validate_int(output, error_mess): #validate funktionen gör att programmet kolla efter eventulla fel, om inte rätt output är med där man använder validate så kommer programmet skriva "error mess"
    while True: #skapar en while loop så att koden innanför validate info körs när man kör programmet.
        try: #provar outputen
            value = int(input(output))  #ger ett värde till outputen
            break
        except: #om outputen inte är korrekt så kommer programmet printa "error mess"
            print("error_mess")
    return value #returnar deffenitionen för validate_int

def print_transaktioner(): #skapar en variabel för upplägget av transaktionerna
    x = 0 #variabel för x
    y = 0 # variabel för y
    z = ("\nAlla transaktioner" #upplägget för print_transaktioner
            "\n{:>3} {:>12} {:>12}"
            "\n-----------------").format("Nr", "Händelse", "saldo") #.format stoppar värden i {} ovan.
    for i in transaktioner: #skapar en forsats så att den loopas varje gång programmet körs.
        x += 1
        y += i 
        z += ("\n{:>3}. {:>9} kr {:>9} kr".format(x,i,y)) #stoppar in värdena för x, y och i 

    return z

while True: #skapar min meny och loopar den varje gång programmet körs
    meny = ("\n###############"
            "\n# Lilla banken"
            "\n# saldo"
            "\n# Meny"
            "\n###############"
            "\n1. Visa transaktioner"
            "\n2. Gör en insättning"
            "\n3. Gör ett uttag"
            "\n4. Avbryt"
            "\nGör ditt val:")

    val = validate_int(meny, "felaktig inmatning.") #när man anger valet så kommer validate köras och se till så man ej skriver in något fel.

    if val == 4: #avslutar programmet
        break
    elif val == 1: #printar talen i den ordning som vi angett i "print_funktioner" om användaren skriver in 1 
        print(print_transaktioner())

    elif val == 2: #vad som händer om användaren skriver in talet 2
        inmatning = validate_int("Ange summa för insättning", "Försök igen") # printar "ange summa för insättning", ifall användaren anger något som inte programmet kommer känna igen så kommer den printa "försök igen"
        saldo += inmatning #adderar mängden man valt sätta in till saldot
        transaktioner.append(inmatning)#appendar den till en listan och sparar värdet.

    elif val == 3: #vad som händer om användaren skriver in talet 3
        uttag = validate_int("Ange hur mycket du vill ta ut","Försök igen") 
        if uttag <= saldo and uttag >=0: #if satts så att användaren inte kan mata ut ett tal större än mängden som finns i saldo
            saldo -= uttag #tar subtraherar uttaget med mängde nsom finns i saldo varje gång man tar ut pengar
            transaktioner.append(-uttag) #lägga till talet i en lista så att den kommer ihåg uttaget.
        else:
            print("Medges ej")
    else:
        print("Error") #om inget av talen användaren matar in finns med i if-satsen ovan kommer "error" printas


print("Ta ditt kvitto och ha en bra dag") #när programmet avslutats kommer "ta ditt kvitto och ha en bra dag" printas