#importar allt jag behöver samt allting från den andra python filen där alla deffenitioner finns
import subprocess
import platform
import time
import defenitioner
global antal_loop
antal_loop = 0




#skapa listor för att minnas mina beräkningar och siffror och använda de i while loopen nedan
basminne = []
längdminne = []
areaminne = []
omkretsminne = []
kvadratminne = []
volymminne = []
hojdenminne = []


#detta är loopen till programmet, nedan för körs allting, inputs, if satser osv, till slut kommer en else loop som skriver ut beräkningarna ifall man inte skriver in "ja" i inputen.
while True:
    användare_input = str(input("Vill du utföra ännu en beräkning ja/nej (nej skriver ut dina beräkningar): "))
    if användare_input == "ja":
        antal_loop += 1
        bas = int(input("ange bas för rektangel: "))
        längd = int(input("ange längd för rektangel: "))

        while True:
            try:
                höjd = int(input("ange höjd för rektangel: "))
                break
            except:
                print("Det är inget heltal! Försök igen")
        
        if höjd < 0:
            höjd = 1+1
        else:
            pass
        if höjd > 10:
            höjd = 10+1
        else:
            pass

        basminne.append(bas)
        längdminne.append(längd)
        areaminne.append(defenitioner.area(bas, längd))
        omkretsminne.append(defenitioner.omkrets(bas, längd))
        kvadratminne.append(defenitioner.kvadrat(bas, längd))
        volymminne.append(defenitioner.volym(bas, längd, höjd))
        hojdenminne.append(höjd)

    else:
        
        time.sleep(1)
        for i in range(antal_loop):
            print("--------------")
            print(f"Beräkning {i + 1}")            
            print(f"Arean: {areaminne[i]} cm2")
            print(f"Omkrets: {omkretsminne[i]} cm")
            print(f"Kvadrat: {kvadratminne[i]}")
            print(f"Volymen 1-{hojdenminne[i]}: {volymminne[i]}cm3")
            print("--------------")
            print(" ")
        break