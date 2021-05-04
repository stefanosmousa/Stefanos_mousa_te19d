#importar allt jag behöver samt allting från den andra python filen där alla deffenitioner finns.
import subprocess
import platform
import defenitioner
global antal_loop
antal_loop = 0




#skapa listor för att minnas mina beräkningar och siffror och använda de i while loopen nedan, gör jobbet lite lättare och finare.
basminne = []
längdminne = []
areaminne = []
omkretsminne = []
kvadratminne = []
volymminne = []
höjdminne = []


#detta är loopen till programmet, nedan för körs allting, inputs, if satser osv, till slut kommer en else loop som skriver ut beräkningarna ifall man inte skriver in "ja" i inputen.
#Jag valde en while loop då den är lättaste att skriva i och den var mest lämplig för denna sorts uppgift. Innanför den skrev jag mina inputs då jag vill att denna ska köras om och om igen
#tills användaren väljer att den inte vill köra koden mer. 
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
        
        if höjd < 0: #här gjorde jag så att höjden skulle skriva in 1 istället om användaren matar in något mindre än 1 och att den skulle skriva 10 ifall användaren väljer att mata in ett tal större än 10.
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
        omkretsminne.append(defenitioner.omkrets(bas, längd,höjd))
        kvadratminne.append(defenitioner.kvadrat(bas, längd))
        volymminne.append(defenitioner.volym(bas, längd, höjd))
        höjdminne.append(höjd)

    else:
        
        for i in range(antal_loop):
            print(f"basen du angivit är {basminne} cm")
            print(f"längden du angivit är {längdminne} cm")
            print(f"höjden du angivit är {höjdminne} cm")
            print("--------------")
            print(f"arean på rektangeln är {areaminne[i]}cm2 och volymerna till alla tal fram till angivna tal för höjderna 1->{höjdminne} är {volymminne[i]} cm3")
            print(f"Omkretsen på rektangeln är: {omkretsminne[i]} cm")
            print(f"Är rektangeln en kvadrat?: {kvadratminne[i]}")
            
            print(" ")
        break