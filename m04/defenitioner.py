#anledningen till att jag valt att göra defenitionerna separat är för att det gör den huvudsakliga koden mycket lättare och finare att läsa av, dessutom blir den inte så klumpig och
#slarvig utan mer direkt och prydlig.

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

#defenition för volymen och hur den ska räknas ut
def volym(bas, längd, höjd):
    volymminne = []
    for i in range(höjd):
        volymminne.append(bas * längd * (i+1))
    return volymminne

#defenition för hur omkrätsen ska räknas
def omkrets(bas, längd, höjd):
    omkretsminne = (bas+längd+höjd)
    return omkretsminne

