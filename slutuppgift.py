from datetime import date #importerar datum så att jag kan läsa av de från csv filerna och använda på min x axel i diagramen
import pandas as pd #pandas är ett bibliotek skrivet just för python koding, det man kan göra med pandas är att manipulera data och/eller analysera den
import numpy as np #numpy är ett numeriskt python bibliotek, den hjälper med att göra beräkningar som till exempel, trigonometriska, statiska och algebraiska beräkningar.
from plotly.subplots import make_subplots #den skapar en "lista" där man kan ange en hel del data för grafer, den kommer sammanställa det så att man kan rada upp de med reader och columner så det ser fint ut. 
import plotly.graph_objects as go #en funktion som jag använde mig av för att skapa diagramen, det finns olika diagram man kan skapa, de jag använde nedan och även 3d diagram, jag kunde ej få pie diagramen att fungera eller 3d diagramen så bar och scatter var det jag fick köra på.


#läser in csv filer som ligger i samma directory och ger dessa ett variabelnamn
df = pd.read_csv("National_Daily_Deaths.csv")
df_gender = pd.read_csv("Gender_Data.csv")
df_total_cases_by_age = pd.read_csv("National_Total_Deaths_by_Age_Group.csv")

#använde mig av "make_subplots" för att ge diagramen ställen de kan rada upp sig på. På ett sätt där det ser bra ut och ger de titlar, gav denna funktionen variabelnamnet "fig" som förkortning till figur.
#i "fig" kommer alla diagramen vara skrivna med sina x och y värden samt vilken rad och column de ska stå i 
fig = make_subplots(rows=2, cols=2, subplot_titles=("kön data", "nationella dagliga dödsfall", "dödsfall per åldersgrupp")) 


#nedan kommer mina 3 diagram, i varje har jag skrivit vilken csv fil de ska använda sig av med hjälp av variabelnamnen jag angav dessa ovan, vilka columner i csv filen de ska läsa av för x- och yaxlen samt vilken position de ska ha.
#här använde jag mig av Bar för att det ger en mycket bättre förståelse av hur antalet smittade förhåller sig mellan män och kvinnor, jag ville göra ett pie diagram men fick det inte att funka på något sätt, satt i kanske 3 timmmar och sökte upp olika lösningar och olika sätt att göra pie diagram med hjälp av plotly grafs men fick det inte att funka på något sätt. Pekar man med musen på könen kommer könet samt antalet fall visas
fig.add_trace(
    go.Bar(x=df_gender["Gender"], y=df_gender["Total_Cases"]),
    row=1, col=1
)
#scatter diagram använde jag mig av för att skapa en visualisering av hur många dödsfall som funnits varje månad: Den skapade en linje som rör sig beroende på mängden fall samt vilken månad fallen inträffat på. Pekar man med musen på en viss pungt på diagrammet kommer datum samt antalet dödsoffer visas
fig.add_trace(
    go.Scatter(x=df["Date"], y=df["National_Daily_Deaths"]),
    row=1, col=2
)
#igen kunde jag inte avnända mig av ett pie diagram för att visualisera datan så jag fick köra på ett pie diagram igen, detta var även ett mycket bättre alternativ för att visa mängden dödsfall per åldersgrupp då det ger en mycket bild. Även här kan man peka med musen på en av staplarna för att visa mer exakt värde av antalet dödsfall per åldersgrupp. 
fig.add_trace(
    go.Bar(x=df_total_cases_by_age["Age_Group"], y=df_total_cases_by_age["Total_Cases"]),
    row=2, col=1
)

fig.update_layout(height=700) # detta get diagramen storleken altså höjden som är relativ till längden
fig.write_html('diagram.html', auto_open=True) #detta skapar en html fil i min mapp med namnet diagram.html för att skapa en hemsida där diagramen visas. "auto_open" gör så att varje gång jag kör igång koden kommer hemsidan att startas per automatik, vilket gör att jag ej behöver gå in på html filen och trycka go live för att den ska öppnas.

#i den lilla rutan på högra hörnet av hemsidan kan man trycka på "trace 0, 1, 2" för att ta bort datan på graferna, trycker man på dessa en gång till kommer de tillbaka. 