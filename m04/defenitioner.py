#defenition för att programmet ska skriva ut om rektangeln är en kvadrat eller om den är en vanlig rektangel
def kvadrat(bas, längd):
    if bas == längd:
        kvadratminne = "Ja"
    else:
        kvadratminne = "Nej"
    return kvadratminne


#defenition för hur arean ska räknas ut
def area(bas, längd):
    areaminne = bas * längd
    return areaminne


#defenition för hur omkrätsen ska räknas
def omkrets(bas, längd):
    omkretsminne = 2*(bas+längd)
    return omkretsminne

#defenition för volymen och hur den ska räknas ut
def volym(bas, längd, höjd):
    volymminne = []
    for i in range(höjd):
        volymminne.append(bas * längd * (i+1))
    return volymminne





#alla dessa är gjorda med funktioner då det är det lättaste sättet att deffinera något 