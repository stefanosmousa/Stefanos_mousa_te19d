import PySimpleGUI as sg
import csv
import pandas as pd
import numpy as np

def pengar():
    värde = sg.popup([[sg.Text('ange summa för insättning',)],
                [sg.Input(size=(25,1), enable_events=True, key='-INPUT-')],
                [sg.OK(), sg.Cancel()]])
    i = 1000
    i+= värde
    with open("saldo.csv", "w+" ) as f:
        thewriter = f.write(str(i))

#saldo
def saldo():
    layout = [  [sg.Button('saldo', size=(19,1))],
                [sg.Button('transaktioner', size=(19,1))],
                [sg.Button('uttag', size=(19,1))],
                [sg.OK(), sg.Cancel()]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
#transaktioner
def transaktioner():
    layout = [  [sg.Button('saldo', size=(19,1))],
                [sg.Button('transaktioner', size=(19,1))],
                [sg.Button('uttag', size=(19,1))],
                [sg.OK(), sg.Cancel()]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event == saldo:
            saldo()
            break
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
#insättning
def insättning():
    layout = [  [sg.Text('ange summa för insättning',)],
                [sg.Input(size=(25,1), enable_events=True, key='-INPUT-')],
                [sg.OK(), sg.Cancel()]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            window.close()
        if event == 'OK':
            window.close()

#uttag
def uttag():

    layout = [  [sg.Text('ange summa för uttag',)],
                [sg.InputText(size=(25,1), enable_events=True, key='-INPUT-')],
                [sg.OK(), sg.Cancel()]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    event, values = window.read()

    # Event Loop to process "events"
    while True:             
        if event in (sg.WIN_CLOSED, 'Cancel'):
            window.close()
        if event == 'OK':
            värde = int(values[0])
            i = 1000
            i+= värde
            with open("saldo.csv", "w+" ) as f:
                thewriter = f.write(str(i))


#logga in
def login():
    sg.theme('Reddit')
    layout = [[sg.Text("Logga in dig hos steffbank")],
            [sg.Text("Mail")],
            [sg.Input()],
            [sg.Text("Lösenord")],
            [sg.Input()],
            [sg.Button('Logga in'), sg.Button('Quit')]]

    window = sg.Window('Window Title', layout) 


    event, values = window.read()

    if event == 'Logga in':
        with open('konto1.csv', 'r') as f:
            data = f.read().strip()
            data_list = data.split(',')
            username = data_list[0]
            password = data_list[1]
            if username == values[0] and password == values[1]:
                window.close()
                startskräm()
            else:
                sg.popup("fel mail eller lösen")
        if event == sg.WIN_CLOSED or event == 'Quit':
            window.close()          

#startskärmen
def startskräm():
    layout = [  [sg.B('saldo', size=(19,1))],
                [sg.B('transaktioner', size=(19,1))],
                [sg.B('sätt in pengar', size=(19,1))],
                [sg.B('ta ut pengar', size=(19,1))],
                [sg.Cancel()]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == 'saldo':
            saldo()
        if event == 'transaktioner':
            transaktioner()
        if event == 'sätt in pengar':
            insättning()
        if event == 'ta ut pengar':
            uttag()
    window.close()


if __name__ == '__main__':
    login()