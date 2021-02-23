
import PySimpleGUI as sg

from captura import Captura
from reconhecedorEigen import Reconhecendo

layout = [[sg.Button('LOGIN'),
           sg.Button('CADASTRAR'),
           sg.Exit("Sair")] ]

window1 = sg.Window('ORIGINAL').Layout(layout)

while True:
    event, values = window1.Read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    if event == 'LOGIN':
        window1.Close()
        r = Reconhecendo()
        r.reconhecedorRosto()

    elif event == 'CADASTRAR':
        window1.Close()
        c = Captura()
        c.capturarFotos()



window1.Close()


